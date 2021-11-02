import preprocessing
import annotation
import test_jsons

pw = input("Please enter password for postgres: ")
dbms = preprocessing.DBMS(pw)

# query = dbms.getQuery()
# queryPlan = dbms.explainQuery(query)

queryPlan = test_jsons.test6

qa = annotation.queryAnnotator()

res = qa.annotateQuery(queryPlan[0])
for i in range(len(res)):
    print("Step {}: {}".format(i+1, res[i]))

