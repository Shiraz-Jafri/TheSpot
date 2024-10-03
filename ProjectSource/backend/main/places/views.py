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
    # results printed 
    " {'address_components': [{'long_name': 'Spring Mill Apartments', "
    " 'short_name': 'Spring Mill Apartments', 'types': ['premise']}, " 
    " {'long_name': '238', 'short_name': '238', 'types': ['street_number']}, "
    " {'long_name': 'North Smith Road', 'short_name': 'N Smith Rd', 'types': ['route']}, " 
    " {'long_name': 'Bloomington', 'short_name': 'Bloomington', 'types': ['locality', 'political']}, "
    " {'long_name': 'Bloomington Township', 'short_name': 'Bloomington Township', 'types': ['administrative_area_level_3', 'political']}, "
    " {'long_name': 'Monroe County', 'short_name': 'Monroe County', 'types': ['administrative_area_level_2', 'political']}, " 
    " {'long_name': 'Indiana', 'short_name': 'IN', 'types': ['administrative_area_level_1', 'political']}, "
    " {'long_name': 'United States', 'short_name': 'US', 'types': ['country', 'political']}, "
    " {'long_name': '47408', 'short_name': '47408', 'types': ['postal_code']}, {'long_name': '3084', 'short_name': '3084', 'types': ['postal_code_suffix']}], "
    " 'formatted_address': 'Spring Mill Apartments, 238 N Smith Rd, Bloomington, IN 47408, USA', 'geometry': {'bounds': {'northeast': {'lat': 39.168474, 'lng': -86.48070799999999},"
    " 'southwest': {'lat': 39.168034, 'lng': -86.4808564}}, "
    " 'location': {'lat': 39.1682539, 'lng': -86.4807822}, "
    " 'location_type': 'ROOFTOP', 'viewport': {'northeast': {'lat': 39.1695616302915, 'lng': -86.47966986970849},"
    " 'southwest': {'lat': 39.1668636697085, 'lng': -86.4823678302915}}},"
    " 'place_id': 'ChIJfx7BlxRkbIgRnShnLVcnvNQ', 'types': ['premise']}' "
    return HttpResponse(results)