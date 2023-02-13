from os import getenv
from dotenv import load_dotenv

admins = {}
load_dotenv()

# client vars
API_ID  =  int ( getenv ( "API_ID" ، "28407968" ))
API_HASH  =  getenv ( "API_HASH" ، "422126161e78bfd7ab9ffa28a15a23f3" )
BOT_TOKEN = getenv("BOT_TOKEN", "6163660815:AAEnVDRJuLF3CYenahT8Yjklp8s2vb4YRHw")
SESSION_NAME = getenv("SESSION_NAME", "AgBjEzA6rDp9TO3dstx2z0fOWu5WyFtMO-FSQvkxHQwAL5zHQRxcHe-Fk8-8DUwfQ3oe3FUKdBzw17S4gsHPcv-vSWnmMlVKebAoAJ2IbCLzCJL4jF-378OjVvIHd9isAkmRO95B5cd_A2zbBAKkpJ7TEEOZSMHBq1_WmO-ICfnFzSb9urtbVyG7m-1fVoNo-w6MoNNzzcunjRIUS-5INKlhyBdL5DZ-ydojfADRm-ohcFAj_m5f-Qopkel0J1vkSDqsSarG8HPRdDhQ4Wc5p4mME2BFUIruJkkIbm-qVvLfxxXqawAZVDtS9hGdemHi52EMEX6I70AX4ZLwkQLYhOjKAAAAAXN7xnEA")
# mandatory vars
OWNER_USERNAME  =  getenv ( "OWNER_USERNAME" ، "U33I7" )
ALIVE_NAME = getenv("ALIVE_NAME", "sonng")
BOT_USERNAME = getenv("BOT_USERNAME", "DHQOBoT")
UPSTREAM_REPO  =  getenv ( "UPSTREAM_REPO" ، "https://github.com/D3NE" )
UPSTREAM_BRANCH = getenv("UPSTREM_BRANCH", "main")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
GROUP_SUPPORT  =  getenv ( "GROUP_SUPPORT" ، "MUSICIQD" )
UPDATES_CHANNEL  =  getenv ( "UPDATES_CHANNEL" ، "N3ZU1" )

# database, decorators, handlers mandatory vars
MONGODB_URL = getenv("MONGODB_URL", "mongodb+srv://veez:mega@cluster0.heqnd.mongodb.net/veez?retryWrites=true&w=majority")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! . $").split())
OWNER_ID  =  list ( map ( int ، getenv ( "OWNER_ID" ، "28407968" ). split ()))
SUDO_USERS  =  قائمة ( خريطة ( int ، getenv ( "SUDO_USERS" ، "28407968" ). split ()))

# image resources vars
IMG_1 = getenv("IMG_1","https://telegra.ph//file/490b818b5b636fcc085b8.jpg")
IMG_2 = getenv("IMG_2", "https://telegra.ph//file/d3700c6e3a4cd2701d6a1.jpg")
IMG_3 = getenv("IMG_3", "https://telegra.ph//file/17c9eb59f87c31aa7b224.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/402c519808f75bd9b1803.jpg")
IMG_5 = getenv("IMG_5", "https://telegra.ph//file/beaf049a125e4d68a0a74.jpg")
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph//file/490b818b5b636fcc085b8.jpg")
