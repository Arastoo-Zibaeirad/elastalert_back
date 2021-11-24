from django.db import models
from django.db.models.fields import BooleanField
import yaml

# Create your models here.
class StrategyManager(models.Manager):
    def get_value(self, queryset, **kwargs):
        a = super().create(**kwargs)
        y = ""
        for i in queryset:
            queries = i.queries.all()
            print("index_name: ", i.index_name)
            
            # for query in queries:
            #     print("query: ",query)
            x = ""
            for i in range (len(queries)):
                c = (f"[{queries[i].event_category} where {queries[i].condition}]\\n ")
                x +=  c
            y += x
        z = "sequence\\n " + y
        print("ZZZZZZZZ: ", z) 
        a.total = z 
        a.save()

class QueryManager(models.Manager):
    def create(self,**kwargs):
        a = super().create(**kwargs)
        print("2222222222", a)
        queries = a.rule.queries.all()
        sequence = a.rule.sequence
        # print('-------', sequence)
        if sequence == False:
            # print('+++++++', sequence)
            z = (f"{queries.event_category} where {queries.condition}")
        
        elif sequence == True:
            x = ""
            for i in range (len(queries)):
                # print("$$$$$len", len(queries))
                c = (f"[{queries[i].event_category} where {queries[i].condition}]\\n  ")
                x +=  c
                z = "sequence\\n " + x 
        
        
        a.total= "ss"
        
        a.save()
        # return z   
    
    
    
    # def create(*args, **kwargs):
        # a = super().create(**kwargs)
        # a.total = "seq"
        # queries = queryset.queries.all()
        
        # print("#######a", args[0])
        
        
        # a.save()
            
#     #         with open(f"rulefile.yaml", "w") as file:
#     #             document = yaml.dump(rule, file)
#     #     return document
#     # def create(self, **kwargs):
#     #     rule = super().create(**kwargs)
#     #     rule.total = "test"
#     #     rule.save()
#     #     return rule
    
#     def get_queryset(self, *args, **kwargs):
#         return super().get_queryset(*args, **kwargs).filter()
    
class Rule(models.Model):
    name = models.CharField(max_length=200, unique=True)
    index_name = models.TextField(blank=True, null=True)
    create_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)
    
    CREATE_RULE = 'create_rule'
    STRATEGY = 'strategy'
    flag_fields = (
        (CREATE_RULE, "create_rule"),
        (STRATEGY, "strategy")
    )
    flag = models.CharField(max_length=250, blank=True, null=True, choices=flag_fields, default=CREATE_RULE)
    total = models.TextField(blank=True, null=True)
   
    default_manager = StrategyManager()
    objects = StrategyManager()


    # @property
    # def total(self):
    #     if self.flag == 'create_rule':
    #         x=""
    #         queries = self.queries.all()
    #         # config = self.config.all() ##config.all() nadare
    #         # print("!!!!!!!!!!!!!!!!!!!!!!!!!", f"{queries[0].event_category} where {queries[0].condition}")
    #         if self.sequence == False:
    #             # print("#####################queries", queries)
                
    #             z = (f"{queries.event_category} where {queries.condition}")

    #             # print("##############################", "HELLLOOO")
    #         elif self.sequence == True:
    #             for i in range (len(queries)):
    #                 b = "sequence\\n "
    #                 c = (f"[{queries[i].event_category} where {queries[i].condition}]\\n  ")
    #                 x = x + c
    #             # print("@@@@@@@@@@@@@@@@@@@@@",f"{queries[0].event_category} where {queries[0].condition}")
    #             z = b + x 
    #         return z   
    #     elif self.flag == 'strategy':
    #         def create_total(self, queryset):
    #             print("AAAAAAAA", queryset)
    #             return f'{queryset}^^^^'
            # print("&&&&&&&", queryset)
            # strategy_name = ""
            # for rule in queryset:
            #     a = str(rule)
            #     strategy_name += f"{a} "            
            # rule = Rule.objects.create(name=strategy_name, index_name='pp', flag='strategy')
            # print("##########stra", )
            
            
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
        return self.name

    # def create_query(self):
    #     # return f"{self.queries.event_category} where {self.queries.condition}"
    # #     if self.sequence:
    # #         return f'sequence\n  [{self.query.event_category} where {self.query.condition}]'    

    # #     elif self.sequence == False:
    #     return f'{self.queries.event_category} where {self.queries.condition}'
    # def create_query_sequence(self):
    #     return f'sequence\n  [{self.queries.event_category} where {self.queries.condition}]'

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
    
    
    default_manager = QueryManager()
    objects = QueryManager()
    

    class Meta:
        verbose_name = 'Query'
        verbose_name_plural = 'Queries'

    def __str__(self):
        return f"{self.rule}"
        # if self.sequence == False:
        #     return f'{self.event_category} where {self.condition}'
        # elif self.sequence:
        #     return f'sequence\n  [{self.event_category} where {self.condition}] '    

       
class Config(models.Model):
    rule = models.OneToOneField(Rule, on_delete=models.CASCADE, related_name='config')
    sequence = models.BooleanField(default=False)
    until = models.BooleanField(default=False)
    maxspan = models.BooleanField(default=False)
    size = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.rule}"