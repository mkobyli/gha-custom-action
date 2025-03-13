import os
from git import Repo


def create_tag():
    tag_name = os.environ['INPUT_TAG-NAME']
    extra_path = os.environ['INPUT_REPO-PATH']
    token = os.environ['INPUT_TOKEN']
    github_workspace =  os.environ['GITHUB_WORKSPACE']
    github_repository =  os.environ['GITHUB_REPOSITORY']

    print("GitHub repository: ", github_repository)

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

    user_name = os.environ['INPUT_USER-NAME']
    email = os.environ['INPUT_USER-EMAIL']

    with repo.config_writer() as config:
      config.set_value('user', 'name', user_name)
      config.set_value('user', 'email', email)

    print(f"User name {user_name} and email {email} have been set for the local repository.")

    last_commit = repo.head.commit
    print(f"Last commit SHA: {last_commit.hexsha} \n Last commit message: {last_commit.message}")

    # Create the tag
    new_tag = repo.create_tag(tag_name, message=tag_name)

    # Push the tag to the remote repository
    remote_url = f'https://x-access-token:{token}@github.com/{github_repository}'
    # remote_url = f'https://{token}@github.com/{username}/{repository}.git'
    origin = repo.remote(name='origin')
    origin.set_url(remote_url)
    origin.push(new_tag)

    print(f"Tag '{tag_name}' created and pushed to the remote repository.")

if __name__ == '__main__':
    create_tag()
