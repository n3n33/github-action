import os
from datetime import datetime
from pytz import timezone

from get_releasenote import get_releasenote
from github_issue import get_github_repo, upload_github_issue


if __name__ == "__main__":
    access_token = os.environ['GIT_ACTION_SECRET']
    repository_name = "github-action"

    seoul_timezone = timezone('Asia/Seoul')
    # seoul_timezone = datetime.today()
    today = datetime.now(seoul_timezone)
    today_date = today.strftime("%Y년 %m월 %d일")

    releaseurl = "https://hadoop.apache.org/docs/stable/"
    
    contents = get_releasenote(releaseurl)
    
    issue_title = f"hadoop release note({today_date})"
    upload_contents = contents
    repo = get_github_repo(access_token, repository_name)
    upload_github_issue(repo, issue_title, upload_contents)
    print("finish")