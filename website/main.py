from flask import Flask
app = Flask(__name__) # this gets the name of the file so Flask knows it's name 
#random comment
@app.route("/")
def hello_world():
    return "<p>Hello, World</p>" 


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")