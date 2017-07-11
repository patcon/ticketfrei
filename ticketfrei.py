import pytoml as toml
import time
import traceback

from retootbot import RetootBot
from retweetbot import RetweetBot
from trigger import Trigger


if __name__ == '__main__':
    # read config in TOML format (https://github.com/toml-lang/toml#toml)
    with open('ticketfrei.cfg') as configfile:
        config = toml.load(configfile)

    trigger = Trigger(config)

    mbot = RetootBot(config, trigger)
    tbot = RetweetBot(trigger, config)

    try:
        statuses = []
        while True:
            statuses = mbot.retoot(statuses)
            statuses = tbot.flow(statuses)
            time.sleep(10)
    except:
        traceback.print_exc()
        tbot.shutdown()
