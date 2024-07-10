# commands.py

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import config
import datetime
import translation

# Variable to store bot start time
start_time = datetime.datetime.now()

def register_commands(app: Client):
    @app.on_message(filters.command("start"))
    async def start(client, message):
        user = message.from_user
        
        # Fetch the picture URL from config
        picture_url = config.START_PIC
        
        # Create main buttons
        main_buttons = [
            [InlineKeyboardButton("Add Me Else You Gay", url=f"http://t.me/{config.BOT_USERNAME}?startgroup=true")],
            [InlineKeyboardButton("Help", callback_data="help"), InlineKeyboardButton("Source", callback_data="source")]
        ]
        
        # Calculate uptime
        uptime_delta = datetime.datetime.now() - start_time
        days = uptime_delta.days
        seconds = uptime_delta.seconds
        hours, remainder = divmod(seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        
        # Format uptime string
        uptime_str = f"{days} days, {hours} hours, {minutes} minutes, {seconds} seconds"
        
        # Send the picture with the start message
        await client.send_photo(
            chat_id=message.chat.id,
            photo=picture_url,
            caption=translation.START_TXT.format(uptime_str=uptime_str),
            reply_markup=InlineKeyboardMarkup(main_buttons)
        )
    
    @app.on_callback_query(filters.regex(r'^(help|back_to_start)'))
    async def help_or_back_callback(client, callback_query):
        if callback_query.data == 'help':
            caption_text = translation.HELP_TXT
        else:  # callback_query.data == 'back_to_start'
            caption_text = translation.START_TXT.format(uptime_str=uptime_str)
        
        # Update message caption and buttons
        await callback_query.answer()
        await callback_query.message.edit_caption(
            caption=caption_text,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("Add Me Else You Gay", url=f"http://t.me/{config.BOT_USERNAME}?startgroup=true")],
                [InlineKeyboardButton("Help", callback_data="help"), InlineKeyboardButton("Source", callback_data="source")]
            ])
        )
    
    @app.on_callback_query(filters.regex(r'^source'))
    async def source_callback(client, callback_query):
        source_video_url = config.SOURCE_VID
        await callback_query.answer()
        await client.send_video(
            chat_id=callback_query.message.chat.id,
            video=source_video_url,
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Back", callback_data="back_to_start")]])
        )
    
    @app.on_message(filters.command("help"))
    async def help(client, message):
        await message.reply(translation.HELP_TXT)

    @app.on_message(filters.command("about"))
    async def about(client, message):
        await message.reply(translation.ABOUT_TXT)

