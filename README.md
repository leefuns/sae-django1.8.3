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
   
##### wsgi.py
<pre><code>
  import os
  import sys
  from django.core.wsgi import get_wsgi_application
  
  root = os.path.dirname(__file__)
  sys.path.insert(0,os.path.join(root, '..', 'site-packages'))
  os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangobook.settings")
  application = get_wsgi_application()
</code></pre>

##### Under the new project root directory site-packages and static folder, copy the django installation directory files and static files to the project folder.

django installation directory is usually in C:\Python27\Lib\site-packages  
static filse usually in C:\Python27\Lib\site-packages\django\contrib\admin\static

