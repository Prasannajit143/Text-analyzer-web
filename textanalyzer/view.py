# from django.shortcuts import render
# from django.http import HttpResponse


# def index(request):
#     return render(request,'index.html')

# def analyze(request):
#     djtext = request.POST.get('text', 'default')
#     removepunct=request.POST.get('removepunct','off')
#     capitalization=request.POST.get('capitalization','off')
#     # spaceremover=request.POST.ger('spaceremover','off')
#     # newlineremover=request.POST.ger('newlineremover','off')
#     if removepunct=='on':
#         analyzed=''
#         li = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
#         for char in djtext:
#             if char not in li:
#                 analyzed= analyzed+char
#         parmas = {
#         'purpose': 'Removed Punctuations',
#         'analyzed_text': analyzed,
#         }
#         djtext=analyzed

#     if capitalization=='on':
#         analyzed=djtext.upper()
#         parmas = {
#         'purpose': 'Removed Punctuations',
#         'analyzed_text': analyzed,
#         }
#         djtext=analyzed

#     # if spaceremover=='on':
#     #     analyzed=djtext.strip()
#     #     parmas = {
#     #     'purpose': 'Removed Punctuations',
#     #     'analyzed_text': analyzed,
#     #     }
#     #     djtext=analyzed

#     # if newlineremover=='on':
#     #     analyzed=''
#     #     for char in djtext:
#     #         if char!='\n':
#     #             analyzed=analyzed+char
#     #     parmas = {
#     #     'purpose': 'Removed Punctuations',
#     #     'analyzed_text': analyzed,
#     #     }
#     #     djtext=analyzed

#     return render(request,'analyze.html',parmas)

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,"index.html")

def analyze(request):
    # Get the text
    djtext = request.POST.get('text', 'default')

    removepunc=request.POST.get('removepunct','off')
    fullcaps=request.POST.get('capitalization','off')
    newlineremover=request.POST.get('spaceremover','off')
    extraspaceremover=request.POST.get('newlineremover','off')

    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext=analyzed
        # return render(request, 'analyze.html', params)
    if fullcaps=="on":
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        params = {'purpose': 'Change To Uppercase', 'analyzed_text': analyzed}
        djtext=analyzed
        # return render(request, 'analyze.html', params)
    if newlineremover=="on":
        analyzed=""
        for char in djtext:
            if char!="\n" and char!="\r":
                analyzed= analyzed + char
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        # Analyze the text
        djtext=analyzed
        # return render(request, 'analyze.html', params)
    if (extraspaceremover == "on"):
        analyzed=" "
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
                analyzed= analyzed + char
        params = {'purpose': 'Change To Uppercase', 'analyzed_text': analyzed}
        djtext=analyzed
        # return render(request, 'analyze.html', params)

    return render(request, 'analyze.html', params)




   


    



