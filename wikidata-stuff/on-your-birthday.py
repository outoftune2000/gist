import requests
from collections import OrderedDict

url = 'https://query.wikidata.org/sparql'

# 1996,2,29

year = 1996
month = 2
day = 20

query = """
SELECT ?entity ?entityLabel ?entityDescription ?sitelinks WHERE {
  ?entity wdt:P31 wd:Q5.
  ?entity wdt:P21 wd:Q6581097.
  ?entity wdt:P569 "+%s-%s-%sT00:00:00Z"^^xsd:dateTime.
  ?entity wikibase:sitelinks ?sitelinks .
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
  FILTER (?sitelinks > 2) 
}
ORDER BY DESC(?sitelinks)
LIMIT 20
""" % (year, month, day)

r = requests.get(url, params = {'format': 'json', 'query': query})
data = r.json()
 
#print(data)

people = []
for item in data['results']['bindings']:
    people.append(
    	OrderedDict({
	        'name': item['entityLabel']['value'],
	        'bio': item['entityDescription']['value']
	        	if 'entityDescription' in item else '',
        })
    )

for item in people:
	print(item['name'] + ' - ' + item['bio'])