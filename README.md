# EZ AWS DNS

Use AWS Route53 to keep a DNS record up to date with a dynamically changing home internet IP address.


## Setup
Install `pyenv`: 
```sh
sudo apt update && sudo apt install -y make build-essential libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev \
libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev python-openssl git

curl https://pyenv.run | bash

# add to end of .bashrc
export PATH="~/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"

pyenv install 3.9.2
pyenv local 3.9.2
```

Install `poetry`:
```sh
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python

# add to end of .bashrc
export PATH=$HOME/.poetry/bin:$PATH
```