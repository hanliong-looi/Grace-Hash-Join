import annotation
import preprocessing

# pw = input("Please enter password for postgres: ")
# dbms = preprocessing.DBMS(pw)

# query = dbms.getQuery()
# queryPlan = dbms.explainQuery(query)

# for row in queryPlan:
#     print(row)

# queryPlan = test_jsons.test6

# for i in range(len(res)):
#     print("Step {}: {}".format(i+1, res[i]))

QA = annotation.queryAnnotator()

def annotate_query(query, dbms):
    queryPlan = dbms.explainQuery(query)
    return QA.annotateQueryPlan(queryPlan[0])

