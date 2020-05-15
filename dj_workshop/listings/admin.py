from django.contrib import admin
# Register your models here.
from .models import Listing
class ListingAdmin(admin.ModelAdmin):
    class Meta:
        model = Listing
    list_display=['id', 'title', 'address', 'city', 'list_date', 'price', 'photo_main', 'realtor', 'is_published',]
    list_display_links=['id', 'title']
    list_filter = ('realtor',)
    list_editable = ('is_published',)
    search_fields = ('title', 'address', 'city', 'price',)
    list_per_page = 2
admin.site.register(Listing, ListingAdmin)
