from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "<h1>Final new Jenkins uploaded. Hello from a traditional deployment! Jenkins CI/CD is working! 🚀</h1>"

if __name__ == '__main__':
    # This part is for local testing; Gunicorn will run the app in production
    app.run(host='0.0.0.0', port=5000)
