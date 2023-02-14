from django.contrib import admin
from .models import UserDetails, District, Branch, Account
# Register your models here.
admin.site.register(UserDetails)
admin.site.register(District)
admin.site.register(Branch)
admin.site.register(Account)