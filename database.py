from os import environ
from config import Config
import motor.motor_asyncio
from pymongo import MongoClient

async def mongodb_version():
    x = MongoClient(Config.DATABASE_URI)
    mongodb_version = x.server_info()['version']
    return mongodb_version

class Database:
    
    def __init__(self, uri, database_name):
        self._client = motor.motor_asyncio.AsyncIOMotorClient(uri)
        self.db = self._client[database_name]
        self.users = self.db.users
        self.notifications = self.db.notifications
        
    async def add_user(self, id, name):
        user = self.new_user(id, name)
        await self.users.insert_one(user)

    async def is_user_exist(self, id):
        user = await self.users.find_one({'id': int(id)})
        return bool(user)

    async def get_all_users(self):
        return self.users.find({})

    async def add_notification(self, user_id):
        return await self.notifications.insert_one({'user_id': int(user_id)})

    async def remove_notification(self, user_id):
        return await self.notifications.delete_many({'user_id': int(user_id)})

    async def get_all_notifications(self):
        return self.notifications.find({})

    def new_user(self, id, name):
        return {
            'id': id,
            'name': name,
            'ban_status': {
                'is_banned': False,
                'ban_reason': '',
            },
        }

db = Database(Config.DATABASE_URI, Config.DATABASE_NAME)
