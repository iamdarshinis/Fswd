from django.contrib import admin
from website.models import Contact_us

admin.site.site_header="Quient Trainings Pvt Ltd"

class Contact_usAdmin(admin.ModelAdmin):
    list_display = ["id","name","email","number","message","added_on"]
    search_fields = ["name"]
    list_filter = ["added_on"]

admin.site.register(Contact_us,Contact_usAdmin)