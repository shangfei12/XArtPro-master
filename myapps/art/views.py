from django.shortcuts import render

from art.models import Art

# Create your views here.
def show(request, artId):
    art = Art.objects.get(pk=artId)
    return render(request,
                  'art/show.html',
                  locals())