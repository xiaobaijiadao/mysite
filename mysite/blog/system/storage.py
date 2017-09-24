from django.core.files.storage import FileSystemStorage
from django.conf import settings

class ImageStorage(FileSystemStorage):
	"""docstring for ImageStorage"""
	def __init__(self, location = settings.MEDIA_ROOT, base_url=settings.MEDIA_URL):
		super(ImageStorage, self).__init__(location, base_url)

	def _save(self, name, content):
		import os, time, random
		print(name)
		ext = os.path.split(name)[1]
		d = os.path.dirname(name)
		fn = time.strftime('%Y%m%d%H%M%S')
		fn = fn + '_%d' % random.randint(0,100)
		name = os.path.join(d, fn+ext)
		print(name)
		return super(ImageStorage, self)._save(name, content)