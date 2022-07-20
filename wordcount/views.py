from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request, 'home.html',)

def eggs(request):
    return HttpResponse('<h1>Eggs</h1>')

def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()

    WordDictionnary = {}
    for word in wordlist:
        if word in WordDictionnary:
            #Increase
            WordDictionnary[word] += 1
        else:
            #add to the dictionary
            WordDictionnary[word] = 1
    sortedwords=sorted(WordDictionnary.items(), key = operator.itemgetter(1), reverse = True)
    return render(request, 'count.html',{'fulltext':fulltext, 'count' : len(wordlist), 'sortedwords' : sortedwords})

def about(request):
    return render(request, 'about.html',)
