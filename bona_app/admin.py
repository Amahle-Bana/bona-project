from django.contrib import admin
from .models import User, Movie

# Register your models here.

# ID GENERATORS
class MovieAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

class UserAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

# USER ADMIN REGISTER
admin.site.register(User, UserAdmin)
admin.site.register(Movie, MovieAdmin)