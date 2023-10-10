from django.db import models
#about
class About(models.Model):
    short_description = models.TextField()
    description = models.TextField()
    image = models.ImageField(upload_to = "about")

    class Meta:
        verbose_name = "About Me"
        verbose_name_plural = "About Me"


    def __str__(self):
        return "About me"
#service
class Service(models.Model):
    name = models.CharField(max_length = 100, verbose_name="Service name")
    description = models.TextField(verbose_name="About service")

    def __str__(self):
        return self.name

# work
class RecentWork(models.Model):
    title = models.CharField(max_length = 100,verbose_name="Work title")
    image = models.ImageField(upload_to="works")

    def __str__(self):
        return self.title

#client
class Client(models.Model):
    name = models.CharField(max_length=100,verbose_name="Client name")
    description = models.TextField(verbose_name="Client say")
    image= models.ImageField(upload_to="clients",default="default.png")

    def __str__(self):
        return self.name