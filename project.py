import preprocessing
import annotation


pw = input("Please enter password for postgres: ")
dbms = preprocessing.DBMS(pw)

query = dbms.getQuery()

"""
select *
from customer C,
orders O
where C.c_custkey =
O.o_custkey;
"""

qa = annotation.queryAnnotator()

res = qa.annotateQuery(dbms.explainQuery(query))
for i in range(len(res)):
    print("Step {}: {}".format(i+1, res[i]))

print("Operation done successfully")