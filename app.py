from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS

app = Flask(__name__, static_folder="front/dist")
import views

CORS(app)
import os


@app.route("/process", methods=["POST"])
def process_data():
    data = request.json
    article = data["article"]

    # print(article)
    processed_data = views.processor(article)

    print(processed_data)

    return jsonify({"output": processed_data})


@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def serve(path):
    if path != "" and os.path.exists(app.static_folder + "/" + path):  # type: ignore
        return send_from_directory(app.static_folder, path)  # type: ignore
    else:
        return send_from_directory(app.static_folder, "index.html")  # type: ignore


if __name__ == "__main__":
    app.run(debug=True)
