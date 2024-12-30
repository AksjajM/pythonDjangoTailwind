from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import Member


# Create your views here.
def members(request):
    mymembers = Member.objects.all().values
    template = loader.get_template('all_members.html')
    context = {
        'mymembers': mymembers,
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
    # retrieve the information of the individual member
    mymember = Member.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'mymember': mymember,
    }
    return HttpResponse(template.render(context, request))

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

def testing(request):
    username = request.user.username
    template = loader.get_template('template.html')
    context = {'username': username}
    return HttpResponse(template.render(context))
#
# def testing(request):
#   if request.user:
#       username = request.user.username
#       return render(request, 'template.html', {'username': username})
#   else:
#       return render(request, 'template.html')