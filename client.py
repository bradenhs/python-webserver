import requests

postResponse = requests.post(
    "http://localhost:5000/create_sum", json={"operands": [1, 2, 3]}
)
print("create_sum(1,2,3)", postResponse.json())

getResponse = requests.get("http://localhost:5000/retrieve_sum?operands=1,2,3")
print("retrieve_sum(1,2,3)", getResponse.json())
