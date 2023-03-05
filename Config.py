import os

class Config(object):
    API_ID = int(os.environ.get("API_ID", "27156263"))
    API_HASH = os.environ.get("API_HASH", "81a4bcf394d694683072f4aa998ef09d")
    BOT_TOKEN = os.environ.get("BOT_TOKEN","5869357822:AAGFb6zohtURbU-d5xEbJJCrmKUeBZccWfQ")
    STRING_SESSION = os.environ.get("STRING_SESSION","1BVtsOGoBuz0P30WBE6EqC8GWs0kF2-iZ9-44OFGqHcy9GQF7nPJKbedNBpJ3YRT2w-0wgbwXN1ortql5mEQP6MxNF1bXSOD7zu2Jlqe3hFTfLoQMavfpI0MLCpcLuBIiDWiSHBNqkRm8isX9RUyuoIvV-J0feIlYJmo1vg40sAxq2qzMGAEd5GThmDG_qr_YTb7ltM6gCMFYNnson0kNay7CFYFNOBxrA-kzDZEPQuXwSe6N9hLng0pNsAkBPRUolNmMsmqzFNvqeuF3rMt42ZJnEm2OWi0vEXDw0Zv2Dr7bTWVrT-6_zF5e6Bp3y-MAXFjpBGjRyHVT_1b7gw8qA1z7a1TpmWQ=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "Electron_music_bot")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "6254798968")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
