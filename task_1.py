import requests as reqs


url = 'https://superheroapi.com/api/2619421814940190/search/'

print('Получаю информацию о Hulk...')
hulk = reqs.get(url + 'Hulk').json()['results'][0]

print('Получаю информацию о Captain America...')
cap = reqs.get(url + 'Captain America').json()['results'][0]

print('Получаю информацию о Thanos...')
thanos = reqs.get(url + 'Thanos').json()['results'][0]

smartest = max([hulk, cap, thanos], key=lambda x: int(x['powerstats']['intelligence']))
print('Самым умным оказался:', smartest['name'], '\nИнтеллект:', smartest['powerstats']['intelligence'])