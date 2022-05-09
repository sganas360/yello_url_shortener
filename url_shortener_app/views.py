from json import JSONDecodeError
from django.shortcuts import render
from django.forms import ValidationError
from django.http import JsonResponse
from .models import Url

BASE_URL = "http://short.est/"
CHARACTERS = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
BASE = len(CHARACTERS)

def index(request):
    my_data = {
        "paths" : [{"label" : "Encode", "url" : "encode"} , {"label" : "Decode", "url" : "decode"}]
    }
    return render(request, "pages/index.html", my_data)

def encode(request):
    if request.method == "GET":
        return render(request, "pages/encode.html")
    elif request.method == "POST":
        try:
            to_be_encoded_url = request.POST["url"]
            if(Url.objects.filter(original_url=to_be_encoded_url)):
                url = Url.objects.get(original_url=to_be_encoded_url)
                if(url.encoded_url):
                    return JsonResponse({"encoded_url" : url.encoded_url} , safe=False)
                else:
                    return JsonResponse({"message" : "This is not a valid url."}, safe=False)
            else:
                new_url = Url.objects.create(original_url = to_be_encoded_url)
                url_characters = []
                id = new_url.id
                while id > 0:
                    index = id % BASE
                    url_characters.append(CHARACTERS[index])
                    id = id // BASE
                append_value = "".join(url_characters[::-1])
                new_url.encoded_url = f"{BASE_URL}{append_value}"
                new_url.full_clean()
                new_url.save()
                return JsonResponse({"encoded_url": new_url.encoded_url} , safe=False)
        except ValidationError as ve:
            return JsonResponse({"error" : ve.message_dict}, safe=False)

def decode(request):
    pass