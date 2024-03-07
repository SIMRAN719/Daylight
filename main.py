from flask import Flask, render_template, request, redirect, url_for
import requests
app = Flask(__name__)

def random_quote():
    API_KEY = '1A0UM0Auf29pbBzWxyRb8g==juYtwJXSTlhWvlG7'
    api_url = 'https://api.api-ninjas.com/v1/quotes'
    response = requests.get(api_url, headers={'X-Api-Key': API_KEY})
    if response.status_code == requests.codes.ok:
        return response.json()
    else:
        print("Error:", response.status_code, response.text)
        
def random_background():
    API_KEY = 'XO1gnSK0SU7_QhnpGTwfQIrE-hZvfh47n96y26HgqCw'
    api_url = 'https://api.unsplash.com/photos/random?query=nature&orientation=landscape'
    response = requests.get(api_url, headers={'Authorization': 'Client-ID ' + API_KEY})
    if response.status_code == requests.codes.ok:
        image_info = response.json()
        image_url = image_info['urls']['regular']
        return image_url
    else:
        print("Error:", response.status_code, response.text)
@app.route('/')
def index():
    quote_ = random_quote()
    qt=quote_[0]['quote']
    auth=quote_[0]['author']
    background = random_background()
    return render_template('index.html', quote=qt,author=auth, background=background)

if __name__ == '__main__':
    app.run(debug=True) 