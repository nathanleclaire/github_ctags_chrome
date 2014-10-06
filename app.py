import git
import sys

url = sys.argv[1]
path = "repos/{0}".format(url.split("/", 3)[-1])
repo = git.repo.base.Repo()
repo.clone_from(url, path)
