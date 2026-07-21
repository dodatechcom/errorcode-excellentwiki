#!/usr/bin/env python3
"""Generate ClickHouse error pages to reach 100+ total."""
import os

BASE = '/home/admin1/projects/ErrorCode.excellentwiki.com/content/tools/clickhouse'
EXISTING = {f.replace('.md', '') for f in os.listdir(BASE) if f.endswith('.md')}

def make_page(slug, title, desc, body):
    return f'''---
title: "[Solution] {title}"
description: "{desc}"
tools: ["clickhouse"]
error-types: ["tool-error"]
severities: ["error"]
---

{body}
'''

PAGES = [
    ("clickhouse-grpc-error", "ClickHouse gRPC Error", "How to fix ClickHouse gRPC connection errors", "## Common Causes\n\n- gRPC port not enabled\n- Max message size exceeded\n- TLS mismatch on gRPC port\n\n## How to Fix\n\n```xml\n<grpc_port>9150</grpc_port>\n```\n\n## Examples\n\n```bash\ncurl -s http://localhost:8123/ping\n```"),
    ("clickhouse-insert-too-many-parts", "ClickHouse Insert Too Many Parts", "How to fix ClickHouse too many parts on insert", "## Common Causes\n\n- Batch inserts too small\n- Insert frequency too high\n- Merge falling behind\n\n## How to Fix\n\n```xml\n<merge_tree>\n  <max_delay_to_insert>10</max_delay_to_insert>\n</merge_tree>\n```\n\n## Examples\n\n```sql\nSELECT table, count() FROM system.parts GROUP BY table HAVING count() > 100;\n```"),
    ("clickhouse-drop-column-error", "ClickHouse Drop Column Error", "How to fix ClickHouse column drop errors", "## Common Causes\n\n- Column referenced in materialized view\n- Column in primary key\n- Lightweight delete conflicts\n\n## How to Fix\n\n```sql\nALTER TABLE mytable DROP COLUMN old_col;\n```\n\n## Examples\n\n```sql\nDESCRIBE TABLE mytable;\n```"),
    ("clickhouse-rename-column-error", "ClickHouse Rename Column Error", "How to fix ClickHouse column rename errors", "## Common Causes\n- Column referenced in view\n- Column in partition key\n- Replication conflict\n\n## How to Fix\n\n```sql\nALTER TABLE mytable RENAME COLUMN old_name TO new_name;\n```\n\n## Examples\n\n```sql\nDESCRIBE TABLE mytable;\n```"),
    ("clickhouse-optimize-error", "ClickHouse Optimize Error", "How to fix ClickHouse OPTIMIZE TABLE errors", "## Common Causes\n- Table locked by merge\n- OPTIMIZE on replicated table needs coordination\n- Too many parts to merge\n\n## How to Fix\n\n```sql\nOPTIMIZE TABLE mytable FINAL;\n```\n\n## Examples\n\n```sql\nSELECT table, count(), sum(rows) FROM system.parts WHERE active GROUP BY table;\n```"),
    ("clickhouse-mutation-error", "ClickHouse Mutation Error", "How to fix ClickHouse table mutation errors", "## Common Causes\n- Mutation already in progress\n- Table locked\n- Disk full during mutation\n\n## How to Fix\n\n```sql\nSELECT * FROM system.mutations WHERE is_done = 0;\nKILL MUTATION WHERE mutation_id = 'ID';\n```\n\n## Examples\n\n```sql\nALTER TABLE mytable DELETE WHERE date < today() - 30;\n```"),
    ("clickhouse-materialized-view-error", "ClickHouse Materialized View Error", "How to fix ClickHouse materialized view errors", "## Common Causes\n- Target table schema mismatch\n- View query syntax error\n- Insert into view not supported\n\n## How to Fix\n\n```sql\nCREATE MATERIALIZED VIEW myview TO target_table AS SELECT * FROM source_table;\n```\n\n## Examples\n\n```sql\nSELECT * FROM system.tables WHERE name = 'myview';\n```"),
    ("clickhouse-kafka-engine-error", "ClickHouse Kafka Engine Error", "How to fix ClickHouse Kafka engine errors", "## Common Causes\n- Kafka broker unreachable\n- Consumer group conflict\n- Schema registry error\n\n## How to Fix\n\n```sql\nCREATE TABLE kafka_table (id UInt64, message String)\nENGINE = Kafka\nSETTINGS kafka_broker_list = 'kafka:9092', kafka_topic_list = 'mytopic', kafka_group_name = 'mygroup', kafka_format = 'JSONEachRow';\n```\n\n## Examples\n\n```sql\nSELECT * FROM system.tables WHERE engine = 'Kafka';\n```"),
    ("clickhouse-s3-engine-error", "ClickHouse S3 Engine Error", "How to fix ClickHouse S3 engine errors", "## Common Causes\n- S3 credentials invalid\n- Bucket path wrong\n- Region mismatch\n\n## How to Fix\n\n```sql\nCREATE TABLE s3_table (id UInt64, name String)\nENGINE = S3('https://bucket.s3.amazonaws.com/data/*.csv', 'access_key', 'secret_key', 'CSV');\n```\n\n## Examples\n\n```sql\nSELECT * FROM s3_table LIMIT 5;\n```"),
    ("clickhouse-s3-source-error", "ClickHouse S3 Source Error", "How to fix ClickHouse S3 table function errors", "## Common Causes\n- File not found in S3\n- Wrong format specification\n- Access denied\n\n## How to Fix\n\n```sql\nSELECT * FROM s3('https://bucket.s3.amazonaws.com/data/*.csv', 'key', 'secret', 'CSV', 'id UInt64, name String');\n```\n\n## Examples\n\n```sql\nSELECT count() FROM s3('https://bucket.s3.amazonaws.com/data/*.csv', 'key', 'secret', 'CSV');\n```"),
    ("clickhouse-named-collection-error", "ClickHouse Named Collection Error", "How to fix ClickHouse named collection errors", "## Common Causes\n- Named collection not defined\n- Parameter missing in collection\n- Collection used in wrong context\n\n## How to Fix\n\n```xml\n<named_collections>\n  <my_s3>\n    <url>https://bucket.s3.amazonaws.com/</url>\n    <access_key>key</access_key>\n    <secret_key>secret</secret_key>\n  </my_s3>\n</named_collections>\n```\n\n## Examples\n\n```sql\nSELECT * FROM s3(my_s3, filename='data.csv', format='CSV');\n```"),
    ("clickhouse-projection-error", "ClickHouse Projection Error", "How to fix ClickHouse projection errors", "## Common Causes\n- Projection data out of sync\n- Projection select query wrong\n- Projection conflicting with deduplication\n\n## How to Fix\n\n```sql\nALTER TABLE mytable ADD PROJECTION myproj (SELECT * ORDER BY id);\nALTER TABLE mytable MATERIALIZE PROJECTION myproj;\n```\n\n## Examples\n\n```sql\nSELECT * FROM mytable WHERE _projection = 'myproj';\n```"),
    ("clickhouse-lightweight-delete-error", "ClickHouse Lightweight Delete Error", "How to fix ClickHouse lightweight delete errors", "## Common Causes\n- Lightweight delete not supported on old parts\n- DELETE too frequent creating too many parts\n- Merge not processing deletes\n\n## How to Fix\n\n```sql\nALTER TABLE mytable DELETE WHERE id = 123;\n```\n\n## Examples\n\n```sql\nSELECT _part, count() FROM mytable WHERE id = 123 GROUP BY _part;\n```"),
    ("clickhouse-replication-lag-error", "ClickHouse Replication Lag Error", "How to fix ClickHouse replication lag", "## Common Causes\n- ZooKeeper cluster unhealthy\n- Network partition between replicas\n- Large mutation causing lag\n\n## How to Fix\n\n```sql\nSELECT * FROM system.replicas;\n```\n\n## Examples\n\n```sql\nSELECT database, table, is_leader, queue_size, inserts_in_queue FROM system.replicas;\n```"),
    ("clickhouse-quorum-insert-error", "ClickHouse Quorum Insert Error", "How to fix ClickHouse quorum insert errors", "## Common Causes\n- Not enough replicas for quorum\n- Replica timed out waiting for quorum\n- Insert timeout too short\n\n## How to Fix\n\n```sql\nINSERT INTO mytable SETTINGS inserts_with_quorum_timeout = 60;\n```\n\n## Examples\n\n```sql\nSELECT * FROM system.replicas WHERE database = 'mydb';\n```"),
    ("clickhouse-async-insert-error", "ClickHouse Async Insert Error", "How to fix ClickHouse async insert errors", "## Common Causes\n- Async inserts buffer full\n- Wait timeout exceeded\n- Async insert not enabled\n\n## How to Fix\n\n```sql\nSET async_insert = 1, wait_for_async_insert = 1;\n```\n\n## Examples\n\n```sql\nSELECT * FROM system.asynchronous_inserts;\n```"),
    ("clickhouse-distributed-subquery-error", "ClickHouse Distributed Subquery Error", "How to fix ClickHouse distributed subquery errors", "## Common Causes\n- Subquery on distributed table causing scatter gather\n- Too many shards in subquery\n- Timeout on distributed subquery\n\n## How to Fix\n\n```xml\n<distributed_product_mode>global</distributed_product_mode>\n```\n\n## Examples\n\n```sql\nSELECT * FROM distributed_table WHERE id IN (SELECT id FROM local_table);\n```"),
    ("clickhouse-table-readonly", "ClickHouse Table Read Only Error", "How to fix ClickHouse table read only errors", "## Common Causes\n- Table marked readonly by ZooKeeper\n- Replica fallen too far behind\n- Disk space full on replica\n\n## How to Fix\n\n```sql\nSYSTEM RESTART REPLICA mytable;\n```\n\n## Examples\n\n```sql\nSELECT * FROM system.replicas WHERE is_readonly = 1;\n```"),
    ("clickhouse-user-not-found", "ClickHouse User Not Found", "How to fix ClickHouse user not found errors", "## Common Causes\n- User not created\n- User created in wrong profile\n- Authentication method mismatch\n\n## How to Fix\n\n```sql\nCREATE USER myuser IDENTIFIED BY 'password';\nGRANT SELECT ON mydb.* TO myuser;\n```\n\n## Examples\n\n```sql\nSELECT * FROM system.users;\n```"),
    ("clickhouse-quota-error", "ClickHouse Quota Error", "How to fix ClickHouse quota exceeded errors", "## Common Causes\n- Query rate limit exceeded\n- Data transfer limit reached\n- Concurrent query limit hit\n\n## How to Fix\n\n```sql\nCREATE QUOTA myquota FOR INTERVAL 1 hour max queries = 100 max result_rows = 1000000;\nCREATE ROLE myrole QUOTA myquota;\n```\n\n## Examples\n\n```sql\nSELECT * FROM system.quotas;\n```"),
    ("clickhouse-table-function-error", "ClickHouse Table Function Error", "How to fix ClickHouse table function errors", "## Common Causes\n- Wrong function name\n- Missing required parameters\n- File not accessible\n\n## How to Fix\n\n```sql\nSELECT * FROM file('data.csv', 'CSV', 'id UInt64, name String');\n```\n\n## Examples\n\n```sql\nSELECT * FROM url('http://example.com/data.json', 'JSON', 'id UInt64');\n```"),
    ("clickhouse-view-not-found", "ClickHouse View Not Found", "How to fix ClickHouse view not found errors", "## Common Causes\n- View does not exist\n- View dropped\n- Wrong database prefix\n\n## How to Fix\n\n```sql\nSELECT name FROM system.tables WHERE engine = 'View';\n```\n\n## Examples\n\n```sql\nCREATE VIEW myview AS SELECT * FROM mytable WHERE status = 'active';\n```"),
    ("clickhouse-access-control-error", "ClickHouse Access Control Error", "How to fix ClickHouse access control errors", "## Common Causes\n- Role not granted to user\n- Permission revoked\n- Row-level security blocking\n\n## How to Fix\n\n```sql\nGRANT SELECT ON mydb.* TO myuser;\nSHOW GRANTS FOR myuser;\n```\n\n## Examples\n\n```sql\nSELECT * FROM system.grants WHERE user = 'myuser';\n```"),
    ("clickhouse-table-function-remote-error", "ClickHouse Remote Table Function Error", "How to fix ClickHouse remote() table function errors", "## Common Causes\n- Remote server unreachable\n- Wrong port in remote connection\n- Authentication failed on remote\n\n## How to Fix\n\n```sql\nSELECT * FROM remote('remote-host:9000', 'mydb.mytable', 'myuser', 'password');\n```\n\n## Examples\n\n```sql\nSELECT count() FROM remote('host1,host2,host3', 'mydb.mytable');\n```"),
]

count = 0
for slug, title, desc, body in PAGES:
    if slug in EXISTING:
        continue
    path = os.path.join(BASE, f'{slug}.md')
    with open(path, 'w') as f:
        f.write(make_page(slug, title, desc, body))
    count += 1

print(f'Generated {count} new ClickHouse pages (total: {len(EXISTING) + count})')
