from os.path import join
import logging

BASE_URL_LIVE = "https://www.bitmex.com/api/v1/"

BASE_URL_TESTING = "https://testnet.bitmex.com/api/v1/"

# The BitMEX API requires permanent API keys. Go to https://testnet.bitmex.com/api/apiKeys to fill these out.
# for TESTING mode
# https://www.bitmex.com/api/apiKeys for LIVE mode
API_KEY = "2v-iYbQDZ89Ns8j4sHhxrAUE"
API_SECRET = "OPUbrYBPPQ81HO7sCAldv0pOH7ropy_wF-dxd8AEKl8vpDoi"


# Instrument to market make on BitMEX.
SYMBOL = "XBTUSD"

# order amount for bitmex in USD
POSITION = 10000

# tick interval used for mcad data
TICK_INTERVAL = '30m'

STOP_LOSS_FACTOR = 0.007
STOP_PROFIT_FACTOR = 0.01
# There is two mode one is TESTING and other is LIVE
MODE = "TESTING"

INTERVAL = 0.002

RELIST_INTERVAL = 0.01

CHECK_POSITION_LIMITS = False
MIN_POSITION = -10000
MAX_POSITION = 10000

LOOP_INTERVAL = 5

# Wait times between orders / errors
API_REST_INTERVAL = 1
API_ERROR_INTERVAL = 10


# Available levels: logging.(DEBUG|INFO|WARN|ERROR)
LOG_LEVEL = logging.INFO
ORDERID_PREFIX = "sam_bitmex_"

# If any of these files (and this file) changes, reload the bot.
WATCHED_FILES = [join("bitmex_bot", f) for f in ["bitmex_bot.py", "bitmex_historical.py", __file__]]


