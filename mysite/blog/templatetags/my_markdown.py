import markdown
from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe


register = template.Library()
@register.filter(is_safe=True)
@stringfilter
def my_markdown(value):
	return mark_safe(markdown.markdown(
		value,
		extensions = ['markdown.extensions.fenced_code',
				'markdown.extensions.codehilite',
				'markdown.extensions.toc',],
		safe_mode = True,
		enable_attributes = False))