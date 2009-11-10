"""
Abstract classes which a crypto backend needs to implement
"""

from django.db import models
from communiki.utils.addtypes import Enumeration

REVISION_TYPES = Enumeration("REVISION_TYPE",
                            ("LATEST", "STABLE"))

WIKI_SYNTAX_CHOICES = ((1, _("Mediawiki")),)

class HeaderNotFound(Exception):
    """
    Signature header could not be found
    """


class KeyProvider(object):
    """
    Provides a list of public keys
    """

    def list_keys(self):
        """
        Returns a list of all Key objects
        """
        pass

    def search_key(self, fingerprint):
        """
        Search for a key with the fingerprint
        """
        pass

class Crypto(object):
    """
    Iteracts with the crypto engine
    """

    def validate(self, text):
        """
        Validate the signature of the text given
        """

