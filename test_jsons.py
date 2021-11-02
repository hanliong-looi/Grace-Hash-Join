test1 = [
    {
      "Plan": {
        "Node Type": "Limit",
        "Startup Cost": 17024.84,
        "Total Cost": 17024.87,
        "Plan Rows": 10,
        "Plan Width": 133,
        "Actual Startup Time": 725.773,
        "Actual Total Time": 725.775,
        "Actual Rows": 10,
        "Actual Loops": 1,
        "Output": ["c.state", "cat.categoryname", "(sum(o.netamount))", "(sum(o.totalamount))"],
        "Shared Hit Blocks": 23,
        "Shared Read Blocks": 1392,
        "Shared Dirtied Blocks": 0,
        "Shared Written Blocks": 0,
        "Local Hit Blocks": 0,
        "Local Read Blocks": 0,
        "Local Dirtied Blocks": 0,
        "Local Written Blocks": 0,
        "Temp Read Blocks": 0,
        "Temp Written Blocks": 0,
        "I/O Read Time": 0.000,
        "I/O Write Time": 0.000,
        "Plans": [
          {
            "Node Type": "Sort",
            "Parent Relationship": "Outer",
            "Startup Cost": 17024.84,
            "Total Cost": 17026.88,
            "Plan Rows": 816,
            "Plan Width": 133,
            "Actual Startup Time": 725.771,
            "Actual Total Time": 725.772,
            "Actual Rows": 11,
            "Actual Loops": 1,
            "Output": ["c.state", "cat.categoryname", "(sum(o.netamount))", "(sum(o.totalamount))"],
            "Sort Key": ["c.state", "(sum(o.totalamount))"],
            "Sort Method": "top-N heapsort",
            "Sort Space Used": 25,
            "Sort Space Type": "Memory",
            "Shared Hit Blocks": 23,
            "Shared Read Blocks": 1392,
            "Shared Dirtied Blocks": 0,
            "Shared Written Blocks": 0,
            "Local Hit Blocks": 0,
            "Local Read Blocks": 0,
            "Local Dirtied Blocks": 0,
            "Local Written Blocks": 0,
            "Temp Read Blocks": 0,
            "Temp Written Blocks": 0,
            "I/O Read Time": 0.000,
            "I/O Write Time": 0.000,
            "Plans": [
              {
                "Node Type": "Aggregate",
                "Strategy": "Hashed",
                "Parent Relationship": "Outer",
                "Startup Cost": 16994.41,
                "Total Cost": 17006.65,
                "Plan Rows": 816,
                "Plan Width": 133,
                "Actual Startup Time": 723.877,
                "Actual Total Time": 724.417,
                "Actual Rows": 832,
                "Actual Loops": 1,
                "Output": ["c.state", "cat.categoryname", "sum(o.netamount)", "sum(o.totalamount)"],
                "Group Key": ["c.state", "cat.categoryname"],
                "Shared Hit Blocks": 13,
                "Shared Read Blocks": 1392,
                "Shared Dirtied Blocks": 0,
                "Shared Written Blocks": 0,
                "Local Hit Blocks": 0,
                "Local Read Blocks": 0,
                "Local Dirtied Blocks": 0,
                "Local Written Blocks": 0,
                "Temp Read Blocks": 0,
                "Temp Written Blocks": 0,
                "I/O Read Time": 0.000,
                "I/O Write Time": 0.000,
                "Plans": [
                  {
                    "Node Type": "Hash Join",
                    "Parent Relationship": "Outer",
                    "Join Type": "Inner",
                    "Startup Cost": 4966.48,
                    "Total Cost": 13742.65,
                    "Plan Rows": 325176,
                    "Plan Width": 133,
                    "Actual Startup Time": 118.314,
                    "Actual Total Time": 354.285,
                    "Actual Rows": 383270,
                    "Actual Loops": 1,
                    "Output": ["c.state", "o.netamount", "o.totalamount", "cat.categoryname"],
                    "Hash Cond": "(o.orderid = ch.orderid)",
                    "Shared Hit Blocks": 13,
                    "Shared Read Blocks": 1392,
                    "Shared Dirtied Blocks": 0,
                    "Shared Written Blocks": 0,
                    "Local Hit Blocks": 0,
                    "Local Read Blocks": 0,
                    "Local Dirtied Blocks": 0,
                    "Local Written Blocks": 0,
                    "Temp Read Blocks": 0,
                    "Temp Written Blocks": 0,
                    "I/O Read Time": 0.000,
                    "I/O Write Time": 0.000,
                    "Plans": [
                      {
                        "Node Type": "Hash Join",
                        "Parent Relationship": "Outer",
                        "Join Type": "Inner",
                        "Startup Cost": 834.86,
                        "Total Cost": 4539.11,
                        "Plan Rows": 60350,
                        "Plan Width": 138,
                        "Actual Startup Time": 22.651,
                        "Actual Total Time": 133.484,
                        "Actual Rows": 60350,
                        "Actual Loops": 1,
                        "Output": ["o.netamount", "o.totalamount", "o.orderid", "ol.orderid", "cat.categoryname"],
                        "Hash Cond": "(ol.orderid = o.orderid)",
                        "Shared Hit Blocks": 9,
                        "Shared Read Blocks": 581,
                        "Shared Dirtied Blocks": 0,
                        "Shared Written Blocks": 0,
                        "Local Hit Blocks": 0,
                        "Local Read Blocks": 0,
                        "Local Dirtied Blocks": 0,
                        "Local Written Blocks": 0,
                        "Temp Read Blocks": 0,
                        "Temp Written Blocks": 0,
                        "I/O Read Time": 0.000,
                        "I/O Write Time": 0.000,
                        "Plans": [
                          {
                            "Node Type": "Hash Join",
                            "Parent Relationship": "Outer",
                            "Join Type": "Inner",
                            "Startup Cost": 464.86,
                            "Total Cost": 2962.11,
                            "Plan Rows": 60350,
                            "Plan Width": 122,
                            "Actual Startup Time": 12.467,
                            "Actual Total Time": 85.647,
                            "Actual Rows": 60350,
                            "Actual Loops": 1,
                            "Output": ["ol.orderid", "cat.categoryname"],
                            "Hash Cond": "(ol.prod_id = p.prod_id)",
                            "Shared Hit Blocks": 4,
                            "Shared Read Blocks": 483,
                            "Shared Dirtied Blocks": 0,
                            "Shared Written Blocks": 0,
                            "Local Hit Blocks": 0,
                            "Local Read Blocks": 0,
                            "Local Dirtied Blocks": 0,
                            "Local Written Blocks": 0,
                            "Temp Read Blocks": 0,
                            "Temp Written Blocks": 0,
                            "I/O Read Time": 0.000,
                            "I/O Write Time": 0.000,
                            "Plans": [
                              {
                                "Node Type": "Seq Scan",
                                "Parent Relationship": "Outer",
                                "Relation Name": "orderlines",
                                "Schema": "public",
                                "Alias": "ol",
                                "Startup Cost": 0.00,
                                "Total Cost": 988.50,
                                "Plan Rows": 60350,
                                "Plan Width": 8,
                                "Actual Startup Time": 0.005,
                                "Actual Total Time": 14.054,
                                "Actual Rows": 60350,
                                "Actual Loops": 1,
                                "Output": ["ol.orderlineid", "ol.orderid", "ol.prod_id", "ol.quantity", "ol.orderdate"],
                                "Shared Hit Blocks": 2,
                                "Shared Read Blocks": 383,
                                "Shared Dirtied Blocks": 0,
                                "Shared Written Blocks": 0,
                                "Local Hit Blocks": 0,
                                "Local Read Blocks": 0,
                                "Local Dirtied Blocks": 0,
                                "Local Written Blocks": 0,
                                "Temp Read Blocks": 0,
                                "Temp Written Blocks": 0,
                                "I/O Read Time": 0.000,
                                "I/O Write Time": 0.000
                              },
                              {
                                "Node Type": "Hash",
                                "Parent Relationship": "Inner",
                                "Startup Cost": 339.86,
                                "Total Cost": 339.86,
                                "Plan Rows": 10000,
                                "Plan Width": 122,
                                "Actual Startup Time": 12.446,
                                "Actual Total Time": 12.446,
                                "Actual Rows": 10000,
                                "Actual Loops": 1,
                                "Output": ["p.prod_id", "cat.categoryname"],
                                "Hash Buckets": 1024,
                                "Hash Batches": 1,
                                "Original Hash Batches": 1,
                                "Peak Memory Usage": 425,
                                "Shared Hit Blocks": 2,
                                "Shared Read Blocks": 100,
                                "Shared Dirtied Blocks": 0,
                                "Shared Written Blocks": 0,
                                "Local Hit Blocks": 0,
                                "Local Read Blocks": 0,
                                "Local Dirtied Blocks": 0,
                                "Local Written Blocks": 0,
                                "Temp Read Blocks": 0,
                                "Temp Written Blocks": 0,
                                "I/O Read Time": 0.000,
                                "I/O Write Time": 0.000,
                                "Plans": [
                                  {
                                    "Node Type": "Hash Join",
                                    "Parent Relationship": "Outer",
                                    "Join Type": "Inner",
                                    "Startup Cost": 1.36,
                                    "Total Cost": 339.86,
                                    "Plan Rows": 10000,
                                    "Plan Width": 122,
                                    "Actual Startup Time": 0.283,
                                    "Actual Total Time": 9.015,
                                    "Actual Rows": 10000,
                                    "Actual Loops": 1,
                                    "Output": ["p.prod_id", "cat.categoryname"],
                                    "Hash Cond": "(p.category = cat.category)",
                                    "Shared Hit Blocks": 2,
                                    "Shared Read Blocks": 100,
                                    "Shared Dirtied Blocks": 0,
                                    "Shared Written Blocks": 0,
                                    "Local Hit Blocks": 0,
                                    "Local Read Blocks": 0,
                                    "Local Dirtied Blocks": 0,
                                    "Local Written Blocks": 0,
                                    "Temp Read Blocks": 0,
                                    "Temp Written Blocks": 0,
                                    "I/O Read Time": 0.000,
                                    "I/O Write Time": 0.000,
                                    "Plans": [
                                      {
                                        "Node Type": "Seq Scan",
                                        "Parent Relationship": "Outer",
                                        "Relation Name": "products",
                                        "Schema": "public",
                                        "Alias": "p",
                                        "Startup Cost": 0.00,
                                        "Total Cost": 201.00,
                                        "Plan Rows": 10000,
                                        "Plan Width": 8,
                                        "Actual Startup Time": 0.003,
                                        "Actual Total Time": 4.330,
                                        "Actual Rows": 10000,
                                        "Actual Loops": 1,
                                        "Output": ["p.prod_id", "p.category", "p.title", "p.actor", "p.price", "p.special", "p.common_prod_id"],
                                        "Shared Hit Blocks": 2,
                                        "Shared Read Blocks": 99,
                                        "Shared Dirtied Blocks": 0,
                                        "Shared Written Blocks": 0,
                                        "Local Hit Blocks": 0,
                                        "Local Read Blocks": 0,
                                        "Local Dirtied Blocks": 0,
                                        "Local Written Blocks": 0,
                                        "Temp Read Blocks": 0,
                                        "Temp Written Blocks": 0,
                                        "I/O Read Time": 0.000,
                                        "I/O Write Time": 0.000
                                      },
                                      {
                                        "Node Type": "Hash",
                                        "Parent Relationship": "Inner",
                                        "Startup Cost": 1.16,
                                        "Total Cost": 1.16,
                                        "Plan Rows": 16,
                                        "Plan Width": 122,
                                        "Actual Startup Time": 0.265,
                                        "Actual Total Time": 0.265,
                                        "Actual Rows": 16,
                                        "Actual Loops": 1,
                                        "Output": ["cat.categoryname", "cat.category"],
                                        "Hash Buckets": 1024,
                                        "Hash Batches": 1,
                                        "Original Hash Batches": 1,
                                        "Peak Memory Usage": 1,
                                        "Shared Hit Blocks": 0,
                                        "Shared Read Blocks": 1,
                                        "Shared Dirtied Blocks": 0,
                                        "Shared Written Blocks": 0,
                                        "Local Hit Blocks": 0,
                                        "Local Read Blocks": 0,
                                        "Local Dirtied Blocks": 0,
                                        "Local Written Blocks": 0,
                                        "Temp Read Blocks": 0,
                                        "Temp Written Blocks": 0,
                                        "I/O Read Time": 0.000,
                                        "I/O Write Time": 0.000,
                                        "Plans": [
                                          {
                                            "Node Type": "Seq Scan",
                                            "Parent Relationship": "Outer",
                                            "Relation Name": "categories",
                                            "Schema": "public",
                                            "Alias": "cat",
                                            "Startup Cost": 0.00,
                                            "Total Cost": 1.16,
                                            "Plan Rows": 16,
                                            "Plan Width": 122,
                                            "Actual Startup Time": 0.250,
                                            "Actual Total Time": 0.252,
                                            "Actual Rows": 16,
                                            "Actual Loops": 1,
                                            "Output": ["cat.categoryname", "cat.category"],
                                            "Shared Hit Blocks": 0,
                                            "Shared Read Blocks": 1,
                                            "Shared Dirtied Blocks": 0,
                                            "Shared Written Blocks": 0,
                                            "Local Hit Blocks": 0,
                                            "Local Read Blocks": 0,
                                            "Local Dirtied Blocks": 0,
                                            "Local Written Blocks": 0,
                                            "Temp Read Blocks": 0,
                                            "Temp Written Blocks": 0,
                                            "I/O Read Time": 0.000,
                                            "I/O Write Time": 0.000
                                          }
                                        ]
                                      }
                                    ]
                                  }
                                ]
                              }
                            ]
                          },
                          {
                            "Node Type": "Hash",
                            "Parent Relationship": "Inner",
                            "Startup Cost": 220.00,
                            "Total Cost": 220.00,
                            "Plan Rows": 12000,
                            "Plan Width": 16,
                            "Actual Startup Time": 10.159,
                            "Actual Total Time": 10.159,
                            "Actual Rows": 12000,
                            "Actual Loops": 1,
                            "Output": ["o.netamount", "o.totalamount", "o.orderid"],
                            "Hash Buckets": 2048,
                            "Hash Batches": 1,
                            "Original Hash Batches": 1,
                            "Peak Memory Usage": 609,
                            "Shared Hit Blocks": 2,
                            "Shared Read Blocks": 98,
                            "Shared Dirtied Blocks": 0,
                            "Shared Written Blocks": 0,
                            "Local Hit Blocks": 0,
                            "Local Read Blocks": 0,
                            "Local Dirtied Blocks": 0,
                            "Local Written Blocks": 0,
                            "Temp Read Blocks": 0,
                            "Temp Written Blocks": 0,
                            "I/O Read Time": 0.000,
                            "I/O Write Time": 0.000,
                            "Plans": [
                              {
                                "Node Type": "Seq Scan",
                                "Parent Relationship": "Outer",
                                "Relation Name": "orders",
                                "Schema": "public",
                                "Alias": "o",
                                "Startup Cost": 0.00,
                                "Total Cost": 220.00,
                                "Plan Rows": 12000,
                                "Plan Width": 16,
                                "Actual Startup Time": 0.008,
                                "Actual Total Time": 5.548,
                                "Actual Rows": 12000,
                                "Actual Loops": 1,
                                "Output": ["o.netamount", "o.totalamount", "o.orderid"],
                                "Shared Hit Blocks": 2,
                                "Shared Read Blocks": 98,
                                "Shared Dirtied Blocks": 0,
                                "Shared Written Blocks": 0,
                                "Local Hit Blocks": 0,
                                "Local Read Blocks": 0,
                                "Local Dirtied Blocks": 0,
                                "Local Written Blocks": 0,
                                "Temp Read Blocks": 0,
                                "Temp Written Blocks": 0,
                                "I/O Read Time": 0.000,
                                "I/O Write Time": 0.000
                              }
                            ]
                          }
                        ]
                      },
                      {
                        "Node Type": "Hash",
                        "Parent Relationship": "Inner",
                        "Startup Cost": 3377.25,
                        "Total Cost": 3377.25,
                        "Plan Rows": 60350,
                        "Plan Width": 7,
                        "Actual Startup Time": 95.610,
                        "Actual Total Time": 95.610,
                        "Actual Rows": 60350,
                        "Actual Loops": 1,
                        "Output": ["c.state", "ch.orderid"],
                        "Hash Buckets": 8192,
                        "Hash Batches": 1,
                        "Original Hash Batches": 1,
                        "Peak Memory Usage": 2239,
                        "Shared Hit Blocks": 4,
                        "Shared Read Blocks": 811,
                        "Shared Dirtied Blocks": 0,
                        "Shared Written Blocks": 0,
                        "Local Hit Blocks": 0,
                        "Local Read Blocks": 0,
                        "Local Dirtied Blocks": 0,
                        "Local Written Blocks": 0,
                        "Temp Read Blocks": 0,
                        "Temp Written Blocks": 0,
                        "I/O Read Time": 0.000,
                        "I/O Write Time": 0.000,
                        "Plans": [
                          {
                            "Node Type": "Hash Join",
                            "Parent Relationship": "Outer",
                            "Join Type": "Inner",
                            "Startup Cost": 938.00,
                            "Total Cost": 3377.25,
                            "Plan Rows": 60350,
                            "Plan Width": 7,
                            "Actual Startup Time": 24.115,
                            "Actual Total Time": 74.639,
                            "Actual Rows": 60350,
                            "Actual Loops": 1,
                            "Output": ["c.state", "ch.orderid"],
                            "Hash Cond": "(ch.customerid = c.customerid)",
                            "Shared Hit Blocks": 4,
                            "Shared Read Blocks": 811,
                            "Shared Dirtied Blocks": 0,
                            "Shared Written Blocks": 0,
                            "Local Hit Blocks": 0,
                            "Local Read Blocks": 0,
                            "Local Dirtied Blocks": 0,
                            "Local Written Blocks": 0,
                            "Temp Read Blocks": 0,
                            "Temp Written Blocks": 0,
                            "I/O Read Time": 0.000,
                            "I/O Write Time": 0.000,
                            "Plans": [
                              {
                                "Node Type": "Seq Scan",
                                "Parent Relationship": "Outer",
                                "Relation Name": "cust_hist",
                                "Schema": "public",
                                "Alias": "ch",
                                "Startup Cost": 0.00,
                                "Total Cost": 930.50,
                                "Plan Rows": 60350,
                                "Plan Width": 8,
                                "Actual Startup Time": 0.294,
                                "Actual Total Time": 11.812,
                                "Actual Rows": 60350,
                                "Actual Loops": 1,
                                "Output": ["ch.customerid", "ch.orderid", "ch.prod_id"],
                                "Shared Hit Blocks": 2,
                                "Shared Read Blocks": 325,
                                "Shared Dirtied Blocks": 0,
                                "Shared Written Blocks": 0,
                                "Local Hit Blocks": 0,
                                "Local Read Blocks": 0,
                                "Local Dirtied Blocks": 0,
                                "Local Written Blocks": 0,
                                "Temp Read Blocks": 0,
                                "Temp Written Blocks": 0,
                                "I/O Read Time": 0.000,
                                "I/O Write Time": 0.000
                              },
                              {
                                "Node Type": "Hash",
                                "Parent Relationship": "Inner",
                                "Startup Cost": 688.00,
                                "Total Cost": 688.00,
                                "Plan Rows": 20000,
                                "Plan Width": 7,
                                "Actual Startup Time": 23.786,
                                "Actual Total Time": 23.786,
                                "Actual Rows": 20000,
                                "Actual Loops": 1,
                                "Output": ["c.state", "c.customerid"],
                                "Hash Buckets": 2048,
                                "Hash Batches": 1,
                                "Original Hash Batches": 1,
                                "Peak Memory Usage": 743,
                                "Shared Hit Blocks": 2,
                                "Shared Read Blocks": 486,
                                "Shared Dirtied Blocks": 0,
                                "Shared Written Blocks": 0,
                                "Local Hit Blocks": 0,
                                "Local Read Blocks": 0,
                                "Local Dirtied Blocks": 0,
                                "Local Written Blocks": 0,
                                "Temp Read Blocks": 0,
                                "Temp Written Blocks": 0,
                                "I/O Read Time": 0.000,
                                "I/O Write Time": 0.000,
                                "Plans": [
                                  {
                                    "Node Type": "Seq Scan",
                                    "Parent Relationship": "Outer",
                                    "Relation Name": "customers",
                                    "Schema": "public",
                                    "Alias": "c",
                                    "Startup Cost": 0.00,
                                    "Total Cost": 688.00,
                                    "Plan Rows": 20000,
                                    "Plan Width": 7,
                                    "Actual Startup Time": 0.005,
                                    "Actual Total Time": 16.771,
                                    "Actual Rows": 20000,
                                    "Actual Loops": 1,
                                    "Output": ["c.state", "c.customerid"],
                                    "Shared Hit Blocks": 2,
                                    "Shared Read Blocks": 486,
                                    "Shared Dirtied Blocks": 0,
                                    "Shared Written Blocks": 0,
                                    "Local Hit Blocks": 0,
                                    "Local Read Blocks": 0,
                                    "Local Dirtied Blocks": 0,
                                    "Local Written Blocks": 0,
                                    "Temp Read Blocks": 0,
                                    "Temp Written Blocks": 0,
                                    "I/O Read Time": 0.000,
                                    "I/O Write Time": 0.000
                                  }
                                ]
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  }
                ]
              }
            ]
          }
        ]
      },
      "Planning Time": 26.171,
      "Triggers": [
      ],
      "Execution Time": 726.800
    }
]

test2 = [
  {
    "Plan": {
      "Startup Cost": 1131.94,
      "Plans": [
        {
          "Startup Cost": 6.67,
          "Plans": [
            {
              "Startup Cost": 0,
              "Plan Width": 0,
              "Node Type": "Bitmap Index Scan",
              "Index Cond": "(author_id < 50)",
              "Plan Rows": 288,
              "Parallel Aware": False,
              "Parent Relationship": "Outer",
              "Total Cost": 6.59,
              "Index Name": "index_name"
            }
          ],
          "Node Type": "Bitmap Heap Scan",
          "Plan Rows": 288,
          "Relation Name": "authored",
          "Alias": "authored",
          "Parallel Aware": False,
          "Recheck Cond": "(author_id < 50)",
          "Parent Relationship": "InitPlan",
          "Plan Width": 27,
          "Subplan Name": "CTE blah",
          "Total Cost": 1131.94
        }
      ],
      "CTE Name": "blah",
      "Node Type": "CTE Scan",
      "Plan Rows": 288,
      "Alias": "blah",
      "Parallel Aware": False,
      "Plan Width": 36,
      "Total Cost": 1137.7
    }
  }
]

test3 = [
  {
    "Plan": {
					"Startup Cost": 0.43,
					"Scan Direction": "Backward",
					"Plan Width": 4,
					"Node Type": "Index Only Scan",
					"Index Cond": "(author_id IS NOT NULL)",
					"Plan Rows": 13170350,
					"Relation Name": "authored",
					"Alias": "authored",
					"Parallel Aware": False,
					"Parent Relationship": "Outer",
					"Total Cost": 374937.56,
					"Index Name": "index_name"
    }
  }
]

test4 = [
  {
    "Plan": {
      "Partial Mode": "Simple",
      "Startup Cost": 308661.16,
      "Plans": [
        {
          "Filter": "((publication.year >= 2000) AND (publication.year <= 2017))",
          "Startup Cost": 0,
          "Plan Width": 8,
          "Node Type": "Seq Scan",
          "Plan Rows": 3279362,
          "Relation Name": "publication",
          "Alias": "publication",
          "Parallel Aware": False,
          "Output": [
            "type"
          ],
          "Parent Relationship": "Outer",
          "Total Cost": 292264.35,
          "Schema": "public"
        }
      ],
      "Node Type": "Aggregate",
      "Strategy": "Hashed",
      "Plan Rows": 7,
      "Parallel Aware": False,
      "Group Key": [
        "publication.type"
      ],
      "Output": [
        "type",
        "count(*)"
      ],
      "Plan Width": 16,
      "Total Cost": 308661.23
    }
  }
]

test5 = [
  {
    "Plan": {
      "Partial Mode": "Simple",
      "Startup Cost": 591845.11,
      "Plans": [
        {
          "Startup Cost": 591845.11,
          "Plans": [
            {
              "Hash Cond": "((publication.crossref)::text = (publication_1.key)::text)",
              "Startup Cost": 306890.2,
              "Plans": [
                {
                  "Startup Cost": 0,
                  "Plan Width": 16,
                  "Node Type": "Seq Scan",
                  "Plan Rows": 5849490,
                  "Relation Name": "publication",
                  "Alias": "publication",
                  "Parallel Aware": False,
                  "Output": [
                    "publication.crossref"
                  ],
                  "Parent Relationship": "Outer",
                  "Total Cost": 263016.9,
                  "Schema": "public"
                },
                {
                  "Startup Cost": 306888.08,
                  "Plans": [
                    {
                      "Filter": "(((publication_1.key)::text ~~ 'conf%'::text) AND (((publication_1.month)::text = '%July%'::text) OR ((publication_1.title)::text ~~ '%July%'::text)))",
                      "Startup Cost": 0,
                      "Plan Width": 77,
                      "Node Type": "Seq Scan",
                      "Plan Rows": 170,
                      "Relation Name": "publication",
                      "Alias": "publication_1",
                      "Parallel Aware": False,
                      "Output": [
                        "publication_1.title",
                        "publication_1.year",
                        "publication_1.key"
                      ],
                      "Parent Relationship": "Outer",
                      "Total Cost": 306888.08,
                      "Schema": "public"
                    }
                  ],
                  "Node Type": "Hash",
                  "Plan Rows": 170,
                  "Parallel Aware": False,
                  "Output": [
                    "publication_1.title",
                    "publication_1.year",
                    "publication_1.key"
                  ],
                  "Parent Relationship": "Inner",
                  "Plan Width": 77,
                  "Total Cost": 306888.08
                }
              ],
              "Node Type": "Hash Join",
              "Plan Rows": 61,
              "Join Type": "Inner",
              "Parallel Aware": False,
              "Output": [
                "publication_1.title",
                "publication_1.year"
              ],
              "Parent Relationship": "Outer",
              "Plan Width": 56,
              "Total Cost": 591843.3
            }
          ],
          "Sort Key": [
            "publication_1.title",
            "publication_1.year"
          ],
          "Node Type": "Sort",
          "Plan Rows": 61,
          "Parallel Aware": False,
          "Output": [
            "publication_1.title",
            "publication_1.year"
          ],
          "Parent Relationship": "Outer",
          "Plan Width": 56,
          "Total Cost": 591845.26
        }
      ],
      "Node Type": "Aggregate",
      "Strategy": "Sorted",
      "Filter": "(count(publication_1.title) > 200)",
      "Plan Rows": 61,
      "Parallel Aware": False,
      "Group Key": [
        "publication_1.title",
        "publication_1.year"
      ],
      "Output": [
        "publication_1.title",
        "publication_1.year"
      ],
      "Plan Width": 56,
      "Total Cost": 591846.33
    }
  }
]

test6 = [
  {
    "Plan": {
      "Startup Cost": 400064,
      "Plans": [
        {
          "Partial Mode": "Simple",
          "Startup Cost": 400063.44,
          "Plans": [
            {
              "Hash Cond": "(authored.author_id = person.person_id)",
              "Startup Cost": 8.46,
              "Plans": [
                {
                  "Startup Cost": 0,
                  "Plan Width": 27,
                  "Node Type": "Seq Scan",
                  "Plan Rows": 13170350,
                  "Relation Name": "authored",
                  "Alias": "authored",
                  "Parallel Aware": False,
                  "Output": [
                    "authored.author_id",
                    "authored.publication_key"
                  ],
                  "Parent Relationship": "Outer",
                  "Total Cost": 365480.5,
                  "Schema": "public"
                },
                {
                  "Startup Cost": 8.45,
                  "Plans": [
                    {
                      "Index Cond": "((person.name)::text = 'Manuel Wimmer'::text)",
                      "Startup Cost": 0.43,
                      "Scan Direction": "Forward",
                      "Plan Width": 4,
                      "Node Type": "Index Scan",
                      "Total Cost": 8.45,
                      "Plan Rows": 1,
                      "Relation Name": "person",
                      "Alias": "person",
                      "Parallel Aware": False,
                      "Output": [
                        "person.person_id"
                      ],
                      "Parent Relationship": "Outer",
                      "Schema": "public",
                      "Index Name": "index_query_4b"
                    }
                  ],
                  "Node Type": "Hash",
                  "Plan Rows": 1,
                  "Parallel Aware": False,
                  "Output": [
                    "person.person_id"
                  ],
                  "Parent Relationship": "Inner",
                  "Plan Width": 4,
                  "Total Cost": 8.45
                }
              ],
              "Node Type": "Hash Join",
              "Plan Rows": 170,
              "Join Type": "Semi",
              "Parallel Aware": False,
              "Output": [
                "authored.publication_key",
                "authored.publication_key"
              ],
              "Parent Relationship": "Outer",
              "Plan Width": 23,
              "Total Cost": 400063.02
            }
          ],
          "Group Key": [
            "(authored.publication_key)::text"
          ],
          "Node Type": "Aggregate",
          "Strategy": "Hashed",
          "Plan Rows": 170,
          "Parallel Aware": False,
          "Output": [
            "authored.publication_key"
          ],
          "Parent Relationship": "Outer",
          "Plan Width": 23,
          "Total Cost": 400065.14
        },
        {
          "Index Cond": "((publication.key)::text = (authored.publication_key)::text)",
          "Startup Cost": 0.56,
          "Scan Direction": "Forward",
          "Plan Width": 143,
          "Node Type": "Index Scan",
          "Total Cost": 0.86,
          "Plan Rows": 1,
          "Relation Name": "publication",
          "Alias": "publication",
          "Parallel Aware": False,
          "Filter": "(publication.year = 2015)",
          "Output": [
            "publication.type",
            "publication.key",
            "publication.title",
            "publication.booktitle",
            "publication.year",
            "publication.journal",
            "publication.month",
            "publication.crossref"
          ],
          "Parent Relationship": "Inner",
          "Schema": "public",
          "Index Name": "publication_pkey"
        }
      ],
      "Node Type": "Nested Loop",
      "Plan Rows": 8,
      "Join Type": "Inner",
      "Parallel Aware": False,
      "Output": [
        "publication.type",
        "publication.key",
        "publication.title",
        "publication.booktitle",
        "publication.year",
        "publication.journal",
        "publication.month",
        "publication.crossref"
      ],
      "Plan Width": 143,
      "Total Cost": 400212.92
    }
  }
]