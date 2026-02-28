from django import forms


class UserForm(forms.Form):
    # name = forms.CharField(help_text='Введите свое имя',label='Имя',initial='undefined')
    # age = forms.IntegerField(help_text='Введите свой возраст',label='Возраст',initial=18)
    # comment=forms.CharField(widget=forms.Textarea,label='Комментарии')
    # name = forms.CharField(min_length=2,max_length=20)
    # age = forms.IntegerField(required=False)
    # email= forms.EmailField(required=False,min_length=7)
    # name = forms.CharField(min_length=2, max_length=20)
    # age = forms.IntegerField(min_value=1,max_value=100)
    # weight = forms.DecimalField(min_value=3,max_value=200,decimal_places=2)
    # name = forms.CharField(min_length=3)
    # age = forms.IntegerField(min_value=1,max_value=100)
    # required_css_class = 'field'
    # error_css_class = 'error'
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'my-field'}))
    age = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'my-field'}))