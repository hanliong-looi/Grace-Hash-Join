import psycopg2

class DBMS:
    def __init__(self):
        self.con = None
        self.cur = None
    
    def __del__(self):
        if self.con:
            self.con.close()

    def connect(self, pw):
        try:
            self.con = psycopg2.connect(database="TPC-H", user="postgres", password=pw, host="127.0.0.1", port="5432")
            print("Database opened successfully")
            self.cur = self.con.cusor()
            return True
        except:
            self.con = None
            print('Failed to connect to database')
            return False

    def getQuery(self):
        print('Enter your query: ')
        query = []
        query.append(input())
        while query[-1][-1] != ';':
            query.append(input())

        joined = ' '.join(query)
        return joined

    def executeQuery(self, query):
        self.cur.execute(query)
        return self.cur.fetchall()

    def explainQuery(self, query):
        queryPlan = self.executeQuery('EXPLAIN (costs false, format json, verbose) ' + query)
        return queryPlan[0][0]
