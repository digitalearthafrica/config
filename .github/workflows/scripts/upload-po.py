import os
from poeditor import POEditorAPI

def get_languages(client, project_id):
    try:
        # Get the list of languages
        languages = client.list_project_languages(project_id)
        print("Raw response from list_project_languages:")
        print(languages)  # Debugging: Print the raw response

        available_languages = {language['code']: language['name'] for language in languages}
        print("Available languages:")
        for code, name in available_languages.items():
            print(f"Code: {code}, Name: {name}")

        # Check if English ('en') exists in the project
        if 'en' in available_languages:
            print("English language found.")
            return 'en'  # If English is found, return the language code
        else:
            print("English language not found. Please ensure the language exists in your POEditor project.")
            return None  # Return None if English is not found

    except Exception as e:
        print(f"Error fetching languages: {e}")
        return None

def upload_terms(file_path, project_id, api_token, language_code):
    if language_code is None:
        print("No valid language code provided. Skipping upload.")
        return
    
    client = POEditorAPI(api_token=api_token)

    project = client.view_project_details(project_id)
    print(f"Before update, {project['name']} (id: {project['id']}) has {project['terms']} terms.")

    update_results = client.update_terms_translations(
        project_id=project_id,
        file_path=file_path,
        language_code=language_code,  # Use the verified language code (e.g., 'en')
        overwrite=True,
        tags='all',
    )

    terms = update_results['terms']
    print("Terms updated:")
    for k, v in terms.items():
        print(f"\t{k}: {v}")

    project = client.view_project_details(project_id)
    print(f"After update, {project['name']} (id: {project['id']}) has {project['terms']} terms.")


if __name__ == '__main__':
    project_id = os.environ['POEDITOR_PROJECT_ID']
    api_token = os.environ['POEDITOR_API_TOKEN']
    
    # Initialize POEditor client
    client = POEditorAPI(api_token=api_token)
    
    # Get the available language and proceed if English is found
    language_code = get_languages(client, project_id)
    if language_code:
        upload_terms('output/messages.po', project_id, api_token, language_code)
