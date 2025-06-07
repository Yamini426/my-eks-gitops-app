from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from my Custom GitOps App! Version 2.0 - Auto-Synced by Argo CD!' # <--- Modify this line

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
