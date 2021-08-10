from django.contrib import admin

from .models import about
from .models import slider
from .models import partner
from .models import advisor
from .models import service
from .models import strategy
from .models import approach
from .models import fund_info
from .models import fund_protect


admin.site.register(about)
admin.site.register(slider)
admin.site.register(partner)
admin.site.register(advisor)
admin.site.register(fund_info)
admin.site.register(fund_protect)



@admin.register(service)
class serviceAdmin(admin.ModelAdmin):
    list_display = ['id', 'name','description']

@admin.register(strategy)
class strategyAdmin(admin.ModelAdmin):
    list_display = ['id', 'name','description']
@admin.register(approach)
class approachAdmin(admin.ModelAdmin):
    list_display = ['id', 'name','description']