# Register your models here.
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from .models import User

admin.site.register(User)
