import sys
import json
import os
from datetime import datetime
platform = os.name
data_template = {
    "tasks": 
    {
        
    }
}
#loading available json into variable data, if not exist create new one with template
try:
    with open("data.json","r") as file:
        data = json.load(file)
except:
    with open("data.json","w") as file:
        print("Json file does not exist, creating json template...")
        json.dump(data_template,file,indent=2)
        data = data_template


#<functions>
#the following function is very useful to find a task from the task id
def get_task_name(data: dict,task_id: str):
    for task in data["tasks"]:
        if int(data["tasks"][task]['id']) == int(task_id):
            return task
        
def get_cur_time_formatted() -> str: 
    cur_date = datetime.now()
    string_time = cur_date.strftime("%Y-%m-%d %H:%M:%S")
    return string_time
def add_task(data: dict ,task_name: str ,status: str) -> dict: #btw status will always be incomplete when creating a new task so its kind of useless but just incase i add a status parameter
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

    if input("Would you like to add a description to this task? y/n") == 'y':
        description = input("Please type in your description...")
    else:
        print("Description will be empty for this task")
        description = ''  
    string_time = get_cur_time_formatted()
    data["tasks"][task_name] = {
        "id" : first_available_id,
        "description" : description,
        "status" : status,
        "CreatedAt" : string_time,
        "UpdatedAt" : string_time,                     
        }
    print(f"Task {task_name} created with ID of {first_available_id}")
    return data
def delete_task(data,task_id):
    task_name = get_task_name(data,task_id)
    del data["tasks"][task_name]
    print(f"Deleted task {task_name}")
    return data     

def update_task(data:dict,task_id:str,new_task_name: str):
    task_name = get_task_name(data,task_id)
    data['tasks'][task_name]["UpdatedAt"] = get_cur_time_formatted()
    old_task_values = data["tasks"].pop(task_name)
    data["tasks"][new_task_name] = old_task_values
    print(f"Renamed task {task_name} with new name {new_task_name}")
    return data
    

def list_tasks(data: dict, list_what = None):
    if list_what == '':
        list_what = None
    valid_list_options = ["incomplete", "in-progress", "complete"]
    if list_what not in valid_list_options and list_what is not None:
        print(f"Invalid list option: {list_what}. Valid options are: {valid_list_options}")
    #select which tasks to list based on list_what variable, if None then it will list all otherwise use valid_list_options    
    for task in data["tasks"]:
        if data["tasks"][task]["status"] == list_what or list_what is None:
            print("---------------")
            print(task,':')
            task_dict = data["tasks"][task]
            for property in task_dict:
                print(f"{property} : {task_dict[property]}")

#function used to change status for a task
def change_status(data: dict,task_id: str, option: int) -> dict:
    task_name = get_task_name(data,task_id)
    valid_list_options = ["incomplete", "in-progress", "complete"]
    data['tasks'][task_name]['status'] = valid_list_options[option]
    data['tasks'][task_name]['UpdatedAt'] = get_cur_time_formatted()
    print(f"set task {task_name} status to {valid_list_options[option]}")                
    return data

def print_help():
    global platform
    #run_command variable is used for storing how to run taskcli, on linux there is a dedicated file that you can just execute
    if platform == 'posix':
        run_command = './taskcli'
    else:
        run_command = 'python taskcli.py'

    print("Please input a working command:")
    print(f"{run_command} add taskname: adds a task with name taskname ")
    print(f"{run_command} list typeoftask: lists all tasks and various info about each task, typeoftask can either be incomplete,in-progress,or complete")
    print(f"{run_command} update task_id task_name: renames task with id of task_id to task_name")
    print(f"{run_command} set-incomplete task_id: sets a task with id of task_id to incomplete if you dont know the id use {run_command} list to find the id")
    print(f"{run_command} set-in-progress task_id")
    print(f"{run_command} set-complete task_id")

#</functions>




#<argumentprocessing>
if len(sys.argv) >= 2:
    if sys.argv[1] == 'add':
        try:
            data = add_task(data,sys.argv[2],"incomplete")
        except:
            print("Please input a valid task name")


    elif sys.argv[1] == 'delete':
        try:
            data = delete_task(data,sys.argv[2])
        except:
            print("please input a valid task id")

    
    elif sys.argv[1] == 'update':
        try:
            data = update_task(data,sys.argv[2],sys.argv[3])
        except:
            print("please input a valid task id and/or valid tasknane")


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
            print("Please input a valid task id")  


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