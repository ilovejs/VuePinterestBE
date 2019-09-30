import os
import random
from flask import Flask, abort, send_from_directory, jsonify
from flask_cors import CORS, cross_origin
from logging.config import dictConfig

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})

DEVELOPMENT = True
DEBUG = True
IMG_ROOT = 'img'

app = Flask(__name__)
CORS(app, support_credentials=True)


@app.route('/image/random', methods=['GET'])
@cross_origin(supports_credentials=True)
def get_infinite_images():
    """
    Randomly get initial images (k=13) to cool start
    :return: images url in {"msg": "Success", "urls": images} format
    """
    try:
        # Filter out system file e.g. .DS_store
        jpegs = [x for x in os.listdir(IMG_ROOT) if x[-3:] == 'jpg']
        app.logger.info(f"jpeg: {jpegs}")
        images = random.choices(jpegs, k=13)
        return jsonify({"msg": "Success", "image_names": images}), 200
    except FileNotFoundError:
        return jsonify({"msg": "Initial Loading failed", "url": []}), 400
    except Exception as e:
        return jsonify({"msg": f"Exception: {e}", "url": []})


@app.route('/image/<filename>', methods=['GET'])
def get_single_image(filename):
    """
    Get a single image file by name. Like Pinterest api response 1 image per GET request.
    :param filename: Image file name
    :return: Image bytes from send_file()
    """
    try:
        app.logger.info(filename, IMG_ROOT)
        return send_from_directory(IMG_ROOT + '/', filename=filename, as_attachment=False)
    except FileNotFoundError:
        abort(404)


if __name__ == '__main__':
    app.run(port=5000)
