from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.exceptions import ObjectDoesNotExist
from .models import User, Comment, Blog
import random, json
import markdown

def index(request):
	blog_display = {}

	blog_display['code_blog'] = readAndFormatForIndex('code')
	blog_display['life_blog'] = readAndFormatForIndex('life')

	return render(request, 'index.html', blog_display)

def readAndFormatForIndex(kind):
	result = []
	length = Blog.objects.filter(kind=kind).count()

	if length != 0:
		blogs = []
		if length >= 8:
			blogs = Blog.objects.filter(kind=kind).order_by('-clickTimes')[0:7]
		else:
			blogs = Blog.objects.filter(kind=kind).order_by('-clickTimes')[0:length]

		for blog in  blogs:
			b = dict(
				title = blog.title, 
				id = blog.id, 
				kind = blog.kind,
				coverImg = 'media/'+str(blog.cover),
			)
			result.append(b)
	return result

def article(request, kind='', tag = ''):
	result = {}
	limit = 5
	key = str(request.GET.get('key'))

	if kind != '' and (kind == 'life' or kind == 'code'):
		paginator = Paginator(readAndFormatForArticle('kind', kind), limit)
	elif tag != '':
		paginator = Paginator(readAndFormatForArticle('tag', tag), limit)
	elif request.GET.get('key'):
		paginator = Paginator(readAndFormatForArticle('key', key), limit)
	else:
		return render(request, 'list.html', result)

	page = request.GET.get('page', 1)
	try:
		blogs = paginator.page(page)
	except PageNotAnInteger:
		blogs = paginator.page(1)
	except EmptyPage:
		blogs = paginator.page(paginator.num_pages)

	result['blogs'] = blogs
	result['blogs_num'] = len(blogs)
	result['isPaging'] = len(blogs)>5
	result['recent_blog'] = getFirstFive()
	result['classify_blog'] = getAllKind()

	return render(request, 'list.html', result)

def readAndFormatForArticle(way, key):
	result = []
	if way == 'kind':
		blogs = Blog.objects.filter(kind=key).order_by('-id')
	elif way == 'tag':
		blogs = Blog.objects.filter(tag=key).order_by('-id')
	elif way == 'key':
		blogs = (Blog.objects.filter(title__icontains=key) | Blog.objects.filter(tag__icontains=key)).order_by('-date')
	else:
		return result

	length = len(blogs)
	if length != 0:
		for blog in  blogs:
			content = str(blog.content).replace('`','').replace('#','')
			b = dict(
				title = blog.title, 
				date_day = str(blog.date.day),
				date_ym = str(blog.date.year) + '-' + str(blog.date.month),
				id = blog.id, 
				coverImg = 'media/'+str(blog.cover),
				author = blog.author,
				clickTimes = blog.clickTimes,
				summary = content[0:100] + '...' if len(content)>100 else content[0:100],
				tag = blog.tag,
				kind = blog.kind,
			)
			result.append(b)
	return result

def getFirstFive():
	result = []
	length = Blog.objects.all().count()

	if length != 0:
		if length >= 5:
			blogs = Blog.objects.all().order_by('-id')[0:5]
		else:
			blogs = Blog.objects.all().order_by('-id')[0:length]
		for blog in  blogs:
			b = dict(
				title = blog.title,
				id = blog.id,
				kind = blog.kind,
			)
			result.append(b)
	return result

def getAllKind():
	result = []
	for tag in Blog.TAG_CHOICES:
		result.append(tag[1])
	return result

def blog(request, kind, blog_id):
	result = {}
	preBlogId = 0
	nextBlogId = 0
	preBlogTitle = ''
	nextBlogTitle = ''

	latestId = Blog.objects.latest('id').id

	blog = Blog.objects.get(id=blog_id)
	blog.clickTimes += 1
	blog.save()

	preId = int(blog_id)+1
	nextId = int(blog_id)-1

	blogs = Blog.objects.filter(kind=kind)

	while preId <= latestId:
		try:
			p = blogs.get(id=preId)
			preBlogTitle = p.title
			preBlogId = preId
			break
		except ObjectDoesNotExist:
			preId += 1
			continue
	while nextId >= 1:
		try:
			n = blogs.get(id=nextId)
			nextBlogTitle = n.title
			nextBlogId = nextId
			break
		except ObjectDoesNotExist:
			nextId -= 1
			continue

	result['blog'] = dict(
		id = blog.id,
		title = blog.title,
		date_day = str(blog.date.day),
		date_ym = str(blog.date.year) + '-' + str(blog.date.month),
		author = blog.author,
		clickTimes = blog.clickTimes,
		content = blog.content, 
		tag = blog.tag,
		kind = blog.kind,
		preId = preBlogId,
		preTitle =preBlogTitle,
		nextId = nextBlogId,
		nextTitle = nextBlogTitle,
	)
	result['pics'] = json.dumps(getPics(blog))
			
	result['comments'] = getComments(blog_id)
	result['recent_blog'] = getFirstFive()
	result['classify_blog'] = getAllKind()

	return render(request, 'blog.html', result)

def getPics(blog):
	pics = dict()
	i = 0
	for pic in blog.pics.all():
		src = 'media/' + str(pic.img)
		pics[i] = src
		i += 1
	return pics

def getComments(blogId):
	commentResult = []
	blog = Blog.objects.get(id=blogId)
	comments = blog.comments.all().filter(isPass=True)
	for comment in comments:
		if not comment.parent:
			c = dict(
				id = comment.id,
				date = comment.date.strftime("%Y年%m月%d日 %H:%I"),
				author = comment.author.name if comment.author.name == 'blank' else '匿名',
				avatarSrc = '/media/'+str(comment.author.pic) if comment.author.name == 'blank' else comment.avatarSrc,
				content = comment.content,
				children = comment.child.all().filter(isPass=True),
				hasChildren = True if comment.child.all() else False,
			)
			if c['hasChildren']:
				i = 0
				cChildren = []
				for child in c['children']:
					cc = dict(
						id = child.id,
						date = child.date.strftime("%Y年%m月%d日 %H:%I"),
						author = child.author.name if child.author.name == 'blank' else '匿名',
						avatarSrc = '/media/'+str(child.author.pic) if child.author.name == 'blank' else child.avatarSrc,
						content = child.content,
					)
					cChildren.append(cc)
				c['children'] = cChildren
			commentResult.append(c)
	return commentResult

def comment(request, kind, blog_id):
	content = request.POST.get('comment_content')
	comment_pid = int(request.POST.get('parent_id'))

	blog = Blog.objects.get(id=blog_id)
	if content != '':
		author = User.objects.get(name='匿名')

		comment = Comment.objects.create(
			content = content, 
			author = author, 
			blog = blog, 
			parent = None if comment_pid==0 else Comment.objects.get(id=comment_pid),
			avatarSrc = '/media/user/'+str(random.randint(1,9))+'.jpg'
			)
		comment.save()

	blog.clickTimes -= 1
	blog.save()
	path = '/blog/' + kind + '/' + str(blog_id) + '/'
	return HttpResponseRedirect(path)

