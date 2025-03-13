import os
from git import Repo


def create_tag():
    tag_name = os.environ['INPUT_TAG-NAME']
    extra_path = os.environ['INPUT_REPO-PATH']
    repo_path =  os.environ['GITHUB_WORKSPACE']

    # Prepare path to repo
    if extra_path != "":
        repo_path = repo_path + '/' + extra_path
    print("repo path: ", repo_path)

    # Create repo object
    repo = Repo(repo_path)

    # Get the Git command object
    git_cmd = repo.git

    # Add the directory to the list of safe directories
    git_cmd.config('--global', '--add', 'safe.directory', repo_path)
    print(f"Added {repo_path} to safe directories.")

    last_commit = repo.head.commit
    print("Last commit message:", last_commit.message)
    print("Last commit SHA:", last_commit.hexsha)

    new_tag = tag_name
    with open(os.environ['GITHUB_OUTPUT'], 'a') as gh_output:
        print(f'new-tag={new_tag}', file=gh_output)

if __name__ == '__main__':
    create_tag()
