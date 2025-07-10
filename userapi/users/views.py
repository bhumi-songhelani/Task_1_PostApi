from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer

@api_view(['POST'])
def create_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    users = User.objects.all()
    all_serialized = UserSerializer(users, many=True)
    return Response({
        "data": all_serialized.data,
        "count": users.count()
    })
