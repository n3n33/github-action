from github import Github

def get_github_repo(acces_token, repo_name):
    g = Github(acces_token)
    repo = g.get_user().get_repo(repo_name)
    return repo

def upload_github_issue(repo, title, body):
    repo.create_issue(title=title, body=body)