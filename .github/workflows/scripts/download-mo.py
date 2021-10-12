import os
from poeditor import POEditorAPI


def download_translation(file_path, project_id, api_token):
    client = POEditorAPI(api_token=api_token)

    client.export(
        project_id=project_id,
        language_code='fr',
        file_type='mo',
        local_file=file_path,
    )


if __name__ == '__main__':
    project_id = os.environ['POEDITOR_PROJECT_ID']
    api_token = os.environ['POEDITOR_API_TOKEN']

    download_translation('./translations/fr/LC_MESSAGES/fr.mo', project_id, api_token)
