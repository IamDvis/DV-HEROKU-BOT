import asyncio

try:
    import uvloop
    uvloop.install()
except ImportError:
    pass

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)

import pyromod.listen

from pyromod.listen.message_handler import MessageHandler

_old_init = MessageHandler.__init__

def _pro_init(self, callback, filters=None):
    _old_init(self, callback, filters)
    old_cb = self.callback
    async def _async_cb(*args, **kwargs):
        return await old_cb(*args, **kwargs)
    self.callback = _async_cb

MessageHandler.__init__ = _pro_init

from pyrogram import Client, filters
from config import *

app = Client(
    name="DVIS",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    in_memory=True,
)

filters.sudo = filters.create(
    lambda _, __, m: bool(m.from_user and m.from_user.id in OWNER_ID),
    "SudoFilter",
)
