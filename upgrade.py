#!/usr/bin/env python

from os import *
import sys
import argparse
import pdb

parser = argparse.ArgumentParser(description="Upgrade React apps from 0.10.x to 0.12.x")
parser.add_argument("-a", "--all", required=False, action='store_true', help="Skip y/n/q prompt and search for all changes. You will be able to review changes before committing.")
parser.add_argument("path", help="Directory of your React app to upgrade")
args = parser.parse_args()

print args.path
if path.isdir(args.path) is False:
  parser.print_help()
  sys.exit("\nDirectory does not exist: " + args.path + "\n")

renameComponentMethods = True
renameCreateClassToFactory = True

codemod = "./bin/codemod.py"

def confirm():
  if args.all == True:
    return True

  ch = sys.stdin.readline().rstrip('\n')
  if ch == "\n" or ch == "y":
    return True
  if ch == "n":
    return False
  elif ch == "q":
    sys.exit()
  else:
    print "sorry, didn\'t understand"

def sub(search, replace):
  print "\n\033[94mReplace:\n\n\033[91m    %s \033[0m with \033[92m %s \033[0m \033[93m\n\n[y,n,q]\033[0m " % (search, replace),
  good = confirm()

  if good:
    cmd = ("%s -m --extensions js,coffee -d %s %s %s" % (codemod, args.path, search, replace))
    print "\n\n"
    system(cmd)

def subString(search, replace):
  searchTermS = "\"\'%s\'\"" % (search)
  replaceTermS  = "\"\'%s\'\"" % (replace)
  searchTermD = '\'\"%s\"\'' % (search)
  replaceTermD  = '\'\"%s\"\'' % (replace)
  sub(searchTermS, replaceTermS)
  sub(searchTermD, replaceTermD)

def subMethod(search, replace):
  # pdb.set_trace()
  searchTerm = "'.%s\\('" % (search)
  replaceTerm  = "'.%s('" % (replace)
  sub(searchTerm, replaceTerm)

def subEvent(search, replace):
  searchTermCbk = "\"%s\"" % (eventToCbk(search))
  replaceTermCbk = "\"%s\"" % (eventToCbk(replace))

  sub(searchTermCbk, replaceTermCbk)
  subString(search, replace)


def subTerm(search, replace):
  searchTerm = "\"%s\"" % search
  replaceTerm = "\"%s\"" % replace
  sub(searchTerm, replaceTerm)

def subString(search, replace):
  searchTerm = "\"%s\"" % search
  replaceTerm = "\"%s\"" % replace
  sub(searchTerm, replaceTerm)

def subKey(search, replace):
  searchTerm = "\"%s:\"" % search
  replaceTerm = "\"%s:\"" % replace
  sub(searchTerm, replaceTerm)

def eventToCbk(event):
  parts = event.split(':')
  parts = [part.capitalize() for part in parts]
  cbk = "on"+ ''.join(parts)
  return cbk

def createFactoryMethod(search, replace):
  searchTerm = "\"%s\"" % search



#
#
#
# UPGRADER CHANGES - For more info look here <http://facebook.github.io/react/blog/2014/10/28/react-v0.12.html>
#
# ______                _     _   _                           _        _____           _
# | ___ \              | |   | | | |                         | |      |_   _|         | |
# | |_/ /___  __ _  ___| |_  | | | |_ __   __ _ _ __ __ _  __| | ___    | | ___   ___ | |
# |    // _ \/ _` |/ __| __| | | | | '_ \ / _` | '__/ _` |/ _` |/ _ \   | |/ _ \ / _ \| |
# | |\ \  __/ (_| | (__| |_  | |_| | |_) | (_| | | | (_| | (_| |  __/   | | (_) | (_) | |
# \_| \_\___|\__,_|\___|\__|  \___/| .__/ \__, |_|  \__,_|\__,_|\___|   \_/\___/ \___/|_|
#                                  | |     __/ |
#                                  |_|    |___/
#
#


if (renameComponentMethods):
  subMethod("renderComponent", "render")
  subMethod("renderComponentToString", "renderToString")
  subMethod("renderComponentToStaticMarkup", "renderToStaticMarkup")
  subTerm("isValidComponent", "isValidElement")
  subTerm("PropTypes.component", "PropTypes.element")
  subTerm("PropTypes.renderable", "PropTypes.node")
