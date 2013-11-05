pycatch
=======

Module wrapper for a useful snippet that breaks into the PDB debugger on an unhandled exception.

*NEW:* in Mac OS X, this snippet now also makes a beep noise when an exception occurs, and in Lion or later will add a notification button to the terminal window in the doc and make the doc icon jump up and down for attention.

Note, I didn't write the snippet! it comes from [here](http://code.activestate.com/recipes/65287-automatically-start-the-debugger-on-an-exception/). As such, I am not releasing it "under a license" or anything, I'm just assuming it's public domain and that the wrapper and setup.py are trivial.

**Installation**

```
python setup.py install --user
```

**Usage**

```python
import pycatch
pycatch.enable()
# or, if you want a warning if it's not actually active:
pycatch.enable(warn=True)

# ipdb mode (requires ipython to be installed):
pycatch.enable(ipython=True)
```


note, as of 1.1, you can now use the iPython debugger (which has tab completion and a bunch of other things) by using the flag in the call to enable.

(pycatch doesn't actually do anything if you're in an interactive session, since an exception wouldn't normally kill the process.)
