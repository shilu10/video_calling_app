from django.shortcuts import render
from django.http import JsonResponse
import random
import time
from agora_token_builder import RtcTokenBuilder
from .models import RoomMember
import json
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def lobby(request):
    return render(request, 'base/home.html')


def room(request):
    return render(request, 'base/room.html')


# for generating the token dynamically, just using the channel name given by the 
# users.
def getToken(request):
    print(request)
    # our app id in agora
    appId = "0e535728ef7e41bf8d63ee1e938f000d"
    # our app certificate
    appCertificate = "8a64047c46a946cc9a7ab8d0c0892460"
    # this is channel name provided by the user, we done this using the ajax
    channelName = request.GET.get('channel')
    # we are giving the random uid for each and every users
    uid = random.randint(1, 230)
    # this is expiration time for the token
    expirationTimeInSeconds = 3600
    # getting the current time stamp
    currentTimeStamp = int(time.time())
    privilegeExpiredTs = currentTimeStamp + expirationTimeInSeconds
    role = 1
    # this is the orginal token from the agora
    token = RtcTokenBuilder.buildTokenWithUid(appId, appCertificate, channelName, uid, role, privilegeExpiredTs)
    
    print(f"get_token/channel = {channelName} + token = {token}")
    # we are providing this as a jsonresponse to our frontend
    return JsonResponse({'token': token, 'uid': uid}, safe=False)


# we are getting the users information from the frontend
@csrf_exempt
def createMember(request):
    data = json.loads(request.body)

    # this is querying the database and storing the values, if there is already 
    # data present we gonna return it, else we are gonna store the data from frontend.

    member, created = RoomMember.objects.get_or_create(
        name=data['name'],
        uid=data['UID'],
        room_name=data['room_name']
    )
    
    # we are sending it to the frontend
    return JsonResponse({'name':data['name']}, safe=False)


# Trying to get the member from the database based on the uid.
def getMember(request):
    uid = request.GET.get('UID')
    room_name = request.GET.get('room_name')

    member = RoomMember.objects.get(
        uid=uid,
        room_name=room_name,
    )
    name = member.name
    return JsonResponse({'name':member.name}, safe=False)


# we are deleting the member, who have left the chat, based on their name and uid and channel
@csrf_exempt
def deleteMember(request):
    data = json.loads(request.body)
    member = RoomMember.objects.get(
        name=data['name'],
        uid=data['UID'],
        room_name=data['room_name']
    )
    member.delete()
    return JsonResponse('Member deleted', safe=False)