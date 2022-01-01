# KorobotSensor

## Overview

* Fetch the sensor values and tweet them.

## Description

* Fetch the sensor values via [PLANEX API](https://www.planex.co.jp/products/ws-usb/).
* Convert the time to Japanese local time (JST).
* Tweet the latest values.

## Requirement

* [Python 3.9](https://www.python.org/downloads/)
* [Twitter Access tokens](https://developer.twitter.com/ja/docs/basics/authentication/guides/access-tokens)
* [PLANEX Sensor WS-USB01-THP](https://amzn.to/38yjbJc) and [API keys](https://www.planex.co.jp/products/ws-usb/)

## Install

~~~
$ pip3 install python-dotenv pytz python-dateutil twitter
~~~

## Usage

* Set API keys in `.env` file.

~~~
TW_CONSUMER_KEY=...
TW_CONSUMER_SECRET=...
TW_TOKEN=...
TW_TOKEN_SECRET=...
SENSOR_MAC=...
SENSOR_TOKEN=...
~~~

* Call the command below.

~~~
$ python3 main.py
~~~

* Example output:

~~~
Time:2020-02-16T11:48:02+09:00, Temperature:25.47 degrees, Humidity:49.1%, Air pressure:1007.37hPa
~~~

## TODO

1. xxx

## Caveats

* xxx

## Licence

* Copyright &copy; 2020-2022 yusami
* Licensed under the [Apache License, Version 2.0][Apache]

[Apache]: http://www.apache.org/licenses/LICENSE-2.0


## Author

* [yusami](https://github.com/yusami)
