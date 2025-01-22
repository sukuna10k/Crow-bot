import os
import logging
from logging.handlers import RotatingFileHandler




BOT_TOKEN = os.environ.get("BOT_TOKEN", "7783135016:AAEDA3NoMMtHpgjf5CroaQAHMkP-VC859k0")
API_ID = int(os.environ.get("API_ID", "24817837"))
API_HASH = os.environ.get("API_HASH", "acd9f0cc6beb08ce59383cf250052686")


OWNER_ID = int(os.environ.get("OWNER_ID", "7428552084"))
DB_URL = os.environ.get("DB_URL", "")
DB_NAME = os.environ.get("DB_NAME", "madflixbotz")


CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002450406603"))
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1002450406603"))


FILE_AUTO_DELETE = int(os.getenv("FILE_AUTO_DELETE", "389")) # auto delete in seconds


PORT = os.environ.get("PORT", "8080")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))



try:
    ADMINS=[7428552084]
    for x in (os.environ.get("ADMINS", "7428552084").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")









CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

DISABLE_CHANNEL_BUTTON = True if os.environ.get('DISABLE_CHANNEL_BUTTON', "True") == "True" else False

BOT_STATS_TEXT = "<b>BOT UPTIME :</b>\n{uptime}"







USER_REPLY_TEXT = "❌Ne m'envoyer pas directement de message.\n\nsur @anime_crow & @AntiFlix_A🔥" 

START_MSG = os.environ.get("START_MESSAGE", "**Salut** {mention}\n\n» Bienvenue dans ⚡️⚡️**__Anti-Crow__**⚡️⚡\n\n» Je suis Marsh Mello - Un bot avancé pour fournir des fichiers anime et films.\n\n» Vous devez rejoindre mes chaînes @Anime_Crow et @AntiFlix_A  pour m'utiliser.\n\n» Profitez de votre expérience de visionnage d'animes. et series.")

FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Salut {mention}\n\n<b>Veuillez rejoindre mon canal mon canal pour pouvoir récupérer votre fichier</b>")





ADMINS.append(OWNER_ID)
ADMINS.append(7428552084)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
   





# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Madflix_Bots
# Backup Channel @JishuBotz
# Developer @JishuDeveloper
