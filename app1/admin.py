from django.contrib import admin

# Register your models here.
from app1.models import RegTable,RegTable2,RegTable3
class StudentAdmin(admin.ModelAdmin):
    list_display=['fname','lname','DOB','Age','Email','gen','Pass','mytext']
admin.site.register(RegTable,StudentAdmin)
class StudentAdmin2(admin.ModelAdmin):
    list_display=['fname','lname','DOB','Age','Email','gen','Pass','mytext']
admin.site.register(RegTable2,StudentAdmin2)
class StudentAdmin3(admin.ModelAdmin):
    list_display=['fname','lname','DOB','Payment_Method','PayMethod']
admin.site.register(RegTable3,StudentAdmin3)

