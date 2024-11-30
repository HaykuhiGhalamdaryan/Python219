import requests

url = "https://jsonplaceholder.typicode.com/"

# Ex 1

get_response = requests.get(f"{url}/comments?postId=1")
post_response = requests.post(f"{url}/posts", json={"userId": 10, "title": "title", "body": "body"})
put_response = requests.put(f"{url}/posts/1", json={"userId": 10, "title": "Updated title", "body": "Updated body"})
del_response = requests.delete(f"{url}/posts/1")

print(get_response.status_code)
print(get_response.text)
print(post_response.status_code)
print(post_response.text)
print(put_response.status_code)
print(put_response.text)
print(del_response.status_code)


# Ex 2, 3

# response = requests.get(f"{url}/posts")
# data = response.json()

# title_result = []
# body_result = []
# for _dict in data:
#       title = _dict['title'].split()
#       body = _dict['body'].split('\n')
      
#       if len(title) > 6:
#             title_result.append(_dict)
            
#       if len(body) > 3:
#             body_result.append(_dict)
            
# print("Responses whose title contains more than 6 words:\n", title_result)
# print("Responses whose body contains more than 3 lines of description(\\n):\n", body_result)
