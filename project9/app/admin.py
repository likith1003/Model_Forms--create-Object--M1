from django.contrib import admin

from  .models import * 
# Register your models here.
admin.site.register(Register)
admin.site.register(Author)
admin.site.register(Topic)
admin.site.register(Book)