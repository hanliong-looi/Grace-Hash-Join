class queryAnnotator:
    def __init__(self):
        # Maps each node to its respective annotation
        self.queryMapper = {
            "Hash Join" : hash_join_annotator,
            "Nested Loop" : nested_loop_annotator,
            "Merge Join" : merge_join_annotator,
            "Seq Scan" : seq_scan_annotator,
            "Index Scan" : index_scan_annotator,
            "Index Only Scan" : index_scan_annotator,
            "Bitmap Heap Scan" : bitmap_scan_annotator,
            "Bitmap Index Scan" : bitmap_scan_annotator,
            "BitmapAnd" : bitmap_scan_annotator,
            "BitmapOr" : bitmap_scan_annotator,
            "Values Scan" : value_scan_annotator,
            "CTE Scan" : cte_scan_annotator,
            "Function Scan" : function_scan_annotator,
            "Subquery Scan" : subquery_scan_annotator,
            "Hash" : hash_annotator,
            "Sort" : sort_annotator,
            "Append" : append_annotator,
            "Aggregate" : aggregate_annotator,
            "Materialize" : materialize_annotator,
            "Unique" : unique_annotator,
            "Limit" : limit_annotator,
            "Result" : result_annotator,
            "Gather" : gather_annotator,
            "Gather Merge" : gather_annotator
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
            if queryNode["Node Type"] not in self.queryMapper:
                print("Cannot find annotation for this query: {}".format(queryNode["Node Type"]))
                continue
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

# Function to annotate Nested Loop
def nested_loop_annotator(queryNode):
    name = "Nested Loop Join"

    # Get type of join if any
    join_type = "" if "Join Type" not in queryNode else queryNode["Join Type"]

    # Get condition of join if any
    join_condition = "" if "Join Filter" not in queryNode else "on join filter " + queryNode["Join Filter"]

    # Build annotation string
    annotation = "{} {} {}".format(join_type, name, join_condition)

    return annotation

# Function to annotate Merge Join
def merge_join_annotator(queryNode):
    name = "Merge Join"

    # Get type of join if any
    join_type = "" if "Join Type" not in queryNode else queryNode["Join Type"]

    # Get condition of join if any
    join_condition = "" if "Merge Cond" not in queryNode else "on condition " + queryNode["Merge Cond"]

    # Build annotation string
    annotation = "{} {} {}".format(join_type, name, join_condition)

    return annotation

# Function to annotate Sequential Scan
def seq_scan_annotator(queryNode):
    scan_name = "Sequential Scan"

    # Get name of relation
    relation_name = queryNode["Relation Name"]

    # Get alias of relation
    alias_name = queryNode["Alias"]

    # Get scan conditions if any
    filter_message = "" if "Filter" not in queryNode else "on condition " + queryNode["Filter"]

    # Build annotation string
    annotation = "{} on table {} with alias '{}' {}".format(scan_name, relation_name, alias_name, filter_message)

    return annotation

# Function to annotate Index Scan or Index Only Scan
def index_scan_annotator(queryNode):
    scan_name = queryNode["Node Type"]

    # Get name of index attribute
    index_name = queryNode["Index Name"]

    # Get direction of index scan
    direction = "" if "Scan Direction" not in queryNode else queryNode["Scan Direction"] + " "

    # Get name of relation
    relation_name = queryNode["Relation Name"]

    # Get scan conditions if any
    filter_message = "" if "Filter" not in queryNode else "on condition " + queryNode["Filter"]

    # Build annotation string
    annotation = "{}{} using {} on table {} {}".format(direction, scan_name, index_name, relation_name, filter_message)

    return annotation

# Function to annotate Bitmap Scan (includes Bitmap Heap Scan, Bitmap Index Scan, BitmapAnd, BitmapOr)
def bitmap_scan_annotator(queryNode):
    scan_name = queryNode["Node Type"]

    # If Node Type is Bitmap Heap Scan
    if "Heap" in scan_name:
        # Get name of relation
        relation_name = queryNode["Relation Name"]

        # Get recheck condition if any
        recheck_condition = "" if "Recheck Cond" not in queryNode else "with recheck condition " + queryNode["Recheck Cond"]

        # Build annotation string
        annotation = "{} on table {} {}".format(scan_name, relation_name, recheck_condition)

        return annotation
    
    # If Node Type is Bitmap Index Scan
    elif "Index" in scan_name:
        # Get name of index attribute
        index_name = queryNode["Index Name"]

        # Get index condition if any
        index_condition = "" if "Index Cond" not in queryNode else "with index condition " + queryNode["Index Cond"]

        # Build annotation string
        annotation = "{} on table {} {}".format(scan_name, index_name, index_condition)

        return annotation
    
    # If Node Type is BitmapAnd or BitmapOr

# Function to annotate Value Scan
def value_scan_annotator(queryNode):
    scan_name = queryNode["Node Type"]

    # Get names of values that were scanned on
    values_name = "on values " + queryNode["Alias"]

    # Build annotation string
    annotation = "{} {}".format(scan_name, values_name)

    return annotation

# Function to annotate Cte Scan
def cte_scan_annotator(queryNode):
    name = "CTE Scan"

    # Get names of relation
    relation_name = queryNode["Alias"]

    # Build annotation string
    annotation = "{} on temporary table {}".format(name, relation_name)

    return annotation

# Function to annotate Function Scan
def function_scan_annotator(queryNode):
    name = "Function Scan"

    # Get name of function
    function_name = queryNode["Function Name"]

    # Build annotation string
    annotation = "{} on function {}".format(name, function_name)

    return annotation

# Function to annotate Subquery Scan
def subquery_scan_annotator(queryNode):
    name = "Subquery Scan"

    # Get name of subquery if any
    subquery_name = "" if "Alias" not in queryNode else "on the subquery '{}'".format(queryNode["Alias"])

    # Get name of filter if any
    filter_cond = "" if "Filter" not in queryNode else "with the filter ".format(queryNode["Filter"])

    # Build annotation string
    annotation = "{} {} {}".format(name, subquery_name, filter_cond)

    return annotation

# Function to annotate Hash
def hash_annotator(queryNode):
    name = "Hash"
    
    # Get name of relation if any
    relation_name = "" if "Relation Name" not in queryNode["Plans"][0] else "on table {}".format(queryNode["Plans"][0]["Relation Name"])

    # Get hash condition if any
    condition = "" if "Hash Cond" not in queryNode else "on condition " + queryNode["Hash Cond"]

    # Build annotation string
    annotation = "{} {} {}".format(name, relation_name, condition)

    return annotation

# Function to annotate Sort
def sort_annotator(queryNode):
    name = "Sort"

    # Get name of keys sorted on
    sort_keys = queryNode["Sort Key"]

    # Separate keys by commas
    sort_key_annotation = ""
    for i in range(len(sort_keys)):
        if i > 0:
            sort_key_annotation += ", "
        sort_key_annotation += sort_keys[i]
    
    # Build annotation string
    annotation = "{} based on {}".format(name, sort_key_annotation)

    return annotation

# Function to annotate Append
def append_annotator():
    return "Append operation"

# Function to annotate Aggregate
def aggregate_annotator(queryNode):
    name = "Aggregate"

    # Get aggregate condition 
    if "Group Key" in queryNode:
        aggregate_cond = "based on the attributes "
        for i, group_key in enumerate(queryNode["Group Key"]):
            if i > 0:
                aggregate_cond += ", "
            aggregate_cond += group_key
                
    # Get outputs
    if "Output" in queryNode:
        output_annotation = "to output the columns "
        for i, output in enumerate(queryNode["Output"]):
            if i > 0:
                output_annotation += ", "
            output_annotation += output

    # Build annotation string
    annotation = "{} {} {}".format(name, aggregate_cond, output_annotation)

    return annotation

# Function to annotate Materialize
def materialize_annotator():
    return "Materialize output into memory"

# Function to annotate Unique
def unique_annotator():
    return "Remove duplicate values"

# Function to annotate Limit
def limit_annotator(queryNode):
    num_rows = queryNode["Plan Rows"]

    # Build annotation string
    annotation = "Limit the result to the top {} rows".format(num_rows)

    return annotation

# Function to annotate Result
def result_annotator(queryNode):
    num_rows = queryNode["Plan Rows"]

    # Build annotation string
    annotation = "{} number of row(s) are obtained as the result".format(num_rows)

    return annotation

# Function to annotate Gather or Gather Merge
def gather_annotator(queryNode):
    name = queryNode["Node Type"]

    # Build annotation string
    annotation = "{} on the output".format(name)

    return annotation