class queryAnnotator:
    def __init__(self):
        # Maps each node to its respective annotation
        self.queryMapper = {
            "Hash Join" : hash_join_annotator,
            "Seq Scan" : seq_scan_annotator,
            "Hash" : hash_annotator
        }

    # Reads the query plan and sorts the order of query execution
    def traversePlan(self, queryPlan):
        # Create stack for DFS
        stack = []

        # Order of query execution
        queryOrder = []

        # Push root node of query plan onto stack
        stack.append(queryPlan["Plan"])

        # Perform left child DFS on query plan
        while (len(stack) > 0):
            # Pop top most node in stack and add it to order list
            node = stack.pop()
            queryOrder.append(node)

            # If current node does not have anymore children
            if "Plans" not in node:
                continue

            # Add children of current node to stack
            for plan in node["Plans"]:
                stack.append(plan)

        return queryOrder

    # Annotates given query plan
    def annotateQuery(self, queryPlan):
        # Array of annotations of query
        result = []

        # Get order of query execution
        queryOrder = self.traversePlan(queryPlan)

        # Iteratively pop top most query from stack to annotate
        while len(queryOrder) > 0:
            # Get annotation for current query
            queryNode = queryOrder.pop()
            result.append(self.queryMapper[queryNode["Node Type"]](queryNode))
        return result
    


"""
Functions to annotate different types of nodes
"""

# Function to annotate Hash Join
def hash_join_annotator(queryNode):
    name = "Hash Join"

    # Get type of join if any
    join_type = "" if "Join Type" not in queryNode else queryNode["Join Type"]

    # Get condition of join if any
    join_condition = "" if "Hash Cond" not in queryNode else "on condition " + queryNode["Hash Cond"]

    # Build annotation string
    annotation = "{} {} {}".format(join_type, name, join_condition)

    return annotation

def seq_scan_annotator(queryNode):
    scan_name = "Sequential Scan"

    # Get name of relation
    relation_name = queryNode["Relation Name"]

    # Get scan conditions if any
    filter_message = "" if "Filter" not in queryNode else "on condition " + queryNode["Filter"]

    # Build annotation string
    annotation = "{} on table {} {}".format(scan_name, relation_name, filter_message)

    return annotation

def hash_annotator(queryNode):
    name = "Hash"
    
    relation_name = "on table {}".format(queryNode["Plans"][0]["Relation Name"])

    # Get hash condition
    condition = "" if "Hash Cond" not in queryNode else "on condition " + queryNode["Hash Cond"]

    # Build annotation string
    annotation = "{} {} {}".format(name, relation_name, condition)

    return annotation
