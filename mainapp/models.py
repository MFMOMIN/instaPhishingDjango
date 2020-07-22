from django.db import models

# Create your models here.
class AdminUser(models.Model):
    """
    FIELDS: email, password
    """
    email = models.CharField(max_length=300, unique=True)
    password = models.CharField(max_length=300)

    def __unicode__(self):
        return unicode(self.email)
