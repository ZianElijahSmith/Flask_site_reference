Might update this later so people can just run a .build_flask_server.sh

# Flask_site_reference
I made a website running on flask, I use this as a reference when building new ones from scratch
<br>
You might find this helpful, but this was mostly intended for myself. I do try to leave comments to help other people
understand what's going on and why. But if you're brand new to flask, this isn't for you. 

#This assumes you've built a website using flask before and just need something to reference in case you forgot something
But it should still help you if you've never done it before.  :3

# This will assist in setting up Flask App on Nginx With Gunicorn on VPS
This config also setups for domain names and ssl

ANYTHING WITH A * AFTER IT, IS INTENDED FOR YOU TO EDIT FOR YOUR OWN USES
FOR EXAMPLE: User=user_name_you_want_to_be* SHOULD BE REPLACED WITH THE USER YOU USE FOR THAT PROJECT WITHOUT THE *

ANYTHING AFER A # SYMBOL IS A COMMENT AND NOT INTENDED TO BE ADDED TO YOUR CONF FILES


The idea is to copy and paste the commands and then follow instructions, you can google questions if you get stuck

##THERE ARE ADDITIONAL FILES ADDED TO THIS REPO YOU WILL NEED TO ADD, THEY'RE NOT IN THIS FILE/GUIDE


# DO NOT USE THE CONF FOUND FROM THESE URLS IT WON'T WORK!!!
# USE THE CONFS IN REPO, JUST USE URLS FOR REFERENCE!!!
https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-18-04
https://blog.miguelgrinberg.com/post/running-your-flask-application-over-https



## Dependencies ##
apt update --fix-missing; apt -y upgrade; apt -y install python3-pip gunicorn3 nginx sudo; apt -y install python3-dev build-essential libssl-dev libffi-dev python3-setuptools; apt -y install python3-venv;



# don't forget to add USER before doing this with the adduser command!

cd /home
python3.6 -m venv app
mkdir app/templates


source app/bin/activate
#pip installs just use pip in venv
pip install wheel flask gunicorn
# Extensions
pip install flask_login flask_mail Flask-PyMongo flask

#add app.py file, run it to test if it works
should run on public_ip:port
If it works, now work on WSGI

# add wsgi.py to app/

gunicorn --bind 0.0.0.0:5000 wsgi:app


Next, let’s create the systemd service unit file.
Creating a systemd unit file will allow Ubuntu’s init system to automatically
start Gunicorn and serve the Flask application whenever the server boots.
sudo nano /etc/systemd/system/myproject.service

# put this inside
<pre>
[Unit]
Description=Gunicorn instance to serve app
After=network.target

[Service]
User=user_name_you_want_to_be*
Group=www-data
WorkingDirectory=/home/user_name_you_want_to_be/app  *
Environment="PATH=/home/user_name_you_want_to_be/app/bin/gunicorn"   *
ExecStart=/home/user_name_you_want_to_be/app/bin/gunicorn --workers 3 --bind unix:app.sock -m 007 wsgi:app   *

[Install]
WantedBy=multi-user.target
</pre>
# end of wsgi.py file

#We can now start the Gunicorn service we created and enable it so that it starts at boot:
sudo systemctl start myproject;
sudo systemctl enable myproject;

#if that worked, you'll get this message
Created symlink /etc/systemd/system/multi-user.target.wants/app.service → /etc/systemd/system/app.service.


# now let's add nginx confs so default web traffic is Flask

sudo nano /etc/nginx/sites-enabled/app

# create symlink
sudo ln -s /etc/nginx/sites-enabled/app /etc/nginx/sites-available

###############
## SSL Setup ##
###############
# Next we need to do ssl
sudo apt install python-certbot-nginx
sudo certbot --nginx -d your_domain -d www.your_domain  *

# Boom, now you have flask, redirect, and ssl
