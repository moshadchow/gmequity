from django.contrib import admin

from .models import about
from .models import slider
from .models import partner
from .models import advisor
from .models import service
from .models import strategy
from .models import approach
from .models import fund_info
from .models import financial_info
from .models import fund_protect
from .models import faq
from .models import company_goal
from .models import sip
from .models import board_member
from .models import news
from .models import tax


admin.site.register(about)
admin.site.register(slider)
admin.site.register(partner)
admin.site.register(advisor)
admin.site.register(fund_info)
admin.site.register(financial_info)
admin.site.register(fund_protect)
admin.site.register(faq)
admin.site.register(company_goal)
admin.site.register(sip)
admin.site.register(board_member)
admin.site.register(news)
admin.site.register(tax)



@admin.register(service)
class serviceAdmin(admin.ModelAdmin):
    list_display = ['id', 'name','description','css_name']

@admin.register(strategy)
class strategyAdmin(admin.ModelAdmin):
    list_display = ['id', 'name','description','css_name']
@admin.register(approach)
class approachAdmin(admin.ModelAdmin):
    list_display = ['id', 'name','description','css_name']