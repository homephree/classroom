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

