try:
    import uvloop
    uvloop.install()
except ImportError:
    pass

import logging
import asyncio
import importlib

from pyrogram import idle

# Import app after uvloop.install() to ensure the loop policy is inherited correctly
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
    for all_module in ALL_MODULES:
        importlib.import_module("DVIS.plugins" + all_module)
    log.info("Bot Started successfully.")
    await idle()

if __name__ == "__main__":
    try:
        import uvloop
        uvloop.install()
    except ImportError:
        pass

    app.run(main())
