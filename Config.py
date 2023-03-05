import os

class Config(object):
    API_ID = int(os.environ.get("API_ID", "27156263"))
    API_HASH = os.environ.get("API_HASH", "81a4bcf394d694683072f4aa998ef09d")
    BOT_TOKEN = os.environ.get("BOT_TOKEN","5869357822:AAGFb6zohtURbU-d5xEbJJCrmKUeBZccWfQ")
    STRING_SESSION = os.environ.get("1BVtsOGwBuyhYvj4TRV1BqSCP3FHdEbrWVvJQEv1-19VbehmLx7fSLdTsjrZ6EHdesOzOckw_Nc2trMEuDE7Q4uP4RwLRoGCG91dD3A6RgV_NOalAmJfemw5lDNM6JxAPEzdJXno7yNrfT9uIo1t4CvGIGvMR2HB4ok65nHrvE_n7mcxOwN5SumBoTFy4e_JeuVZILXapOIdJvlT1ARyerigfOiGKeJW4F86YDRFFGATIw8bw7B5QSw7VsdYuG1lW1qsZlEupli8T99-wtjGWPtIHhrZ0R2pmIE6fREScim4R90qFJGS47RengwIXl_RogW3J6jAFV4OJCrpoJINuZL6IGOXuU64=")
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
