
from django import http
from django.db.models import query
from django.db.models.query import QuerySet
from django.http import response
from django.shortcuts import render
from rest_framework import HTTP_HEADER_ENCODING, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from .models import Rule, Query, Config, Strategy
from .serializers import RuleSerializer

from rest_framework import viewsets
from django.shortcuts import get_object_or_404
import yaml


def test(request, id):
    strategy = Strategy.objects.get(id=id)
    rules = strategy.rules.all()
    # rule = request.rules
    # f = strategy_id.rules.add(rule)
    print(rules)
    # print(rule)
    # print(f)
    return response.HttpResponse("fff")


# def rule_yaml(request):
#     res = response.HttpResponse(content_type='text/yaml')
#     res['Content-Disposition'] = 'attachment; filename = rule.yaml'
#     rules = Rule.objects.all()
    
#     lines = []
#     for rule in rules:
        
#         lines.append(f"{rule.name}\n{rule.index_name}\n{rule.total}\n{rule.sequence}\n{rule.create_time}\n{rule.modified_time}\n\n\n")
        
#         # for i in range(len(rules)):
#         #     with open(f"rulefile{i}.yaml", "w") as file:
#         #         document = yaml.dump(rule, file)
                

#     res.writelines(lines)
#     # print("########lenrule: ", len(rules))
#     print("########res: ", res)




#     # return response.HttpResponse("OK")
#     return res







def query_total(request):
    try:
        
        rule = Rule.objects.get(id=3)
        queries = rule.queries.all()
        print("1: ", queries)
        seq = rule.config.sequence
        print("seq: ", seq)
       
       
        # x = ""
        
        for i in range (len(queries)):
            # print("test: ",queries[i].event_category)
            
            b = "sequence\n "
            # print("test: ",)
            
            
        #     c = (f"[{queries[i].event_category} where {queries[i].condition}] ")
        #     x = x + c

        # z = b + x 
        # print(z)

            
            
            # if query.sequence == False:
            #     a += str(f"{queries[i].event_category} where {queries[i].condition} ")

            # elif query.sequence:
            #     # for i in range(len(queries)):
            #     a += str(f"sequence\\n [{queries[0].event_category} where {queries[0].condition}] ")
            #     # a += 'sequence [%s where aaa] '%query.event_category[1]
            #     print(a)


            # print(a)
        return response.HttpResponse("hello")            


    except:
        return response.HttpResponse("ERROR")
        
    # return response.HttpResponse(queries) 
    # return response.HttpResponse(query)
    




# def query_total_detail(request, pk):
#     try:

#         rule = Rule.objects.get(pk=pk)
#         q = rule.queries.all()

#     except:
#         return response.HttpResponse("does not exist")    
    
#     return response.HttpResponse(q)

# def get_rule_id(request, pk):
#     rule = Rule.objects.get(pk=pk)
#     queries = rule.queries.all()
#     config = rule.config.all()
#     for query in queries:
#         if query.sequence == False:
#             print(f"{query.event_category} where {query.condition}")
        
#         elif query.sequence:
#             print(f"sequence\\n [{query.event_category} where {query.condition}] ")

#     return response.HttpResponse(queries)
    
# Create your views here.
# ############################################################
# class RuleList(generics.ListCreateAPIView):
#     queryset = Rule.objects.all()
#     serializer_class = RuleSerializer
#     pass


# class RuleViewSets(viewsets.ModelViewSet):
#     """
#     A simple ViewSet for listing or retrieving users.
#     """
#     serializer_class = RuleSerializer
#     def get_queryset(self):
#         rule = Rule.objects.all()
#         return rule

#     def list(self, request):
#         """
#         List of all rules
#         """
#         queryset = Rule.objects.all()
#         serializer = RuleSerializer(queryset, many=True)
#         return Response(serializer.data)

#     def retrieve(self, request, *args, **kwargs):
#         """
#         retrieve the rule base on the name
#         """
#         params = kwargs
#         print(params['pk'])
#         name = Rule.objects.filter(name=params['pk'])
#         serializer = RuleSerializer(name, many=True)
#         return Response(serializer.data)

############################################

    # def retrieve(self, request, *args, **kwargs):
    #     """
    #     retrieve the rules based on index name
    #     """
    #     params = kwargs
    #     print(params['pk'])
    #     index_name = Rule.objects.filter(index_name=params['pk'])
    #     serializer = RuleSerializer(index_name, many=True)
    #     return Response(serializer.data)
        
    # def create(self, request, *args, **kwargs):

    #     """
    #     create a new rule 
    #     """

    #     rule_data = request.data
    #     new_rule = Rule.objects.create(name=rule_data["name"], index_name=rule_data["index_name"])
    #     new_rule.save()
    #     serializer = RuleSerializer(new_rule)
    #     return Response(serializer.data)

    # def destroy(self, request, *args, **kwargs):
    #     logedin_user = request.user
    #     if(logedin_user == "admin"):
    #         rule = self.get_object()
    #         rule.delete()
    #         response_message = {"message": "item has been deleted"}
    #     else:
    #         response_message = {"message": "not allowed"}

    #     return Response(response_message)


    # def get(self, request, *args, **kwargs):
    #     try:
    #         id = request.query_params["id"]
    #         if id != None:
    #                 rule = Rule.objects.get(id=id)
    #                 serializer = RuleSerializer(rule)
    #     except:    
    #         rule = self.get_queryset()
    #         serializer = RuleSerializer(rule, many=True)
        
    #     return Response(serializer.data)




    # def post(self, request, *args, **kwargs):    
        
    #     rule_data = request.data
    #     new_rule = Rule.objects.create(name=rule_data["name"], index_name=rule_data["index_name"])
    #     new_rule.save()
    #     serializer = RuleSerializer(new_rule)
    #     return Response(serializer.data)


# @api_view(["GET"])
# def rule_list(request):
#     rule = Rule.objects.all()
#     rule_serialize = RuleSerializer(rule, many=True)
#     return Response(rule_serialize.data)

# @api_view(["GET"])
# def rule_detail(request, pk):
#     try:
#         rule = Rule.objects.get(id=pk)
#     except:
#         return response.HttpResponse(status=404)
#     rule_serialize = RuleSerializer(rule, many=False)
#     return Response(rule_serialize.data)
    
# @api_view(["POST"])
# def rule_save(request):
#     rule = RuleSerializer(data=request.data)
    
#     if rule.is_valid():
#         rule.save()
#         return Response(rule.data, status=201)
#     return Response()

# @api_view(["POST"])
# def rule_update(request, pk):
#     instance = Rule.objects.get(id=pk)
#     rule = RuleSerializer(instance=instance, data=request.data)
#     if rule.is_valid():
#         rule.save()
    
#     return Response()

# @api_view(["DELETE"])
# def rule_delete(request, pk):
#     instance = Rule.objects.get(id=pk)
#     # rule = RuleSerializer(instance=instance, data=request.data)
#     # if rule.is_valid():
#     #     rule.save()
#     instance.delete()
#     return Response("Rule Deleted")