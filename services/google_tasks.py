# Google Tasks Moment

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from auth import get_credentials
import json


def get_service():
    creds = get_credentials()
    return build("tasks", "v1", credentials=creds)

def get_task_lists():
    try: 
        service = get_service()
        results = service.tasklists().list().execute()
        lists = results.get("items", [])

        return lists
    
    except HttpError as err:
        print(f"Google API error: {err}")
        return []

    except Exception as err:
        print(f"Couldn't connect to Google: {err}")
        return []

def get_tasks(list_id):
    try:
        service = get_service()
        results = service.tasks().list(tasklist=list_id).execute()
        tasks = results.get("items",[])

        return tasks
    
    except HttpError as err:
        print(f"Google API error: {err}")
        return []
    
    except Exception as err:
        print(f"Oops! An error occured? Here: {err}")
        return []

def update_task(task_id):
    try:
        service = get_service()
    except:
        print("die")



task_lists = get_task_lists()
tasks = get_tasks("MDA5MjI5MzkyMTY5MTg2OTAyNTc6MDow")

with open("Tasks.json", "w") as json_file:
        json.dump(tasks, json_file, indent=4)