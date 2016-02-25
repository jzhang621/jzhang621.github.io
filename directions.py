import requests
import json
from urllib import urlencode


base_url = 'https://maps.googleapis.com/maps/api/directions/json?'


waypoints = [(37.741559, -122.443185), (37.746186, -122.449212), (37.739265, -122.454509), (37.737897, -122.449991)]

origin = (37.733063, -122.433819)
destination = (37.733063, -122.433819)


def make_google_directions_url(origin, destination, waypoints, mode='walking'):
  """
  Construct the url used to get directions from the Google API.

  :param tuple origin: Tuple (lat, long) of the origin.
  :param tuple destination: Tuple (lat, long) of the destination.
  :param list waypoints: List of tuple (lat, long) of waypoints to include along the route.
  :param str mode: The mode of transporation (walking, driving, bicylcling)
  :return: URL to query Google Maps.
  """
  origin_key = '{0},{1}'.format(origin[0], origin[1])
  destination_key = '{0},{1}'.format(destination[0], destination[1])
  
  flattened_waypoints = map(lambda point: '{0},{1}'.format(point[0], point[1]), waypoints)
  waypoints_key = '|'.join(flattened_waypoints)

  kwargs = {'origin': origin_key, 'destination': destination_key, 'waypoints': waypoints_key, 'mode': mode}
  encoded_args = urlencode(kwargs)
  return base_url + encoded_args


def get_json_directions(url):
  """
  Make a request to the given url, and return the json response.
  """
  resp = requests.get(url)
  if resp.status_code == 200:
    return resp.json()
  else:
    print 'Failed to return data for %s', url


def parse_directions(json_response):
  """
  Parse the json response data into a list of points. Each point is a dictionary in the form of {'lat': lat, 'long': long}
  """
  output_path = []
  route = json_response['routes'][0]

  for leg in route['legs']:
    for step in leg['steps']:
      start = step['start_location']
      end = step['end_location']
      output_path.extend([start, end])

  return output_path

origin = (40.045112, -124.076594)
destination = (40.289025, -124.357272)


url = make_google_directions_url(origin, destination, [], 'driving')
resp = get_json_directions(url)

directions = parse_directions(resp)
import pdb; pdb.set_trace()

with open('directions.json', 'w') as d:
  json.dump(directions, d)
