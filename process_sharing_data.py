import json
import os

with open('full_data.json') as json_file:  
	data = json.load(json_file)
	data = data['data']
	most_like = 0
	most_sad = 0
	most_angry = 0
	most_haha = 0
	most_love = 0
	most_wow = 0
	most_total = 0

	# excl_stats
	i = 0
	for post in data:
		if 'message' in post:
			if 'sharing' in post['message']:
				# print json.dumps(post['reactions']['data'], indent=4, sort_keys=True)
				like = 0
				sad = 0
				angry = 0
				haha = 0
				love = 0
				wow = 0
				total = 0
				if 'reactions' in post:
					for react in post['reactions']['data']:
						if react['type'] == 'LIKE':
							like+=1
						elif react['type'] == 'SAD':
							sad+=1
						elif react['type'] == 'ANGRY':
							angry+=1
						elif react['type'] == 'HAHA':
							haha+=1
						elif react['type'] == 'LOVE':
							love+=1
						elif react['type'] == 'WOW':
							wow+=1
						total+=1
					if like > most_like:
						most_like = like
						most_like_post = post
						most_like_info = {
						'author': post['from']['name'],
						'message': post['message'],
						'like': like,
						'sad': sad,
						'angry': angry,
						'haha': haha,
						'love': love,
						'wow': wow
						}
					if sad > most_sad:
						most_sad = sad
						most_sad_post = post
						most_sad_info = {
						'author': post['from']['name'],
						'message': post['message'],
						'like': like,
						'sad': sad,
						'angry': angry,
						'haha': haha,
						'love': love,
						'wow': wow
						}
					if angry > most_angry:
						most_angry = angry
						most_angry_post = post
						most_angry_info = {
						'author': post['from']['name'],
						'message': post['message'],
						'like': like,
						'sad': sad,
						'angry': angry,
						'haha': haha,
						'love': love,
						'wow': wow
						}
					if haha > most_haha:
						most_haha = haha
						most_haha_post = post
						most_haha_info = {
						'author': post['from']['name'],
						'message': post['message'],
						'like': like,
						'sad': sad,
						'angry': angry,
						'haha': haha,
						'love': love,
						'wow': wow
						}
					if love > most_love:
						most_love = love
						most_love_post = post
						most_love_info = {
						'author': post['from']['name'],
						'message': post['message'],
						'like': like,
						'sad': sad,
						'angry': angry,
						'haha': haha,
						'love': love,
						'wow': wow
						}
					if wow > most_wow:
						most_wow = wow
						most_wow_post = post
						most_wow_info = {
						'author': post['from']['name'],
						'message': post['message'],
						'like': like,
						'sad': sad,
						'angry': angry,
						'haha': haha,
						'love': love,
						'wow': wow
						}
					if total > most_total:
						most_total = total
						most_total_post = post
						most_total_info = {
						'author': post['from']['name'],
						'message': post['message'],
						'like': like,
						'sad': sad,
						'angry': angry,
						'haha': haha,
						'love': love,
						'wow': wow
						}

print 'MOST LIKES ON A SHARING POST: ' + str(most_like)
print 'Info for that post:'
print json.dumps(most_like_info, indent=4, sort_keys=True)
print '\n\nMOST SAD\'S ON A SHARING POST: ' + str(most_sad)
print 'Info for that post:'
print json.dumps(most_sad_info, indent=4, sort_keys=True)
print '\n\nMOST ANGRY\'S ON A SHARING POST: : ' + str(most_angry)
print 'Info for that post:'
print json.dumps(most_angry_info, indent=4, sort_keys=True)
print '\n\nMOST HAHA\'S ON A SHARING POST: : ' + str(most_haha)
print 'Info for that post:'
print json.dumps(most_haha_info, indent=4, sort_keys=True)
print '\n\nMOST LOVE\'S ON A SHARING POST: : ' + str(most_love)
print 'Info for that post:'
print json.dumps(most_love_info, indent=4, sort_keys=True)
print '\n\nMOST WOW\'S ON A SHARING POST: : ' + str(most_wow)
print 'Info for that post:'
print json.dumps(most_wow_info, indent=4, sort_keys=True)
print '\n\nMOST TOTAL REACTS ON A SHARING POST: : ' + str(most_total)
print 'Info for that post:'
print json.dumps(most_total_info, indent=4, sort_keys=True)