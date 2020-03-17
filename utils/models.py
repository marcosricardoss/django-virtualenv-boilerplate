from urllib.parse import urlparse, urlunparse

from django.conf import settings
from django.db import models
from django.template import loader
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _


class CreationModificationDateMixin(models.Model):
    """
    Abstract base class with a creation
    and modification date and time
    """
    class Meta:
        abstract = True

    created = models.DateTimeField(
        _("creation date and time"), auto_now_add=True)
    updated = models.DateTimeField(
        _("modification date and time"), auto_now=True)


class UrlMixin(models.Model):
    """
    A replacement for get_absolute_url()
    Models extending this mixin should have
    either get_url or get_url_path implemented.
    """
    class Meta:
        abstract = True

    def get_url(self):
        if hasattr(self.get_url_path, "dont_recurse"):
            raise NotImplementedError
        try:
            path = self.get_url_path()
        except NotImplementedError:
            raise
        website_host = getattr(settings,
                               "SITE_HOST",
                               "localhost:8000")
        return f"http://{website_host}/{path}"
    get_url.dont_recurse = True

    def get_url_path(self):
        if hasattr(self.get_url, "dont_recurse"):
            raise NotImplementedError
        try:
            url = self.get_url()
        except NotImplementedError:
            raise
        bits = urlparse(url)
        return urlunparse(("", "") + bits[2:])
    get_url_path.dont_recurse = True

    def get_absolute_url(self):
        return self.get_url_path()


class MetaTagsMixin(models.Model):
    """
    Abstract base class for generating meta tags
    """
    class Meta:
        abstract = True

    meta_keywords = models.CharField(
        _("Keywords"),
        max_length=255,
        blank=True,
        help_text=_("Separate keywords with commas."))
    meta_description = models.CharField(
        _("Description"),
        max_length=255,
        blank=True)
    meta_author = models.CharField(
        _("Author"),
        max_length=255,
        blank=True)
    meta_copyright = models.CharField(
        _("Copyright"),
        max_length=255,
        blank=True)

    def get_meta(self, name, content):
        tag = ""
        if name and content:
            tag = loader.render_to_string("utils/meta.html", {
                "name": name,
                "content": content,
            })
        return mark_safe(tag)

    def get_meta_keywords(self):
        return self.get_meta("keywords", self.meta_keywords)

    def get_meta_description(self):
        return self.get_meta("description", self.meta_description)

    def get_meta_author(self):
        return self.get_meta("author", self.meta_author)

    def get_meta_copyright(self):
        return self.get_meta("copyright", self.meta_copyright)

    def get_meta_tags(self):
        return mark_safe("\n".join((
            self.get_meta_keywords(),
            self.get_meta_description(),
            self.get_meta_author(),
            self.get_meta_copyright(),
        )))
