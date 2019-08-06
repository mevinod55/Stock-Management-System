from django.contrib import admin
from .models import Desktops
from .models import Laptops
from .models import Mobiles
# Register your models here.

admin.site.register(Desktops)
admin.site.register(Laptops)
admin.site.register(Mobiles)
