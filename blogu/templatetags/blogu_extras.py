from django import template
from blogu.models import Category,Blog

register = template.Library()

@register.inclusion_tag('blogu/cats.html')
def get_category_list(cat=None):
    print Category.objects.all()
    return {'cats':Category.objects.all().order_by('name'), "act_cat": cat}

@register.inclusion_tag('blogu/blogs.html')
def get_blogs_list(cat=None):
    if cat:
        c=Category.objects.get(slug=cat)
        if c:
            blogs=Blog.objects.filter(category=c).order_by('-likes')[:5]
    else:
        blogs=Blog.objects.order_by('-likes')[:5]
    return {'blogs':blogs}
