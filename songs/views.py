from rest_framework.decorators import api_view
from rest_framework.response import Response

from songs.models import Song
from songs.serializers import SongSerializer

@api_view(['GET'])
def songs_list(request):



    return Response('ok')
