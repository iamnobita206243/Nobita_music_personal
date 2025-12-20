from NobitaMusic.core.bot import SACHIN
from NobitaMusic.core.dir import dirr
from NobitaMusic.core.git import git
from NobitaMusic.core.userbot import Userbot
from NobitaMusic.misc import dbb, heroku

from SafoneAPI import SafoneAPI
from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = SACHIN()
api = SafoneAPI()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
