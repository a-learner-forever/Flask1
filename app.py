from flask import Flask, request

app = Flask(__name__)
stores=[{"name":"MyStore","items":[
    {
        "name":"chair7",
        "price":1205
    },
    {
        "name":"table",
        "price":400
    }
]
}
]

@app.get("/store")
def get_stores():
    return{"stores":stores}

@app.post("/store")
def create_store():
    request_data=request.get_json()
    new_store={"name":request_data["name"],"items":[]}
    stores.append(new_store)
    return new_store,201