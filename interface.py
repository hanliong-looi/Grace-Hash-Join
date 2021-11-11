from flask import render_template, Flask, jsonify, request
import preprocessing
import project

app = Flask("__main__")

connected = False
while not connected:
    dbms = preprocessing.DBMS()
    pw = input("Please enter password for postgres: ")
    connected = dbms.connect(pw)

@app.route("/")
def my_index():
    return render_template("index.html", token="From Flask")

@app.route("/api/test")
def text_api():
    return jsonify({"data":"hello sir"})

@app.route("/api/get_query", methods=['POST'])
def get_query():
    request_data = request.get_json()
    query_str = request_data["query"]
    app.logger.info(f'received data from client: {query_str}')
    try:
        res, plan, e_msg = project.annotate_query(query_str, dbms)
        return jsonify({"plan": plan, "instructions": res, "error": 0, "error_message":e_msg})
    except Exception as e_msg:
        return jsonify({"plan":"", "instructions":"", "error":1, "error_message":f"Incorrect SQL Query: {e_msg}"})

    

app.run(debug=False)
