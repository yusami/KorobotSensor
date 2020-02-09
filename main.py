import config
import sensor
from twitter import *

def main():
    tw = Twitter(auth=OAuth(config.TW_TOKEN, config.TW_TOKEN_SECRET, config.TW_CONSUMER_KEY, config.TW_CONSUMER_SECRET))
  
    # Post a message
    items = sensor.main()
    # print("-time:{0[0]}, temperature:{0[1]}degrees, humidity:{0[2]}%, air pressure:{0[3]}hPa".format(item))
    msg = "Time:{0[0]}, Temperature:{0[1]} degrees, Humidity:{0[2]}%, Air pressure:{0[3]}hPa".format(items)
    print(msg)
    tw.statuses.update(status=msg)
    print("Tweet is done successfully.")

if __name__ == '__main__':
    main()

