from django import forms


class SearchDeveloperForm(forms.Form):
    developer_name = forms.CharField(max_length=50, label='Застройщик', required=False)
    developer_address = forms.CharField(max_length=50, label='Адрес застройщика', required=False)
    developer_site = forms.CharField(max_length=50, label='Сайт застройщика', required=False)
    
    
class SearchGeneralForm(forms.Form):
    name = forms.CharField(max_length=50, label='Название ЖК', required=False)
    address = forms.CharField(max_length=50, label='Адрес ЖК', required=False)
    