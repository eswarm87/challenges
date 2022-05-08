from retreivedata import deep_get


res = {
    "name": "testing",
    "info": {
        "name": "Test",
        "date": "2021-06-12"
    },
    "result": [{
        "name": "test1",
        "value": 2.5
    }, {
        "name": "test2",
        "value": 1.9
    },{
        "name": "test1",
        "value": 3.1
    }]
}

# Define a function that takes two parameters named
# object : the full JSON object keys : an Array of keys in the order

deep_get(res, "info") # output: {'name': 'Test', 'date': '2021-06-12'}
deep_get(res, "info.date") # output: '2021-06-12'
deep_get(res, "result") # output: [{'name': 'test1', 'value': 2.5}, {'name': 'test2', 'value': 1.9}, {'name': 'test1', 'value': 3.1}]
deep_get(res, "result[2]") # output: {'name': 'test1', 'value': 3.1}
deep_get(res, "result[2].name") # output: 'test1'


