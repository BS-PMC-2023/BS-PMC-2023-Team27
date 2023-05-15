
from django.contrib import admin
from .models import Passenger,Worker,ContactUs

admin.site.register(Passenger)
admin.site.register(Worker)
# Register your models here.
admin.site.register(ContactUs)

