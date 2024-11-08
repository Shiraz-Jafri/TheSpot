from django.shortcuts import render
from django.http import HttpResponse
import googlemaps
from django.conf import settings
def get_spots(request):

    # use google maps api library
    # use places_nearby function
    # get the user's location from request url.
    # get the list of places
    # serialize the list of places and add it to the user's near by places
    # field. 
    return HttpResponse('Spots')

def get_a_spot(request):
    # get the place from request url
    # query list of places and filter it by the request url place
    # if the place exists, send it to the front end
    # react will use axios to get the data and present it.
    gmaps = googlemaps.Client(key=settings.GOOGLE_API_KEY)
    results = gmaps.geocode('238 N Smith Road, Bloomington, IN')
    return HttpResponse(results)