import facebook

token = "EAACEdEose0cBAB9lj73ASy2yXyzo7BL6wrtZCJnmOT6lZBNtHZBZCcAePFFoqZCtWamX4RRv2ADGrosguxjtncpDOBVu0xli1bpkfQ273JfKPkhMyLGQ6R5riYyA3GrUCLBnXlRgjdA4sIqZBwKyZCUP95ZBgepg5lpXqu9yed74ZCAvO3rIHYQTNPo8Uwyo3rsItExIqxo5aQgZDZD"
graph = facebook.GraphAPI(token)
app_id = '969118063243452' # Obtained from https://developers.facebook.com/
app_secret = '16d9236a6c4da38b14138025f4290a52' # Obtained from https://developers.facebook.com/

# Extend the expiration time of a valid OAuth access token.
extended_token = graph.extend_access_token(app_id, app_secret)
print(extended_token) #verify that it expires in 60 days