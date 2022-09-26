from django.db import models
from djangogram.users import models as user_model
from django_countries.fields import CountryField


# Create your models here.
class TimeStamedModel(models.Model):
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Post(TimeStamedModel):
    author = models.ForeignKey(
                user_model.User, 
                null=True, 
                on_delete=models.CASCADE, 
                related_name= 'post_author'
            )
    #djangogram image = models.ImageField(blank=False)
    image_01 = models.ImageField(blank=False, null=True) # blank=False)
    image_02 = models.ImageField(blank=True, null=True) # blank=False) #일시 수정_2206272310
    cooking_time = models.PositiveIntegerField(blank=False) # 수정_2207052004
    country = CountryField(countries_flag_url='//flags.example.com/{code}.png')    # 수정_2207262126 나라 추가, 2207282353
    caption = models.TextField(blank=False)
    image_likes = models.ManyToManyField(
                    user_model.User,
                    blank=True,
                    related_name='post_image_likes'
            )

    def __str__(self):
        return f"{self.author}: {self.caption}"


class Comment(TimeStamedModel):
    author = models.ForeignKey(
            user_model.User, 
            null=True, 
            on_delete=models.CASCADE, 
            related_name= 'comment_author'
        )
    posts = models.ForeignKey(
            Post, 
            null=True, 
            on_delete=models.CASCADE, 
            related_name= 'comment_post'
        )
    contents = models.TextField(blank=True)

    def __str__(self):
        return f"{self.author}: {self.contents}"

