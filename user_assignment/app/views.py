from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from app.models import User
from app.serializers import UserSerializer


@api_view(['GET'])
def apiOverView(request):
    api_urls = {
        'Users List': '/user-list/',
        'User Detail': '/user-detail/<int:pk>',
        'Create User': '/user-create/',
        'Update': '/user-update/<int:pk>',
        'Delete': '/user-delete/<int:pk>'
    }
    return Response(api_urls)


@api_view(['GET'])
def UserList(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def UserDetail(request, pk):
    try:
        user = User.objects.get(id=pk)
        if user is not None:
            serializer = UserSerializer(user, many=False)
        if request.user.id == serializer.data['id']:
            return Response(serializer.data)
        else:
            return Response("User is not authenticated to view User Detail")
    except User.DoesNotExist:
        return Response("User doesn't exist")


@api_view(['POST'])
def UserCreate(request):
    serializer = UserSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def UserUpdate(request, pk):
    user = User.objects.get(id=pk)
    serializer = UserSerializer(instance=user, data=request.data)
    if serializer.is_valid():
        serializer.save()
    if 'id' in serializer.data.items():
        if request.user.id == serializer.data['id']:
            return Response(serializer.data)
    else:
        return Response("User is not authenticated to update User Detail")


@api_view(['DELETE'])
@permission_classes([IsAuthenticatedOrReadOnly])
def UserDelete(request, pk):
    user = User.objects.get(id=pk)
    serializer = UserSerializer(user, many=False)
    if request.user.id == serializer.data['id']:
        user = User.objects.get(id=pk)
        user.delete()
        return Response("User deleted successfully")

    else:
        return Response("User is not authenticated to delete User Detail")