import sqlite3

from catalog_api.models import Tracks, Genres
from catalog_api.serializer import TracksSerializer, GenresSerializer
import response_code

from logger import get_logger
logger = get_logger()


def inject_data(data):
    """
    this function is for insert all the data from the json. The json must be the results of all the tracks.
    first save the value of the genres in a separate table and then make a query with the value of the
    track in turn and add them
    :param data: collection iterable
    :return: return_code, message status for the function
    """
    genres_data = None
    if data is not None:
        for each in data:
            for each2 in each['genres']:
                if each2['name'] != 'Music':
                    if Genres.objects.filter(genreId=each2['genreId'], name=each2['name'], url=each2['url']).exists():
                        genres_data = each2
                    else:
                        genres = Genres(**each2)
                        genres.save()
                        genres_data = each2
            if 'contentAdvisoryRating' in each:  # since some tracks do not have this field, it must be verified first
                contentAdvisoryRating = each['contentAdvisoryRating']
            else:
                contentAdvisoryRating = ''
            tracks = Tracks(
                artistName=each['artistName'],
                id=each['id'],
                name=each['name'],
                releaseDate=each['releaseDate'],
                kind=each['kind'],
                artistId=each['artistId'],
                artistUrl=each['artistUrl'],
                contentAdvisoryRating=contentAdvisoryRating,
                artworkUrl100=each['artworkUrl100'],
                genres=Genres.objects.get(genreId=genres_data['genreId'], name=genres_data['name'],
                                          url=genres_data['url']),

            )
            tracks.save()
        return_code = response_code.SUCCESS
    else:
        return_code = response_code.EMPTY_DATASET
    return return_code


def query_by_name(params=dict):
    """
    This function takes the search parameter and through the django ORM query the object is obtained, and once
    serialized by query_organizer, returning a success code and the track information
    :param params: the search parameter must be a dictionary, in this case it is searched by the name of the song
    :return: return_code: the endpoint status message
    :return: track: the track information in json format
    """
    track = None
    try:
        query_set = Tracks.objects.get(name=params['name'])
        track = query_organizer(query_set)
    except Exception as ex:
        logger.error(f'Error in query_by_name: {ex}')

    if track is None:
        return_code = response_code.EMPTY_DATASET
    else:
        return_code = response_code.SUCCESS
    return return_code, track


def top_50():
    """
    this function performs a search of all the tracks and takes 50, since there is no indicative value of the
     most favorite, the 50 are taken in the order they were entered in the table
    :return: return_coe: the endpoint status message
    :return: data_track: a list with all the information of the 50 tracks in json format
    """
    data_track = []
    try:
        query_set = list(Tracks.objects.all())
        for each in range(len(query_set)):
            if each <= 50:
                data_track.append(query_organizer(query_set[each]))
    except Exception as ex:
        logger.error(f'Error in top_50: {ex}')

    if data_track is None:
        return_code = response_code.EMPTY_DATASET
    else:
        return_code = response_code.SUCCESS
    return return_code, data_track


def query_organizer(query_set):
    """
    this function takes the object of the query and serializes it, having a document inside the other, the
     serialization must also go through GenresSerializer and add the information to the json of the track
    :param query_set: query object
    :return: track: json with all the data from the track
    """
    track = TracksSerializer(query_set).data
    query_genres = Genres.objects.get(id=track['genres'])
    genres = GenresSerializer(query_genres).data
    track['genres'] = genres
    return track


def delete_track(params=dict):
    """
    the function looks up the ID parameter of the track since it is one of the few unique values
    that cannot be repeated. With this value the query of the object is made, and it is eliminated from the table
    :param params: a json, with the ID of the track to delete
    :return: return_coe: the endpoint status message
    """
    try:
        track_delete = Tracks.objects.get(id=params['id'])
        track_delete.delete()
        return_code = response_code.SUCCESS
    except Exception as ex:
        logger.error(f'Error in delete_document: {ex}')
        return_code = response_code.UNEXPECTED_ERROR

    return return_code


def add_new_track(data=dict):
    """
    the function takes the data and adds the corresponding values
    to the table, makes a query of the genres object and adds the values
    :param data: a json, with the data of the new track
    :return: return_coe: the endpoint status message
    """
    try:
        tracks = Tracks(
            artistName=data['artistName'],
            id=data['id'],
            name=data['name'],
            releaseDate=data['releaseDate'],
            kind=data['kind'],
            artistId=data['artistId'],
            artistUrl=data['artistUrl'],
            contentAdvisoryRating=data['contentAdvisoryRating'],
            artworkUrl100=data['artworkUrl100'],
            genres=Genres.objects.get(genreId=data['genres']['genreId'], name=data['genres']['name'],
                                      url=data['genres']['url']),

        )
        tracks.save()
        return_code = response_code.SUCCESS
    except Exception as ex:
        logger.error(f'Error in add_new_track: {ex}')
        return_code = response_code.UNEXPECTED_ERROR

    return return_code


def query_by_genres(params):
    """
    this function takes the parameter that in this case is the musical genre and through SQL
     makes a query to bring all the tracks with that genre
    :param params: is a dictionary, which takes the name of the genre of the tracks to bring
    :return: return_code: the endpoint status message
    :return: track: tracks information in tuple format
    """
    tracks = None
    dict_track = {}
    list_track = []
    try:
        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM catalog_api_genres WHERE name LIKE ?", (params['name_genres'],))
        genres = cursor.fetchone()

        cursor.execute("SELECT * FROM catalog_api_tracks WHERE genres_id LIKE ?", (genres[0],))
        tracks = cursor.fetchall()
        return_code = response_code.SUCCESS
    except Exception as ex:
        logger.error(f'Error in query_by_genres: {ex}')
        return_code = response_code.UNEXPECTED_ERROR

    return return_code, list_track

