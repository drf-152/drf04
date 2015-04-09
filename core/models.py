from django.db import models


class AAAA(models.Model):
    name = models.CharField(
        max_length=255,
        blank=False,
    )
    bbs = models.ManyToManyField(
        to='core.BBBB',
        related_name='aa_bbs',
        blank=True,
        null=True,
    )

    def __unicode__(self):
        return self.name


class BBBB(models.Model):
    name = models.CharField(
        max_length=255,
        blank=False,
    )

    def __unicode__(self):
        return self.name



class CCCC(models.Model):
    name = models.CharField(
        max_length=255,
        blank=False,
    )
    bb = models.ForeignKey(
        to='core.BBBB',
        related_name='bb_ccs',
        blank=False,
        null=False,
    )
    show_me = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name
