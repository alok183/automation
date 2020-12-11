#!bin/bash
# owner alok.shrivastava(alok183)
apt-get -y update 
apt-get -y install git
pip3 install --user --upgrade kapitan
git clone https://github.com/ramaro/kapitan-examples.git

tail -f /dev/null