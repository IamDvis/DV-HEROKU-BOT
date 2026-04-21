import inspect

# Monkey-patch inspect to correctly identify Pyromod's async handler.
# This prevents Kurigram from dispatching it to a worker thread, which fixes the "different loop" RuntimeError.
_old_is_coro = inspect.iscoroutinefunction
def _new_is_coro(obj):
    if getattr(obj, "__name__", "") == "resolve_future_or_callback":
        return True
    return _old_is_coro(obj)
inspect.iscoroutinefunction = _new_is_coro

import pyromod.listen  # noqa
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
