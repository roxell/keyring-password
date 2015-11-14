#!/usr/bin/python
import sys
import keyring

try:
    servicename, username = sys.argv[1:]
except ValueError as e:
    print 'Error parsing arguments: %s' % (e,)
    print 'Usage: %s SERVICENAME USERNAME' % (sys.argv[0],)
    sys.exit(1)

password = keyring.get_password(servicename, username)
if password:
    print password

# vim: set ts=8 sw=4 sts=4 et tw=80 fileencoding=utf-8 :
