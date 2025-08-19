from django.db import models

# Create your models here.
class Booking(models.Model):
    ID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255)
    BookingDate = models.DateTimeField(null=False)
    No_of_guests = models.SmallIntegerField(null=False)
    def __str__(self):
        return self.first_name


# Add code to create Menu model
class Menu(models.Model):
   ID = models.AutoField(primary_key=True)
   Title = models.CharField(max_length=255)
   Price = models.DecimalField(null=False, max_digits=10, decimal_places=2)
   Inventory = models.SmallIntegerField(null=False)

   def __str__(self):
    return f'{self.Title} : {str(self.Price)}'