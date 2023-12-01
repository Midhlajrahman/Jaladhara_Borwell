from django.db import models

# Create your models here.


class Services(models.Model):
    service_name = models.CharField(max_length=150)
    image = models.FileField(upload_to="media")
    service_description = models.TextField()
    slug = models.SlugField(unique=True, max_length=100)

    def __str__(self):
        return self.service_name


class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    profile_image = models.ImageField(upload_to="media")
    position = models.CharField(max_length=50)
    testimonial_content = models.CharField(max_length=300)

    def __str__(self):
        return self.name


class Contact(models.Model):
    service=models.ForeignKey(Services, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)
    email = models.EmailField()
    adress = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name


class Enquiry(models.Model):
    service=models.ForeignKey(Services, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    client_adress = models.CharField(max_length=300)
    description = models.TextField()

    def __str__(self):
        return self.full_name
    

class Project(models.Model):
    image=models.FileField(upload_to="media" ,blank=True , null=True)
    video=models.FileField(upload_to="media" , blank=True , null=True) 
