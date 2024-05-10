from flask import Flask, jsonify, request
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


#--------------------------------------------- 01 -------------------------------------------
@app.route("/users",methods=["GET"])
def fn_get():
    return jsonify({
        "payload":"success"
    })
    
#--------------------------------------------- 02 -------------------------------------------    
    
@app.route("/user",methods=["POST"])
def fn_post():
    return jsonify({
        "payload":"success"
    })
    
#--------------------------------------------- 03 -------------------------------------------
    
@app.route("/user", methods=["DELETE"])
def fn_delete():
    return jsonify({
        "payload":"success"
    })
 
#--------------------------------------------- 04 -------------------------------------------    

@app.route("/user", methods=["PUT"])
def fn_put():
    return jsonify({
        "payload":"success",
        "error":False
    })
 
#--------------------------------------------- 05 ------------------------------------------- 
    
@app.route("/api/v1/users", methods=["GET"])
def fn_api_get():
    return jsonify({
        "payload":[]
    })

#--------------------------------------------- 06 -------------------------------------------

@app.route("/api/v1/user", methods=["POST"])
def fn_api_post():
    
    email = request.args.get("email")
    name = request.args.get("name")
    return jsonify({
        'payload': {
             'email':email,
             'name':name
        },
    })
  
#--------------------------------------------- 07 -------------------------------------------
    
@app.route("/api/v1/user/add", methods=['POST'])
def fn_api_add():
    email = request.form["email"]
    name = request.form["name"]
    id = request.form['id']
    return jsonify({
        'payload' : {
            'email':email,
            'name':name,
            'id':id
        }
    })
 

#--------------------------------------------- 08 -------------------------------------------

   
@app.route("/api/v1/user/create", methods=['POST'])   
def fn_api_create():
    email = request.json['email']
    name = request.json['name']
    id =   request.json['id']
    return jsonify({
        'payload' : {
            'email':email,
            'name':name,
            'id':id
        }
    })

    
    
    

if __name__ == "__main__":
    app.run(debug=True)