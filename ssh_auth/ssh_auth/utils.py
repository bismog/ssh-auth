#!/usr/bin/env python
# -*- coding: utf8 -*-

import logging
import logging.config
import yaml
# import StringIO

# Loading config. Of course this is in another file in the real life

# global_config = yaml.load(StringIO.StringIO(YAML_CONF))
with open('log_config.yaml', 'r') as f:
    global_config = yaml.load(f.read())

# Configuring logging with the subset of the dict
#

logging.config.dictConfig(global_config['logging'])
