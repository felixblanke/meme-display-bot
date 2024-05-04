# Telegram meme display bot

This projects implements the backend for a Telegram bot to display memes from Telegram messages as a slide show.
The functionality is simple:
1. All images contained in messages the bot can see are downloaded.
2. A simple website displays all stored images successively, starting from newest to oldest.


### Configuration

First, you need to register [a Telegram bot](https://core.telegram.org/bots) for this purpose.
If you want your memes to be displayed at `memes.example.com`, register `memes.example.com/webhook` [as a webhook for your bot](https://core.telegram.org/bots/api#setwebhook), e.g. by sending the following POST request to `https://api.telegram.org/bot<TOKEN>/setWebhook`
```json
{
    "url": "https://memes.example.com/webhook",
    "allowed_updates": ["message"]
}
```

Next, clone this repository on your server and create a `config.json` file in the repository directory with the following entries:
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
