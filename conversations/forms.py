from django import forms


class AddCommentForm(forms.Form):

    message = forms.CharField(required=True, widget=forms.TextInput(attrs={"placeholder": "대화를 입력하세요"}))