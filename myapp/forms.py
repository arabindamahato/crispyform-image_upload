from django import forms

STATES = (
	('','--select State--'),
	('WB','West Bengal'),
	('KA','Karnataka'),
	('MH','Maharastra'),
	('JH','Jharkhand'),

	)

# Crispy form 
class AddressForm(forms.Form):
	email = forms.EmailField(widget = forms.TextInput(attrs={'placeholder':'Enter Email'}))
	password = forms.CharField(widget = forms.PasswordInput())
	address_1 = forms.CharField(
		label = 'Address',
		widget = forms.TextInput(attrs={'placeholder':'1234 mail st'}))
	address_2 = forms.CharField(
		widget = forms.TextInput(attrs={'placeholder':'Apartment, studio or floor'}))
	city = forms.CharField()
	state = forms.ChoiceField(choices = STATES)
	zip_code = forms.CharField(label = "Zip")
	# check_me_out = forms.BooleanField(required = False)


class ImageUploadForm(forms.Form):
	name = forms.CharField(max_length=10)
	images = forms.ImageField(required=True)


	