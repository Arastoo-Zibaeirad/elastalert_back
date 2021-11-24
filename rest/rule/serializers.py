from django.db.models import fields
from rest_framework import serializers
from .models import Query, Rule

class RuleSerializer(serializers.ModelSerializer):
    serialization_title = "Rule"
    """many should be false because each query related to one rule
       name should be 'query' as the same as related_name in OntoOneField
    """
    query = serializers.StringRelatedField(many=False)
    
    class Meta:
        model = Rule
        fields = "__all__"
        # depth = 1
        # fields = ['name', 'index_name', 'query']


# class QuerySerializer(serializers.ModelSerializer):
#     serialization_title = "Queryrule_query.id"
#     class Meta:
#         model = Query
#         fields = "__all__"
        
