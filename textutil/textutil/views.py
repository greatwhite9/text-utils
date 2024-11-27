from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyse(request):
    # Get the text from request
    text = request.POST.get('txt', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    captialise = request.POST.get('captialise', 'off')
    counter = request.POST.get('charcounter', 'off')

    punctutations = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
    
    
    if removepunc == 'on':
        analysed = ''
        for char in text:
            if char not in punctutations:
                analysed  = analysed + char
        params = {'purpose': "Removed Punctutations", 'analysed_text': analysed}
        return render(request, "analyse.html", params)

    elif captialise == 'on':
        text = text.upper()
        params = {'purpose':'Converted Text to UPPERCASE', "analysed_text": text}
        return render(request, "analyse.html", params)
    
    elif counter == 'on':
        length = len(text)
        params = {'purpose':'Converted Text to UPPERCASE', "analysed_text": f'Number of characters: {length}'}
        return render(request, "analyse.html", params)

    else:
        return HttpResponse("Error")
