from pyrogram import Client, filters
import requests
import pyfiglet
import aiohttp
import io
import time

afk_users = {}

def register_pmfilter(app: Client):
    @app.on_message(filters.command("afk"))
    async def afk(client, message):
        afk_users[message.from_user.id] = True
        await message.reply("You are now AFK.")

    @app.on_message(filters.command("alive"))
    async def alive(client, message):
        await message.reply("I'm alive and kicking!")

    @app.on_message(filters.command("echo"))
    async def echo(client, message):
        text = message.text.split(" ", 1)[1] if len(message.command) > 1 else "You need to provide text to echo."
        await message.reply(text)

    @app.on_message(filters.command("figlet"))
    async def figlet_command(client, message):
        text = message.text.split(" ", 1)[1] if len(message.command) > 1 else "You need to provide text."
        result = pyfiglet.figlet_format(text)
        await message.reply(f"<pre>{result}</pre>", parse_mode="html")

    @app.on_message(filters.command("img") & filters.reply)
    async def img_info(client, message):
        if message.reply_to_message.photo:
            photo = message.reply_to_message.photo[-1]
            file_info = await client.get_file(photo.file_id)
            await message.reply(f"Photo Info:\nFile ID: {file_info.file_id}\nSize: {file_info.file_size} bytes")
        else:
            await message.reply("Please reply to an image.")

    @app.on_message(filters.command("phlogo"))
    async def phlogo(client, message):
        text = message.text.split(" ", 1)[1] if len(message.command) > 1 else "You need to provide text."
        # Add your Pornhub logo generation logic here
        # This is a placeholder
        await message.reply("Feature under construction.")

    @app.on_message(filters.command("ping"))
    async def ping(client, message):
        start = time.time()
        await message.reply("Pong!")
        end = time.time()
        latency = round((end - start) * 1000)
        await message.reply(f"Pong! Latency: {latency} ms")

    @app.on_message(filters.command("q") & filters.reply)
    async def quote(client, message):
        quoted_message = message.reply_to_message
        await message.reply(f"Quoted: {quoted_message.text}")

    @app.on_message(filters.command("shorturl"))
    async def shorturl(client, message):
        url = message.text.split(" ", 1)[1] if len(message.command) > 1 else "You need to provide a URL."
        response = requests.get(f"https://api.shrtco.de/v2/shorten?url={url}")
        if response.status_code == 201:
            short_url = response.json()["result"]["short_link"]
            await message.reply(f"Short URL: {short_url}")
        else:
            await message.reply("Failed to shorten URL.")

    @app.on_message(filters.command("sname") & filters.reply)
    async def sname(client, message):
        user_name = message.reply_to_message.from_user.first_name
        await message.reply(f"Decoded Name: {user_name}")

    @app.on_message(filters.command("webss"))
    async def webss(client, message):
        url = message.text.split(" ", 1)[1] if len(message.command) > 1 else "You need to provide a URL."
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://image.thum.io/get/width/1200/{url}") as resp:
                if resp.status == 200:
                    img_data = io.BytesIO(await resp.read())
                    await client.send_photo(chat_id=message.chat.id, photo=img_data)
                else:
                    await message.reply("Failed to capture screenshot.")
