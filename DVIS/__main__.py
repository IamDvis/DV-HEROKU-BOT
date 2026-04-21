import asyncio

# Initialize event loop AT THE VERY TOP to avoid any different loop errors when importing pyromod/pyrogram
try:
    import uvloop
    uvloop.install()
except ImportError:
    pass

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)

import logging
import importlib

from pyrogram import idle
from DVIS import app
from DVIS.plugins import ALL_MODULES

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler()]  # Output to console
)

logging.getLogger("pyrogram").setLevel(logging.ERROR)
logging.getLogger("pymongo").setLevel(logging.ERROR)

log = logging.getLogger("DVIS-HEROKU-BOT")

async def main():
    log.info("Starting bot...")
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("DVIS.plugins" + all_module)
    log.info("Bot Started")
    await idle()
    await app.stop()

if __name__ == "__main__":
    loop.run_until_complete(main())
