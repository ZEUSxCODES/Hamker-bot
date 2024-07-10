from pyrogram import Client, filters

def register_commands(app: Client):
    @app.on_message(filters.command("start"))
    async def start(client, message):
        await message.reply("Hello! I'm your bot. Use /help to see what I can do.")

    @app.on_message(filters.command("help"))
    async def help(client, message):
        help_text = """
        Here is the help menu of the bot:

        /afk : Mark yourself as AFK (away from keyboard)
        /alive : Shows the alive status of the bot
        /echo : Sends the given text
        /figlet : Generates a figlet of given name
        /img : Shows information about the replied image
        /phlogo : Generates a Pornhub logo of the given text
        /ping : Shows the ping latency and system stats of the bot
        /q : Makes a quote of the replied message
        /shorturl : Shortens the given URL
        /start : Starts the bot
        /sname : Decodes the name of the replied user with Unicode
        /webss : Captures a screenshot of the given site
        """
        await message.reply(help_text)

    @app.on_message(filters.command("about"))
    async def about(client, message):
        about_text = "This is a multi-feature Telegram bot created using Pyrogram."
        await message.reply(about_text)
