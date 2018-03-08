import facebook
import json
import requests
import os
token = "EAAcIl8Q8WD8BAAZBqmHbdyOO59peZC7q0pubKtv6Jac64Q5btGsQQAH2LuHylPtjbJTClWWDKq8mQ9tjqYAv5a3DfCg2umwcmrmhNDQIWeXvIdhvkgswecDFjMNgOxZBdevXyYf17oCcm0NQPZAV20W33yAqH9wZD"
graph = facebook.GraphAPI(access_token=token, version=2.7)

batch_directory = "./post_batches"
if not os.path.exists(batch_directory):
    os.makedirs(batch_directory)

batch_size = 100
batch_num = 0
posts_fetched = 0
fields = 'feed.limit(' + str(batch_size) + '){message,from,reactions.limit(500),comments.limit(100),id}'
print("batch size: " + str(batch_size))
print("fetching group feed batch " + str(batch_num	) + " ...")
feed = graph.get_object(id='1573851542881057', fields=fields)
feed = feed['feed']
print("done")
print("writing to file ...")
f = open(batch_directory + '/' + str(batch_num) + ".json", "w")
f.write('batch ' + str(batch_num) + '\n' + json.dumps(feed, indent=2, sort_keys=True) + '\n')
f.close()
batch_num = batch_num + 1
posts_fetched = posts_fetched + batch_size
print("done")
print("total posts fetched: " + str(posts_fetched) + "\n")

while(True):
	try:
		print("fetching group feed batch " + str(batch_num) + " ...")
		feed=requests.get(feed['paging']['next']).json()
		print("done")
		print("writing to file ...")
		f = open(batch_directory + '/' + str(batch_num) + ".json", "w")
		f.write('batch ' + str(batch_num) + '\n' + json.dumps(feed, indent=2, sort_keys=True) + '\n')
		f.close()
		batch_num = batch_num + 1
		posts_fetched = posts_fetched + batch_size
		print("done")
		print("total posts fetched: " + str(posts_fetched) + "\n")

	except KeyError as e:
		print("end of feed")
		break

print("done")