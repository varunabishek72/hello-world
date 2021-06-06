from flask import Flask
app = Flask(__name__)

@app.route('/')
def Varun():
    return 'Hello Varun'
 
if __name__ == "__main__":     
    app.run()
