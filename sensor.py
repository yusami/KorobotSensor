import urllib.request
import json
import config
import datetime
from pytz import timezone
from dateutil import parser

# Configs for the device
mac = config.SENSOR_MAC
token = config.SENSOR_TOKEN

def main():
    # Time range
    time_to = datetime.datetime.today().astimezone(timezone('UTC'))
    time_from = time_to - datetime.timedelta(hours=1)
    time_to_str = time_to.strftime("%Y-%m-%d+%H:%M:%S")
    time_from_str = time_from.strftime("%Y-%m-%d+%H:%M:%S")
    print(time_from_str,time_to_str)

# URL for planex cloud
    url='https://svcipp.planex.co.jp/api/get_data.php?type=WS-USB01-THP&mac=' + mac + '&from=' + time_from_str + '&to=' + time_to_str + '&token=' + token
    print(url)

# Call the request
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as res:
            # Parse the response
            items = json.load(res)
            if len(items) == 0:
                print("-Empty response")
                return None
            # print(items)
            for item in items:
                print(item)
                # Convert the time from UTC to JST
                dt = parser.parse(item[0]+"Z").astimezone(timezone('UTC'))
                # print(dt, dt.tzname())
                dt = dt.astimezone(timezone('Asia/Tokyo'))
                print("-local time:", dt, dt.tzname())
                # for i in item:
                    # print(i)
                # print("-temperature:{0}, humidity:{1}, air pressure:{2}".format(item[1], item[2], item[3]))

            # Print the latest data
            item = items[-1]
            dt = parser.parse(item[0]+"Z").astimezone(timezone('UTC'))
            item[0] = dt.replace(microsecond=0).astimezone(timezone('Asia/Tokyo')).isoformat()

            print("-time:{0[0]}, temperature:{0[1]} degrees, humidity:{0[2]}%, air pressure:{0[3]}hPa".format(item))

            return item
    except urllib.error.HTTPError as err:
        print("HTTP error: ", err.code)
    except urllib.error.URLError as err:
        print("HTTP error: ", err.reason)

if __name__ == '__main__':
    main()

