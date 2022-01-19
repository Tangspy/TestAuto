import os,sys


# print(os.path.abspath(__file__))
# print(os.path.dirname(os.path.abspath(__file__)))
# print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

driver_path = os.path.join(project_path+'/resources')
output_path = os.path.join(project_path+'/output')
conf_path = os.path.join(project_path+'/conf')
common_path = os.path.join(project_path+'/common')
pages_path = os.path.join(project_path+'/pages')
test_cases_path = os.path.join(project_path+'/test_cases')

# print(conf_path)