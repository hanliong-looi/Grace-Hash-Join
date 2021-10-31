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

qa = annotation.queryAnnotator(dbms.explainQuery(query))
qa.traversePlan()

print("Operation done successfully")