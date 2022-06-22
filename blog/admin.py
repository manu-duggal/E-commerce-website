from django.contrib import admin

# Register your models here.
from blog.models import Blogpost

admin.site.register(Blogpost)