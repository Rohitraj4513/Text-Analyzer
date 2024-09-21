# Import necessary modules from Django
from django.http import HttpResponse  # Used to return HTTP responses
from django.shortcuts import render   # Used to render HTML templates

# Define the index view to render the index.html page
def index(request):
    return render(request,'index.html')

# Define the analyze view which processes the text submitted through the form
def analyze(request):
# Get the input text from the form (default value is 'default' if no text is provided)
    dtext =request.POST.get('text', 'default')
# Get the status of the checkboxes for different text transformations
    removepun =request.POST.get('removepun','off')
    uppercaps = request.POST.get('uppercaps' , 'off')
    newlinermv = request.POST.get('newlinermv','off')
    spaceremove = request.POST.get('spaceremove' , "off")
    charcount = request.POST.get('charcount' , "off")

# If the 'Remove Punctuation' checkbox is checked
    if(removepun == 'on'):
        punctuation = '''\.,?!:;“”‘’'—()-[].../&"'''
        analyze = ""
        for char in dtext:
            if char not in punctuation:
                analyze = analyze + char
        dict = {'purpose': 'remove punctuation', 'analyze_text': analyze}
        dtext = analyze

  # If the 'Convert to Uppercase' checkbox is checked
    if(uppercaps == "on"):
        analyze = ""
        for char in dtext:
            analyze = analyze + char.upper()
        dict = {'purpose': 'To uppercase Convert', 'analyze_text': analyze}
        dtext = analyze

 # If the 'Remove Newlines' checkbox is checked
    if(newlinermv == "on"):
        analyze= ""
        for char in dtext:
            if char != "\n" and char != "\r":
                analyze = analyze + char
        dict = {'purpose': 'Remove Uppercase', 'analyze_text': analyze}
        dtext =analyze

# If the 'Remove Extra Spaces' checkbox is checked
    if(spaceremove == "on"):
        analyze = ""
        for index ,char in enumerate(dtext):
            if not (dtext[index] == " " and dtext[index + 1] == " "):
                analyze = analyze +char
        dict = {'purpose': 'Remove Extra space', 'analyze_text': analyze}
        dtext = analyze

  # If the 'Count Characters' checkbox is checked
    if(charcount == "on"):
        analyze = 0
        for index , char in enumerate(dtext):
            if not(dtext[index] == " "):
                analyze = analyze + 1
        dict = {'purpose': 'Count Char Value', 'analyze_text': analyze}
        dtext = analyze

 # If none of the options are selected, return an error message
    if(charcount != "on" and spaceremove != "on" and newlinermv != "on" and uppercaps != "on" and removepun != 'on'):
        return HttpResponse("Error")

 # Render the analyze.html page and pass the dictionary with the analyzed data
    return render(request, 'analyze.html', dict)

































