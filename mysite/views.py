from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request,'index.html')
    #return HttpResponse("Home")
def contact(request):
    return render(request,'contact.html')
def analyze(request):
    djtext=(request.POST.get('text', 'default'))
    removepunc=request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')
    if removepunc=="on":
        punctuations='''/[-[\]{}()*+?.,\\^$|#\]/,;:''"\\$&"@='''
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char


        params={'purpose':'Removed Punctuation','analyzed_text':analyzed}
        djtext=analyzed
        #return render(request,'analyze.html',params)
    if fullcaps=="on":
        analyzed=""
        for char in djtext:
            analyzed=analyzed + char.upper()
        params = {'purpose': 'changed to uppercase', 'analyzed_text': analyzed}
        djtext=analyzed
        #return render(request, 'analyze.html', params)
    if newlineremover=="on":
        analyzed = ""
        for char in djtext:
            if char!="\n" and char!="\r":
                analyzed = analyzed + char
        params = {'purpose': 'Removed Newlines', 'analyzed_text': analyzed}
        djtext=analyzed
        #return render(request, 'analyze.html', params)
    if extraspaceremover=="on":
        analyzed = ""
        for index,char in enumerate(djtext):
            if djtext[index]==" " and djtext[index+1]==" ":
                pass
            else:
                analyzed = analyzed + char
        params = {'purpose': 'removed space', 'analyzed_text': analyzed}
        djtext=analyzed
        #return render(request, 'analyze.html', params)
    if charcount=="on":
        count=0
        for index,char in enumerate(djtext):
            if not(djtext[index]==" "):
                count+=1
        params = {'purpose': 'no. of characters are:', 'analyzed_text': count}
        djtext=analyzed
        #return render(request, 'analyze.html', params)
    if(removepunc!="on" and fullcaps!="on" and newlineremover!="on" and extraspaceremover!="on" and charcount!="on"):
        return HttpResponse("Sorry!!! you don't choose any option.............ERROR")


    return render(request,'analyze.html',params)
