from django import forms
from .models import Article

class ArticleForm(forms.Form):
    title = forms.CharField()
    content = forms.CharField()
    # yesorno = forms.BooleanField()
    # due_date = forms.DateTimeField()



class ArticleModelForm(forms.ModelForm):
    title = forms.CharField(
        label='제목',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )

    content = forms.CharField(
        label='내용',
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': '내용을 입력해주세요',
                'rows': 10,
            }
        )
    )


    class Meta:
        model = Article
        fields = '__all__'