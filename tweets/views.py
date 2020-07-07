import random
from django.http import JsonResponse, HttpResponse, Http404
from django.shortcuts import render
from .models import Tweet
def home_view(request, *args, **kwargs):
    return render(request, 'pages/home.html', context={}, status=200)


def tweets_list(request, *args, **kwargs):
    obj = Tweet.objects.all()
    tweet_list = [{"id": x.id, "content": x.content, "likes": random.randint(0, 199)}for x in obj]
    data = {
        "response": tweet_list
    }
    return JsonResponse(data)

def tweet_detail_view(request, tweet_id, *args, **kwargs):
    '''
    RestAPI that consume by javascript or java/react/swift/php
    '''

    data = {
        'id' : tweet_id,
    }
    status = 200
    try:
        obj = Tweet.objects.get(id=tweet_id)
        data['content'] = obj.content
    except:
        data['message'] = 'Not Found'
        status = 404
    return JsonResponse(data, status=status)