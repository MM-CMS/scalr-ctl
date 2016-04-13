__author__ = 'Dmitriy Korsakov'

import os

CONFIG_DIRECTORY = os.path.expanduser(os.environ.get("SCALRCLI_HOME", os.path.join(os.path.expanduser("~"), ".scalr")))
CONFIG_PATH = os.path.join(CONFIG_DIRECTORY, "%s.yaml" % os.environ.get("SCALRCLI_PROFILE", "default"))
