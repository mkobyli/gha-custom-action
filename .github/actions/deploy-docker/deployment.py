import os
from git import Repo


def create_tag():
    tag_name = os.environ['INPUT_TAG-NAME']
    extra_path = os.environ['INPUT_REPO-PATH']
    github_workspace =  os.environ['GITHUB_WORKSPACE']
    repo_path = github_workspace

    # Prepare path to repo if not in default place
    if extra_path != "":
        repo_path = github_workspace + '/' + extra_path
    print("Path to repo: ", repo_path)

    # Create repo object
    repo = Repo(repo_path)

    # Get the Git command object
    git_cmd = repo.git

    # Add the directory to the list of safe directories
    git_cmd.config('--global', '--add', 'safe.directory', repo_path)
    print(f"Added {repo_path} to safe directories.")

    last_commit = repo.head.commit
    print(f"Last commit SHA: {last_commit.hexsha} \n Last commit message: {last_commit.message}")

    # Create the tag
    new_tag = repo.create_tag(tag_name, message=tag_name)

    # Push the tag to the remote repository
    origin = repo.remote(name='origin')
    origin.push(new_tag)

    print(f"Tag '{tag_name}' created and pushed to the remote repository.")

if __name__ == '__main__':
    create_tag()
