from django.shortcuts import render

# Create your views here.

def index(request):
	blog_display = {}
	blog_display['code_blog'] = [
		'一篇文章',
		'两篇文章',
		'三篇文章',
		'四篇文章',
		'五篇文章',
		'六篇文章',
		'七篇文章',
		'八篇文章',
	]
	blog_display['life_blog'] = [
		'一篇记事',
		'两篇记事',
		'三篇记事',
		'四篇记事',
		'五篇记事',
		'六篇记事',
		'七篇记事',
		'八篇记事',
	]
	return render(request, 'index.html', blog_display)

def article(request):
	return render(request, 'list.html')

