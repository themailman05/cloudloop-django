from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse, HttpResponse
from django.db.models import Count, Q
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

from . import models
from . import serializers

from userauth import models as userauth_models

@login_required
def load_sessions(request):
    """Load user looper sessions

    - Retrieve all of the sessions that include the user.
    - returns {"sessions":[session]}
    """
    sessions = models.Session.objects.filter(clients=request.user)
    session_data = serializers.SessionSerializer(sessions).data
    return JsonResponse({'sessions':session_data})

@login_required
def load_loops(request):
    """Load loops from session

    - Does not transmit audio data, just sends the loop objects
    - returns json {loops:[Loop]}
    """
    session = models.Session.objects.get(hash_id=request.GET['id'])
    # make sure we are a part of this session before we get the loops
    if not request.user in session.clients.all():
        return HttpResponse(status=403)
    # Session filter
    q = [Q(session=session)]
    loops = models.Loop.objects.filter(*q)
    loops_data = serializers.LoopListSerializer
    return JsonResponse({"loops":loops_data})

@login_required
def add_session(request):
    """Add user to session

    - Create session if existing one with title does not exist
    - User is added to the session"""
    title = request.POST['title'].strip()

    if models.Session.objects.filter(title=title).exists():
        session = models.Session.objects.get(title=title)
    else:
        thread = models.Session(title=title)
        thread.save()

    if not request.user in session.clients.all():
        thread.clients.add(request.user)
    return HttpResponse(status=200)