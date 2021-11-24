from os import name
from django.contrib import admin
from .models import Rule, Query, Config
import random
# Register your models here.

@admin.action(description='strategy')
def strategy(modeladmin, request, queryset):

    # queryset.update(flag='strategy')
    strategy_name = ""
    for rule in queryset:
        a = str(rule)
        strategy_name += f"{a} "    
    
    indexname = ""
    for rule in queryset:
        a = str(rule)
        indexname += f"{rule.index_name}, "
    
    rule = Rule.objects.get_value(queryset, name=strategy_name, index_name=indexname, flag='strategy')
    
    # b = rule.create_total(queryset)
    
    # print(b)
    # a = print("^^^^^^^^^^^", queryset)
    
    # # rule.flag = str(queryset[0])
    # # print("##################", queryset[0])

    #     # print("!!!!!!!!!!!!!!!", rule)
    # # print("@@@@@@@@@@@", strategy_name)
    # rule.save()
    # for rule in queryset:
    #     queries = rule.queries.all()
    #     # print("#########################queries", queries)
    #     rule.query_sum = f""
        # print("##################a", d)
        # for query in a:
        #     zz += str(query.event_category)
    # rule.query_sum = 
   
    # rule.save()       
        
    # print("##########", queryset)
    # print("##########", request)
    # Rule.objects.create(name='test_strategy',index_name = 'test_index')




class QueryInline(admin.TabularInline):
    model = Query
    extra = 1

class ConfigInline(admin.TabularInline):
    model = Config

class RuleAdmin(admin.ModelAdmin):
    # class Meta:
    #     model = Rule
    list_display = ['id', 'name', 'index_name', 'create_time', 'modified_time','total','flag']
    search_fields = ['name', 'index_name', 'create_time', 'modified_time']
    list_display_links = ['name']
    inlines = [
        QueryInline,
        ConfigInline,
        ]
    actions = [strategy]
    
    # def qt(self, request):
    #     rule = Rule.objects.all()
    #     # q = rule.queries.all()
    #     return q

class QueryAdmin(admin.ModelAdmin):
    list_display = ['id', 'event_category', 'condition',]
    # list_editable = ['sequence']
    search_field = ['event_category', 'condition']


admin.site.register(Rule, RuleAdmin)
admin.site.register(Query, QueryAdmin)
# admin.site.register(Query) 