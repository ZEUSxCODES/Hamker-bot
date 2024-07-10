import os

# Telegram API credentials
API_ID = os.getenv('API_ID', 'YOUR_API_ID')  # Replace with your Telegram API ID
API_HASH = os.getenv('API_HASH', 'YOUR_API_HASH')  # Replace with your Telegram API hash
BOT_TOKEN = os.getenv('BOT_TOKEN', 'YOUR_BOT_TOKEN')  # Replace with your Telegram bot token

# URLs for media
START_PIC = os.getenv('START_PIC', 'https://te.legra.ph/file/1f2ac2fe8cdf202799847.jpg')  # URL for bot start photo
SOURCE_VID = os.getenv('SOURCE_VID', 'https://te.legra.ph/file/fecf4e578f159374f33c4.mp4')  # URL for source video

# Bot username
BOT_USERNAME = os.getenv('BOT_USERNAME', 'Bot_Username')  # Replace with your bot's Telegram username

# MongoDB URI and database name
DATABASE_URI = os.getenv('DATABASE_URI', 'mongodb://localhost:27017/')
DATABASE_NAME = os.getenv('DATABASE_NAME', 'your_database_name')

# Telegram Updates Channel ID or username
UPDATES_CHANNEL = os.getenv('UPDATES_CHANNEL', 'your_channel_username_or_id')

# Other configurations
MAX_WORKERS = int(os.getenv('MAX_WORKERS', '50'))

# Features enabled configuration
FEATURES_ENABLED = {
    'force_subscribe': os.getenv('FORCE_SUBSCRIBE_ENABLED', 'True').lower() == 'true',
    'image_processing': os.getenv('IMAGE_PROCESSING_ENABLED', 'True').lower() == 'true',
    'video_processing': os.getenv('VIDEO_PROCESSING_ENABLED', 'True').lower() == 'true',
    # Add more features as needed
}
