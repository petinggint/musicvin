from motor.motor_asyncio import AsyncIOMotorClient

from config import MONGO_DB_URI

from ..logging import LOGGER

LOGGER(__name__).info("ʟᴀɢɪ ɢᴡ ᴋᴏɴᴇᴋɪɴ ᴅᴜʟᴜ ᴋᴇ ᴍᴏɴɢᴏ...")
try:
    _mongo_async_ = AsyncIOMotorClient(MONGO_DB_URI)
    mongodb = _mongo_async_.Anon
    LOGGER(__name__).info("ʙᴇʀʜᴀsɪʟ ᴋᴏɴᴇᴋ ᴍᴏɴɢᴏ.")
except:
    LOGGER(__name__).error("ɢᴀɢᴀʟ ᴋᴏɴᴇᴋ, ᴋᴇ ᴅᴀᴛᴀʙᴀsᴇ ᴍᴏɴɢᴏ ʟᴜ.")
    exit()
