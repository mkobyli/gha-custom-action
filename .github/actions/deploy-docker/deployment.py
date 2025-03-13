import os
from git import Repo


def create_tag():
    tag_name = os.environ['INPUT_TAG-NAME']
    repo_path =  os.environ['GITHUB_WORKSPACE']
    repo = Repo(path=repo_path)
    last_commit = repo.head.commit
    print("Last commit message:", last_commit.message)
    print("Last commit SHA:", last_commit.hexsha)

    new_tag = tag_name
    with open(os.environ['GITHUB_OUTPUT'], 'a') as gh_output:
        print(f'new-tag={new_tag}', file=gh_output)

if __name__ == '__main__':
    create_tag()
