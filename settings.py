#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: huangshan
# datetime: 2019/12/20 2:13 PM
# software: PyCharm

from tornado.options import options, define
from pymongo import MongoClient
from common.config import MONGO_SETTINGS
import motor

define("port", default=9802, help="run on the given port", type=int)
define("config", default=None, help="tornado config file")
define("defbug", default=False, help="debug mode")
define("bind_ip", default="0.0.0.0", help="the bind ip")

settings = {}
settings["static_path"] = ''
settings['debug'] = True
settings['cookie_secret'] = "protagonisths@gmail.com-huangshan"
settings['xsrf_cookies'] = True
# settings['db'] = MongoClient(MONGO_SETTINGS['mongo']['host'], MONGO_SETTINGS['mongo']['port'])
settings['db'] = motor.MotorClient(MONGO_SETTINGS['mongo']['host'], MONGO_SETTINGS['mongo']['port'])
# if settings['debug']:
#     LOG_LEVEL = logging.DEBUG
# else:
#     LOG_LEVEL = logging.INFO
#
# if options.config:
#     tornado.options.parse_config_file(options.config)
