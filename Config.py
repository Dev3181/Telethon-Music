import os

class Config(object):
    API_ID = int(os.environ.get("API_ID", "6213538"))
    API_HASH = os.environ.get("API_HASH", "8ce3522bd21cc937eee4c68813d501d5")
    BOT_TOKEN = os.environ.get("BOT_TOKEN",5624218847:AAH5OjoF5BfFREMhPq5H1yRtKO7xBfV0yyo)
    STRING_SESSION = os.environ.get("STRING_SESSION", 1BVtsOGcBu4aYPM4-bW2apejWQVxJq0e-4FRgPw2qBhGMraRh2eQx_gkamcb6nyk4a0gx7Xf3-mFBDQ9Rzlt33_BBBRVzZ-hUe-oDmOKDE8wY57rPSrqt3-rQWKTvdhQenJBUtKA8IwsF_tsT1Kx3yYqdMSWPOgGC_lRY071Ig8AEtXg0VeOxD5F-el4VdF-e5YsNMBaXm4mPlhcuaAOIAr_iORK8R39z3ovL9ZmGI-2NTYN1ZIPIn7ZfD-goDLMemDy2cYxsI-ACczkniqC1RvxJdzj6ltpiBFBCvm5Vs6UemqBxOhzywq3mae7oukurUIVDUvsqWORLF2Juoryc1tcYyNA2M8w=)
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
