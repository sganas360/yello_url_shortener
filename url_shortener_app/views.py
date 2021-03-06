from json import JSONDecodeError
from django.shortcuts import render
from django.forms import ValidationError
from django.http import JsonResponse
from .models import Url

#Constants
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
            # Checks if the URL has been previously encoded and if yes, it returns the shortened URL for that URL 
            if(Url.objects.filter(original_url=to_be_encoded_url)):
                url = Url.objects.get(original_url=to_be_encoded_url)
                if(url.encoded_url):
                    return JsonResponse({"encoded_url" : url.encoded_url} , safe=False)
                else:
                    return JsonResponse({"message" : "This is not a valid url."}, safe=False)
            else:
                # Creates and encodes the new URL
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
    if request.method == "GET":
        return render(request, "pages/decode.html")
    elif request.method == "POST":
        try:
            to_be_decoded_url = request.POST["url"]
            # Checks if the URL has been previously encoded and if yes, it will return the original URL 
            if(Url.objects.filter(encoded_url=to_be_decoded_url)):
                url = Url.objects.get(encoded_url = to_be_decoded_url)
                return JsonResponse({"original_url" : url.original_url}, safe=False)
            else:
                return JsonResponse({"message" : "This is not a valid shortened url that has an original url attached to it."} , safe=False)
        except ValidationError as ve:
            return JsonResponse({"error": ve.message_dict}, safe=False)