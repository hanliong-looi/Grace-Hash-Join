import annotation
import preprocessing

# connected = False
# while not connected:
#     dbms = preprocessing.DBMS()
#     pw = input("Please enter password for postgres: ")
#     connected = dbms.connect(pw)

# query = dbms.getQuery()
# queryPlan = dbms.explainQuery(query)

# queryPlan = test_jsons.test6

# for i in range(len(res)):
#     print("Step {}: {}".format(i+1, res[i]))

QA = annotation.queryAnnotator()

def annotate_query(query, dbms):
    queryPlan = dbms.explainQuery(query)
    return QA.annotateQueryPlan(queryPlan[0])

# res, plan = annotate_query(query, dbms)
# for step in res:
#     print(step)