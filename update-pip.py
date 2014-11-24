#!/usr/bin/env python

"""
Update all the packages (in alphabetical order)
that you have installed globally with pip
(i.e. with `sudo pip install`).

http://pythonadventures.wordpress.com/2013/05/22/update-all-pip-packages/

Jabba Laci, 2013--2014 (jabba.laci@gmail.com)

Modified to accept arguments
Rafael Kueng, 2014-11-24 (rafi.kueng@gmx.ch)
"""

from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import os
import pip
import argparse

parser = argparse.ArgumentParser()
#parser.add_argument("--verbosity", help="increase output verbosity")
group = parser.add_mutually_exclusive_group()
group.add_argument("-d", "--dry",    help="do a dryrun (print commands to stdout instead of running)", action="store_true")
group.add_argument("-l", "--list",   help="list packages that will be updated", action="store_true")
group.add_argument("-u", "--update", help="update packages (asks for sudo if not in venv)", action="store_true")
args = parser.parse_args()


dists = []
for dist in pip.get_installed_distributions():
    dists.append(dist.project_name)

dists = sorted(dists, key=lambda s: s.lower())
dists.insert(0, 'pip')  # let 'pip' be the first

if args.dry or args.list or args.update:
    for dist_name in dists:
        if args.list:
            print(dist_name)
            continue
        cmd = "sudo pip install {0} -U".format(dist_name)
        print('#', cmd)
        if args.update:
            os.system(cmd)
else:
    parser.print_help()
