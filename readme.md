<h2>Preview</h2>

<pre>
Python Django Framework Project.
Will gladly be questioned and will listen to all your suggestions.
Contact me via links in my profile.
Installation down below.
Remember to read PatchNotes.
</pre>

<pre>
Site has the following features:
 1) Navigation bar.
 2) Registration form.
 3) Login and Logout.
 4) Reset password form via email.
 7) Change password form.
 5) Articles creation form.
 6) Smart articles feed.
 8) Personal user profile.
 9) Change user profile information and avatar.
10) Leaving comments under articles.
 </pre>
 
 <pre>
Upcoming features:
 1) View all of your articles.
 2) In-site messanger (prob.)
 </pre>
 
 <pre>
 P.S. 
 I'm back-end developer so don't criticize the site beauty and front-end part. Thanks.
</pre>
------------
<h2>Installation</h2>

1) Install all required solutions.
   ```
    sudo apt-get update
    sudo apt-get install -y git python3-venv python3-pip vim
    git clone https://github.com/pkozhem/django-project-dev1.git
    cd django-project-dev1
   ```
2) Create and activate virtual environment.
   ```
    python3 -m venv venv
    source venv/bin/activate
   ```
3) a) If you want production version, install all frameworks and libraries for production.
   ```
    python3 -m pip install -r headproject/requirements/prod.txt
   ```
   b) If you want development version, install all frameworks and libraries for development.
   ```
    python3 -m pip install -r headproject/requirements/dev.txt
   ```
4) Set your environment variables.
   ```
    nano headproject/headproject/settings/env.template
   ```
   Don't forget to save and exit (ctrl+s, ctrl+x). Then do this.
   ```
    cp headproject/headproject/settings/.env.template headproject/headproject/settings/.env 
   ```
5) If you chose production version.
   ```
    nano headproject/headproject/settings/prod.py
   ```
   Find ALLOWED_HOSTS variable and input between [ ] needed IP address in ' ', example: ALLOWED_HOSTS = ['127.0.0.1:8000', 'localhost:8001'].
   Don't forget to save and exit (ctrl+s, ctrl+x).
6) ```
    python3 manage.py makemigrations
    python3 manage.py migrate
   ```
7) To run app locally.<br>
   a) Using production settings:
      ```
       python3 manage.py runserver --settings=headproject.settings.prod
      ```
   b) Using development settings:
      ```
       python3 manage.py runserver --settings=headproject.settings.dev
      ```
   ----------
8) To run this app on server you can choose any solution stack (for example Linux + NGINX + Gunicorn) 
   and setup them as you want.
