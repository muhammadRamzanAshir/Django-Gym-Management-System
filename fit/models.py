from django.db import models

# Create your models here.
class PricingPlan(models.Model):
    title         = models.CharField(max_length=100)
    price         = models.DecimalField(max_digits=6, decimal_places=2)
    description   = models.CharField(max_length=100 , default="SINGLE CLASS")
    features      = models.TextField(help_text="Enter Features seprated by a coma (,)")
    created_at    = models.DateTimeField(auto_now_add=True)
    updated_at    = models.DateTimeField(auto_now=True)
    
    def get_features(self):
        return self.features.split(',')
    
    def __str__(self):
        return self.title

class WhyChooseUs(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    icon_class = models.CharField(
        max_length=100, 
        help_text="Enter the FontAwesome or custom icon class (e.g., 'flaticon-034-stationary-bike')"
    )

    def __str__(self):
        return self.title
    
class Class(models.Model):
    title       = models.CharField(max_length=255)
    category    = models.CharField(max_length=255)
    image       = models.ImageField(upload_to='img/classes')
    link        = models.URLField(blank=True, null=True)
    created_at  = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

class GalleryImage(models.Model):
    image           = models.ImageField(upload_to='gallery/', help_text='upload an image for the gallery')
    title           = models.CharField(max_length=100, blank=True, null=True , help_text='Title of the image')
    description     = models.TextField(blank=True, null=True, help_text='Description of the image')
    
    def __str__(self):
        return self.title if self.title else 'Gallery Image'

class TeamMember(models.Model):
    name = models.CharField(max_length=100, help_text='Name of the team member')
    role = models.CharField(max_length=100, help_text='Role of the team member')
    image = models.ImageField(upload_to='team/', help_text='Upload image of the team member')

    def __str__(self):
        return self.name
    
class Banner(models.Model):
    heading  = models.CharField(max_length=200, help_text="Main Heading of  the Banner ")
    subheading = models.TextField(help_text="subheading of the banner ")
    button_text = models.CharField(max_length=50, help_text="Text for button")
    button_link = models.URLField(help_text="URL the button redirects to ")
    background_image = models.ImageField(upload_to='banner/', help_text="Background image for the banner")
    
    def __str__(self):
        return self.heading

class contactInfo(models.Model):
    address = models.TextField()
    phone_numbers = models.CharField(max_length=255)  # Comma-separated numbers
    email = models.EmailField()

    def get_phone_numbers(self):
        return self.phone_numbers.split(',')

    def __str__(self):
        return "Contact Information"


class Hero(models.Model):
    image = models.ImageField(upload_to='hero/')
    tagline = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    register_link = models.URLField(default='http://127.0.0.1:8000/auth/')
    login_link = models.URLField(default='http://127.0.0.1:8000/auth/')

    def __str__(self):
        return self.title

class SiteSettings(models.Model):
    logo = models.ImageField(upload_to='logos/', default='logos/default_logo.png')
    title = models.CharField(max_length=255, default="Gym", help_text="Website Title")

    
    def __str__(self):
        return "Site Settings"