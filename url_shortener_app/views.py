from django.shortcuts import render

def index(request):
    my_data = {
        "paths" : [{"label" : "Encode", "url" : "encode"} , {"label" : "Decode", "url" : "decode"}]
    }
    return render(request, "pages/index.html", my_data)

def encode(request):
    pass

def decode(request):
    pass