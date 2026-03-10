from django.db import models

# Create your models here.
class userModel(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, default="name")
    email = models.EmailField()
    phone = models.CharField(max_length=13)
    user_status = models.CharField(max_length=10, default="pending")
    address = models.CharField(max_length=1000, null=True)
    password = models.CharField(max_length=25)
    image = models.ImageField(upload_to='media/user/')
    class Meta:
        db_table = "User_Details"
        ordering = ['-user_id']