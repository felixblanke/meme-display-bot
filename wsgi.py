import json
from pathlib import Path

from flask import Flask, request, render_template
import requests
import uuid

static_folder_name = "photos"

app = Flask(__name__, static_folder=static_folder_name)
app.config.from_file("config.json", load=json.load)


@app.route("/webhook", methods=["POST"])
def webhook_receiver():
    return_value = "ok", 200

    data = request.json

    if "photo" not in data["message"]:
        return return_value
    file_request = {"file_id": data["message"]["photo"][-1]["file_id"]}

    response = requests.post(
        f"https://api.telegram.org/bot{app.config['TOKEN']}/getFile", file_request
    )
    if response.status_code != 200:
        return return_value

    response = response.json()

    if not response["ok"]:
        return return_value

    file_path = response["result"]["file_path"]

    image_response = requests.get(
        f"https://api.telegram.org/file/bot{app.config['TOKEN']}/{file_path}"
    )

    suffix = Path(file_path).suffix
    name = str(uuid.uuid4()) + suffix

    with (Path(app.static_folder) / name).open("wb") as handle:
        for data in image_response.iter_content():
            handle.write(data)

    return return_value


@app.route(f"/{static_folder_name}/", methods=["GET"])
def photos():
    return [str(p.name) for p in Path(app.static_folder).iterdir()]


@app.route("/", methods=["GET"])
def meme_page():
    return render_template(
        "main.html",
        imgDir=Path(app.static_folder).name + "/",
        displayTime=app.config["DISPLAY_TIME"],
    )
