from flask import Flask, jsonify, make_response,request, redirect, url_for
from flask_restful import Resource, Api
from flask_swagger import swagger
from PIL import Image
from io import BytesIO

app = Flask(__name__)
api = Api(app)


def validate(value):
    if value['in'] not in ['query', 'header', 'path', 'formData']:
        raise ValueError('Invalid location')
    return value


class UploadImage(Resource):
    def post(self):
        img = request.files['image']
        img = Image.open(BytesIO(img.read()))
        return {"result": "Image received and processed"}


api.add_resource(UploadImage, '/upload_image', endpoint='upload_image')


def output_json(data, code, headers=None):
    resp = make_response(jsonify(data), code)
    resp.headers.extend(headers or {})
    return resp





@app.route('/')
def index():
    return jsonify({'message': 'Hello, World!'})


@app.route('/docs')
def documentation():
    return redirect(url_for('static', filename='swagger-ui/index.html'))


if __name__ == '__main__':
    app.run(debug=True)