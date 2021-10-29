import preprocessing


pw = input("Please enter password for postgres: ")
dbms = preprocessing.DBMS(pw)

query = dbms.getQuery()

# for row in dbms.executeQuery(query):
#     print(row)

for row in dbms.explainQuery(query):
    print(row)

print("Operation done successfully")