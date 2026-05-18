"""
helper/upload_helper.py
✅ 4GB File Upload Helper
Is file ko  helper/  folder mein rakho.
plugins/file_rename.py mein import karo:
    from helper.upload_helper import get_upload_client
"""

from config import Config


async def get_upload_client(bot, file_size: int):
    """
    File size ke hisaab se sahi client return karta hai.
    
    - 2GB tak  → normal bot client (bot)
    - 2GB se zyada → user client (4GB support)
    
    Returns: (client, error_message)
    - agar 4GB se badi file hai → (None, error_msg)
    - agar STRING_SESSION nahi set → (None, error_msg)  
    - warna → (client_object, None)
    """
    limit_2gb = 2 * 1024 * 1024 * 1024   # 2,147,483,648 bytes
    limit_4gb = 4 * 1024 * 1024 * 1024   # 4,294,967,296 bytes

    # 4GB se badi file — koi bhi nahi upload kar sakta
    if file_size > limit_4gb:
        size_gb = file_size / (1024 ** 3)
        return None, (
            f"❌ **File too large!**\n\n"
            f"📦 File Size: `{size_gb:.2f} GB`\n"
            f"🚫 Maximum allowed: `4 GB`\n\n"
            f"Telegram 4GB se badi files support nahi karta."
        )

    # 2GB se badi file — user client chahiye
    if file_size > limit_2gb:
        if not Config.STRING_SESSION:
            size_gb = file_size / (1024 ** 3)
            return None, (
                f"❌ **File 2GB se badi hai!**\n\n"
                f"📦 File Size: `{size_gb:.2f} GB`\n\n"
                f"4GB support ke liye owner ko `STRING_SESSION` "
                f"environment variable set karni hogi.\n\n"
                f"💡 Telegram Premium account ka string session chahiye."
            )
        # User client import karo bot.py se
        from bot import user
        return user, None

    # Normal file — bot client use karo
    return bot, None


def readable_size(size_bytes: int) -> str:
    """Bytes ko human-readable format mein convert karta hai"""
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size_bytes < 1024.0:
            return f"{size_bytes:.2f} {unit}"
        size_bytes /= 1024.0
    return f"{size_bytes:.2f} TB"
