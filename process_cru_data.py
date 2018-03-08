import json
import os

#1385 total posts

def count_chars(word):
    return len(word) - word.count(' ')

person = 'carson gerard miller'

with open('full_data.json') as json_file:  
	data = json.load(json_file)
	data = data['data']
	total_excl_count = 0
	total_excl_ratio = 0
	total_punc_count = 0
	post_count = 0
	max_excl = 0
	max_excl_ratio = 0
	max_excl_punc_ratio = 0
	max_excl_name = ''
	max_excl_ratio_name = ''
	max_excl_ratio_message = ''
	max_excl_message = ''
	max_excl_punc_ratio_message = ''
	max_excl_punc_ratio_name = ''

	person_total_excl_count = 0
	person_total_excl_ratio = 0
	person_total_punc_count = 0
	person_post_count = 0
	person_max_excl = 0
	person_max_excl_ratio = 0
	person_max_excl_punc_ratio = 0
	person_max_excl_ratio_message = ''
	person_max_excl_message = ''
	person_max_excl_punc_ratio_message = ''
	person_max_excl_punc_ratio_name = ''

	# excl_stats
	for post in data:
		if 'message' in post:
			excl_count = post['message'].count('!')
			punc_count = excl_count
			punc_count += post['message'].count('?')
			punc_count += post['message'].count(';')
			punc_count += post['message'].count('.')
			total_punc_count += punc_count
			num_chars = count_chars(post['message'])
			excl_ratio = excl_count / float(num_chars)
			total_excl_count += excl_count
			total_excl_ratio += excl_ratio
			post_count += 1
			if punc_count != 0:
				excl_punc_ratio = excl_count / float(punc_count)

			if excl_count > max_excl:
				max_excl_name = post['from']['name']
				max_excl = excl_count
				max_excl_message = post['message']
				# print post['from']['name']
				# print excl_count
				# print post['message']
				# print('\n\n')

			if excl_ratio > max_excl_ratio:
				max_excl_ratio_name = post['from']['name']
				max_excl_ratio = excl_ratio
				max_excl_ratio_message = post['message']

			if excl_punc_ratio > max_excl_punc_ratio:
				max_excl_punc_ratio_name = post['from']['name']
				max_excl_punc_ratio = excl_punc_ratio
				max_excl_punc_ratio_message = post['message']

	# stats for specific person
	for post in data:
		if post['from']['name'].lower() == person.lower():
			if 'message' in post:
				person_excl_count = post['message'].count('!')
				person_punc_count = person_excl_count
				person_punc_count += post['message'].count('?')
				person_punc_count += post['message'].count(';')
				person_punc_count += post['message'].count('.')
				person_total_punc_count += person_punc_count
				person_num_chars = count_chars(post['message'])
				person_excl_ratio = person_excl_count / float(person_num_chars)
				person_total_excl_count += person_excl_count
				person_total_excl_ratio += person_excl_ratio
				person_post_count += 1

				if person_punc_count != 0:
					person_excl_punc_ratio = person_excl_count / float(person_punc_count)

				if person_excl_count > person_max_excl:
					person_max_excl = person_excl_count
					person_max_excl_message = post['message']

				if person_excl_ratio > person_max_excl_ratio:
					person_max_excl_ratio = person_excl_ratio
					person_max_excl_ratio_message = post['message']

				if person_excl_punc_ratio > person_max_excl_punc_ratio:
					person_max_excl_punc_ratio = person_excl_punc_ratio
					person_max_excl_punc_ratio_message = post['message']

		
#print total excl stats
print('TOTAL_STATS')
avg_excl = total_excl_count/float(post_count)
avg_excl_ratio = total_excl_ratio/float(post_count)
total_excl_punc_ratio = total_excl_count/float(total_punc_count)
print('total excl: ' + str(total_excl_count))
print('total posts: ' + str(post_count))
print('average number of excl: ' + str(avg_excl))
print('average excl ratio: ' + str(avg_excl_ratio))
print('total excl punc ratio: ' + str(total_excl_punc_ratio))
print('max excl: ' + str(max_excl))
print('max excl name: ' + str(max_excl_name))
print('max excl ratio: ' + str(max_excl_ratio))
print('max excl punc ratio: ' + str(max_excl_punc_ratio))
print('max excl ratio name: ' + max_excl_ratio_name)
print('max excl punc ratio name: ' + max_excl_ratio_name)
print('max excl message:\n'.upper() + max_excl_message + '\n')
print('max excl ratio message:\n'.upper() + max_excl_ratio_message + '\n')
print('max excl punc ratio message:\n'.upper() + max_excl_message)
print('\n\n')

#print specific person stats
print(person.upper() + ' STATS')
person_avg_excl = person_total_excl_count/float(person_post_count)
person_avg_excl_ratio = person_total_excl_ratio/float(person_post_count)
person_total_excl_punc_ratio = person_total_excl_count/float(person_total_punc_count)
print(person + ' total excl: ' + str(person_total_excl_count))
print(person + ' total posts: ' + str(person_post_count))
print(person + ' average number of excl: ' + str(person_avg_excl))
print(person + ' average excl ratio: ' + str(person_avg_excl_ratio))
print(person + ' total excl punc ratio: ' + str(person_total_excl_punc_ratio))
print(person + ' max excl: ' + str(person_max_excl))
print(person + ' max excl ratio: ' + str(person_max_excl_ratio))
print(person + ' max excl punc ratio: ' + str(person_max_excl_punc_ratio))
print('max excl message:\n'.upper() + person_max_excl_message + '\n')
print('max excl ratio message:\n'.upper() + person_max_excl_ratio_message + '\n')
print('max excl punc ratio message:\n'.upper() + person_max_excl_punc_ratio_message)
print('\n\n')