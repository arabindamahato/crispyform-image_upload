from django.urls import path
from myapp import views

urlpatterns = [
    # path('<id>/',views.index, name = "index" ),
    path('crispy-form-demo/',views.crispy_form_demo, name = "crispy_form_demo"), # it means bootstrap form creating by forms.py.
    path('image-upload/', views.image_upload, name="image_upload"), # image upload form 
    path('register/', views.register, name="register")

]


