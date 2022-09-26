from django import forms
from .models import Post, Comment
from django_countries.widgets import CountrySelectWidget    # 수정:2207282353


class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["caption", "cooking_time", "image_01", "image_02", "country"]    # 수정_2207052015, 2207262127

        labels = {
            "caption": "내용",
            # dangogram "image": "사진",
            "cooking_time" : "조리시간",    # 수정_2207052004
            "country" : "country",       # 수정_2207262127
            "image_01": "사진",
            "image_02": "사진"
        }

        widgets = {'country': CountrySelectWidget()}        # 수정:2207282353



class UpdatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["caption", "cooking_time", "image_01", "image_02", "country"]    # 수정_2207072058


class CommentForm(forms.ModelForm):
    contents = forms.CharField(widget=forms.Textarea, label="")

    class Meta:
        model = Comment
        fields = ["contents"]


