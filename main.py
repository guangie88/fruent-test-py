#!/usr/bin/env python
from fluent import sender
import json
import sys

if len(sys.argv) != 2:
    sys.exit('Usage: script <JSON serializable string>')

s = sys.argv[1]

try:
    logger = sender.FluentSender('app', host='127.0.0.1', port=24224)
    logger.emit('py', json.loads(s))
    print('Sent {}'.format(s))
except Exception as e:
    print('Error: {}'.format(e))

