import sqlite3
import yaml
import time
import os, re

"""first delete all strategy and rule files"""
def del_yaml(dir, pattern):
    dir = "D:\\Downloads\\VSCode\\elastalert\\rest\\"
    pattern = "Aras_*"
    for f in os.listdir(dir):
        if re.search(pattern, f):
            os.remove(os.path.join(dir, f))

def create_yaml():
    conn = sqlite3.connect('D:\\Downloads\\VSCode\\elastalert\\rest\\db.sqlite3')

    """This is for creating strategy yaml file"""
    cursor_strategy = conn.execute("SELECT * FROM rule_strategy")
    for row in cursor_strategy:
        strategy_name = row [1]
        create_time = row [2]
        modified_time = row [3]
        strategy_alias = row [4]
        strategy_total = row [5]
        dict_file = """[{'ANPdata' : ['creation_date = %s', 'maturity = production', 'updated_date = %s']},
                                {'ANPrule' : [{'author': ["Elastic"]}, {'language': "eql"}, {'rule_id': "55"}, {'threat': 'ghgf'}]},
                                {'name': \" %s \"},
                                {'index': "%s"},
                                {'type': "any"},
                                {'eql' : {'query': "%s"}}]"""%(create_time, modified_time, strategy_name, strategy_alias, strategy_total)
                        
        dict_file = yaml.safe_load(dict_file)          
        with open(f'D:\\Downloads\\VSCode\\elastalert\\rest\\Aras_strategy_{strategy_name}.yaml', 'w') as file:
            yaml.dump(dict_file, file)

    """This is for creating rule yaml file"""
    cursor_rule = conn.execute("SELECT * FROM rule_rule")
    for row in cursor_rule:
        name = row [1]
        index_name = row [2]
        create_time = row [3]
        modified_time = row [4]
        total = row [6]
        dict_file = """[{'ANPdata' : ['creation_date = %s', 'maturity = production', 'updated_date = %s']},
                                {'ANPrule' : [{'author': ["Elastic"]}, {'language': "eql"}, {'rule_id': "55"}, {'threat': 'ghgf'}]},
                                {'name': \" %s\"},
                                {'index': "%s"},
                                {'type': "any"},
                                {'eql' : {'query': "%s"}}]"""%(create_time, modified_time, name, index_name, total)
                        
        dict_file = yaml.safe_load(dict_file)          
        with open(f'D:\\Downloads\\VSCode\\elastalert\\rest\\Aras_rule_{name}.yaml', 'w') as file:
            yaml.dump(dict_file, file)
        
    conn.close()

del_yaml("D:\\Downloads\\VSCode\\elastalert\\rest\\", "Aras_*")

time.sleep(10)

create_yaml()
