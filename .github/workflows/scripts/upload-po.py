import os
from poeditor import POEditorAPI


def upload_terms(file_path, project_id, api_token):
    client = POEditorAPI(api_token=api_token)

    project = client.view_project_details(project_id)
    print(f"Before update, {project['name']} (id: {project['id']}) has {project['terms']} terms.")

    update_results = client.update_terms_translations(
        project_id=project_id,
        file_path=file_path,
        language_code='fr',
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

    upload_terms('output/messages.po', project_id, api_token)
