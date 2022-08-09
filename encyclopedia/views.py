from django.shortcuts import render
from . import util
from markdown2 import Markdown
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def title(request,title):
    store=Markdown()
    entry=util.get_entry(title)
    if title not in util.list_entries():
        return HttpResponse("Error : Requested page was not found")
    return  render(request, "encyclopedia/title.html", {
        "data":store.convert(entry),
        "title": title
    })

def search(request):

    data=request.GET.get("search")
    lst=util.list_entries()
    markdowner=Markdown()
    flag=0

    if data in lst:
        return HttpResponseRedirect(reverse("title", kwargs={"title":data}))
        flag=1
        exit()

    for i in lst:
        if data in i:
            return render(request,"encyclopedia/search.html",{
            "result":i
            })
            flag=1

    if flag==0:
        return HttpResponse("No Result Found")



def create(request):
    return render(request, "encyclopedia/create.html",{
        "entries": util.list_entries()
        })



