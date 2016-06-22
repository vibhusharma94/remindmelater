
Django SetUP Guide
===============


#### 1.  **Install Git**
        sudo apt-get update
        sudo apt-get install git
       
####  2. **Clone Repository**
 
    git clone git@github.com:vibhusharma94/remindmelater.git

####  3. **Install PIP and VirtualEnv**
 
         sudo apt-get install build-essential python-dev
         sudo apt-get install python-pip
         sudo apt-get install python-virtualenv
    
#### 4. **Create Virtual Enviornment**
        virtualenv env

#### 5. **Activate Enviornment**
         source env/bin/activate
    
#### 6. **Install Requirements**
 
       cd remindmelater
       pip install -r requirements.txt

#### 7. **Setup Mysql**
      sudo apt-get install mysql-server
      mysql -u root -p
      create database rmldb;

#### 8. **Create django tables**
      python manage.py migrate

#### 9. **Start Django test server**
      python manage.py runserver 8000

#### 10. **Test django app**
      python manage.py test apps.rml -k -v 3

#### 11. **Start celery worker**
      celery -A rmlapp worker -B --loglevel=info


Database Model
===============

####  **Table name: reminder**
      id int(11) NOT NULL AUTO_INCREMENT
      message longtext NOT NULL
      email varchar(255) DEFAULT NULL
      number int(10) unsigned DEFAULT NULL
      scheduled_on datetime(6) NOT NULL
      is_delivered tinyint(1) NOT NULL
      created datetime(6) NOT NULL
