from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


# Create your views here.
@api_view(['GET'])
def artiste_list(request):
    if request.method == 'GET':
        artistes = Artiste.objects.all()
        serializer= ArtisteSerializer(artistes,many=True)
        return Response(serializer.data)

@api_view(['GET'])
def song_list(request):
    song = Song.objects.all()
    serializer= SongSerializer(song,many=True)
    return Response(serializer.data)

@api_view(['GET','PUT','DELETE'])
def song_detail(request, id):

    try :
       song = Song.objects.get(pk=id)
    except Song.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer= SongSerializer(song)
        return Response(serializer.data)
    elif request.method == 'PUT':    
        serializer= SongSerializer(song,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)    

    elif request.method == 'DELETE':
        song.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# @api_view(['GET'])
# def lyric_list(request):
#     lyrics = Lyric.objects.all()
#     serializer= LyricSerializer(lyrics,many=True)
#     return Response(serializer.data)    
