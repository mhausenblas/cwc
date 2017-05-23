#!/usr/bin/env python

"""
An example app server with an HTTP API.

@author: Michael Hausenblas, http://mhausenblas.info/#i
@since: 2017-05-22
"""

import logging
import os
import json
import tornado.ioloop
import tornado.web
import random
import time

from tornado.escape import json_encode

DEBUG = True

##############################################################################
# The following enviroment variables can be overridden:

# By default the app server serves on 9876 but you can
# make it listen on a different port by setting the env
# variable `CWCPORT` (note that the app server listens on
# all network interfaces, i.e. 0.0.0.0).
PORT = os.getenv('CWCPORT', 9876)

# Defines the current version of the app server:
VERSION = '0.5'

if DEBUG:
  FORMAT = "%(asctime)-0s %(levelname)s %(message)s [at line %(lineno)d]"
  logging.basicConfig(level=logging.DEBUG, format=FORMAT, datefmt="%Y-%m-%dT%I:%M:%S")
else:
  FORMAT = "%(asctime)-0s %(message)s"
  logging.basicConfig(level=logging.INFO, format=FORMAT, datefmt="%Y-%m-%dT%I:%M:%S")


class Health(tornado.web.RequestHandler):
  def get(self):
    """
    Handles `/healthz` resource.
    """
    try:
      logging.info("/healthz serving from %s has been invoked from %s", self.request.host, self.request.remote_ip)
      self.set_header("Content-Type", "application/json")
      self.write(json_encode(
        {
          "status" : "all is well"
        }
      ))
      self.finish()
    except Exception, e:
      logging.debug(e)
      self.set_status(404)

class Info(tornado.web.RequestHandler):
  def get(self):
    """
    Handles `/info` resource.
    """
    try:
      logging.info("/info serving from %s has been invoked from %s", self.request.host, self.request.remote_ip)
      self.set_header("Content-Type", "application/json")
      self.write(json_encode(
        {
          "version" : VERSION,
          "running_on" : self.request.host,
          "request_from" : self.request.remote_ip
        }
      ))
      self.finish()
    except Exception, e:
      logging.debug(e)
      self.set_status(404)

if __name__ == "__main__":
  app = tornado.web.Application([
      (r"/healthz", Health),
      (r"/info", Info)
  ])
  app.listen(PORT, address='0.0.0.0')
  logging.info("This is the CWC service in version v%s listening on port %s", VERSION, PORT)
  tornado.ioloop.IOLoop.current().start()
