from os import getenv
from dotenv import load_dotenv

admins = {}
load_dotenv()

# client vars
API_ID  =  int ( getenv ( "API_ID" ، "23559116" ))
API_HASH  =  getenv ( "API_HASH" ، "ac878ed19ca558e9a23e891098e328af" )
BOT_TOKEN = getenv("BOT_TOKEN", "5783978621:AAHJoLEsec64khzOwXH6XdDy6XoT5miuFTo")
SESSION_NAME = getenv("SESSION_NAME", "AgBSLjNibN9S2HnQstcyD-YtJqKgnN-yCx3JIzsw29IkPgWhzogVRKDCpvuXR1gMdIf9Iltxb5sFIvAeAkp_iE7fR3vvHneN9bSa0UzvyDs2S3AhCE53PSgRG7lcQIM3ZxqOxGHCFdAX4zC5KJbNgExe-3Q8L3gWmIsi9roQ1Djj-uZlMRDItP2wAprog1oQQdau2-TsyoJrstEQnHVm8sbBilyZh-nJ7GFjdNDzz5-4gC9qXCD46OlHntbaE2JxaxXaDSgxIUOPIlzIe8BW3R4C0TQip7Nwv6Ys3v0XJL0dO5ak6T4kWQzfU-BjsVETDF3pCT3Ociu5XdLMu-RD3PuuAAAAATS8SQwA")

# mandatory vars
OWNER_USERNAME  =  getenv ( "OWNER_USERNAME" ، "OI_I6" )
ALIVE_NAME = getenv("ALIVE_NAME", "sonng")
BOT_USERNAME = getenv("BOT_USERNAME", "OOII5BOT")
UPSTREAM_REPO  =  getenv ( "UPSTREAM_REPO" ، "https://github.com/vxl3/MyBot" )
UPSTREAM_BRANCH = getenv("UPSTREM_BRANCH", "main")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
GROUP_SUPPORT  =  getenv ( "GROUP_SUPPORT" ، "MUSICIQD" )
UPDATES_CHANNEL  =  getenv ( "UPDATES_CHANNEL" ، "I404P" )

# database, decorators, handlers mandatory vars
MONGODB_URL = getenv("MONGODB_URL", "mongodb+srv://veez:mega@cluster0.heqnd.mongodb.net/veez?retryWrites=true&w=majority")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! . $").split())
OWNER_ID  =  list ( map ( int ، getenv ( "OWNER_ID" ، "5179721996" ). split ()))
SUDO_USERS  =  قائمة ( خريطة ( int ، getenv ( "SUDO_USERS" ، "5179721996" ). split ()))

# image resources vars
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.png")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.png")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/d70bb6fa92728763c671f.png")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/430dcf25456f2bb38109f.png")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/cd5c96a3c7e8ae1913ef3.png")
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/c83b000f004f01897fe18.png")
