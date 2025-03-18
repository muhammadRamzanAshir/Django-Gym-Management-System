from django.contrib import admin
from .models import PricingPlan,WhyChooseUs,Class,GalleryImage,TeamMember,Banner,contactInfo,Hero,SiteSettings
from django.utils.html import format_html

@admin.register(PricingPlan)
class PricingPlanAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'description', 'updated_at')  # Corrected 'updated_at'
    search_fields = ('title',)

@admin.register(WhyChooseUs)
class WhyChooseUsAdmin(admin.ModelAdmin):
    list_display = ('title', 'icon_preview', 'description')

    def icon_preview(self, obj):
        """Display the icon in the admin panel."""
        return format_html('<span class="{}" style="font-size:24px;"></span>', obj.icon_class)
    icon_preview.short_description = 'Icon'

admin.site.register(Class)
admin.site.register(GalleryImage)
admin.site.register(TeamMember)
admin.site.register(contactInfo)

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('heading', 'subheading','button_text')

@admin.register(Hero)
class HeroAdmin(admin.ModelAdmin):
    list_display = ('title', 'tagline')

@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ('title','logo')