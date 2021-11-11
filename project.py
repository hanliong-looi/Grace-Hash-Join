import annotation

QA = annotation.queryAnnotator()

def annotate_query(query, dbms):
    queryPlan = dbms.explainQuery(query)
    return QA.annotateQueryPlan(queryPlan[0])