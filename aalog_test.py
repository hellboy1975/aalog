"""
this file is here as a helper to debug CLI commands.  In theory
there should be no need to do a python install prior to testing using
this script, however it will need to be changed manually to access
the CLI commands
"""
import aalog.cli as cli

if __name__ == '__main__':
    cli.init()
