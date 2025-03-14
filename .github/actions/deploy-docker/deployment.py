import os
import sys
import git

def create_tag():
    # Get inputs
    user_name = os.environ['INPUT_USER-NAME']
    email = os.environ['INPUT_USER-EMAIL']
    token = os.environ['INPUT_TOKEN']
    repo_url = os.environ['INPUT_REPO-URL']
    branch = os.environ['INPUT_BRANCH']
    tag_name = os.environ['INPUT_TAG-NAME']
    tag_message = os.environ['INPUT_TAG-MESSAGE'] if len(os.environ['INPUT_TAG-MESSAGE']) > 5 else ''

    # Prepare the repository URL with the token
    repo_clone_url = repo_url.replace('https://', f'https://{token}@')

    # Clone the repository
    repo_path = '/siv/repo'
    repo = git.Repo.clone_from(repo_clone_url, repo_path, branch=branch)

    # Configure Git user
    with repo.config_writer() as config:
        config.set_value('user', 'name', user_name)
        config.set_value('user', 'email', email)

    # Origin set up
    origin = repo.remote(name='origin')

    # Log latest commit and sha
    last_commit = repo.head.commit
    print(f"Last commit SHA: {last_commit.hexsha}\n Last commit message: {last_commit.message}")

    print("Updating submodules...")
    # Update submodules
    # repo.git.submodule('update', '--init', '--recursive')

    # Check for changes in submodules
    # if repo.is_dirty(untracked_files=True):
    #     # Commit the changes
    #     repo.git.add(update=True)
    #     repo.index.commit("Auto updated submodules")

    #     # Push the changes
    #     origin = repo.remote(name='origin')
    #     origin.push(branch)

     # Log latest commit and sha
    last_commit = repo.head.commit
    print(f"Last commit SHA: {last_commit.hexsha}\n Last commit message: {last_commit.message}")

    # Create a new tag
    new_tag = repo.create_tag(tag_name, message=tag_message)

    # Push the tag to the remote repository
    origin.push(new_tag)

    print(f"Submodules updated, changes committed, and tag '{tag_name}' created and pushed to the remote repository.")


if __name__ == "__main__":
    create_tag()
