from pandas import DataFrame
import json
# pd.set_option('display.mpl_style', 'default') # Make the graphs a bit prettier
# figsize(15, 5)

with open('full_data.json') as json_file:
	data = json_file.read()
	data = data.encode('ascii')
	data = json.loads(data)
	print data
	df = DataFrame(data)
	df.to_csv('cru.csv', header=True, index=False, encoding='utf-8')