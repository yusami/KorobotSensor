import time
import sensor
import os
import tweepy
from dotenv import load_dotenv

def main():
    # Twitter configs
    load_dotenv(verbose=True)
    CONSUMER_KEY = os.environ.get("TW_CONSUMER_KEY")
    assert CONSUMER_KEY != None, "TW_CONSUMER_KEY should be configured."
    CONSUMER_SECRET = os.environ.get("TW_CONSUMER_SECRET")
    assert CONSUMER_SECRET != None, "TW_CONSUMER_SECRET should be configured."
    ACCESS_TOKEN = os.environ.get("TW_TOKEN")
    assert CONSUMER_KEY != None, "TW_TOKEN should be configured."
    ACCESS_SECRET = os.environ.get("TW_TOKEN_SECRET")
    assert CONSUMER_KEY != None, "TW_TOKEN_SECRET should be configured."

    # Twitter client
    client = tweepy.Client(
        consumer_key = CONSUMER_KEY,
        consumer_secret = CONSUMER_SECRET,
        access_token = ACCESS_TOKEN,
        access_token_secret = ACCESS_SECRET
    )
  
    # Fetch the sensor data
    item = None
    for i in range(10):
        item = sensor.main()
        if item != None:
            break
        # Wait a while and retry if an error occurs
        print("-Retrying...")
        time.sleep(5)

    # No date is avaiable so we have nothing to do here
    if item == None:
        print("No sensor date is available")
        sys.exit(1)
    msg = "Time:{0[0]}, Temperature:{0[1]} degrees, Humidity:{0[2]}%, Air pressure:{0[3]}hPa".format(item)
    print(msg)

    # Post a message
    client.create_tweet(text=msg)
    print("Tweet is done successfully.")

if __name__ == '__main__':
    main()
