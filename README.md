# SPOT_Test
The following project is the result of a Backend developer test for SPOT, in which they ask for the following guidelines:
![image](https://user-images.githubusercontent.com/39286595/169639872-c81382a1-7378-4c0e-a789-9d8e7b0c81f1.png)

## Solutions for each exercise
First, all the data of each track was saved in a SQLite database, this was done through an endpoint that takes the list of tracks as a parameter to save them in a table, the different musical genres are also saved in another table. This facilitates the query and ORM operations. in addition to completing some bonus tasks.
 **Endpoint**:
 http://localhost:port/api/catalog/inject_data/
 

### -An endpoint to provide a search lookup within the tracks (at least by name, but is open to any suggestions):

  The endpoint takes as a parameter the name of the track to search for and through a function called query_by_name a query is made of the object with the    ORM method, once found it is serialized with a function called query_organizer, thus returning a json with the track searched for and a message of          success.\
   **Endpoint:**
  http://localhost:port/api/catalog/get_by_name/
  
  **request:**
 {
    "name":"Whiskey Glasses"
}

 **Response:**
 {
    "RETURN_CODE": "SUCCESS",
    "CONTENT": {
        "id": 1440111980,
        "artistName": "Morgan Wallen",
        "name": "Whiskey Glasses",
        "releaseDate": "2016-01-01",
        "kind": "songs",
        "artistId": 829142092,
        "artistUrl": "https://music.apple.com/us/artist/morgan-wallen/829142092",
        "contentAdvisoryRating": "",
        "artworkUrl100": "https://is3-ssl.mzstatic.com/image/thumb/Music125/v4/ac/f5/19/acf51942-e001-2d6e-e0e6-49b3fd09cac4/842812106569_01_img001.jpg/100x100bb.jpg",
        "genres": {
            "id": 3,
            "genreId": 6,
            "name": "Country",
            "url": "https://itunes.apple.com/us/genre/id6"
        }
    }
}
  
  ### -An endpoint that would allow to get the top 50 popularity tracks:
  
Since no reference was found to which of the 100 tracks are most popular, the endpoint had a function called top_50 that saves all the tracks in a list and with a for 50 tracks were taken in the order in which they were saved in the list. table, in this way the endpoint returns a success code and the list of 50 tracks\
 **Endpoint:**
  http://localhost:port/api/catalog/get_50_top/
  
 **Response:**
 {
    "RETURN_CODE": "SUCCESS",
    "CONTENT": [
        {
            "id": 1440111980,
            "artistName": "Morgan Wallen",
            "name": "Whiskey Glasses",
            "releaseDate": "2016-01-01",
            "kind": "songs",
            "artistId": 829142092,
            "artistUrl": "https://music.apple.com/us/artist/morgan-wallen/829142092",
            "contentAdvisoryRating": "",
            "artworkUrl100": "https://is3-ssl.mzstatic.com/image/thumb/Music125/v4/ac/f5/19/acf51942-e001-2d6e-e0e6-49b3fd09cac4/842812106569_01_img001.jpg/100x100bb.jpg",
            "genres": {
                "id": 3,
                "genreId": 6,
                "name": "Country",
                "url": "https://itunes.apple.com/us/genre/id6"
            }
        },
        {
            "id": 1440111985,
            "artistName": "Morgan Wallen",
            "name": "Chasin' You",
            "releaseDate": "2018-04-27",
            "kind": "songs",
            "artistId": 829142092,
            "artistUrl": "https://music.apple.com/us/artist/morgan-wallen/829142092",
            "contentAdvisoryRating": "",
            "artworkUrl100": "https://is3-ssl.mzstatic.com/image/thumb/Music125/v4/ac/f5/19/acf51942-e001-2d6e-e0e6-49b3fd09cac4/842812106569_01_img001.jpg/100x100bb.jpg",
            "genres": {
                "id": 3,
                "genreId": 6,
                "name": "Country",
                "url": "https://itunes.apple.com/us/genre/id6"
            }
        }, ...
  
  ### -An endpoint to remove a track, using a given identifier (defined by you):
  
The endpoint uses a function called delete_track, which takes as a parameter the ID of the track to be deleted, since it is one of the values ​​that is unique for each track. In this way an ORM query is made where it takes the found track and deletes it using .delete(). In this way, the endpoint returns a successful message if there were no problems.\
 **Endpoint:**
  http://localhost:port/api/catalog/delete/
  
  **request:**
  {
    "id":"1440111980"
}

 **Response:**
  {
    "RETURN_CODE": "SUCCESS"
}
  
  ### -An endpoint to add new tracks using ORM:
  
  The endpoint takes as parameters the values ​​to be saved from the track, and through an add_new_track function, each value is taken in order and is created/saved with the .save() method.\
 **Endpoint:**
  http://localhost:port/api/catalog/create/
  
  **request:**
  {
        "id": 1440111980,
        "artistName": "Morgan Wallen",
        "name": "Whiskey Glasses",
        "releaseDate": "2016-01-01",
        "kind": "songs",
        "artistId": 829142092,
        "artistUrl": "https://music.apple.com/us/artist/morgan-wallen/829142092",
        "contentAdvisoryRating": "",
        "artworkUrl100": "https://is3-ssl.mzstatic.com/image/thumb/Music125/v4/ac/f5/19/acf51942-e001-2d6e-e0e6-49b3fd09cac4/842812106569_01_img001.jpg/100x100bb.jpg",
        "genres": {
            "id": 3,
            "genreId": 6,
            "name": "Country",
            "url": "https://itunes.apple.com/us/genre/id6"
        }
    }
    
 **Response:**
 {
    "RETURN_CODE": "SUCCESS"
}


### Bonus Task

### -Use a Database (suggested: SQLite), instead of the JSON File. Include a create schema in the repo and instructions on how to implement it.

As already mentioned, the json data was saved in a sqlite database, creating two tables, one for the tracks and the other for the musical genres. It was already explained which endpoint was used for this. In addition to the two tables already named, the other tables that come by default in an SQLite database were created.

### -Add authentication API endpoint(s) with Django Rest Framework (DRF).

For this, an endpoint was created that is used to create a user, only saving username and password, using the default create of django saving the user in the database in the auth_user table. In this way, when logging in, the user and password are first authenticated and then the default django login is used. Another point would be that a session token system was used, with which a decorator was created to protect the endpoints, in this way they can only be used if the session token is available.\
**Endpoint:**
Create user: http://localhost:port/api/user/create/

**request:**
{
    "username": "jorge",
    "password": "jorge"

}

**Response:**
 {
    "RETURN_CODE": "SUCCESS"
}

**Endpoint:**
login: http://localhost:port/api/login/
**request:**
{
    "username": "jorge",
    "password": "jorge"

}

**Response:**
   SUCCESS


### -Use SQL instead of ORM only for SELECT queries / Create an endpoint to return the tracks grouped by genres

These two bonus tasks were done together, since an endpoint was created that takes the name of the genre to search as a request and through the function query_by_genres it was connected to the SQLite database and through SQL commands a query was made to find the id of the genre to search to use it and filter the tracks with the same ID, in this way a list is returned with the tracks that match the requested genre\
**Endpoint:**
http://localhost:port/api/catalog/get_by_genres/

**Request:**
{
    "name_genres": "Latin"
}

**Response**:
{
    "RETURN_CODE": "SUCCESS",
    "CONTENT": [
        [
            "Bad Bunny & Tainy",
            1465503235,
            "Callaita",
            "2019-05-31",
            "songs",
            1126808565,
            "https://music.apple.com/us/artist/bad-bunny/1126808565",
            "Explict",
            "https://is4-ssl.mzstatic.com/image/thumb/Music114/v4/a8/5d/7c/a85d7c43-777a-f2b7-5abc-1e4d59d8fe7c/193483903545.jpg/100x100bb.jpg",
            2
        ],
        [
            "Becky G. & KAROL G",
            1609137778,
            "MAMIII",
            "2022-04-20",
            "songs",
            550411604,
            "https://music.apple.com/us/artist/becky-g/550411604",
            "",
            "https://is5-ssl.mzstatic.com/image/thumb/Music116/v4/9e/9b/e6/9e9be6a5-431d-3f48-f7b8-76d0726b909e/886449885053.jpg/100x100bb.jpg",
            2
        ], . . .
        
 ## Give an overview of how your code is structured.
 
 The code is structured with apps, organizing models, serializer, views and operations, in this last one you will find the functions used by the endpoints, in addition to taking some general scruds where the status codes to be returned are taken. Also a module called logger, which enables the error messages of the indicated functions and display them on the console and logs (if used).
 
 ## Provide instructions on how to run your code. (THIS IS IMPORTANT!)


