from decouple import config
from flask import Flask, abort, request, jsonify, make_response
app = Flask(__name__)

@app.route("/")
def hello():
    return "Well... Hello them!"

@app.route('/hello_name', methods=['GET'])
def hello_name():
	if request.args:
		return make_response(jsonify(message="Hello noname"))
	else:
		args = request.args.to_dict()

		if 'name' in args:
			message = "Hello " + args['name']
		else:
			message = "Hello noname"

		return make_response(jsonify(message=message))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(config('PORT')))