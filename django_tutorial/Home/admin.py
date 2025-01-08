from django.contrib import admin
from.models import Departments,Doctors,Booking,Contact
# Register your models here.

admin.site.register(Departments)
admin.site.register(Doctors)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'p_name', 'p_name', 'p_email', 'doc_name','booked_on')
admin.site.register(Booking,BookingAdmin)
admin.site.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
