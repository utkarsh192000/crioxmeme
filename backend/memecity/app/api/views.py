from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from app.models import Meme
from app.api.serializers import MemeSerializer


@api_view(['GET', 'POST'])
def meme_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        meme =Meme.objects.all().order_by('-id')[:100]
        serializer = MemeSerializer(meme,many =True )
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = MemeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"id":serializer.data['id']}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def meme_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        meme = Meme.objects.get(pk=pk)
    except Meme.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MemeSerializer(meme)
        return Response(serializer.data)
