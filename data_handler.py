import os
import csv

UserStoryHeaders = ["id", "title", "description", "criteria", "business_value", "estimation", "status" ]
StatusHeaders = ["name"]
user_story_csv_file = os.path.dirname(__file__) + '/UserStory.csv'
status_csv_file = os.path.dirname(__file__) + '/Status.csv'


def get_status_list():
    with open(status_csv_file, "r") as csv_file :
        csvReader = csv.DictReader(csv_file, StatusHeaders)
        
        return list(csvReader)
        
        
def add_story(new_story):
    with open(user_story_csv_file, "a") as csv_file:
        csvWriter = csv.DictWriter(csv_file, UserStoryHeaders)
        csvWriter.writerow(new_story)


def get_story_by_id(story_id): 
    return list(filter(lambda row: story_id == row['id'], get_user_story_list()))[0]
        
        
def update_story(story_id, updated_story):
    stories = get_user_story_list()
    for row in stories:
        if(row['id'] == story_id):
            row['title'] = updated_story['title']
            row['description'] = updated_story['description']
            row['criteria'] = updated_story['criteria']
            row['business_value'] = updated_story['business_value']
            row['estimation'] = updated_story['estimation']
            row['status'] = updated_story['status']
    
    set_user_story_list(stories)
    
            
def delete_story(story_id): 
    story_list = get_user_story_list()
    filtered_story_list = list(filter(lambda row: story_id != row['id'], story_list))
    set_user_story_list(filtered_story_list)
    

def get_user_story_list():
    with open(user_story_csv_file, "r") as csv_file :
        csvReader = csv.DictReader(csv_file, UserStoryHeaders)

        return list(csvReader)
        
        
def set_user_story_list(stories):
    with open(user_story_csv_file, "w") as csv_file:
        csvWriter = csv.DictWriter(csv_file, UserStoryHeaders)
        csvWriter.writerows(stories)

    
def set_default_statuses():
    if(os.path.exists(status_csv_file)):
        os.unlink(status_csv_file)
    with open(status_csv_file, 'w') as status_csv:
        writer = csv.writer(status_csv)
        writer.writerow(["Planning"])
        writer.writerow(["To Do"])
        writer.writerow(["Done"])
        writer.writerow(["In Progress"])
        writer.writerow(["Review"])
    
    
def clear_user_stories():
    if(os.path.exists(user_story_csv_file)):
        os.unlink(user_story_csv_file)
