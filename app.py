from flask import Flask

# Create a Flask application instance
app = Flask(__name__)

# Define a route (URL path) and its function
@app.route('/')
def home():
    return "Hello, Tony"

@app.route('/av')
def avengers():
    return "Hello, Avengers"

@app.route('/greet')
def greet_world():
    return "Hello, World!!"

@app.route('/greet/india')
def greet_india():
    return "Hello, Indi!!"

#run app
if __name__ == "__main__":
    app.run(debug=True)
