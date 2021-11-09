from flask import render_template, Flask, jsonify, request
import preprocessing
import project

app = Flask("__main__")
pw = input("Please enter password for postgres: ")
dbms = preprocessing.DBMS(pw)

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
    res, plan = project.annotate_query(query_str, dbms)

    return jsonify({"plan": plan, "instructions": res})

app.run(debug=False)