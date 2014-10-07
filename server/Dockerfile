from debian:wheezy

run apt-get update && \
    apt-get install -y ctags python python-pip python2.7-dev git-core libpq-dev

run git clone https://github.com/nathanleclaire/incorrigible-dotfiles /incorrigible-dotfiles
run cd /incorrigible-dotfiles && ./install_dotfiles.sh

run mkdir /code
add requirements.txt /code/requirements.txt
workdir /code
run pip install -r requirements.txt
add . /code

cmd ["bash"]
