import json
def get_data():
    import http.client
    conn = http.client.HTTPConnection("jsonplaceholder.typicode.com")
    conn.request("GET","/users/1")
    res=conn.getresponse()
    data=res.read()
    return json.loads(data.decode("utf-8"))

