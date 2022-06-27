from django.shortcuts import redirect, render
import random
from . import util
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.files.base import ContentFile, File
from markdown2 import Markdown

markdowner = Markdown()


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def title(request, title):
    entry = util.get_entry(title)
    if entry == None:
            return render(request, "encyclopedia/error.html")
    else:
        converted_entry = markdowner.convert(entry)
        return render(request, "encyclopedia/title.html", {
            "title": title,
            "entry": converted_entry
        })
def newpage(request):
    return render(request, "encyclopedia/newpage.html")

def random_page(request):
    entry_title = random.choice(util.list_entries())
    entry_content = markdowner.convert(util.get_entry(entry_title))
    return render(request, "encyclopedia/title.html", {
        "title": entry_title,
        "entry": entry_content,
    })

def search(request):
    if request.method == 'GET':
        newitems = []
        newitemswithfind = []
        search = request.GET.get('q')
        newsearch = search.lower()
        for item in util.list_entries():
            newitem = item.lower()
            newitems.append(newitem)
            if newitem.find(newsearch) >= 0:
                newitemswithfind.append(newitem)
    return render(request, 'encyclopedia/searchresults.html', {
        "title": newsearch,
        "entries": newitems,
        "goodentries": newitemswithfind,
    })

def createdpage(request):
    if request.method == 'GET':
        title = request.GET.get('title')
        content = request.GET.get('content')
        a = open(f"entries/{title}.md", "x")
        a.write(f"{content}")
        a.close()
        return HttpResponseRedirect('/')

def edit(request, title):
    entry = util.get_entry(title)
    return render(request, "encyclopedia/editpage.html", {
        "title":title,
        "entry": entry
    })

def submitedit(request):
    if request.method == 'GET':
        title = request.GET.get('newtitle')
        entry = request.GET.get('newentry')
        f = open(f"entries/{title}.md", "w")
        f.write(entry)
        f.close()
        return HttpResponseRedirect('/')