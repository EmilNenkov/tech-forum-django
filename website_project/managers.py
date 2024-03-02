from django.db import models

class CustomUserManager(models.Manager):
    def get_latest_user(self):
        return self.latest('date_created')
    
