#!/usr/bin/env python2

import sys
import subprocess
from optparse import OptionParser

#options = OptionParser()
#options.add_option("--format", attr=value, help="format")

sparrow_target = sys.argv[1]

if "/" in sparrow_target:
    sparrow_basic_part = "task"
else:
    sparrow_basic_part = "plg"

del sys.argv[:2]

cmd = ["sparrow", sparrow_basic_part, "run", sparrow_target]
while len(sys.argv) > 0:
    for i, val in enumerate(sys.argv):
        param = "%s=%s" %( sys.argv[0], sys.argv[1] )
        cmd.append('--param')
        cmd.append(param)
        del sys.argv[:2]

subprocess.call(cmd)
