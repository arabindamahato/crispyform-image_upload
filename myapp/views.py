from django.shortcuts import render , redirect
from myapp.models import *
from django.forms import modelformset_factory, inlineformset_factory
from myapp.forms import *


#Create your views here.

# ------------------------------------------------Model Form Set_Factory ------------------------------------------

# def index(request, id):
#     topic = Topic.objects.get(id=id)
#     webpage_form = modelformset_factory(Webpage, exclude=("top_name",), extra=1)
#     if request.method == "POST":
#         # queryset means sql django to retrive data
#         form = webpage_form(request.POST, queryset = Webpage.objects.filter(top_name_id=id))
#         if form.is_valid():
#             instances = form.save(commit=False) # saved the form and store in a instances variable. instances is just a variable
#             for instance in instances:
#                 instance.top_name_id = id
#                 instance.save()
#     form = webpage_form(queryset = Webpage.objects.filter(top_name_id = id))
                
#     return render(request, "index.html", {"form":form})


#-------------------------------------------------Inline Form Set_Factory-------------------------------------------



def index(request, id):
    topic = Topic.objects.get(id=id)
    webpage_form = inlineformset_factory(Topic, Webpage, exclude=("top_name",), extra=1, can_delete=True)
    if request.method == "POST":
        form = webpage_form(request.POST, instance = topic)
        if form.is_valid():
            form.save()           
            return redirect('index', id = topic.id)
    form = webpage_form(instance = topic)
                
    return render(request, "index.html", {"form":form})


#-------------------------------------------------Crispy Form  Demo-------------------------------------------
# crispy form (Address form) | for details go to forms.py
def crispy_form_demo(request):
	form = AddressForm()
	return render(request, "crispy_form_demo.html", context={'form':form})





#-------------------------------------------------Crispy Image Upload-------------------------------------------

def image_upload(request):
	if request.method == "POST":
		print(request.FILES)

	form = ImageUploadForm()
	return render(request, "image_upload.html", context={'form':form})



#--------------------------------------------Register User -------------------------------------------


def register(request):
    addressform = AddressForm()
    img_upload = ImageUploadForm()
    return render(request, "register.html", context={"form1":addressform, "form2":img_upload})


















