from debian:wheezy

run apt-get update && \
    apt-get install -y ctags python python-pip python2.7-dev

run mkdir /code
add requirements.txt /code/requirements.txt
workdir /code
run pip install -r requirements.txt
add . /code

cmd ["bash"]
