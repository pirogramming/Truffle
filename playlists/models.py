from django.db import models
from django.conf import settings
# Create your models here
from accounts.models import Profile

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

    
class PlayList(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length = 20)
    description = models.CharField(max_length=50)
    detail = models.TextField()
    main_image = models.ImageField(upload_to = 'playlist/main_image/%Y/%m/%d')
    tags = models.ManyToManyField('Tag', blank=True, verbose_name='tags')
    scrap = models.ManyToManyField(Profile, related_name='scrap',through = 'Scrap')
    comments = models.ManyToManyField(Profile, related_name='comments',through = 'Comments')
    
    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.id])     #내용submit

    def add_tag_string(self, tag_string):
        tag_list = tag_string.split("#")[1:]
        tag_list = [tag.strip() for tag in tag_list]

        for tag_word in tag_list:
            if Tag.objects.filter(name=tag_word).count() == 1:
                tag = Tag.objects.get(name=tag_word)
            else:
                tag = Tag.objects.create(name=tag_word)
            self.tags.add(tag)
        self.save()

    def get_tag_string(self):
        self.tags.clear()
        tags = [tag.name for tag in self.tags.all()]
        if tags:
            return f"#{'  # '.join(tags)}"
        else:
            return ''

class Scrap(models.Model):
    user = models.ForeignKey(Profile,related_name='scrap_user',on_delete=models.CASCADE)
    playlist = models.ForeignKey(PlayList,related_name='scrap_playlist', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    
class Comments(models.Model):
    user = models.ForeignKey(Profile,related_name='comments_user', on_delete=models.CASCADE)
    playlist = models.ForeignKey(PlayList,related_name='comments_playlist', on_delete=models.CASCADE)
    comment=models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add = True)

class Card(models.Model):
    text=models.TextField()
    playlist=models.ForeignKey(PlayList,on_delete=models.CASCADE)

    
    
class Photo(models.Model):
    image=models.ImageField()
    card=models.ForeignKey(Card,on_delete=models.CASCADE)
    
