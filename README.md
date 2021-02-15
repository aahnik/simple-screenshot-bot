# simple-screenshot-bot


You send a text message to the bot, it finds all the links in the message, and replies with the screenshots of all the pages.

Plain and simple bot, with no fancy features.

It uses webhook, to obtain updates from Telegram. In Heroku, it sleeps when there is no traffric for 30 mins. That means it saves you dyno-hours. 

It gets activated as soon as a new message is received.

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/aahniks/simple-screenshot-bot)

