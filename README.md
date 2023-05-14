# Real estate simple site engine

Real estate simple site engine.


## Prepare virtual environment

Install package `python3-venv` to work with python virtual environment.

Update packages on your system `!(it depends on your operating system)`
in this document I use Ubuntu as my operating system. 

So I run update command:

```console
$ sudo apt update
```

and run command:

```console
$ sudo apt install -y python3-venv
```

Then jump to project folder:

```console
$ cd real_estate_agency
```

and create new python environment to run the code:
```console
$ python3 -m venv venv
```

Activate new virtual environment:

```console
$ source venv/bin/activate
```

As a result, you will see command line prompt like this:

```console
(venv) real_estate_agency $
```

Next step, install all necessary dependencies

```console
(venv) real_estate_agency $  pip3 install -r requirements.txt
```

## Prepare database file

Download database file `db.sqlite3` and put it to the project folder, near `manage.py` file.


## Run data migrations 

To run data migrations, execute command:

```console
  (venv) real_estate_agency $ python3 manage.py migrate
```

Migration process takes approximately `5-7 minutes`, it depends on your workstation power.


## Create superuser account

To create superuser account, run command:

```console
  (venv) real_estate_agency $ python3 manage.py createsuperuser
```

This process accompanied with questions, you have just answer to create superuser.


## Run real estate site

To start agency site execute command:

```console
  (venv) real_estate_agency $ python3 manage.py runserver
```

Afterwards, in web browser open link: http://127.0.0.1:8000/admin/

Enter `username` and `password` of superuser you have created in the previous step.

As a result, you will see administration web form, where you can manipulate with all program entities (Flats, Owners, Users, Complaints).


# Projects goals

This site was written as a study project for Python web development course [Devman](https://dvmn.org)
