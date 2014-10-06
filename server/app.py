from git.repo.base import Repo
import sys, os

url = sys.argv[1]
path = "repos/{0}".format(url.split("/", 3)[-1])

if __name__ == '__main__':
    if not os.path.isdir(path):
        repo = Repo.clone_from(url, path)
