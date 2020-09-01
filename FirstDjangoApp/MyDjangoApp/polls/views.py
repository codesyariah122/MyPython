from django.http import HttpResponse

# Create your views here.
def index(request):
	return HttpResponse("<h1 style='color:crimson;'>Hello World, I'm Using Django</h1>")