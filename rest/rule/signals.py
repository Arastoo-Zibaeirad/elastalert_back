# from .models import Rule, Query, Config, Strategy

# def change_my_name_plz (sender, instance, created, **kwargs):
#     if created:
#         Rule.objects.create(name='something', index_name='sth')



# from django.db.models.signals import post_save
# from django.contrib.auth.models import Strategy
# from django.dispatch import receiver
# from .models import Rule
 
 
# @receiver(post_save, sender=Strategy)
# def create_profile(sender, instance, created, **kwargs):
#     if created:
#         Rule.objects.create(strategy=instance)
  
# @receiver(post_save, sender=Strategy)
# def save_profile(sender, instance, **kwargs):
#         instance.rule.save()


from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Rule, Strategy
import yaml

##we say who is send signals to this function(create_rule)... @receiver myani daryaft konandeye in signal function create_rule ast
@receiver(post_save, sender=Rule)
def create_yaml(sender, instance, created, **kwargs):
    """
    after creating an object in rule, we want to create a yaml file 
    """
    if created:
        dict_file = """[{'ANPdata' : ['creation_date = %s', 'maturity = production', 'updated_date = %s']},
                        {'ANPrule' : [{'author': ["Elastic"]}, {'language': "eql"}, {'rule_id': "55"}, {'threat': 'ghgf'}]},
                        {'name': \" %s \"},
                        {'index': "%s"},
                        {'type': "any"}]"""%(instance.create_time, instance.modified_time, instance.name, instance.index_name)
                
        dict_file = yaml.safe_load(dict_file)          
        with open(f'{instance.name}.yaml', 'w') as file:
            yaml.dump(dict_file, file)

# @receiver(post_save, sender=Strategy)
# def create_rule(sender, instance, created, **kwargs):
#     """
#     create a rule when an object from Strategy is created.
#     """
#     if created:
#         print(instance)
#         Rule.objects.create(name=instance.strategy_name, index_name=instance.rules)
