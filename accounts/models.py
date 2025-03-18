from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class AuthForms(models.Model):
    girisback = models.ImageField(upload_to='backgrounds/', blank=True, null=True, help_text="Background Image for Giris")
    kayitback = models.ImageField(upload_to='backgrounds/', blank=True, null=True, help_text="Background Image for Kayit")
    pargraph_login = models.TextField(help_text="Subheading for login")
    pargraph_singup = models.TextField(help_text="Subheading for signup")

    def __str__(self):
        return f"AuthForms - Login/Signup Backgrounds"

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    activation_key = models.CharField(max_length=50, unique=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username