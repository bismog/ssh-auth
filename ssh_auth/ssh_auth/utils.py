#!/usr/bin/env python
# -*- coding: utf8 -*-

import os
import logging
import logging.config
import yaml
# import StringIO

PATH = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = '{}/log_config.yaml'.format(PATH)

# Loading config. Of course this is in another file in the real life

# global_config = yaml.load(StringIO.StringIO(YAML_CONF))
with open(CONFIG_PATH, 'r') as f:
    global_config = yaml.load(f.read())

# Configuring logging with the subset of the dict
#

logging.config.dictConfig(global_config['logging'])
