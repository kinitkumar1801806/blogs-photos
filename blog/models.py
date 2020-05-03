from django.db import models

# Create your models here.
class BlogPost(models.Model):
    post_id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=50,default="")
    head0 = models.CharField(max_length=500,default="")
    chead0 = models.CharField(max_length=5000,default="")
    head1 = models.CharField(max_length=500,default="")
    chead1 = models.CharField(max_length=5000,default="")
    head2 = models.CharField(max_length=500,default="")
    chead2 = models.CharField(max_length=5000,)
    pub_date=models.DateField()
    thumbnail=models.ImageField(upload_to='shop/images',default="")

    def __str__(self):
        return  self.title
class DefenceBlog(models.Model):
    post_id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=50,default="")
    head0 = models.CharField(max_length=500,default="")
    chead0 = models.CharField(max_length=5000,default="")
    head1 = models.CharField(max_length=500,default="")
    chead1 = models.CharField(max_length=5000,default="")
    head2 = models.CharField(max_length=500,default="")
    chead2 = models.CharField(max_length=5000,)
    pub_date=models.DateField()
    thumbnail=models.ImageField(upload_to='shop/images',default="")

    def __str__(self):
        return  self.title

class SoftwareBlog(models.Model):
    post_id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=50,default="")
    head0 = models.CharField(max_length=500,default="")
    chead0 = models.CharField(max_length=5000,default="")
    head1 = models.CharField(max_length=500,default="")
    chead1 = models.CharField(max_length=5000,default="")
    head2 = models.CharField(max_length=500,default="")
    chead2 = models.CharField(max_length=5000,)
    pub_date=models.DateField()
    thumbnail=models.ImageField(upload_to='shop/images',default="")

    def __str__(self):
        return  self.title

class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    desc = models.CharField(max_length=500, default="")

    def __str__(self):
        return self.name
class Gallery(models.Model):
    image=models.ImageField(upload_to='shop/images',default="")
    upload_by=models.CharField(max_length=100,default=" Admin")
    title=models.CharField(max_length=300,default="")
    category=models.CharField(max_length=300,default="")

class Animals(models.Model):
    image=models.ImageField(upload_to='shop/images',default="")
    upload_by=models.CharField(max_length=100,default=" Admin")
    title=models.CharField(max_length=300,default="")
    category=models.CharField(max_length=300,default="")

class Accessories(models.Model):
    image=models.ImageField(upload_to='shop/images',default="")
    upload_by=models.CharField(max_length=100,default=" Admin")
    title=models.CharField(max_length=300,default="")
    category=models.CharField(max_length=300,default="")

class Nature(models.Model):
    image=models.ImageField(upload_to='shop/images',default="")
    upload_by=models.CharField(max_length=100,default=" Admin")
    title=models.CharField(max_length=300,default="")
    category=models.CharField(max_length=300,default="")

class Monuments(models.Model):
    image=models.ImageField(upload_to='shop/images',default="")
    upload_by=models.CharField(max_length=100,default=" Admin")
    title=models.CharField(max_length=300,default="")
    category=models.CharField(max_length=300,default="")

class HolyPlaces(models.Model):
    image=models.ImageField(upload_to='shop/images',default="")
    upload_by=models.CharField(max_length=100,default=" Admin")
    title=models.CharField(max_length=300,default="")
    category=models.CharField(max_length=300,default="")     


class Heritage(models.Model):
    image=models.ImageField(upload_to='shop/images',default="")
    upload_by=models.CharField(max_length=100,default=" Admin")
    title=models.CharField(max_length=300,default="")
    category=models.CharField(max_length=300,default="")

class Vehicles(models.Model):
    image=models.ImageField(upload_to='shop/images',default="")
    upload_by=models.CharField(max_length=100,default=" Admin")
    title=models.CharField(max_length=300,default="")
    category=models.CharField(max_length=300,default="")                


