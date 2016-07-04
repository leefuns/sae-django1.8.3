## This is a tutorial on the sae deployment django1.8.3.
### About registration and to create applications, and will not be detailed here, please refer to other tutorials.
>
### Profiles
####  Sae reference document links:[Click it](http://www.sinacloud.com/doc/sae/python/tutorial.html#shi-yong-web-kai-fa-kuang-jia) 
>

##### config.yaml
<pre><code>
   name: lemuzi
   version: 3
   libraries:
   \- name:"django"
   version:"1.8.3"
   handlers:
   \- url: /static
   static_dir: static
</pre></code>
