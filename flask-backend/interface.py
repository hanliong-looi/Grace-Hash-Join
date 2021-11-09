import flask
import preprocessing
import project

app = flask.Flask("__main__")
test_input = 'select * from customer C, orders O where C.c_custkey = O.o_custkey;'
pw = input("Please enter password for postgres: ")
dbms = preprocessing.DBMS(pw)

@app.route("/")
def my_index():
    return flask.render_template("index.html", token="From Flask")

@app.route("/api/test")
def text_api():
    app.logger.info("get request from FE")
    return flask.jsonify({"data":"hello sir"})

@app.route("/api/get_query")
def get_query():
    res, plan = project.annotate_query(test_input, dbms)

    return flask.jsonify({"plan": plan, "instructions": res})

app.run(debug=True)