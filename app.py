from flask import Flask 


app= Flask(__name__)


@app.route('/')
def homepage():

	return """
	<div> <center>
    <h1 > Well come to Claire_codes Docker Demo!</h1>
    <h3>Python Flask in Docker!</h3>
    <p> This is a sample web-app for running Flask inside Docker.</p>
   </center> </div>
  """



if __name__ == '__main__':
	app.run(debug=True, host ='127.0.0.1')
