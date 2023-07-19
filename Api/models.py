from django.db import models


class Images(models.Model):
    images = models.FileField(upload_to="other_images")


    def __str__(self):
        return str(self.images) 


    class Meta:
        verbose_name_plural = "Images"


class House(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    address = models.TextField()
    type = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    image = models.ImageField(upload_to="images", blank=True, null=True)
    build_year = models.CharField(max_length=100)
    agent = models.CharField(max_length=100)
    other_images = models.ManyToManyField(Images, blank=True)



    def __str__(self):
        return self.name



class Booking(models.Model):
    name = models.CharField(max_length=100)
    inspection_date = models.CharField(max_length=100)
    inspection_time = models.CharField(max_length=100)
    house_location = models.CharField(max_length=100)
    property_name = models.CharField(max_length=100)


    def __str__(self):
        return self.name
    

    class Meta:
        verbose_name_plural = "Bookings"
        