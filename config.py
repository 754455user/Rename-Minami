import os, time, re
id_pattern = re.compile(r'^.\d+$')



class Config(object):
    # pyro client config
    API_ID    = os.environ.get("API_ID", "")
    API_HASH  = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 
   
    # database config
    DATABASE_NAME = os.environ.get("DATABASE_NAME","")     
    DATABASE_URL  = os.environ.get("DATABASE_URL","")
 
    # other configs
    BOT_UPTIME  = time.time()
    START_PIC   = os.environ.get("START_PIC", "")
    ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '').split()]

    # channels logs
    FORCE_SUBS   = os.environ.get("FORCE_SUBS", "") 
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", ""))

    # wes response configuration     
    WEBHOOK = bool(os.environ.get("WEBHOOK", False))

    # ✅ 4GB File Support — User Session (String Session)
    # Isko set karo Telegram premium account ka string session
    # Generate karo: python -c "from pyrogram import Client; Client(':memory:', api_id=API_ID, api_hash=API_HASH).run()"
    STRING_SESSION = os.environ.get("STRING_SESSION", "")

    # ✅ Max file size limit (4GB = 4096 MB)
    MAX_FILE_SIZE = int(os.environ.get("MAX_FILE_SIZE", 4096)) * 1024 * 1024  # bytes mein


class Txt(object):
    # part of text configuration
    START_TXT = """Hello {} 👋 

➻ This Is An Advanced And Yet Powerful Rename Bot.

➻ Using This Bot You Can Rename And Change Thumbnail Of Your Files.

➻ You Can Also Convert Video To File And File To Video.

➻ This Bot Also Supports Custom Thumbnail And Custom Caption.

<b>Bot Is Made By :</b> @MadflixBotz"""

    ABOUT_TXT = """
╭───────────────⍟
├<b>🤖 My Name</b> : {}
├<b>🖥️ Developer</b> : <a href=https://t.me/MadflixBotz>MadflixBotz</a> 
├<b>👨‍💻 Programer</b> : <a href=https://t.me/MadflixSupport>Jishu Developer</a>
├<b>📕 Library</b> : <a href=https://github.com/pyrogram>Pyrogram</a>
├<b>✏️ Language</b> : <a href=https://www.python.org>Python 3</a>
├<b>💾 Database</b> : <a href=https://cloud.mongodb.com>Mongo DB</a>
├<b>📊 Build Version</b> : <a href=https://instagram.com/jishukumarsinha>Rename v4.7.0</a></b>     
╰───────────────⍟
"""

    HELP_TXT = """
🌌 <b><u>How To Set Thumbnail</u></b>
  
➪ /start - Start The Bot And Send Any Photo To Automatically Set Thumbnail.
➪ /del_thumb - Use This Command To Delete Your Old Thumbnail.
➪ /view_thumb - Use This Command To View Your Current Thumbnail.

📑 <b><u>How To Set Custom Caption</u></b>

➪ /set_caption - Use This Command To Set A Custom Caption
➪ /see_caption - Use This Command To View Your Custom Caption
➪ /del_caption - Use This Command To Delete Your Custom Caption
➪ Example - <code>/set_caption 📕 Name ➠ : {filename}

🔗 Size ➠ : {filesize} 

⏰ Duration ➠ : {duration}</code>

✏️ <b><u>How To Rename A File</u></b>

➪ Send Any File And Type New File Name And Select The Format [ Document, Video, Audio ].           

𝗔𝗻𝘆 𝗢𝘁𝗵𝗲𝗿 𝗛𝗲𝗹𝗽 𝗖𝗼𝗻𝘁𝗮𝗰𝘁 :- <a href=https://t.me/MadflixSupport>Developer</a>
"""

    PROGRESS_BAR = """\n
 <b>🔗 Size :</b> {1} | {2}
️ <b>⏳️ Done :</b> {0}%
 <b>🚀 Speed :</b> {3}/s
️ <b>⏰️ ETA :</b> {4}
"""

    DONATE_TXT = """
<b>🥲 Thanks For Showing Interest In Donation! ❤️</b>

If You Like My Bots & Projects, You Can 🎁 Donate Me Any Amount From 10 Rs Upto Your Choice.

<b>🛍 UPI ID:</b> `kumarjishusinha@ibl`
"""


    SEND_METADATA = """<b><u>🖼️  HOW TO SET CUSTOM METADATA</u></b>

For Example :-

<code>By :- @MadflixBotz</code>

💬 For Any Help Contact @MadflixSupport
"""


# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @MadflixBotz
# Backup Channel @JishuBotz
# Developer @JishuDeveloper
# Contact @MadflixSupport
