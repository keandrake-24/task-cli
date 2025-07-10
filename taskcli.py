import sys
import json
from datetime import datetime
data_template = {
    "tasks": 
    {
        
    }
}
try:
    with open("data.json","r") as file:
        data = json.load(file)
except:
    with open("data.json","w") as file:
        print("Json file does not exist, creating json template...")
        json.dump(data_template,file,indent=2)
        data = data_template


#<functions>

def add_task(data: dict ,task_name: str ,status: str) -> dict:
    cur_date = datetime.now()
    

    #search for the lowest available id
    taken_ids = list()
    for task in data["tasks"]:
        taken_ids.append(data["tasks"][task]['id'])
    i = 1
    while True:
        if i not in taken_ids:
            first_available_id = i
            break
        else:
            i += 1

    string_time = cur_date.strftime("%Y-%m-%d %H:%M:%S")
    if input("Would you like to add a description to this task? y/n") == 'y':
        description = input("Please type in your description...")
    else:
        print("Description will be empty for this task")
        description = ''    
    data["tasks"][task_name] = {
        "id" : first_available_id,
        "description" : description,
        "status" : status,
        "CreatedAt" : string_time,
        "UpdatedAt" : string_time                     
        }
    print(f"Task {task_name} created with ID of {first_available_id}")
    return data


def list_tasks(data: dict, list_what = None):
    valid_list_options = ["incomplete", "in-progress", "complete"]
    if list_what not in valid_list_options and list_what is not None:
        print(f"Invalid list option: {list_what}. Valid options are: {valid_list_options}")
    #select which tasks to list based on list_what variable, if None then it will list all otherwise use valid_list_options    
    for task in data["tasks"]:
        if data["tasks"][task]["status"] == list_what or list_what is None:
            print(task)
            task_dict = data["tasks"][task]
            for property in task_dict:
                print(f"{property} : {task_dict[property]}")

#function used to change status for a task
def change_status(data: dict,task_id: int, option: int) -> dict:
    valid_list_options = ["incomplete", "in-progress", "complete"]
    #loop over the tasks to find the task with the task id chosen
    for task in data["tasks"]:
        if int(data["tasks"][task]['id']) == int(task_id):
            data["tasks"][task]['status'] = valid_list_options[option]                
    return data

def print_help():
    print("Please input a working command:")
    print("taskcli.py add taskname: adds a task with name taskname (BTW if you delete a task creating a new task will cause it to take up the id of that previously deleted task)")
    print("taskcli.py list typeoftask: lists all tasks and various info about each task, typeoftask can either be incomplete,in-progress,or complete")
    print("taskcli.py set-incomplete task_id: sets a task with id of task_id to incomplete if you dont know the id use taskcli.py list to find the id")
    print("taskcli.py set-in-progress")
    print("taskcli.py set-complete")

#</functions>




#<argumentprocessing>
if len(sys.argv) - 1 >= 1:
    if sys.argv[1] == 'add':
        try:
            data = add_task(data,sys.argv[2],"incomplete")
        except:
            print("Please input a valid task name")
    elif sys.argv[1] == 'list':
        if len(sys.argv) - 1 >= 2:
            list_tasks(data,sys.argv[2])
        else:
            list_tasks(data)
    elif sys.argv[1] == 'set-incomplete':
        try:
            data = change_status(data,sys.argv[2],0)
        except:
            print("please input a task id")
         
    elif sys.argv[1] == 'set-in-progress':
        try:
            data = change_status(data,sys.argv[2],1)
        except: 
            print("Please input a task id")       
    elif sys.argv[1] == 'set-complete':
        try:
            data = change_status(data,sys.argv[2],2)
        except:
            print("Please input a task id")
    else:        
        print_help()

else:
    print_help()
#</argumentprocessing>

with open("data.json","w") as file:
    json.dump(data,file,indent=2)