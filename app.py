import os, random
from flask import Flask, Response, abort, send_from_directory, jsonify
from flask import send_file

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
IMG_ROOT = os.environ['IMG_ROOT']


@app.route('/image/init', methods=['GET'])
def initial_image_list():
    """
    Randomly get 20 images to cool start
    :return: 20 images url in {"msg": "Success", "urls": images} format
    """
    try:
        images = random.choices(os.listdir('/Users/mike/Code/PY/InfiniteScrollPhoto/img'), k=20)
        return jsonify({"msg": "Success", "urls": images}), 200
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
