import git
import os

url = os.argv[1]
path = "repos/{0}".format(url.split("/", 3))
repo = git.repo.base.Repo()
repo.clone_from(url, path)
