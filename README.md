# Django REST with React

- [Tutorial blog post](https://www.valentinog.com/blog/tutorial-api-django-rest-react/)
- [Django models documentation](https://docs.djangoproject.com/en/2.0/ref/models/fields/)


### Level zero:
 - Installing [pipenv](https://pipenv.readthedocs.io/en/latest/)
 - Using pipenv to create virtual env
	 - `pipenv --three`
 - Installing django rest framework
	 - `pipenv install django djangorestframework`
 - [ ] Spawn a shell within virtual env; WHAT IS THAT?
	 - `pipenv shell`

### Starting up a project

 - Create django proejct:
	 - `django-admin startproject project`
 - Creating a new django application:
	 - Django projects consists of many **applications**
	 - Ideally those applications should do only one thing
	 - `cd project`
	 - `django-admin startapp app_name`
 
### Setting up a model:
- Some example:
```python
from django.db import models 

# Create your models here.

class  Article(models.Model):
	name = models.CharField(max_length=300)
	heade_pl = models.TextField()
	header_en = models.TextField()
	content_pl = models.TextField()
	content_en = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)

	def  __str__(self):
		return  self.name
```
- After making changes to the model:
	- `python manage.py makemigrations app_name`
	- `python manage.py migrate`

### Serialization:
- **[Serialization](https://en.wikipedia.org/wiki/Serialization)** is the act of transforming an object into another data format.
- After transforming an object we can save it to a file or send it through the network.
- Create `serializers.py` inside app_name directory
```python 
from rest_framework import serializers
from articles.models import Article

class  ArticleSerializer(serializers.ModelSerializer):
	class  Meta:
		model = Article
		fields =  '__all__' 
```
- Fields: assign all like above or do it manualy

### Setting up controll... Views
- Coming from other frameworks you may find surprising that **Django has no controllers**.
- The controller encapsulates the logic for processing requests and returning responses. In the traditional MVC architecture there is the Model, the View, and the Controller.
- Django is a **MVT framework**. That is, Model – View – Template. 
	- *The View takes care of the request/response lifecycle.*
- There are many types of views in Django: 
	- [function views](https://docs.djangoproject.com/en/2.0/topics/http/views/)
	- [class based views](https://docs.djangoproject.com/en/2.0/topics/class-based-views/)
	- [generic views](https://docs.djangoproject.com/en/2.0/topics/class-based-views/generic-display/).
- Use **function views only if the time spent customizing a generic view is more than the time spent writing the view by hand**.
- As with plain Django, in Django REST framework there are many ways for writing views:
	-   [function based views](http://www.django-rest-framework.org/api-guide/views/#function-based-views)
	-   [class based views](http://www.django-rest-framework.org/api-guide/views/#class-based-views)
	-   [generic API views](http://www.django-rest-framework.org/api-guide/generic-views/#generic-views)
- This tutorial uses generic API views; the goal of this app is:
	- listing collection of models
	- creating new objects in database
	- so the choice is [ListCreateAPIView](http://www.django-rest-framework.org/api-guide/generic-views/#listcreateapiview)
		- cos its read-write
- Example `view.py`:
```python
from leads.models import Lead # import model
from leads.serializers import LeadSerializer # import serializer
from rest_framework import generics # import generics from rest..

class LeadListCreate(generics.ListCreateAPIView):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer
```

### Setting up the rout... the urls
- Even though DRF comes with a [resourceful router](http://www.django-rest-framework.org/api-guide/routers/), the simplest way to map a URL to a view is [URL mapping](https://docs.djangoproject.com/en/2.0/topics/http/urls/).
- Our goal is to wire up ArticleListCreate to **api/article/**.
- In other words we want to make GET and POST requests to **api/article/** for listing and creating models.
- First configure URL mappings to include app urls (`in project/urls.py`):
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
	path('admin/', admin.site.urls),
	path('', include(articles.urls)),
]
```
- Now create a new file named `./articles/urls.py`
	- In this file we’ll wire up ArticleListCreate to **api/article/**:
```python
from django.urls import path
from . import views

urlpatterns = [
    path('api/article/', views.ArticleListCreate.as_view() ),
]
```
- **You can now perform a 'sanity check' with:**
	- `python manage.py runserver`
	- Head over 
		- [http://127.0.0.1:8000/api/article/](http://127.0.0.1:8000/api/lead/) 
		- and you’ll see the [browsable API](http://www.django-rest-framework.org/topics/browsable-api/)

> Written with [StackEdit](https://stackedit.io/).
