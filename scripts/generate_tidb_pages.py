#!/usr/bin/env python3
"""Generate TiDB error pages to reach 100+ total."""
import os

BASE = '/home/admin1/projects/ErrorCode.excellentwiki.com/content/tools/tidb'
EXISTING = {f.replace('.md', '') for f in os.listdir(BASE) if f.endswith('.md')}

def make_page(slug, title, desc, body):
    return f'''---
title: "[Solution] {title}"
description: "{desc}"
tools: ["tidb"]
error-types: ["tool-error"]
severities: ["error"]
---

{body}
'''

PAGES = [
    ("tidb-region-error", "TiDB Region Error", "How to fix TiDB region errors", "## Common Causes\n\n- Region not available\n- Region leader election failed\n- Region size too large\n\n## How to Fix\n\n```sql\nSHOW TABLE t1 REGIONS;\n```\n\n## Examples\n\n```sql\nSHOW TABLE t1 INDEX idx_name REGIONS;\n```"),
    ("tidb-tikv-error", "TiKV Store Error", "How to fix TiKV store errors", "## Common Causes\n- TiKV store down\n- Store disk full\n- Raft group not healthy\n\n## How to Fix\n\n```bash\ntiup ctl pd-ctl store 1\n```\n\n## Examples\n\n```bash\ntiup ctl pd-ctl stores\n```"),
    ("tidb-pd-error", "TiDB Placement Driver Error", "How to fix TiDB PD errors", "## Common Causes\n- PD cluster not healthy\n- PD leader not elected\n- PD schedule conflict\n\n## How to Fix\n\n```bash\ntiup ctl pd-ctl member\n```\n\n## Examples\n\n```bash\ntiup ctl pd-ctl cluster status\n```"),
    ("tidb-tso-error", "TiDB TSO Error", "How to fix TiDB Timestamp Oracle (TSO) errors", "## Common Causes\n- PD cannot allocate TSO\n- TSO too slow\n- Clock drift\n\n## How to Fix\n\n```sql\nSHOW VARIABLES LIKE 'tidb_current_ts';\n```\n\n## Examples\n\n```bash\ntiup ctl pd-ctl tso 1\n```"),
    ("tidb-gc-error", "TiDB GC Error", "How to fix TiDB garbage collection errors", "## Common Causes\n- GC stuck\n- GC lifetime too long\n- GC not cleaning old data\n\n## How to Fix\n\n```sql\nSHOW VARIABLES LIKE 'tidb_gc_life_time';\nSET GLOBAL tidb_gc_life_time = '10m';\n```\n\n## Examples\n\n```sql\nSELECT * FROM mysql.tidb WHERE variable_name = 'tikv_gc_last_run_time';\n```"),
    ("tidb-lock-error", "TiDB Lock Error", "How to fix TiDB pessimistic and optimistic lock errors", "## Common Causes\n- Lock conflict detected\n- Lock wait timeout\n- Deadlock detected\n\n## How to Fix\n\n```sql\nSHOW VARIABLES LIKE 'innodb_lock_wait_timeout';\n```\n\n## Examples\n\n```sql\nSELECT * FROM information_schema.innodb_trx;\n```"),
    ("tidb-ddl-error", "TiDB DDL Error", "How to fix TiDB DDL errors", "## Common Causes\n- DDL job queue full\n- DDL timeout\n- DDL not supported in TiDB\n\n## How to Fix\n\n```sql\nSHOW DDL JOBS;\n```\n\n## Examples\n\n```sql\nADMIN CANCEL DDL JOBS 1;\n```"),
    ("tidb-dml-error", "TiDB DML Error", "How to fix TiDB DML errors", "## Common Causes\n- Data too large for row\n- Auto-increment conflict\n- Unique constraint violation\n\n## How to Fix\n\n```sql\nSHOW WARNINGS;\n```\n\n## Examples\n\n```sql\nSHOW VARIABLES LIKE 'tidb_auto_random_base';\n```"),
    ("tidb-oom-error", "TiDB Out of Memory Error", "How to fix TiDB OOM errors", "## Common Causes\n- Query using too much memory\n- Distinct result too large\n- Join producing cartesian product\n\n## How to Fix\n\n```sql\nSET GLOBAL tidb_mem_quota_query = 1073741824;\n```\n\n## Examples\n\n```sql\nSHOW VARIABLES LIKE 'tidb_mem_quota_query';\n```"),
    ("tidb-transaction-error", "TiDB Transaction Error", "How to fix TiDB transaction errors", "## Common Causes\n- Transaction too large\n- Transaction commit timeout\n- Transaction conflicts\n\n## How to Fix\n\n```sql\nSET tidb_txn_mode = 'pessimistic';\n```\n\n## Examples\n\n```sql\nSHOW VARIABLES LIKE 'tidb_txn_mode';\n```"),
    ("tidb-auth-error", "TiDB Authentication Error", "How to fix TiDB authentication errors", "## Common Causes\n- Wrong password\n- User not found\n- SSL required\n\n## How to Fix\n\n```sql\nCREATE USER 'myuser'@'%' IDENTIFIED BY 'password';\nGRANT ALL ON *.* TO 'myuser'@'%';\n```\n\n## Examples\n\n```sql\nSELECT user, host FROM mysql.user;\n```"),
    ("tidb-backup-error", "TiDB Backup Error", "How to fix TiDB BR backup errors", "## Common Causes\n- Backup storage not accessible\n- Backup timeout\n- Concurrent backup conflicts\n\n## How to Fix\n\n```bash\nbr backup full --pd pd-host:2379 --storage s3://bucket/path\n```\n\n## Examples\n\n```bash\nbr backup full --pd pd-host:2379 --storage local:///backup\n```"),
    ("tidb-br-error", "TiDB BR Restore Error", "How to fix TiDB BR restore errors", "## Common Causes\n- Backup version incompatible\n- Target cluster not empty\n- Storage format wrong\n\n## How to Fix\n\n```bash\nbr restore full --pd pd-host:2379 --storage s3://bucket/path\n```\n\n## Examples\n\n```bash\nbr restore full --pd pd-host:2379 --storage local:///backup\n```"),
    ("tidb-import-error", "TiDB Import Error", "How to fix TiDB Lightning import errors", "## Common Causes\n- Source file not accessible\n- Schema not created\n- Import timeout\n\n## How to Fix\n\n```bash\ntiup tidb-lightning --config tidb-lightning.toml\n```\n\n## Examples\n\n```bash\ntiup tidb-lightning --checkpoint-error-destroy=all\n```"),
    ("tidb-cdc-error", "TiDB CDC Error", "How to fix TiDB CDC (Change Data Capture) errors", "## Common Causes\n- CDC changefeed failed\n- Sink unreachable\n- Checkpoint lag too high\n\n## How to Fix\n\n```bash\ntiup ctl pd-ctl changefeed list\n```\n\n## Examples\n\n```bash\ntiup ctl pd-ctl changefeed query changefeed-id\n```"),
    ("tidb-split-error", "TiDB Region Split Error", "How to fix TiDB region split errors", "## Common Causes\n- Region size exceeding threshold\n- Split merge conflict\n- Hot region not splitting\n\n## How to Fix\n\n```sql\nSPLIT TABLE t1 BETWEEN (0) AND (1000000) REGIONS 10;\n```\n\n## Examples\n\n```sql\nSHOW TABLE t1 REGIONS;\n```"),
    ("tidb-wait-error", "TiDB Wait Error", "How to fix TiDB wait and timeout errors", "## Common Causes\n- Lock wait timeout exceeded\n- Connection pool exhausted\n- Query waiting for PD TSO\n\n## How to Fix\n\n```sql\nSET tidb_lock_wait_timeout = 5000;\n```\n\n## Examples\n\n```sql\nSHOW VARIABLES LIKE 'tidb_lock_wait_timeout';\n```"),
    ("tidb-partition-error", "TiDB Partition Error", "How to fix TiDB table partition errors", "## Common Causes\n- Partition count exceeded limit\n- Partition pruning not working\n- Partition key type wrong\n\n## How to Fix\n\n```sql\nCREATE TABLE t1 (id INT) PARTITION BY RANGE (id) (\n  PARTITION p0 VALUES LESS THAN (100),\n  PARTITION p1 VALUES LESS THAN (200)\n);\n```\n\n## Examples\n\n```sql\nSHOW CREATE TABLE t1;\n```"),
    ("tidb-sequence-error", "TiDB Sequence Error", "How to fix TiDB sequence errors", "## Common Causes\n- Sequence exhausted\n- Sequence cache too small\n- Sequence type mismatch\n\n## How to Fix\n\n```sql\nCREATE SEQUENCE myseq START WITH 1 INCREMENT BY 1 CACHE 100;\n```\n\n## Examples\n\n```sql\nSELECT nextval(myseq);\n```"),
    ("tidb-placement-error", "TiDB Placement Policy Error", "How to fix TiDB placement rule errors", "## Common Causes\n- Placement policy not found\n- TiFlash replica not available\n- Label not matching placement rule\n\n## How to Fix\n\n```sql\nCREATE PLACEMENT POLICY my_policy PRIMARY_REGION=\"region1\" REGIONS=\"region1,region2\";\n```\n\n## Examples\n\n```sql\nSELECT * FROM mysql.placement_policies;\n```"),
    ("tidb-plan-replayer-error", "TiDB Plan Replayer Error", "How to fix TiDB plan replayer errors", "## Common Causes\n- Plan replayer dump failed\n- Plan file not accessible\n- Plan replayer analyze failed\n\n## How to Fix\n\n```sql\nPLAN REPLAYER DUMP EXPLAIN ANALYZE SELECT * FROM mytable WHERE id = 1;\n```\n\n## Examples\n\n```sql\nPLAN REPLAYER LOAD 'plan_file';\n```"),
    ("tidb-prepared-stmt-error", "TiDB Prepared Statement Error", "How to fix TiDB prepared statement errors", "## Common Causes\n- Prepared statement not found\n- Parameter count mismatch\n- Prepared statement limit exceeded\n\n## How to Fix\n\n```sql\nPREPARE stmt FROM 'SELECT * FROM mytable WHERE id = ?';\nSET @id = 1;\nEXECUTE stmt USING @id;\n```\n\n## Examples\n\n```sql\nSHOW VARIABLES LIKE 'tidb_max_prepared_stmt_count';\n```"),
    ("tidb-json-error", "TiDB JSON Error", "How to fix TiDB JSON function errors", "## Common Causes\n- JSON path syntax wrong\n- JSON value type mismatch\n- JSON document too large\n\n## How to Fix\n\n```sql\nSELECT JSON_EXTRACT('{\"a\": 1}', '$.a');\n```\n\n## Examples\n\n```sql\nSELECT JSON_VALID('{\"a\": 1}');\n```"),
    ("tidb-auto-random-error", "TiDB Auto Random Error", "How to fix TiDB auto_random errors", "## Common Causes\n- auto_random not enabled\n- Shard bits too many\n- auto_random conflict\n\n## How to Fix\n\n```sql\nCREATE TABLE t1 (id BIGINT AUTO_RANDOM PRIMARY KEY, name VARCHAR(100));\n```\n\n## Examples\n\n```sql\nSHOW CREATE TABLE t1;\n```"),
    ("tidb-slow-query-error", "TiDB Slow Query Error", "How to fix TiDB slow query errors", "## Common Causes\n- Query execution time exceeding threshold\n- Missing index causing full scan\n- Plan regression\n\n## How to Fix\n\n```sql\nSELECT query, exec_last_tm FROM information_schema.slow_query ORDER BY exec_last_tm DESC LIMIT 10;\n```\n\n## Examples\n\n```sql\nSELECT query, query_time FROM information_schema.slow_query WHERE query_time > 1;\n```"),
    ("tidb-statistics-error", "TiDB Statistics Error", "How to fix TiDB statistics errors", "## Common Causes\n- Statistics not collected\n- Statistics outdated\n- Histogram too large\n\n## How to Fix\n\n```sql\nANALYZE TABLE mytable;\n```\n\n## Examples\n\n```sql\nSHOW STATS_META WHERE table_name = 'mytable';\n```"),
    ("tidb-metrics-error", "TiDB Metrics Error", "How to fix TiDB monitoring metrics errors", "## Common Causes\n- Prometheus not scraping TiDB metrics\n- Grafana dashboard not showing data\n- Metrics endpoint not accessible\n\n## How to Fix\n\n```bash\ncurl http://tidb-host:10080/metrics\n```\n\n## Examples\n\n```bash\ncurl http://tikv-host:20180/metrics | head -20\n```"),
    ("tidb-connection-error", "TiDB Connection Error", "How to fix TiDB connection errors", "## Common Causes\n- TiDB not listening on port\n- Max connections reached\n- Client SSL mismatch\n\n## How to Fix\n\n```sql\nSHOW VARIABLES LIKE 'max_connections';\n```\n\n## Examples\n\n```sql\nSHOW PROCESSLIST;\n```"),
    ("tidb-restore-error", "TiDB BR Restore Error", "How to fix TiDB BR restore errors after backup", "## Common Causes\n- Backup data corrupted\n- Restore target cluster version mismatch\n- Storage path not accessible\n\n## How to Fix\n\n```bash\nbr restore full --pd pd-host:2379 --storage local:///backup\n```\n\n## Examples\n\n```bash\nbr restore full --pd pd-host:2379 --storage s3://bucket/path\n```"),
    ("tidb-tidb-node-error", "TiDB Server Node Error", "How to fix TiDB server node errors", "## Common Causes\n- TiDB server not running\n- TiDB server OOM\n- TiDB server disk full\n\n## How to Fix\n\n```bash\ncurl http://tidb-host:10080/status\n```\n\n## Examples\n\n```bash\ncurl http://tidb-host:10080/info\n```"),
    ("tidb-placement-rule-error", "TiDB Placement Rule Error", "How to fix TiDB PD placement rule errors", "## Common Causes\n- Placement rule not found in PD\n- Rule constraint not met\n- Rule priority conflict\n\n## How to Fix\n\n```bash\ntiup ctl pd-ctl placement-rules\n```\n\n## Examples\n\n```bash\ntiup ctl pd-ctl config show-rules\n```"),
    ("tidb-table-filter-error", "TiDB Lightning Table Filter Error", "How to fix TiDB Lightning table filter errors", "## Common Causes\n- Filter syntax wrong\n- Table not matching filter\n- Exclude filter too broad\n\n## How to Fix\n\n```toml\n[mydumper]\ndatasource-type = \"file\"\nfilter = [\"mydb.mytable\"]\n```\n\n## Examples\n\n```bash\ntiup tidb-lightning --filter='mydb.mytable'\n```"),
]

count = 0
for slug, title, desc, body in PAGES:
    if slug in EXISTING:
        continue
    path = os.path.join(BASE, f'{slug}.md')
    with open(path, 'w') as f:
        f.write(make_page(slug, title, desc, body))
    count += 1

print(f'Generated {count} new TiDB pages (total: {len(EXISTING) + count})')
