from django import forms


class NewPostForm(forms.ModelForm):
    picture = forms.ImageField(required=True)
    caption = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder':'caption'}), required=True)



