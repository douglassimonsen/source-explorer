TODO:
1. create a dependency tree for Redshift table, views, materialized views.
2. Fix up the powerbi parser to work, returning Redshift sources
4. Allow one to input two reports, choose metrics and return the queries + trees that generate them
5. Offer ability to convert PowerBI queries to actual views
6. Use psycopg2 transactions to identify transform steps in Python
7. Look for other ways to identify Python transforms. Maybe allow manual verification of Python stuff?
8. Parse connection info in PowerBI to identify appropriate DB
9. Add view definition and top 5 rows for each table/view. Allow copying a "select * from <view> limit 100"
10. Save all results in a SQLite DB so it doesn't need to always touch prod