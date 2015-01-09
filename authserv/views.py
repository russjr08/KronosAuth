from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from authserv.models import User
import hashlib
import json
import uuid

# Create your views here.

# /api/create_user/
@csrf_exempt
def create_user_api(request):
    username = request.POST.get("username", "undefined")
    username = username.strip()
    username = username.replace(" ", "")
    print(username)
    password = request.POST.get("password", "undefined")
    if (username is not "undefined" and username) and (request.POST.get("password", "undefined")
                                                       is not "undefined" and password):
        if len(username) > 15:
            return HttpResponse(json.dumps({'message': 'Username is too long!'}), content_type="application/json")

        # Check to see if the username is taken
        if User.objects.filter(username=username).exists():
            return HttpResponse(json.dumps({'message': 'User already exists!'}), content_type="application/json")

        user = User.objects.create(username=username,
                                   password_hash=hashlib.sha256(request.POST.get("password", "undefined")).hexdigest())
        user.uuid = str(uuid.uuid4())
        user.save()
        json_data = json.dumps({'username': user.username})
        return HttpResponse(json_data, content_type="application/json")
    else:
        return HttpResponse(json.dumps({'message': 'Missing a required field!'}), content_type="application/json")


# /api/login/
@csrf_exempt
def login_api(request):
    user = user_exists(request.POST.get("username", "undefined"))
    user_hash = hashlib.sha256(request.POST.get("password", "undefined")).hexdigest()

    if user is not None and user.password_hash == user_hash:
        # Check if user has a UUID, and if not, create one for them.
        if user.uuid == "unresolved-uuid":
            print("User: " + user.username + " doesn't have a UUID, assigning one now!")
            user.uuid = str(uuid.uuid4())
            print("UUID assigned successfully. (" + user.uuid + ")")
            user.save()

        if user.disabled == True:
            json_data = json.dumps({'message': 'Account is disabled.'})
            return HttpResponse(json_data, content_type="application/json")

        user.auth_token = User.generate_auth_token()
        json_data = json.dumps({'message': 'Authentication Successful.',
                                'username': user.username, 'auth_token': user.auth_token, 'uuid': user.uuid})

        user.save()
        return HttpResponse(json_data, content_type="application/json")
    else:
        return HttpResponse(json.dumps({'message': 'Failed to authenticate.'}), content_type="application/json")


# /api/verify_token/
@csrf_exempt
def check_token(request):
    user = user_exists(request.POST.get("username", "undefined"))
    token = request.POST.get("auth_token", "undefined")

    if user is not None and token == user.auth_token:
        json_data = json.dumps({'message': 'Authentication Token is valid.', 'username': user.username})

        return HttpResponse(json_data, content_type="application/json")
    else:
        json_data = json.dumps({'message': 'Authentication Token is invalid.'})
        return HttpResponse(json_data, content_type="application/json")


# /api/get_user/:user_name
@csrf_exempt
def get_user(request, user_name):
    user = user_exists(user_name)

    if user is not None:
        json_data = json.dumps({'message': 'User exists.', 'username': user.username, 'uuid': user.uuid})
        return HttpResponse(json_data, content_type="application/json")
    else:
        json_data = json.dumps({'message': 'User not found.'})
        return HttpResponse(json_data, content_type="application/json")


def user_exists(name):
    try:
        user = User.objects.get(username=name)
    except User.DoesNotExist:
        return None

    return user
