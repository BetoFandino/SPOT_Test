from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from authenticate_user import has_permission_decorator
from catalog_api import operations


class CatalogViewSet(viewsets.ModelViewSet):

    @action(methods=['post'], url_path='inject_data', detail=False)
    @has_permission_decorator()
    def inject_tracks(self, request):
        return_code = operations.inject_data(request.data)
        return Response({
            'RETURN_CODE': return_code
        })

    @action(methods=['post'], url_path='get_by_name', detail=False)
    @has_permission_decorator()
    def get_tracks(self, request):
        return_code, track = operations.query_by_name(request.data)
        return Response({
            'RETURN_CODE': return_code,
            'CONTENT': track
        })

    @action(methods=['get'], url_path='get_50_top', detail=False)
    @has_permission_decorator()
    def get_tracks_top(self, *args, **kwargs):
        return_code, track = operations.top_50()
        return Response({
            'RETURN_CODE': return_code,
            'CONTENT': track
        })

    @action(methods=['post'], url_path='delete', detail=False)
    @has_permission_decorator()
    def delete_track(self, request):
        return_code = operations.delete_track(request.data)
        return Response({
            'RETURN_CODE': return_code
        })

    @action(methods=['post'], url_path='create', detail=False)
    @has_permission_decorator()
    def new_track(self, request):
        return_code = operations.add_new_track(request.data)
        return Response({
            'RETURN_CODE': return_code
        })

    @action(methods=['post'], url_path='get_by_genres', detail=False)
    @has_permission_decorator()
    def query_by_genres(self, request):
        return_code, tracks = operations.query_by_genres(request.data)
        return Response({
            'RETURN_CODE': return_code,
            'CONTENT': tracks
        })
