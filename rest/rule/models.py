from django.db import models
from django.db.models.fields import BooleanField
import requests
import random
import json
import yaml
from django.core.files.base import ContentFile, File
import time
# from django.db.models.signals import post_save

# class StrategyManager(models.Manager):
#     def get_value(self, queryset, **kwargs):
#         a = super().create(**kwargs)
#         y = ""
#         for i in queryset:
#             queries = i.queries.all()
#             print("index_name: ", i.index_name)
            
#             # for query in queries:
#             #     print("query: ",query)
#             x = ""
#             for i in range (len(queries)):
#                 c = (f"[{queries[i].event_category} where {queries[i].condition}]\\n ")
#                 x +=  c
#             y += x
#         z = "sequence\\n " + y
#         print("ZZZZZZZZ: ", z) 
#         a.total = z 
#         a.save()

# class QueryManager(models.Manager):
#     def create(self,**kwargs):
#         a = super().create(**kwargs)
#         print("2222222222", a)
#         queries = a.rule.queries.all()
#         sequence = a.rule.sequence
#         # print('-------', sequence)
#         if sequence == False:
#             # print('+++++++', sequence)
#             z = (f"{queries.event_category} where {queries.condition}")
        
#         elif sequence == True:
#             x = ""
#             for i in range (len(queries)):
#                 # print("$$$$$len", len(queries))
#                 c = (f"[{queries[i].event_category} where {queries[i].condition}]\\n  ")
#                 x +=  c
#                 z = "sequence\\n " + x 
        
        
#         a.total= "ss"
        
#         a.save()
#         # return z   
    
    
# class CustomRuleManager(models.Manager):    
#     def create(self, **kwargs):
#         q = super().create(**kwargs)
#         dict_file = """[{'ANPdata' : ['creation_date = %s', 'maturity = production', 'updated_date = %s']},
#                         {'ANPrule' : [{'author': ["Elastic"]}, {'language': "eql"}, {'rule_id': "55"}, {'threat': 'ghgf'}]},
#                         {'name': \" %s \"},
#                         {'index': "%s"},
#                         {'type': "any"}]"""%(q.create_time, q.modified_time, q.name, q.index_name)
                                       
#         dict_file = eval(dict_file)
#         with open(f'testyaml{random.random()}.yaml', 'w') as file:
#             documents = yaml.dump(dict_file, file)
        
#         return documents

# class CustomStrategyManager(models.Manager):
#     def create(self, *args, **kwargs):
#         s = super().create(*args, **kwargs)
#         rule = Rule.objects.create(name=s.strategy_name, index_name="sss")
#         rs = s.rules.all()
#         for r in rs:
            
#             print("@@@@@@@@@@@@@@",r)

#         print("#################done")

# class CustomStrategyManager(models.Manager):
#     def create(self, **kwargs):
#         strategy_rule_create_queryset = super().create(**kwargs)
#         print("##", strategy_rule_create_queryset)
        
#         rule = Rule.objects.create(name="ee", index_name="ee")
#         rule.save()
#         return rule
        
        
      
class Rule(models.Model):
    name = models.CharField(max_length=200, unique=True)
    index_name = models.TextField(blank=True, null=True)
    create_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)
    # rule_file = models.FileField(blank=True, upload_to='')
    CREATE_RULE = 'create_rule'
    STRATEGY = 'strategy'
    flag_fields = (
        (CREATE_RULE, "create_rule"),
        (STRATEGY, "strategy")
    )
    flag = models.CharField(max_length=250, blank=True, null=True, choices=flag_fields, default=CREATE_RULE)
    total = models.TextField(blank=True, null=True)
    # objects = CustomRuleManager()
    # default_manager = CustomRuleManager()

        
    @property
    def index_alias(self):
        indices_name = self.index_name.split(", ")
        index = []
        for indx in indices_name:
            index.append(indx)

        if len(index) >= 2:
            print(len(index))
            print("you should define an alias")
            url = 'http://192.168.250.123:9200/_aliases?pretty'
            headers = {
            'Content-Type': 'application/json'
            }
            alias_name = f"alias{random.random()}"
            data = '{"actions" : [ { "add" : { "indices" : %s, "alias" : "%s" } } ]}'%(json.dumps(index), alias_name)
            # data = json.dumps(data)
            print(data)
            try:
                res1 = requests.post(url, headers=headers, data=data)
                res = res1.json()
                print("RESPONSE: ",res)
                rule = Rule.objects.get(id=self.id)
                rule.index_name = alias_name
                # self.index_name= alias_name
                # indices_name = alias_name
                rule.save()            
            except:
                print("ERROR")
        return indices_name

    @property
    def total(self):
        # if self.flag == 'create_rule':
        x=""
        queries = self.queries.all()
        # config = self.config.all() ##config.all() nadare
        if self.sequence == False:
            z = (f"{queries.event_category} where {queries.condition}")
        elif self.sequence == True:
            for i in range (len(queries)):
                b = "sequence\\n "
                c = (f"[{queries[i].event_category} where {queries[i].condition}]\\n  ")
                x = x + c
            z = b + x 
        return z   

    #     elif self.flag == 'strategy':
    #         def create_total(self, queryset):
    #             print("AAAAAAAA", queryset)
    #             return f'{queryset}^^^^'
            # strategy_name = ""
            # for rule in queryset:
            #     a = str(rule)
            #     strategy_name += f"{a} "            
            # rule = Rule.objects.create(name=strategy_name, index_name='pp', flag='strategy')
            
            
    # def create_total(self,queryset):
    #     return f'{queryset}       -----------------------------'       
                
            
    @property
    def sequence(self):
        if self.config.sequence == False:
            return False
        else: 
            return True

    class Meta:
        verbose_name = 'Rule'
        verbose_name_plural = 'Rules'

    def __str__(self):
        return f"{self.name}"
    

