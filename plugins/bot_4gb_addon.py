# ✅ Yeh code apne bot.py ya __main__.py mein add karo
# Bot client ke saath ek USER client bhi banao STRING_SESSION se

from pyrogram import Client
from config import Config

# Normal Bot Client (2GB limit)
bot = Client(
    "RenameBot",
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.BOT_TOKEN
)

# ✅ User Client — 4GB file support ke liye
# STRING_SESSION set hone par hi chalu hoga
if Config.STRING_SESSION:
    user = Client(
        "UserSession",
        api_id=Config.API_ID,
        api_hash=Config.API_HASH,
        session_string=Config.STRING_SESSION
    )
else:
    user = None  # 4GB support disabled


# ✅ Upload function — user client se 4GB tak upload
async def upload_file_4gb(client_bot, message, file_path, file_name, thumb=None):
    """
    4GB tak ki file upload karta hai user session se.
    Agar STRING_SESSION nahi hai to normal bot se upload karta hai (2GB limit).
    """
    from helper_func_addon import check_file_size
    import os

    file_size = os.path.getsize(file_path)
    limit_2gb = 2 * 1024 * 1024 * 1024  # 2GB

    if file_size > limit_2gb:
        if user is None:
            await message.reply_text(
                "❌ **File 2GB se badi hai!**\n\n"
                "4GB support ke liye `STRING_SESSION` env variable set karo.\n"
                "Ek Telegram Premium account ka string session chahiye."
            )
            return False

        # User client se upload (4GB tak)
        upload_client = user
    else:
        # Normal bot client se upload (2GB tak)
        upload_client = client_bot

    return upload_client  # calling function mein is client se send_document/send_video karo
