from django.contrib import admin
from .models import Staff,Customer,performanceReport,customerPlatform,customerPackage,customerCatogery,Admin

# Register your models here.
admin.site.register(Staff)
admin.site.register(Customer)
admin.site.register(performanceReport)
admin.site.register(customerPlatform)
admin.site.register(customerPackage)
admin.site.register(customerCatogery)
admin.site.register(Admin)
