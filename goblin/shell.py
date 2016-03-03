from __future__ import unicode_literals
from goblin import connection
from goblin import models
from goblin import properties
from goblin import gremlin
from goblin import exceptions

import readline
import code
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--host", help="Enter the hostname of the graph database")
parser.add_argument(
    "--username", help="Enter the username associated with the graph database")
parser.add_argument(
    "--password", help="Enter the password associated with the graph database")
parser.add_argument("--database", help="Enter the graph database name")
args = parser.parse_args()

if not args.host:
    args.host = 'localhost'
if not args.username:
    args.username = ''
if not args.password:
    args.password = ''
if not args.database:
    args.database = 'graph'

hd = connection._parse_host(
    args.host, args.username, args.password, args.database)
host = hd.get('host', 'localhost')
port = hd.get('port', 8184)
username = hd.get('username', '')
password = hd.get('password', '')
graph_name = hd.get('graph_name', 'graph')

connection.setup(
    [host, ], graph_name=graph_name, username=username, password=password)

del args, parser, username, password, hd


class __help_object(object):

    def __repr__(self):
        return """The following have already been imported:
  - goblin.connection as connection
  - goblin.models as models
  - goblin.properties as properties
  - goblin.gremlin as gremlin
  - goblin.exceptions as exceptions"""

    def __str__(self):
        return self.__repr__()

    def __unicode__(self):
        return self.__repr__()

HELP = __help_object()

vars = globals().copy()
vars.update(locals())

shell = code.InteractiveConsole(vars)
shell.interact(
    banner="Goblin GraphDB Shell. Connected to %s:%s on graph `%s`. Type 'HELP' for available commands"
    % (host, port, graph_name))
