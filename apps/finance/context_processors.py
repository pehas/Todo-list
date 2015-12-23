from .models import Category


def categories(request):
	context = {}
	context['categories'] = Category.objects.all()
	return context