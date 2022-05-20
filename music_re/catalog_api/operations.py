from catalog_api.models import Tracks, Genres
from catalog_api.serializer import TracksSerializer, GenresSerializer
import response_code

from logger import get_logger
logger = get_logger()


def inject_data(data):
    """
    this function is for insert all the data from the json
    :param data: collection iterable
    :return: return_code, code status for the function
    """
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
            if 'contentAdvisoryRating' in each:
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


# def query(params, valid_param):
#
#     if is_valid_params(params, valid_param):
#
#         if 'all' in params:
#             tracks = Tracks.objects.all()
#         else:
#             for
#             tracks = Tracks.objects.get()

def query_by_name(params):

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
    track = TracksSerializer(query_set).data
    query_genres = Genres.objects.get(id=track['genres'])
    genres = GenresSerializer(query_genres).data
    track['genres'] = genres
    return track


def delete_track(params):
    try:
        track_delete = Tracks.objects.get(id=params['id'])
        track_delete.delete()
        return_code = response_code.SUCCESS
    except Exception as ex:
        logger.error(f'Error in delete_document: {ex}')
        return_code = response_code.UNEXPECTED_ERROR

    return return_code


def add_new_track(data):
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
