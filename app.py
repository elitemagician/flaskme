from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
	return 'OK CJ IS THE KING! TESING AUTOMATION 2'

if __name__ == "__main__":
	app.run()
