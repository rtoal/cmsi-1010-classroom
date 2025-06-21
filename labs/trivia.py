import requests
from urllib.parse import unquote

url = "https://opentdb.com/api.php?amount=1&type=multiple&encode=url3986"
response = requests.get(url)
if response.status_code != 200:
    raise ValueError(f'API error: {response.status_code}')
body = response.json()
if body['response_code'] != 0:
    raise ValueError(f'OpenTDB error: {body["response_code"]}')
question = body['results'][0]
question['category'] = unquote(question['category'])
question['question'] = unquote(question['question'])
question['correct_answer'] = unquote(question['correct_answer'])
question['incorrect_answers'] = [
    unquote(ans) for ans in question['incorrect_answers']]
print(question)
