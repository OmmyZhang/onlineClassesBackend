from django.db import models

class SessionRecord(models.Model):
    my_session = models.CharField(max_length=64)
    openid = models.CharField(max_length=127)
    active_time = models.DateTimeField()
    
    def __str__(self):
        return self.my_session + ' : ' + self.openid + ' @' + str(self.active_time)


class AppInfo(models.Model):
    appid = models.CharField(max_length=128)
    secret = models.CharField(max_length=128)

