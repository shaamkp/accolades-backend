import uuid
from django.db import models
from django.contrib.auth.models import User,Group
from general.encryption import encrypt

from general.functions import get_auto_id
from general.middleware import RequestMiddleware
from general.models import BaseModel


class ChiefProfile(BaseModel):
    username = models.CharField(max_length=128)
    user = models.OneToOneField("auth.User", on_delete=models.CASCADE)
    password = models.TextField()

    def save(self, *args, **kwargs):
        if not self.creator:
            # First we need create an instance of that and later get the current_request assigned
            request = RequestMiddleware(get_response=None)
            request = request.thread_local.current_request

            if self._state.adding:
                auto_id = get_auto_id(ChiefProfile)

                chief_username = self.username
                password = User.objects.make_random_password(length=12, allowed_chars="abcdefghjkmnpqrstuvwzyx#@*%$ABCDEFGHJKLMNPQRSTUVWXYZ23456789")
                chief_email = f"{chief_username}@talrop.com"

                user = User.objects.create_user(
                    username=chief_username,
                    email=chief_email,
                    password=password
                )

                self.creator = request.user
                self.updater = request.user
                self.auto_id = auto_id
                self.user = user
                self.password = encrypt(password)

        super(ChiefProfile, self).save(*args, **kwargs)


PROFILE_GENDER_CHOICES = (
    ('male', 'Male'),
    ('female', 'Female'),
    ('others', 'Others'),
)

class Profile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date_added = models.DateTimeField(db_index=True, auto_now_add=True)
    user = models.OneToOneField("auth.User",on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=128, blank=True, null=True)
    phone = models.CharField(max_length=128, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    gender = models.CharField(max_length=128,choices=PROFILE_GENDER_CHOICES, blank=True, null=True)
    photo = models.ImageField(upload_to="profile/",blank=True,null=True)
    username = models.CharField(max_length=155,blank=True,null=True)
    password = models.TextField(blank=True, null=True)    
    is_verified = models.BooleanField(default=False)
    is_profile_updated = models.BooleanField(default=False)
    is_email_verified = models.BooleanField(default=False)
    gender = models.CharField(max_length=128, choices=PROFILE_GENDER_CHOICES, null=True, blank=True)
    dob = models.DateField(blank=True, null=True)
    

    class Meta:
        db_table = 'users_profile'
        verbose_name ='profile'
        verbose_name_plural ='profiles'
        ordering = ('name',)
        
    def __str__(self):
        if self.name:
            return self.name
        else:
            return self.phone



 