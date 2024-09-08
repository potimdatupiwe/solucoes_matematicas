from django.db import models
import datetime
from django.utils import timezone

class User(models.Model):
    user = models.CharField(max_length=200,null = False, primary_key=True)
    password = models.CharField(max_length=200, null = True)
    login_date = models.DateTimeField('date published') 
    login = models.BooleanField(default=True)
    def __str__(self):
        return self.user
    def logoutuser(self):
        return self.login_date+datetime.timedelta(minutes=60)<=timezone.now()
class Question(models.Model): 
    user12 = models.ForeignKey(User, on_delete=models.CASCADE)
    value = models.CharField(max_length=2000, primary_key=True)
    url = models.CharField(max_length=200, null = True)