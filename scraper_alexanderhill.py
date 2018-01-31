import requests as r

espn_url = 'http://www.espn.com/nba/story/_/id/22211929/nba-power-rankings-our-expert-panel-unveils-rankings-week-16'
headers1 = {'user-agent': 'Alexander Hill (lex.m.hill@gmail.cm)'}
response = r.get(espn_url, headers=headers1)
with open('espnrankings.txt', 'a') as espn:
	print(response.text, file=espn)
print()
