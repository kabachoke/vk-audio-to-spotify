from os import error
import requests, urllib.parse, json


def Authorize(client_id):
    scopes = 'playlist-modify-private%20playlist-modify-public%20playlist-read-private'
    redirect_url = urllib.parse.quote_plus('http://example.com/callback/')
    requestURL = 'https://accounts.spotify.com/authorize?client_id={0}&response_type=token&redirect_uri={1}&scope={2}'.format(client_id, redirect_url, scopes)
    
    print(requestURL)
    

def SearchTrack(searchname):
    headers = {
        'Authorization': 'Bearer {}'.format(access_token),
        'Content-Type' : 'application/x-www-form-urlencoded'
    }
    requestURL = 'https://api.spotify.com/v1/search?type=track&q={}&limit=1'.format(urllib.parse.quote_plus(searchname))
    response = requests.get(requestURL, headers=headers)
    data = json.loads(response.content.decode('utf-8'))
    try:       
        result = data['tracks']['items'][0]['id']
        return result
    except Exception:
        return 0


def CreateJsonIds():
    with open('parsed/groupedtracks.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        k = len(data)
        for item in data:
            k -= 1
            print(k)

            searchname = ''
            if item['IsPlaylist']:
                for track in item['Tracks']:
                    searchname = item['Artist'] + ' ' + track['Title']
                    trackID = SearchTrack(searchname)
                    if trackID != 0:
                        track['Id'] = trackID
            else:
                searchname = item['Artist'] + ' ' + item['Title']
                trackID = SearchTrack(searchname)
                if trackID != 0:
                    item['Id'] = trackID

        with open ('parsed/groupedtracksid.json', 'w', encoding='utf-8') as s:
            json.dump(data, s, ensure_ascii=False, indent=4)
                

def CreatePlaylistSpotify(name):
    userID = '31svv5gclz6vit5brtudtlnz5474'
    headers = {
        'Authorization': 'Bearer {}'.format(access_token),
        'Content-Type' : 'application/json'
    }
    data = {
        'name' : name,
        'public' : False
    }
    requestURL = 'https://api.spotify.com/v1/users/{0}/playlists'.format(userID)
    response = requests.post(requestURL, headers=headers, data=json.dumps(data))
    responseData = json.loads(response.content.decode('utf-8'))
    
    return responseData['id']


def AddTrackToPlaylist(playlistID, trackID):
    if trackID != '':
        headers = {
            'Authorization': 'Bearer {}'.format(access_token),
            'Content-Type' : 'application/json'
        }
        data = {
            'uris': ['spotify:track:{}'.format(trackID)]
        }

        requestURL = 'https://api.spotify.com/v1/playlists/{0}/tracks'.format(playlistID)
        response = requests.post(requestURL, headers=headers, data=json.dumps(data))  


def TransferTracks():
    with open('parsed/groupedtracksid.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        basePlaylistId = CreatePlaylistSpotify('MyVKCollectionTracks')

        for item in data:
            if item['IsPlaylist']:
                playlistId = CreatePlaylistSpotify(item['Artist'])
                for track in item['Tracks']:
                    AddTrackToPlaylist(playlistId, track['Id'])
                item['Id'] = playlistId
            else:
                AddTrackToPlaylist(basePlaylistId, item['Id'])

        with open ('parsed/groupedtracksidfinish.json', 'w', encoding='utf-8') as s:
            json.dump(data, s, ensure_ascii=False, indent=4)


access_token = 'BQBw2MYjjlYMgmv-Bl5ARol3evq6k9bDKIGg-e-9ZkZDl_L6rNUTBsHUvL4Dk5Dye8Kx6syKnCltyj_ujzTOomWiCoHC9Hq0mR_cS_URL2xN2W3g799rARJ3EHiMhHziJAutAeZy4GaqkcDYmD6CSnstiirUivPmtAzf_lwbSioC1aEUv8fvptP78hkXE9Etjfp5h0CJ7CMT10xKLmiR0Wt38dLWD8driORXfxFGzQ04u88'
#Authorize('b69a5e81d56f485a9e5dc9ee9d005543')
#CreateJsonIds()
#AddTrackToPlaylist('6UbBS4cYHX93QraoUOffRT')
TransferTracks()