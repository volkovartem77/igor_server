# Igor Server. Deploy on server Ubuntu 18.04 (DigitalOcean 1GB/1CPU)

### Install Python 3.8

**Make sure that you are logged in as root**

```
apt-get update
sudo apt install -y python3-pip
sudo apt install -y build-essential libssl-dev libffi-dev python3-dev
ln -s /usr/bin/python3.8 /usr/local/bin/python
alias pip=pip3 >> ~/.bash_aliases
```

### Install Git, Server, Redis, Supervisor

```
apt-get install git-core
git clone https://github.com/volkovartem77/igor_server.git
```
```
apt-get install redis-server -y
chown redis:redis /var/lib/redis
```
```
apt-get install supervisor -y
mkdir /var/log/igor_server
cp ~/igor_server/flask_server.conf /etc/supervisor/conf.d/flask_server.conf
supervisorctl update
```

### Creating virtualenv using Python 3.8

```
pip install virtualenv
virtualenv -p /usr/bin/python3.8 ~/igor_server/venv
cd ~/igor_server; . venv/bin/activate
pip install -r requirements.txt
python configure.py
deactivate
```

### Start server
```supervisorctl start flask_server```


### Requests
GET
get users (default sort ID, by ID, by Name) {'status': 'ok', {'result': list]}} {status: fail}
http://127.0.0.1:5000/get_users

get user (by ID, by Name) {'status': 'ok', {'result': dict]}} {status: fail}
http://127.0.0.1:5000/get_user?user_id=0
http://127.0.0.1:5000/get_user?user_name=Andrey

remove user (by ID) {status: ok} {status: fail}
http://127.0.0.1:5000/remove_user?user_id=0

remove all
http://127.0.0.1:5000/remove_all_users

POST
add user {status: ok} {status: fail}
http://127.0.0.1:5000/add_user

update user {status: ok} {status: fail}
http://127.0.0.1:5000/update_user