class Query(models.Model):
    rule = models.ForeignKey(Rule, on_delete=models.CASCADE, related_name='queries')
    
    ANY = 'any'
    PROCESS = 'process'
    NETWORK = 'network'
    FILE = 'file'
    REGISTRY = 'registry'
    AUTHENTICATION = 'authentication'
    CONFIGURATION = 'configuration'
    DATABASE = 'database'
    DRIVER = 'driver'
    HOST = 'host'
    IAM = 'iam'
    INTRUSION_DETECTION = 'intrusion_detection'
    MALWARE = 'malware'
    PACKAGE = 'package'
    SESSION = 'session'
    THREAT = 'threat'
    WEB = 'web'

    event_category_fields = (
        (ANY, "any"),
        (PROCESS, "process"),
        (NETWORK, "network"),
        (FILE, "file"),
        (REGISTRY, "registry"),
        (AUTHENTICATION, "authentication"),
        (CONFIGURATION, "configuration"),
        (DATABASE, "database"),
        (DRIVER, "driver"),
        (HOST, "host"),
        (IAM, "iam"),
        (INTRUSION_DETECTION, "intrusion_detection"),
        (MALWARE, "malware"),
        (PACKAGE, "package"),
        (SESSION, "session"),
        (THREAT, "threat"),
        (WEB, "web"),
    )
   
    event_category = models.CharField(max_length=32, default=ANY, choices=event_category_fields)
    condition = models.CharField(max_length=200)
    by = models.BooleanField(default=False)
    create_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)
    # default_manager = QueryManager()
    # objects = QueryManager()
    
    class Meta:
        verbose_name = 'Query'
        verbose_name_plural = 'Queries'

    def __str__(self):
        return f"{self.rule}"  

       
class Config(models.Model):
    rule = models.OneToOneField(Rule, on_delete=models.CASCADE, related_name='config')
    sequence = models.BooleanField(default=False)
    until = models.BooleanField(default=False)
    maxspan = models.BooleanField(default=False)
    size = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.rule}"
    
class Strategy(models.Model):
    rules = models.ManyToManyField(Rule)
    strategy_name = models.CharField(max_length=100)
    
    # objects = CustomStrategyManager()
    # default_manager = models.Manager()
    
    class Meta:
        verbose_name = 'Strategy'
        verbose_name_plural = 'Strategies'
        # unique_together = [['rules']]
    
    def __str__(self):
        return f"{self.strategy_name}"
    
    "**************************************************************"
    # def create_strategy(sender, instance, created, **kwargs):
    #     if created:
    #         Rule.objects.create(rule=instance)
    #         print("strategy created!")
    # post_save.connect(create_strategy, sender=Strategy)
    # def update_strategy(sender, instance, created, **kwargs):
    #     if created == False:
    #         pass    
    
    
    
    
    
    # def save(self, *args, **kwargs):
    #     super(Strategy,self).save(*args, **kwargs)
    # @property
    # def ww(self):
    #     strategy = Strategy.objects.get(id=self.id)
        # w = strategy.rules.all()
        # print("@@@@@@@@@@@@@@@@@@@@@@",strategy)
        # print("@@@@@@@@@@@@@@@@@@@self.rules.all(): ",w)
        # print("@@@@@@@@@@@@@@@@@@@@@@",self.strategy_name)
        
        

        # Rule.objects.create(name=self.strategy_name, index_name=str(self.index_alias()))
        # strategy = Strategy.objects.get(id=self.id)

    
    # def index_alias(self):
    #     "------------------------------------------------------------------------------------"
    #     # strategy = Strategy.objects.all()[]
    #     strategy = Strategy.objects.get(id=self.id)
    #     w = strategy.rules.all()
    #     # strategy = Strategy.objects.get(id=self.id)
        
    #     # objects = strategy.rules.all()
    #     # w = strategy.rules.all()
    #     # rule = Rule.objects.first()
    #     # strategies = rule.strategy_set.all()
    #     print("@@@@@@@@@@@@@@@@@@@@@@",strategy)
    #     print("@@@@@@@@@@@@@@@@@@@@@@",w)
        
    #     # Rule.objects.create(name=self.strategy_name, index_name="s")
        
    #     return "ww"

    
    
        
        
        
    
        



        # strategy = Strategy.objects.get(id=self.id)
        # name = strategy.strategy_name
        # rules = Rule.objects.filter(name=name)
        # print(rules)
        # return 'nafb'
        # strategy_rules = strategy.rules.all()
        # print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@",strategy_rules)
        # index = []
        # for rule in strategy_rules:
        #     index.append(rule.index_name)
        # print(index)    
        # return 'test'
        # if len(index) >= 2:
        #     print(len(index))
        #     print("you should define an alias")
        #     url = 'http://192.168.250.123:9200/_aliases?pretty'
        #     headers = {
        #     'Content-Type': 'application/json'
        #     }
        #     alias_name = f"alias{random.random()}"
        #     data = '{"actions" : [ { "add" : { "indices" : %s, "alias" : "%s" } } ]}'%(json.dumps(index), alias_name)
        #     print(data)
        #     try:
        #         res1 = requests.post(url, headers=headers, data=data)
        #         res = res1.json()
        #         print("RESPONSE: ",res)
        #         print("alias_name: ",alias_name)
                         
        #     except:
        #         print("ERROR")
        # return 'rr'
            
