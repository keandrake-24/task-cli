import sys
import json
arguments = sys.argv
data_template = {
    tasks: 
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