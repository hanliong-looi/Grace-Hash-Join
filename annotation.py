class queryAnnotator:
    def __init__(self):
        self.queryMapper = {}
        self.queryOrder = []

    def traversePlan(self, queryPlan):
        # Create stack for DFS
        stack = []

        # Push root node of query plan onto stack
        stack.append(queryPlan["Plan"])

        while (len(stack) > 0):
            node = stack.pop()
            print(node)
            self.queryOrder.append(node)

            if "Plans" not in node:
                continue

            for plan in node["Plans"]:
                stack.append(plan)

    def annotateQuery(self):
        result = []
        for query in self.queryOrder:
            result.append(self.queryMapper[query["Node Type"]])
        return result
    
        
