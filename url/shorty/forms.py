from django import forms
from .validators import validate_url, validate_dot_com


class submitURLForm(forms.Form):
    url = forms.CharField(label='Submit URL', validators=[validate_url, validate_dot_com])
    # def clean(self):
    #     clean_data = super(submitURLForm, self).clean()
    #     print(clean_data)
    #     url = clean_data.get('url')
    #     url_validator = URLValidator()
    #     try:
    #         url_validator(url)
    #     except:
    #         raise forms.ValidationError("Invalid URL")
    #     return url
    #     print(url)

    # def clean_url(self):
    #     url = self.cleaned_data['url']
    #     print(url)
    #
    #     url_validator = URLValidator()
    #     try:
    #         url_validator(url)
    #     except:
    #         raise forms.ValidationError("Invalid URL")
    #     return url


