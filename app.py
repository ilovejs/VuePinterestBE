import os
import random

from flask import Flask, abort, send_from_directory, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
IMG_ROOT = os.environ['IMG_ROOT']
CORS(app, support_credentials=True)


@app.route('/image/init', methods=['GET'])
@cross_origin(supports_credentials=True)
def initial_image_list():
    """
    Randomly get initial images to cool start
    :return: images url in {"msg": "Success", "urls": images} format
    """
    try:
        # filter out system file e.g. .DS_store
        jpgs = [x for x in os.listdir('/Users/mike/Code/PY/InfiniteScrollPhoto/img') if x[-3:] == 'jpg']
        print(jpgs)
        images = random.choices(jpgs, k=13)
        return jsonify({"msg": "Success", "image_names": images}), 200
    except FileNotFoundError:
        return jsonify({"msg": "Initial Loading failed", "url": []}), 400


@app.route('/image/<filename>', methods=['GET'])
def get_image(filename):
    """
    Get a single image file by name. Like Pinterest api response 1 image per GET request.
    :param filename: Image file name
    :return: Image bytes from send_file()
    """
    try:
        print(filename, IMG_ROOT)
        return send_from_directory('img/', filename=filename, as_attachment=False)
    except FileNotFoundError:
        abort(404)


if __name__ == '__main__':
    app.run()
