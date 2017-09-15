from decouple import config
from flask import Flask, abort, request, jsonify, make_response, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return "Well... Hello then!"


@app.route('/hello_name', methods=['GET'])
def hello_name():
    if len(request.args) < 1:
        print("No arguments passed")
        return make_response(jsonify(message="Hello noname"))
    else:
        args = request.args.to_dict()

        if 'name' in args:
            if args['name'] == 'temer':
                abort(make_response(jsonify(message="Sem golpe! Fora Temer"), 403))

            print("Arguments name: " + args['name'])
            message = "Hello " + args['name']
        else:
            print("No argument name passed")
            message = "Hello noname"

        return make_response(jsonify(message=message))


@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/login', methods=['POST'])
def login():
    username = str(request.form['username'])
    if username == 'temer':
        abort(make_response(jsonify(message="Sem golpe! Fora Temer"), 403))
    else:
        return hello_name()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(config('PORT')))