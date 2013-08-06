# code copied shamelessly from here:
# http://code.activestate.com/recipes/65287-automatically-start-the-debugger-on-an-exception/

import sys

def _info(type, value, tb):
    if hasattr(sys, 'ps1') or not sys.stderr.isatty():
        # we are in interactive mode or we don't have a tty-like
        # device, so we call the default hook
        sys.__excepthook__(type, value, tb)
    else:
        import traceback, pdb, platform, os
        
        # if we're on Mac OS X, make the beep noise and alert the system:
        if platform.system() == "Darwin":
            os.system("tput bel")
            
        # we are NOT in interactive mode, print the exception...
        traceback.print_exception(type, value, tb)
        print
        
        # ...then start the debugger in post-mortem mode.
        pdb.pm()

def enable(warn=False):
    """enable breaking into the debugger on an unhandled exception.
    use warn=True to print a warning if inactive because you're already in an 
    interactive terminal."""
    sys.excepthook = _info
    if warn and hasattr(sys, 'ps1') or not sys.stderr.isatty():
        print """
pycatch warning: this is an interactive session, so not using custom PDM activation."""

