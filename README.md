# Introduction
My URL shortener uses `http://short.est/` as the base URL like in the example given from the challenge prompt. My algorithm will append an alphanumeric value to the end of the base URL based on the order it is encoded. The use of a combination of numbers, uppercase and lowercase letters will yield more possible URLs with less characters to append to the base URL. This allows for easier scaling when large numbers of URLs need to be encoded.
# Objectives
1. When given a URL to encode, a shortened URL is returned in JSON.
2. When given a URL to decode, the original URL is returned in JSON.
3. A unique URL yields a unique shortened URL.
4. No two different URLs will have the same shortened URL and vice versa.
# Assumptions
## For Installation
- Python3 is already installed on the machine
- Postgresql is already installed on the local machine
## For the Program
- Assumes that a valid URL is passed through, but validation errors are raised just in case a non-valid URL does get passed through the application
# How to Run my Program
1. Clone this repo to the local machine
```bash
$ git clone https://github.com/sganas360/yello_url_shortener.git
```
2. Create a virtual environment 
```bash
$ python3 -m venv .venv
```
3. Use the virtual environment 
```bash
$ source .venv/bin/activate
```
4. Install dependencies 
```bash
$ pip install -r requirements.txt
```
5. Create local database
```bash
$ createdb url_shortener_db
```
6. Make Migrations
```bash
$ python3 manage.py makemigrations
```
7. Migrate
```bash
$ python3 manage.py migrate
```
8. Start the developmental server and go to the default port on your browser which will be http://localhost:8000/
```bash
$ python3 manage.py runserver
```
9. Choose between the two paths
- Click on `Encode URL` button to enter a url that you want to encode 
- Click on `Decode URL` button to enter a url that you want to decode to its original URL
10. Enter the appropriate URL based on the path
- Enter the URL that you want to encode on the input and click `Submit`, then you will receive a JSON response of the shortend URL or a validation error 
- Enter the shortened URL that you want to decode on the input and click `Submit`, then you will receive a JSON response of the original url or a validation error 
12. Clicking `Home` takes you to the home screen where you can choose to click between `Encode` or `Decode`
# Example Usage
1. Entering a new URL that has not been encoded through the  `/encode` endpoint  will return the shortened URL in JSON
```
Input:
https://yello.co/resource/?_sft_resource_type=webinar
```
```json
Output:
{
"encoded_url": "http://short.est/1"
}
```
2.  Entering another new URL that has not been previously encoded through the  `/encode` endpoint will return a new shortened URL in JSON
```
Input:
https://github.com/sganas360/yello_url_shortener
```
```json
Output:
{
"encoded_url": "http://short.est/2"
}
```
3. Entering a previously encoded URL will return that same URL encoded for it previously in JSON
```
Input:
https://yello.co/resource/?_sft_resource_type=webinar
```
```json
Output:
{
"encoded_url": "http://short.est/1"
}
```
4. Entering an invalid url through the  `/encode` endpoint will return a message with a validation error
```
Input:
this is not a url
```
```json
Output:
{
"error": 
  {
  "original_url": 
  ["Enter a valid URL."]
  }
}
```
5. Entering the shortened url to the `/decode` endpoint will return the original URL in JSON as long as the shortened URL is actually valid
```
Input:
http://short.est/1
```
```json
Output:
{
"original_url": "https://yello.co/resource/?_sft_resource_type=webinar"
}
```
5. Entering a shortened url to the `/decode` endpoint that is has not been previously encoded will return an error message
```
Input:
http://short.est/1ab1
```
```json
Output:
{
"message": "This is not a valid shortened url that has an original url attached to it."
}
```