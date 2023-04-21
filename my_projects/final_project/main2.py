#!/usr/bin/python3
"""Final Python Project"""

from pprint import pprint

import requests

url = "https://anime-db.p.rapidapi.com/anime"

querystring = {"page":"1","size":"10","sortBy":"ranking","sortOrder":"asc"}

headers = {
	"X-RapidAPI-Key": "b7ab5efca6mshb004f071c154defp16bc21jsn088ae64102c2",#this is where your key goes
	"X-RapidAPI-Host": "anime-db.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

pprint(response.text)
