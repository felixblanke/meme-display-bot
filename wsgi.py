import json
from pathlib import Path

from flask import Flask, request, render_template
import requests
import uuid

app = Flask(__name__, static_folder='photos')
app.config.from_file("config.json", load=json.load)

@app.route('/webhook', methods=['POST'])
def webhook_receiver():
    data = request.json

    try:
        if "photo" not in data["message"]:
            return "ok", 200
        file_request = {
            "file_id": data["message"]["photo"][-1]["file_id"]
        }

        response = requests.post(
            f"https://api.telegram.org/bot{app.config['TOKEN']}/getFile",
            file_request
        )
        if response.status_code != 200:
            return "ok", 200

        response = response.json()

        if not response["ok"]:
            return "ok", 200

        file_path = response["result"]['file_path']

        image_response = requests.get(
            f"https://api.telegram.org/file/bot{app.config['TOKEN']}/{file_path}"
        )

        suffix = Path(file_path).suffix
        name = str(uuid.uuid4()) + suffix

        with (Path(app.config["IM_PATH"]) / name).open("wb") as handle:
            for data in image_response.iter_content():
                handle.write(data)

    except Exception as ex:
        raise ex

    return "ok", 200

@app.route("/photos/", methods=["GET"])
def photos():
    return [str(p.name) for p in Path(app.config["IM_PATH"]).iterdir()]

@app.route("/", methods=["GET"])
def meme_page():
    return render_template("main.html", imgDir=app.config["IM_PATH"] + "/", displayTime=app.config["DISPLAY_TIME"])
