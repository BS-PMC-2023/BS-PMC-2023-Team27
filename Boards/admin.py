
from django.contrib import admin
from .models import Passenger, Worker, ContactUs, Workerreport, Order, Flight

admin.site.register(Passenger)
admin.site.register(Worker)

# Register your models here.
admin.site.register(ContactUs)
admin.site.register(Workerreport)


admin.site.register(Flight)

admin.site.register(Order)
