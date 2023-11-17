import base64
from requests import post, get
import time
import json
import pandas as pd
import psycopg2

#conectar ao banco de dados postgres AWS
def db_connect():
    conn = psycopg2.connect(
    database="", user="", password="",
    host='', port= '')
    conn.autocommit = True
    return conn

#capturar e formatar token de acesso
def get_token():
    auth_string = ""
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization" : "Basic "+ auth_base64,
        "Content-Type" : "application/x-www-form-urlencoded",
    }
    data = {"grant_type": "client_credentials"}
    result = post(url, headers=headers, data=data)
    json_result = json.loads(result.content)
    token = json_result["access_token"]
    return token

#set autorizador
def get_auth_header(token):
    return {"Authorization": "Bearer "+ token}

#ETL dos dados
def run_spotify_etl(token, conn):
    cursor = conn.cursor()
    url =  "https://api.spotify.com/v1/browse/new-releases?limit=50"
    headers = get_auth_header(token)
    query_url = url
    result = get(query_url, headers=headers)
    time.sleep(2)
    json_result = json.loads(result.content)
    selected_data = [{"album_id": song["id"], 
                      "artist_id": song["artists"][0]["id"],
                      "name": song["name"],
                      "tracks": song["total_tracks"],
                      "release": song["release_date"],
                      "album_type": song["album_type"]} for song in json_result["albums"]["items"]]

    # Query to be inserted
    insert_query_album = "INSERT INTO spotify.albums(album_id, artist_id, name, tracks, release, album_type) VALUES (%s, %s, %s, %s, %s, %s) ON CONFLICT (album_id) DO NOTHING"
    insert_query_artist = "INSERT INTO spotify.artists(artist_id, name, genre, popularity, followers) VALUES (%s, %s, %s, %s, %s) ON CONFLICT (artist_id) DO NOTHING"
    insert_query_tracks = "INSERT INTO spotify.tracks(track_id, album_id, artist_id, name, release, duration, popularity, album_type) VALUES (%s, %s, %s, %s, %s, %s, %s, %s) ON CONFLICT (track_id) DO NOTHING"
    # Extracting only the relevant bits of data from the json object      
    for song in json_result["albums"]["items"]:
        #extração de dados do artista
        artist_id = song["artists"][0]["id"]
        url_artist = f"https://api.spotify.com/v1/artists/{artist_id}"
        query = f"?q={artist_id}&type=artist&limit=1"
        query_artist = url_artist + query
        artist_result = get(query_artist, headers=headers)
        time.sleep(2)
        artist_json_result = json.loads(artist_result.content)
        genre = artist_json_result["genres"]
        if genre:
            genre_to_insert = artist_json_result["genres"][0]
        else:
            genre_to_insert = None

        #extração das tracks
        album_id = song["id"]
        url_album = f"https://api.spotify.com/v1/albums/{album_id}"
        #query_album = f"?q={url_album}&type=album&limit=1"
        query_album = url_album
        album_result = get(query_album, headers=headers) 
        album_json_result = json.loads(album_result.content)

        cursor.execute(insert_query_artist, 
                       (artist_json_result["id"], 
                        artist_json_result["name"], 
                        genre_to_insert, artist_json_result["popularity"], 
                        artist_json_result["followers"]["total"]))
        cursor.execute(insert_query_album, (song["id"], song["artists"][0]["id"], song["name"], song["total_tracks"], song["release_date"], song["album_type"]))

        for track in album_json_result["tracks"]["items"]:
            track_id = track["id"]
            url_track = f"https://api.spotify.com/v1/tracks/{track_id}"
            #query_album = f"?q={url_album}&type=album&limit=1"
            query_track= url_track
            track_result = get(query_track, headers=headers)
            time.sleep(2)
            track_json_result = json.loads(track_result.content)
            cursor.execute(insert_query_tracks, (track_id, song["id"], song["artists"][0]["id"], track_json_result["name"], song["release_date"], track_json_result["duration_ms"], track_json_result["popularity"], track_json_result["album"]["album_type"]))

    conn.commit()
    cursor.close()
    conn.close()


token = get_token()
conn = db_connect()
run_spotify_etl(token, conn)
