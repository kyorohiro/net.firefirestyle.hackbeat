import flask
import os

app = flask.Flask(__name__, static_url_path='',static_folder="public")

@app.route("/")
def root():
    return  app.send_static_file("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=int(os.environ.get('PORT', 8080)))

