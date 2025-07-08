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
    num_tasks = 0

    for i in data["tasks"]:
        num_tasks += 1

    string_time = cur_date.strftime("%Y-%m-%d %H:%M:%S")
    if input("Would you like to add a description to this task? y/n") == 'y':
        description = input("Please type in your description...")
    else:
        print("Description will be empty for this task")
        description = ''    
    data["tasks"][task_name] = {
        "id" : num_tasks + 1,
        "description" : description,
        "status" : status,
        "CreatedAt" : string_time,
        "UpdatedAt" : string_time                     
        }
    print(f"Task {task_name} created with ID of {num_tasks + 1}")
    return data


def list_tasks(data: dict) -> dict:
    for task in data["tasks"]:
        print(task)
        task_dict = data["tasks"][task]
        for property in task_dict:
            print(f"{property} : {task_dict[property]}")

#</functions>




#<argumentprocessing>
try:
    if sys.argv[1] == 'add':
        try:
            data = add_task(data,sys.argv[2],"incomplete")
        except:
            print("Please input a valid task name")
    elif sys.argv[1] == 'list':
        list_tasks(data)
except:
    print("Please input a working command:")
    print("taskcli.py add taskname: adds a task with name taskname")
    print("taskcli.py list: lists all tasks and various info about each task")
#</argumentprocessing>

with open("data.json","w") as file:
    json.dump(data,file,indent=2)