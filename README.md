Local (mac) dev config - using pyenv to control python versions
```
   brew update
   pyenv install 3.5.2
   pyenv virtualenv 3.5.2 classroom
```

Server side node config, assuming python is installed:

   sudo apt-get install npm nodejs-legacy

Local node config - using node to install

```
nvm config to allow me to have iojs and node together
export NVM_DIR=`brew --prefix nvm`
source $(brew --prefix nvm)/nvm.sh
nvm use --delete-prefix v6.10.1
```
#Option 1

- use a simple scripted JupyterHub install, backed by S3 notebook 
trying s3 model "https://github.com/danielfrg/s3contents"

## Other options

It might be worth trying cloudfront / cf option ; https://mihevc.org/2017/10/26/jupyterhub-for-teamwork-on-aws.html

Can also consider the emr option https://aws.amazon.com/blogs/big-data/running-jupyter-notebook-and-jupyterhub-on-amazon-emr/
This gives lots of scalability options but prob overkill for simple classroom.

It might be worth thinking about containerising the config using Elastic Beanstalk - but would have to make
sure that the Jupyter config (s3 model) is applied on each version. Especially - not suer how to add user accounts
in beanstalk.

`pip3 install awsebcli


## see also python install

sudo yum install git

curl -L https://raw.githubusercontent.com/pyenv/pyenv-installer/master/bin/pyenv-installer | bash

vim .bash_profile

add following lines to .bash_profile:

export PATH="/home/ec2-user/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
sudo yum install gcc

sudo yum install openssl-devel

sudo yum install bzip2-devel

sudo yum install sqlite-devel

sudo yum install readline-devel

sudo yum install patch

pyenv install 3.5.2

Install lxml lib
sudo yum install libxml2-dev libxslt-dev python34-dev python35-dev


add user

sudo vi /etc/ssh/sshd_config
:
PasswordAuthentication yes

sudo adduser <user>
sudo passwd <user>

add npm

curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.6/install.sh | bash
. ~/.nvm/nvm.sh
nvm install 6.11.5
node -e "console.log('Running Node.js ' + process.version)"

