import datetime
import jwt
from .models import User
from .checkpassword import check_user_password
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.


def index(request):
    return HttpResponse('<h1>App is running</h1>')


@csrf_exempt
@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def register_user(request):
    user = User()
    first_name = request.data.get('first_name')
    last_name = request.data.get('last_name')
    email = request.data.get('email')
    password = make_password(request.data.get('password'))
    record = {
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "password": password
    }
    user.collection.insert_one(record)
    return HttpResponse("User registered successfully")


@csrf_exempt
@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def login_user(request):
    users = User()
    email = request.data.get('email')
    password = request.data.get('password')

    user = users.collection.find_one({'email': email})

    if user is not None and check_user_password(user['password'], password):
        # Logging in
        # Redirect to a success page
        payload = {
            'user_id': str(user['_id']),
            'first_name': user['first_name'],
            'last_name': user['last_name'],
            'email': user['email'],
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1),
            'iat': datetime.datetime.utcnow(),
        }
        token = jwt.encode(payload, 'DeadlySecret$', algorithm='HS256')
        return Response({'token': token})
    else:
        # Show an error message
        return HttpResponse('Invalid username or password')


def update_user_details(request):
    user_model = User()
    updated_data = {
        'first_name': 'John',
        'last_name': 'Smith',
        'email': "mocelo9636@docwl.com"
    }
    user_model.update_user('test@email.com', updated_data)
    return HttpResponse('User updated successfully')
