# Telegram meme display bot

This projects implements the backend for a Telegram bot to display memes from Telegram messages as a slide show.
The functionality is simple:
1. All images contained in messages the bot can see are downloaded.
2. A simple website displays all stored images successively, starting from newest to oldest.


### Configuration

First, you need to register [a Telegram bot](https://core.telegram.org/bots) for this purpose.
Next, clone this repository on your server.
In the repository directory, create a `config.json` file with the following entries:
```json
{
    "TOKEN": "YOUR-BOT-TOKEN",
    "DISPLAY_TIME": 5000 // time in milliseconds for which images are displayed
}
```
By default the images are stored in a directory named `photos` in the repository directory.


### Deployment

This projects uses the python frame work Flask.
There are various ways to [deploy a Flask project](https://flask.palletsprojects.com/en/3.0.x/deploying/).
