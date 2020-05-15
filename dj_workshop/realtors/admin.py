from django.contrib import admin
# Register your models here.
from .models import Realtor
class RealtorAdmin(admin.ModelAdmin):
    class Meta:
        model = Realtor
    list_display = ['id', 'name', 'email', 'phone']
    list_per_page = 1
    list_display_links = ['id','name']
    search_fields = ('id', 'name', 'email')
    list_filter = ('name',)

admin.site.register(Realtor,RealtorAdmin)
