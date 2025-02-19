from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hysam Khan is deploying Flask App at Vercel"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

