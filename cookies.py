from flask import Flask, make_response, request, render_template

app = Flask(__name__)

@app.route('/')
def setCookies():
	resp = make_response(render_template('cookies.html'))
	resp.set_cookie('username', 'CJ')
	return resp

@app.route('/get')
def getCookies():
	username = request.cookies.get('username')
	return 'The User is ' + username

if __name__ == '__main__':
	app.run(debug=True)