from flask import Flask,request 

# import requests
# res = requests.post('http://localhost:5000/index', json={"text1":"lalala"})
# if res.ok:
#     print(res.json())


app = Flask(__name__)



@app.route("/",methods=['POST'])
def index():
    texts=request.get_json(force=True)
    return texts


if __name__ == '__main__':
    app.run(debug=False)
              

