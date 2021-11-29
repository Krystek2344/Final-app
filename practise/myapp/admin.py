from django.contrib import admin
from .models import Aircraft
from .models import WorkOrder


admin.site.register(Aircraft)
admin.site.register(WorkOrder)


