pycatch
=======

Module wrapper for a useful snippet that breaks into the PDB debugger on an unhandled exception.

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
```

(pycatch doesn't actually do anything if you're in an interactive session, since an exception wouldn't normally kill the process.)
