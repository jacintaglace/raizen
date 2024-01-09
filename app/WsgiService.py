from gevent import monkey as curious_george
curious_george.patch_all()

import gunicorn.app.base
import gunicorn
from gunicorn import glogging 
from gunicorn.workers import sync
import gevent 
import gunicorn.workers.ggevent

class StandaloneApplication(gunicorn.app.base.BaseApplication):

    def __init__(self, app, options=None):
        self.options = options or {}
        self.application = app
        super().__init__()

    def load_config(self):
        config = {key: value for key, value in self.options.items()
                  if key in self.cfg.settings and value is not None}
        for key, value in config.items():
            self.cfg.set(key.lower(), value)

    def load(self):
        return self.application