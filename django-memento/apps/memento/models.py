from django.db import models
from autoslug import AutoSlugField

from django.utils.translation import ugettext_lazy as _

class Board(models.Model):
    """A board is what contains the stickers.
       A board can have many topics and can 
       contain many posts.
    """
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = _('Board')
        verbose_name_plural = _('Boards')

    def __unicode__(self):
        return self.name


class Post(models.Model):
    """A post is related to a board and
       a board can contain many posts."""
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from='name') 
    board = models.ForeignKey(Board)

    class Meta:
        verbose_name = _('Post')
        verbose_name_plural = _('Posts')

    def __unicode__(self):
        return name

    @models.permalink
    def get_absolute_url(self):
        return ('')
