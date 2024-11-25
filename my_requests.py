import requests

url = "https://jsonplaceholder.typicode.com/"

response = requests.get(f"{url}/posts")
data = response.json()

title_result = []
body_result = []
for _dict in data:
      title = _dict['title'].split()
      body = _dict['body'].split('\n')
      
      if len(title) > 6:
            title_result.append(_dict)
            
      if len(body) > 3:
            body_result.append(_dict)
            
print("Responses whose title contains more than 6 words:\n", title_result)
print("Responses whose body contains more than 3 lines of description(\\n):\n", title_result)


