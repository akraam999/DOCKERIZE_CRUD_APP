from django.contrib import admin
from nembers.models import *
# Register your models here.
@admin.register(Student)
class EtudiantAdmin(admin.ModelAdmin): 
    list_display = ('first_name','last_name','email','classLevel')

@admin.register(ClassLevel)
class classAdmin(admin.ModelAdmin):
    list_display =('level','total_student')

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('Title',)

@admin.register(Admin)
class AdminAdmin(admin.ModelAdmin):
    list_display = ('username','email','password')



