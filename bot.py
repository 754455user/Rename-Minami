from datetime import datetime
from pytz import timezone
from pyrogram import Client, __version__
from pyrogram.raw.all import layer
from config import Config
from aiohttp import web
from route import web_server
import pyromod
import pyrogram.utils

pyrogram.utils.MIN_CHANNEL_ID = -100999999999999


class Bot(Client):

    def __init__(self):
        super().__init__(
            name="renamer",
            api_id=Config.API_ID,
            api_hash=Config.API_HASH,
            bot_token=Config.BOT_TOKEN,
            workers=200,
            plugins={"root": "plugins"},
            sleep_threshold=15,
        )

    async def start(self):
        await super().start()
        me = await self.get_me()
        self.mention = me.mention
        self.username = me.username
        self.uptime = Config.BOT_UPTIME

        # ✅ 4GB Support - User Client Start
        if Config.STRING_SESSION:
            try:
                await user.start()
                user_me = await user.get_me()
                print(f"✅ User Client Started: {user_me.first_name} (4GB Support Active)")
            except Exception as e:
                print(f"❌ User Client Failed: {e}")
        else:
            print("⚠️ STRING_SESSION not set — 4GB support disabled (2GB limit)")

        if Config.WEBHOOK:
            app = web.AppRunner(await web_server())
            await app.setup()
            await web.TCPSite(app, "0.0.0.0", 8080).start()

        print(f"{me.first_name} Is Started.....✨️")

        for id in Config.ADMIN:
            try:
                await self.send_message(id, f"**{me.first_name} Is Started...**")
            except:
                pass

        if Config.LOG_CHANNEL:
            try:
                curr = datetime.now(timezone("Asia/Kolkata"))
                date = curr.strftime('%d %B, %Y')
                time = curr.strftime('%I:%M:%S %p')
                await self.send_message(
                    Config.LOG_CHANNEL,
                    f"**{me.mention} Is Restarted !!**\n\n"
                    f"📅 Date : `{date}`\n"
                    f"⏰ Time : `{time}`\n"
                    f"🌐 Timezone : `Asia/Kolkata`\n\n"
                    f"🉐 Version : `v{__version__} (Layer {layer})`</b>"
                )
            except:
                print("Please Make This Is Admin In Your Log Channel")

    async def stop(self, *args):
        await super().stop()
        # ✅ User Client Stop
        if Config.STRING_SESSION:
            try:
                await user.stop()
            except:
                pass


# ✅ User Client for 4GB file upload
user = Client(
    name="user_4gb",
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    session_string=Config.STRING_SESSION if Config.STRING_SESSION else None,
    no_updates=True,
)

Bot().run()

# Jishu Developer
# Don't Remove Credit 🥺
# Telegram Channel @MadflixBotz
# Backup Channel @JishuBotz
# Developer @JishuDeveloper
# Contact @MadflixSupport
