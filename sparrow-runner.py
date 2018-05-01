#!/usr/bin/env python

import subprocess
import argparse

options = argparse.ArgumentParser(description='Sparrow wrapper.')
options.add_argument("--format", type=str, help="format", nargs="?")
options.add_argument('sparrow_target', metavar="target", type=str, help='Your task or name of plugin')
options.add_argument('params', metavar="params", type=None, help="Parameters for action", nargs="*")
args = vars(options.parse_args())

sparrow_target = args["sparrow_target"]
params = args["params"]
format_opt = args["format"]




if "/" in sparrow_target:
    sparrow_basic_part = "task"
else:
    sparrow_basic_part = "plg"



cmd = ["sparrow", sparrow_basic_part, "run", sparrow_target ]

while len(params) > 0:
    for i, val in enumerate(params):
        param = "%s=%s" %( params[0], params[1] )
        cmd.append('--param')
        cmd.append(param)
        del params[:2]

if format_opt:
    cmd.append("--format")
    cmd.append("%s" %( format_opt ))

#print cmd

subprocess.call(cmd)
