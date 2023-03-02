from django.contrib import admin

# Register your models here.
from AuthSys.authapp.models import AuthUser


@admin.register(AuthUser)
class AuthUserAdmin(admin.ModelAdmin):
    pass