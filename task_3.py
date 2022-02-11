import requests as reqs
from datetime import datetime, timedelta
import time

fromdate = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
fromdate = fromdate - timedelta(days=1)
fromdate = int(time.mktime(fromdate.timetuple()))

print(f"Searching all questions from {datetime.fromtimestamp(fromdate)}")

page = 1
while True:
    resp = reqs.get(f'https://api.stackexchange.com/2.3/questions?page={page}&pagesize=100&fromdate={fromdate}&order=desc&sort=creation&tagged=Python&site=stackoverflow', timeout=5)
    resp = resp.json()
    
    if len(resp['items']) == 0:
        break

    for i, item in enumerate(resp['items']):

        if len(item['title']) > 50:
            item['title'] = item['title'][:47] + '...'
        print(f"{(i + 1) + 100 * (page - 1)}. {item['title']}")

        print(f"    Date: {datetime.fromtimestamp(item['creation_date'])}")

        short_link = '/'.join(item['link'].split('/')[:-1]).replace('questions', 'q')
        print(f"    Link: {short_link}")

        print(f"    Solved: {item['is_answered']}")

    page += 1
