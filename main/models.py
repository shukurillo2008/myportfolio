from django.db import models
from django.contrib.auth.models import User

class AboutMe(models.Model):
    auth = models.OneToOneField(User,on_delete=models.SET_NULL, null=True)
    email = models.EmailField(null=True, blank=True)
    name = models.CharField(max_length=255)
    l_name = models.CharField(max_length=255)
    age = models.DateField(blank=True, null=True)
    location = models.CharField(max_length=255)
    body = models.TextField()
    img = models.ImageField(upload_to='myimage/')
    resume = models.FileField(upload_to='resume/')
    texnology = models.CharField(max_length=255)
    phone = models.CharField(max_length=255, null=True, blank=True)
    degree = models.CharField(max_length=255, null=True, blank=True)
    freelance = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self) -> str:
        return self.name


class MyCharacter(models.Model):
    title= models.CharField(max_length=255)
    body = models.TextField()

    def __str__(self) -> str:
        return self.title
    

class IndicatorWin(models.Model):
    award = models.PositiveIntegerField(default=0)
    customer = models.PositiveIntegerField(default=0)
    project = models.PositiveIntegerField(default=0)
    workplace = models.PositiveIntegerField(default=0)


class ClientComment(models.Model):
    name = models.CharField(max_length=255)
    l_name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    image = models.ImageField(upload_to='clients/', null=True, blank=True)
    body = models.TextField()

    def __str__(self) -> str:
        return self.name
   

class History(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    date_start = models.DateField(blank=True, null=True)
    date_end = models.DateField(blank=True, null=True)

    def __str__(self) -> str:
        return self.title
    

class Hobby(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.title
    

class MySkills(models.Model):
    title = models.CharField(max_length=255)
    protsent = models.PositiveIntegerField(default=0)

    def __str__(self) -> str:
        return self.title
    

class MyServise(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()

    def __str__(self) -> str:
        return self.title
    

class Pricing(models.Model):
    servise = models.ManyToManyField(MyServise)
    title = models.CharField(max_length=255)
    price = models.PositiveIntegerField(default=0)

    def __str__(self) -> str:
        return self.title
    

class Motto(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    
    def __str__(self) -> str:
        return self.title


class CategoryWork(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.title


class MyWork(models.Model):
    worktype = models.ForeignKey(CategoryWork, on_delete=models.SET_NULL, null=True)
    client = models.CharField(max_length=255)
    date = models.DateField()
    time_taken = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    info = models.TextField()

    def __str__(self) -> str:
        return self.title
    

class MyWorkImage(models.Model):
    work = models.ForeignKey(MyWork, on_delete=models.SET_NULL, null=True, related_name='image')
    img = models.ImageField(upload_to='workimages/')

    def __str__(self) -> str:
        return self.work.title
    

class CategoryBlog(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.title
    

class Blog(models.Model):
    category = models.ForeignKey(CategoryBlog, on_delete=models.SET_NULL, null=True)
    posted = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='blogimages/')
    title = models.CharField(max_length=255)
    body = models.TextField()

    def __str__(self) -> str:
        return self.title
    

class ContactMe(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    sub = models.CharField(max_length=255)
    text = models.TextField()

    def __str__(self) -> str:
        return self.name


class Social(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    link = models.CharField(max_length=255, blank=True, null=True)
    
    def __str__(self) -> str:
        return self.name

