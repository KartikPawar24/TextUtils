# This is created by me

from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    param = {'name': 'Kartik', 'place': 'Mars'}
    return render(request, 'index.html')
    # return HttpResponse("<h1>Home</h1><br>"
    #                     "<a href='removepunc'>Direct to Remove Punc Page</a><br>"
    #                     "<a href='capfirst'>Direct to capitalizefirst Page</a><br>"
    #                     "<a href='newlineremove'>Direct to newlineremove Page</a><br>"
    #                     "<a href='spaceremove'>Direct to spaceremove Page</a><br>"
    #                     "<a href='charcount'>Direct to charcount Page</a>")

def analyze(request):
    intext = request.GET.get('text', 'notextfound')
    #print(intext)
    removepunc = request.GET.get('removepunc', 'off')
    capfirst = request.GET.get('capfirst', 'off')
    newlineremove = request.GET.get('newlineremove', 'off')
    spaceremove = request.GET.get('spaceremove', 'off')
    charcount = request.GET.get('charcount', 'off')

    #print(removepunc)
    if removepunc == 'on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in intext:
            if char not in punctuations:
                analyzed += char
        param = {'purpose': 'Removing Punctuations from the text', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', param)

    elif capfirst == 'on':
        analyzed = intext.capitalize()
        param = {'purpose': 'Capitalizing First Character', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', param)
    
    elif newlineremove == 'on':
        analyzed = intext.strip('\n')
        param = {'purpose': 'Removing New Line from the text', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', param)
    
    elif spaceremove == 'on':
        analyzed = intext.strip()
        param = {'purpose': 'Removing Extra Space from the text', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', param)
    
    elif charcount == 'on':
        analyzed = len(intext)
        param = {'purpose': 'Character Counting from the text', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', param)
    
    else:
        return HttpResponse("ERROR!!!")
    # return HttpResponse("<h1>Analyze Text</h1></br>"
    #                     "<a href='/'>Direct to Home Page</a>")