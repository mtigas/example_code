from django.db import models
from django.utils.translation import ugettext_lazy as _

class DemoModel(models.Model):
    name   = models.CharField(_('name'),max_length=50)
    length = models.IntegerField(_('length in inches'))

    def __unicode__(self):
        return u"%s (%sin)" % (self.name,self.length)
