import requests, base64, urllib

def Authorize(client_id, client_secret):
    requestURL = 'https://accounts.spotify.com/api/token?scopes=playlist-modify-private'
    b64_auth_str = base64.b64encode((client_id + ':' + client_secret).encode()).decode()
    headers = {
        'Authorization': 'Basic {}'.format(b64_auth_str),
        'Content-Type' : 'application/x-www-form-urlencoded'
    }
    data  = {
        'grant_type' : 'authorization_code',
        'code' : '',
        'redirect_uri' : ''
        } 
    response = requests.post(requestURL, data, headers)
    print(response.status_code)
    print(response.headers)
    print(response.content)
    
Authorize('b69a5e81d56f485a9e5dc9ee9d005543', '3419ac59304140b29c166ad55b90158f')