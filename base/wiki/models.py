"""
Base Wiki Model

Abstract classes which a wiki backend needs to implement
"""

from django.db import models
from communiki.utils.addtypes import Enumeration

REVISION_TYPES = Enumeration("REVISION_TYPE",
                            ("LATEST", "STABLE"))

WIKI_SYNTAX_CHOICES = ((1, _("Mediawiki")),)


class Source(models.Model):
    """
    Datasource defines a source for data
    """
    name = models.CharField(null=False)
    uri = models.TextField(null=False)


    def update(self):
        """
        Update the Source to pull data from upstream URL
        """
        pass

    def refresh_namespaces(self):
        """
        Refreshes all active Namespaces
        """
        #for ns in self.
        #FIXME




class Namespace(models.Model):
    """
    A Namespace represents an independend subset of Pages.
    
    It can be in import form
    """
    name = models.CharField(max_length=255)
    source = models.ForeignKey(Source)
    source_ident = models.CharField("Source Identifier", null=True, blank=True,
                                    help_text=_("A identifier for the Source"))
    disabled = models.BooleanField(default=False,
                                    help_text=_("Disables the namspace"))
    read_only = models.BooleanField(default=False,
                                    help_text=_("Disables changes to namespace"))

    def refresh(self):
        """
        Refreshes all informations when the Source changed
        """
        pass

    class Meta:
        abstract = True


class Page(models.Model):
    name = models.CharField(max_length=255)


    def list_versions(self):
        """
        Returns a iterator with all version of a Page
        """
        return

    def get_version(self, version=None, tagged=REVISION_TYPES.LATEST):
        """
        Returns a specific version of the Document. 
        
        The request can eighter be a specific version depending on the backend 
        or a tagged request if version is None.
        """
        raise NotImplemented

    class Meta:
        abstract = True


class Revision(models.Model):
    """A specific revision of the Page"""
    namespace = models.ForeignKey(Namespace, editable=False)
    page = models.ForeignKey(Page, editable=False)
    version = models.CharField(null=False, blank=False, editable=False)
    is_new = False
    mime_type = models.CharField(null=True, blank=True)
    wiki_syntax = models.IntegerField(choices=WIKI_SYNTAX_CHOICES, blank=True,
                                      help_text=_("In case of a wiki page, which syntax to use"))

    def get_content(self):
        """
        Returns the content of the revision
        """
        raise NotImplemented

    def set_content(self, content):
        """
        Sets the content to new text
        """
        if not self.is_new:
            raise ValueError, "Can't change a old revision"

    content = property(get_content, set_content)

    def list_attributes(self):
        """
        Returns a list of attribute names
        """
        pass
    
    def __iter__(self):
        """
        Returns a iteratorn over the attributes
        """
        pass

    def __setattr__(self, key, value):
        """
        Set the attribute of the key/value meta pair
        """
        pass

    def commit(self):
        """
        Commits data to the repository.
        """
        pass

    def sign(self):
        """
        sign local changes
        """
        pass 

    class Meta:
        abstract = True


