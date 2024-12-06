import os
from poeditor import POEditorAPI

def get_languages(client, project_id):
    try:
        # Use list_project_languages instead of get_project_languages
        languages = client.list_project_languages(project_id)  # Correct method
        print("Available languages:")
        for language in languages['languages']:
            print(f"Code: {language['code']}, Name: {language['name']}")
    except Exception as e:
        print(f"Error fetching languages: {e}")

if __name__ == '__main__':
    project_id = os.environ['POEDITOR_PROJECT_ID']
    api_token = os.environ['POEDITOR_API_TOKEN']
    
    # Initialize POEditor client
    client = POEditorAPI(api_token=api_token)
    
    # Fetch and display available languages
    get_languages(client, project_id)
