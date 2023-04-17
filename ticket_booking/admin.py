from django.contrib import admin
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from ticket_booking.models import Update_profile

# Register your models here.
admin.site.register(Station)
admin.site.register(Train)
admin.site.register(Trip)
admin.site.register(Ticket)



class AccountInLine(admin.StackedInline):
    model = Update_profile
    can_delete = False
    verbose_name_plural = 'Accounts'

class CustomizeUser(UserAdmin):
    inlines = (AccountInLine, )

admin.site.unregister(User)
admin.site.register(User, CustomizeUser)
admin.site.register(Update_profile)