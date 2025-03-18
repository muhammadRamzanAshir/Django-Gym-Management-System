from django.shortcuts import render
from .models import PricingPlan,WhyChooseUs,Class,GalleryImage,TeamMember,Banner, contactInfo,Hero,SiteSettings
import accounts.views as account_view

def index(request):
    why_choose_us = WhyChooseUs.objects.all()
    pricing_plans = PricingPlan.objects.all()
    gallery_images = GalleryImage.objects.all()
    classes = Class.objects.all()
    banner = Banner.objects.first()
    team_members = TeamMember.objects.all()
    contact_info = contactInfo.objects.first()
    hero_slides = Hero.objects.all()
    # logo
    site_settings = SiteSettings.objects.first() 
    context = {
        'pricing_plans': pricing_plans,
        'why_choose_us': why_choose_us,
        'classes': classes,
        'gallery_images':gallery_images,
        'team_members':team_members,
        'banner':banner,
        'contact_info':contact_info,
        'hero_slides':hero_slides,
        'site_settings':site_settings,
    }
    print(banner)  # Debugging line to check the context
    return render(request, 'index.html', context)