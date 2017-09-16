from django.db import models

# Create your models here.
class Blog(models.Model):
	title = models.CharField(max_length = 64)
	author = models.CharField(max_length = 50, default = 'blank')
	date = models.DateField(auto_now_add = True)
	pic = models.ImageField(upload_to = 'img/blog/', default = 'img/blog/no_img.jpg')
	content = models.TextField()
	kind = models.CharField(max_length = 50)
	tag = models.CharField(max_length = 50)

class User(models.Model):
	name = models.CharField(max_length = 50)
	pwd = models.CharField(max_length = 50)
	power = models.IntegerField(default = 0)
	pic = models.ImageField(upload_to = 'img/user/', default = 'img/user/no_img.jpg')
	thumb = models.ImageField(upload_to = 'img/user/thumb', blank = True)
	# 0:普通用户  1：亲密用户   2：管理员

class Comment(models.Model):
	date = models.DateTimeField(auto_now_add = True)
	content = models.TextField()
	author = models.ForeignKey(User)
	blog = models.ForeignKey(Blog)
