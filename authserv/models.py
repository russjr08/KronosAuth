from django.db import models
import string, random

from uuid import uuid4
# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=15)
    uuid = models.CharField(max_length=36)
    password_hash = models.CharField(max_length=100)
    auth_token = models.CharField(max_length=80)
    disabled = models.BooleanField(default=False)

    @classmethod
    def create(cls, username, password_hash):
        user = cls(username=username, password_hash=password_hash, uuid=uuid4())
        return user

    def account_active(self):
        if(self.disabled):
            return False
        else:
            return True

    @staticmethod
    def generate_auth_token():
        chars = string.ascii_letters + string.digits
        size = random.randrange(1, 80)
        return ''.join(random.choice(chars) for _ in range(size))

    def generate_uuid(self):
        self.uuid = uuid4()

    def __unicode__(self):
        return self.username
