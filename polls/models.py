# import datetime
# from django.db import models
# from django.utils import timezone
# from django.contrib import admin


# # Create your models here.

# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')
#     def __str__(self):
#         return self.question_text
#     @admin.display(
#         boolean=True,
#         ordering='pub_date',
#         description='Published recently?',
#     )    
#     def was_published_recently(self):
#         now = timezone.now()
#         return now - datetime.timedelta(days=1) <= self.pub_date <= now

# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)
#     def __str__(self):
#         return self.choice_text

  


# class Publication(models.Model):
#     title = models.CharField(max_length=30)

#     class Meta:
#         ordering = ['title']

#     def __str__(self):
#         return self.title

# class Article(models.Model):
#     headline = models.CharField(max_length=100)
#     publications = models.ManyToManyField(Publication)

#     class Meta:
#         ordering = ['headline']

#     def __str__(self):
#         return self.headline

# # Lens App Models

# # class KelvinInstrument(models.Model):
# #     title = models.CharField(max_length=30)


# class Kelvin(models.Model):
#     title = models.CharField(max_length=30)
#     def __str__(self):
#         return self.title 
    
# #     cover = models.ImageField(upload_to='images/')

    

# class Post(models.Model):
#     title = models.CharField(max_length=30)
#     cover = models.ImageField(upload_to='images/')
#     # kelvin = models.ForeignKey(Kelvin, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.title      




class OpticalTypeFlag(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title 

class OpticalTypes(models.Model):
    title = models.CharField(max_length=30)
    opticaltypeflags = models.ManyToManyField(OpticalTypeFlag)
    def __str__(self):
        return self.title
    
class Project(models.Model):
    title = models.CharField(max_length=50)
    created = models.DateTimeField(default=timezone.now)
    # updated = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.title 


class Manufacturer(models.Model):
    title = models.CharField(max_length=50)
    created = models.DateTimeField(default=timezone.now)
    # updated = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.title 
    



class Material(models.Model):
        title = models.CharField(max_length=50)
        Description = models.TextField(max_length=100,null=True, blank=True)
        Wc = models.DecimalField(max_digits=6, decimal_places=3, null=True)
        Ri = models.DecimalField(max_digits=6, decimal_places=3, null=True)
        Dk = models.DecimalField(max_digits=6, decimal_places=3, null=True)
        Modulus = models.DecimalField(max_digits=6, decimal_places=3, null=True)
        created = models.DateTimeField(default=timezone.now)
        def __str__(self):
            return self.title 


class Lens(models.Model):
    title = models.CharField(max_length=50)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    created = models.DateTimeField(default=timezone.now)
    # updated = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.title 
