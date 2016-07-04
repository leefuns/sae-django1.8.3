## This is a tutorial on the sae deployment django1.8.3.
### About registration and to create applications, and will not be detailed here, please refer to other tutorials.
  
####  Sae reference document links:[Click it](http://www.sinacloud.com/doc/sae/python/tutorial.html#shi-yong-web-kai-fa-kuang-jia) 

##### config.yaml
<pre><code>
   name: lemuzi
   version: 3
     
   libraries:
   - name:"django"
   version:"1.8.3"
     
   handlers:
   - url: /static
   static_dir: static
</code></pre>
  
##### index.wsgi
<pre><code>
   import os
   import sys
   
   root = os.path.dirname(__file__)
   sys.path.insert(0, os.path.join(root, 'site-packages'))
   os.environ.setdefault("DJANGO_SETTINGS_MODULE" , "djangobook.settings")
   
   from django.core.wsgi import get_wsgi_application  
   application = get_wsgi_application()
</code></pre>

Under the new project root directory site-packages and static folder, copy the django installation directory files and static files to the project folder.

django installation directory is usually in C:\Python27\Lib\site-packages  
static filse usually in C:\Python27\Lib\site-packages\django\contrib\admin\static

#### About mysql
Exporting local databases through navicat software and then uploaded to the sae database.  

#### Settings.py file in a shared server environment and local development environment
##### settings.py
<pre><code>
  if socket.gethostname() != 'Your computer name':
      from sae.const import MYSQL_DB, MYSQL_USER, MYSQL_PASS, MYSQL_HOST,MYSQL_PORT 
      DATABASES = {
          'default': {
              'ENGINE': 'django.db.backends.mysql',
              'NAME': 'Your app name',
              'USER': 'User name',
              'PASSWORD': 'Password',
              'HOST': 'Mysql host',
              'PORT': '3307',
          }
      }
  else:
      DATABASES = {
          'default': {
              'ENGINE': 'django.db.backends.mysql',
              'NAME': 'Local Database name',
              'USER': 'User name',
              'PASSWORD': 'Password',
              'HOST': 'Mysql host',
              'PORT': 'Mysql port',
          }
      }
</code></pre>
