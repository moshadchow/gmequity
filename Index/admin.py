from django.contrib import admin

from .models import about
from .models import slider
from .models import partner
from .models import category
from .models import product
from .models import advisor


admin.site.register(about)
admin.site.register(slider)
admin.site.register(partner)
admin.site.register(advisor)

@admin.register(category)
class categoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'cat_nm']


@admin.register(product)
class productAdmin(admin.ModelAdmin):
    list_display = ['id', 'p_name', 'image', 'cat']
