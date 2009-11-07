
import sys
import os

def add_externals():
    """
    Add the external repositories to the PYTHONPATH
    """
    ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), 
                                        os.pardir, os.pardir, "external"))
    # django
    sys.path.insert(1, os.path.join(ROOT, "django", "django"))
    # markup modules
    sys.path.insert(1, os.path.join(ROOT, "wikimarkup"))
