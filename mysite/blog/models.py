from django.db import models
from django.db.models.fields.files import ImageFieldFile
from django.conf import settings
from .system.storage import ImageStorage

# Create your models here.
class ClassName(object):
	"""docstring for ClassName"""
	def __init__(self, arg):
		super(ClassName, self).__init__()
		self.arg = arg
		

class Blog(models.Model):
	KIND_CHOICES = (
		('code', 'code'),
		('life', 'life'),
	)
	TAG_CHOICES = (
		('python', 'python'),
		('机器学习', '机器学习'),
		('阅历', '阅历'),
	)

	title = models.CharField(max_length = 64)
	author = models.CharField(max_length = 50, default = 'blank')
	date = models.DateField(auto_now_add = True)
	content = models.TextField()
	kind = models.CharField(max_length = 50, choices = KIND_CHOICES)
	tag = models.CharField(max_length = 50,  choices = TAG_CHOICES)
	isReprint = models.BooleanField(default = False)
	reprintSource = models.CharField(max_length = 100, default = '', blank = True)
	clickTimes = models.IntegerField(default = 0)
	cover = models.ImageField(upload_to = 'blog/%Y_%m', storage=ImageStorage(), blank=True)

	def addTimes(self):
		self.clickTimes += 1

	def __str__(self):
		return self.title

class Pic(models.Model):
	belong = models.ForeignKey(Blog)
	img = models.ImageField(upload_to = 'blog/%Y_%m', storage=ImageStorage())

class User(models.Model):

	POWER_CHOICES = (
		('host', 'host'),
		('user', 'user'),
		('vistor', 'vistor'),
	)
	name = models.CharField(max_length = 50)
	pwd = models.CharField(max_length = 50)
	power = models.CharField(max_length = 20, default = 'user', choices = POWER_CHOICES)
	pic = models.ImageField(upload_to = 'user/', blank=True)

	def __str__(self):
		return self.name
	# 0:普通用户  1：亲密用户   2：管理员

class AbstractComment(models.Model):
	parent = models.ForeignKey('self', blank=True, null=True, related_name='child')
	class Meta:
		abstract = True

class Comment(AbstractComment):
	date = models.DateTimeField(auto_now_add = True)
	content = models.TextField()
	author = models.ForeignKey(User, blank=True, null=True)
	blog = models.ForeignKey(Blog, related_name='comments')
	isPass = models.BooleanField(default=False)
	avatarSrc = models.CharField(max_length = 50, blank=True)
	def __str__(self):
		return self.content
