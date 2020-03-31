from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from utils.models import SchemaMicrodata
from utils.fields import (
    MultilingualCharField, MultilingualTextField)
from utils.models import (
    MetaTagsMixin, CreationModificationDateMixin, UrlMixin)
from utils.models import (
    object_relation_mixin_factory as generic_relation)

FavoriteObjectMixin = generic_relation(is_required=True)
OwnerMixin = generic_relation(prefix="owner",
                              prefix_verbose=_("Owner"),
                              is_required=True,
                              add_related_name=True,
                              limit_content_type_choices_to={
                                  "model__in": ("user",
                                                "institution")})


class Like(FavoriteObjectMixin, OwnerMixin):
    class Meta:
        verbose_name = _("Like")
        verbose_name_plural = _("Likes")

    def __str__(self):
        return _(f"{self.owner_content_object} "
                 f"likes {self.content_object}")


class Category(models.Model):
    title = models.CharField(_("Title"), max_length=200)

    def __str__(self):
        return self.title


class Idea(MetaTagsMixin, CreationModificationDateMixin, SchemaMicrodata, UrlMixin):
    class Meta:
        verbose_name = _("Idea")
        verbose_name_plural = _("Ideas")

    title = MultilingualCharField(_("Title"), max_length=200)
    title_itemprop = models.CharField(
        _("Title microdata item property"),
        name="title_itemprop",
        max_length=200,
        unique=False,
        blank=True,
        null=False,
        default="",
        editable=True,
        choices=(("ACCESS_MODE", "accessMode"),
                 ("ALTERNATE_NAME", "alternateName"),
                 ("BOOK_EDITION", "bookEdition"),
                 ("DESCRIPTION", "description"),
                 ("HEADLINE", "headline")))
    description = MultilingualTextField(_("Description"), blank=True)

    content = MultilingualTextField(_("Content"))
    content_itemprop = models.TextField(
        _("Content microdata item property"),
        name="content_itemprop",
        max_length=200,
        unique=False,
        blank=True,
        null=False,
        default="",
        editable=True,
        choices=(("ACCESS_MODE", "accessMode"),
                 ("ALTERNATE_NAME", "alternateName"),
                 ("BOOK_EDITION", "bookEdition"),
                 ("DESCRIPTION", "description"),
                 ("HEADLINE", "headline")))

    categories = models.ManyToManyField(Category,
                                        verbose_name=_("Category"),
                                        blank=True,
                                        related_name="ideas")

    def __str__(self):
        return self.title

    def get_url_path(self):
        return reverse("detail", kwargs={
            "idea_id": str(self.pk),
        })

    """ @classmethod
    def itemprop_fields(cls):
        return ["title", "content"] + super().itemprop_fields() """

    # multilingual version

    @classmethod
    def itemprop_fields(cls):
        fields = ["title", "content"]
        lang_fields = []
        for lang in settings.LANGUAGES:
            safe_suffix = lang[0].replace("-", "_")
            lang_fields = lang_fields + [f"{field}_{safe_suffix}"
                                         for field in fields]
        print(lang_fields + super().itemprop_fields())
        return lang_fields + super().itemprop_fields()
