from flask import Flask
app = Flask("app")
@app.route("/")
def home():
   return "<h1>Hello from CI/CD Pipeline - Version 1</h1>"
app.run(host="0.0.0.0", port=5000)
