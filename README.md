# KorobotSensor

## Overview

* Fetch the sensor values and tweet them.

## Description

* Fetch the sensor values via [PLANEX API](https://www.planex.co.jp/products/ws-usb/).
* Convert the time to Japanese local time (JST).
* Tweet the latest values.

## Requirement

* Python 3.7
* Twitter API keys
* [PLANEX Sensor WS-USB01-THP](https://amzn.to/38yjbJc) and [API keys](https://www.planex.co.jp/products/ws-usb/)

## Install

~~~
$ pip3 install python-dotenv pytz python-dateutil twitter
~~~

## Usage

* Call the command below.

~~~
$ python3 main.py
~~~

## TODO

1. xxx

## Caveats

* xxx

## Licence

* Copyright &copy; 2020 yusami
* Licensed under the [Apache License, Version 2.0][Apache]

[Apache]: http://www.apache.org/licenses/LICENSE-2.0


## Author

* [yusami](https://github.com/yusami)
