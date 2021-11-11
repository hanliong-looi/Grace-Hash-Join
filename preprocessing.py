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
            self.cur = self.con.cursor()
            return True
        except:
            self.con = None
            print('Failed to connect to database')
            return False

    def executeQuery(self, query):
        try:
            self.cur.execute(query)
            self.con.commit()
            return self.cur.fetchall()
        except Exception as e:
            self.con.rollback()
            raise ValueError(e)

    def explainQuery(self, query):
        queryPlan = self.executeQuery('EXPLAIN (costs false, format json, verbose) ' + query)
        return queryPlan[0][0]
