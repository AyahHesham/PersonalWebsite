from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import blog


# Register your models here.


class blogModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'

admin.site.register(blog,blogModelAdmin)

