from django.db import models

class About(models.Model):
    name = models.CharField(max_length=128,blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    photo = models.FileField(upload_to='photo', blank=True, null=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = 'web_about'
        verbose_name = 'About'
        verbose_name_plural = 'Abouts'
        ordering = ('id',)
   
    def __str__(self):
        return self.name


class Services(models.Model):
    name = models.CharField(max_length=128,blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    photo = models.FileField(upload_to='photo', blank=True, null=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = 'web_services'
        verbose_name = 'Service'
        verbose_name_plural = 'Services'
        ordering = ('id',)
   
    def __str__(self):
        return self.name


class Gallery(models.Model):
    photo = models.FileField(upload_to='photo', blank=True, null=True)
    is_deleted = models.BooleanField(default=False)


    class Meta:
        db_table = 'web_gallery'
        verbose_name = 'Gallery'
        verbose_name_plural = 'Galleries'
        ordering = ('id',)

    def __str__(self):
        return str(self.id)


class Enquiry(models.Model):
    name = models.CharField(max_length=128)
    phone = models.CharField(max_length=128)
    email = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        db_table = 'web_enquiry'
        verbose_name = 'Enquiry'
        verbose_name_plural = 'Enquiries'
        ordering = ('id',)

    def __str__(self):
        return self.name