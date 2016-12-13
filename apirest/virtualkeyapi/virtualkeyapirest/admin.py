from django.contrib import admin
from virtualkeyapirest.models import  Doors , User, Rol, AssignPermissions
# Register your models here.
admin.site.register(Rol)
admin.site.register(User)
admin.site.register(Doors)
admin.site.register(AssignPermissions)