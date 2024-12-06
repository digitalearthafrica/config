import os
from poeditor import POEditorAPI

def get_languages(client, project_id):
    try:
        # Use list_project_languages to get the languages
        languages = client.list_project_languages(project_id)
        print("Raw response from list_project_languages:")
        print(languages)  # Debugging: Print the raw response

        # Check if the response has the expected structure
        if isinstance(languages, dict) and 'languages' in languages:
            print("Available languages:")
            for language in languages['languages']:
                print(f"Code: {language['code']}, Name: {language['name']}")
        else:
            print("Unexpected response structure. Please check the raw response.")
            
    except Exception as e:
        print(f"Error fetching languages: {e}")

if __name__ == '__main__':
    project_id = os.environ['POEDITOR_PROJECT_ID']
    api_token = os.environ['POEDITOR_API_TOKEN']
    
    # Initialize POEditor client
    client = POEditorAPI(api_token=api_token)
    
    # Fetch and display available languages
    get_languages(client, project_id)
