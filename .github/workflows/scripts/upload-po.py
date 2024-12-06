import os
from poeditor import POEditorAPI

# List available methods for POEditorAPI class
def list_methods(client):
    print("Available methods in POEditorAPI:")
    for method in dir(client):
        print(method)

def get_languages(client, project_id):
    try:
        languages = client.get_project_languages(project_id)
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
    
    # List all available methods for POEditorAPI
    list_methods(client)
    
    # Fetch and display available languages
    get_languages(client, project_id)
