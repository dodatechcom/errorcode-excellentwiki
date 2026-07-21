#!/usr/bin/env python3
"""Generate YugabyteDB error pages to reach 100+ total."""
import os

BASE = '/home/admin1/projects/ErrorCode.excellentwiki.com/content/tools/yugabyte'
EXISTING = {f.replace('.md', '') for f in os.listdir(BASE) if f.endswith('.md')}

def make_page(slug, title, desc, body):
    return f'''---
title: "[Solution] {title}"
description: "{desc}"
tools: ["yugabyte"]
error-types: ["tool-error"]
severities: ["error"]
---

{body}
'''

PAGES = [
    ("yugabyte-tablet-split-error", "YugabyteDB Tablet Split Error", "How to fix YugabyteDB tablet split errors", "## Common Causes\n\n- Tablet too large to split\n- Split during high write load\n- Tablet server not available\n\n## How to Fix\n\n```bash\nyb-admin list_tablets mydb mytable 0\n```\n\n## Examples\n\n```bash\nyb-admin master_leader_status\n```"),
    ("yugabyte-tserver-not-found", "YugabyteDB TServer Not Found", "How to fix YugabyteDB TServer not found errors", "## Common Causes\n\n- TServer not registered with master\n- TServer crashed and restarted\n- Network partition\n\n## How to Fix\n\n```bash\nyb-admin list_tablet_servers\n```\n\n## Examples\n\n```bash\nyb-admin master_leader_status\n```"),
    ("yugabyte-master-leader-error", "YugabyteDB Master Leader Error", "How to fix YugabyteDB master leader election errors", "## Common Causes\n\n- No master leader elected\n- Split-brain condition\n- Master quorum lost\n\n## How to Fix\n\n```bash\nyb-admin master_leader_status\n```\n\n## Examples\n\n```bash\nyb-admin list_masters\n```"),
    ("yugabyte-backup-error", "YugabyteDB Backup Error", "How to fix YugabyteDB backup errors", "## Common Causes\n\n- Backup storage not accessible\n- Backup path permissions wrong\n- Backup during schema change\n\n## How to Fix\n\n```bash\nyb-admin backup_snapshots start my_backup\n```\n\n## Examples\n\n```bash\nyb-admin list_snapshots\n```"),
    ("yugabyte-restore-error", "YugabyteDB Restore Error", "How to fix YugabyteDB restore errors", "## Common Causes\n- Snapshot not found\n- Target keyspace already exists\n- Restore path not writable\n\n## How to Fix\n\n```bash\nyb-admin restore_snapshots_start snapshot_id\n```\n\n## Examples\n\n```bash\nyb-admin list_snapshots\n```"),
    ("yugabyte-replication-error", "YugabyteDB Replication Error", "How to fix YugabyteDB replication errors", "## Common Causes\n- Tablet replica lag too high\n- Follower tablet not catching up\n- Network partition between zones\n\n## How to Fix\n\n```bash\nyb-admin list_tablets mydb mytable 0\n```\n\n## Examples\n\n```bash\nyb-admin table_statistics mydb mytable\n```"),
    ("yugabyte-ysql-error", "YugabyteDB YSQL Error", "How to fix YugabyteDB YSQL query errors", "## Common Causes\n- SQL syntax not supported\n- DDL not supported in YSQL\n- Transaction isolation level wrong\n\n## How to Fix\n\n```sql\nSELECT * FROM mytable WHERE id = 1;\n```\n\n## Examples\n\n```sql\nSELECT version();\n```"),
    ("yugabyte-ycql-error", "YugabyteDB YCQL Error", "How to fix YugabyteDB YCQL query errors", "## Common Causes\n- CQL query syntax error\n- Keyspace not found\n- Consistency level not met\n\n## How to Fix\n\n```bash\nycqlsh -e \"SELECT * FROM mykeyspace.mytable LIMIT 5\"\n```\n\n## Examples\n\n```bash\nycqlsh -e \"DESCRIBE KEYSPACES\"\n```"),
    ("yugabyte-connection-error", "YugabyteDB Connection Error", "How to fix YugabyteDB connection errors", "## Common Causes\n- TServer not listening on port\n- Load balancer not configured\n- Firewall blocking connection\n\n## How to Fix\n\n```bash\nyb-admin list_tablet_servers\n```\n\n## Examples\n\n```bash\npsql -h yugabyte-host -p 5433 -U yugabyte -d yugabyte\n```"),
    ("yugabyte-ddl-error", "YugabyteDB DDL Error", "How to fix YugabyteDB DDL errors", "## Common Causes\n- DDL blocked by concurrent transaction\n- Schema change timeout\n- Unsupported DDL in YSQL\n\n## How to Fix\n\n```sql\nSELECT * FROM pg_stat_activity WHERE wait_event_type = 'Lock';\n```\n\n## Examples\n\n```sql\nCREATE TABLE mytable (id INT PRIMARY KEY, name VARCHAR(100));\n```"),
    ("yugabyte-dml-error", "YugabyteDB DML Error", "How to fix YugabyteDB DML errors", "## Common Causes\n- Write conflict on unique key\n- Transaction too large\n- Write path failure\n\n## How to Fix\n\n```sql\nINSERT INTO mytable (id, name) VALUES (1, 'Alice') ON CONFLICT DO NOTHING;\n```\n\n## Examples\n\n```sql\nSELECT * FROM mytable WHERE id = 1;\n```"),
    ("yugabyte-transaction-error", "YugabyteDB Transaction Error", "How to fix YugabyteDB transaction errors", "## Common Causes\n- Transaction aborted due to conflict\n- Deadlock detected\n- Transaction timeout\n\n## How to Fix\n\n```sql\nBEGIN;\nSELECT * FROM mytable WHERE id = 1 FOR UPDATE;\nUPDATE mytable SET name = 'Bob' WHERE id = 1;\nCOMMIT;\n```\n\n## Examples\n\n```sql\nSHOW transaction_status;\n```"),
    ("yugabyte-gflag-error", "YugabyteDB GFlag Error", "How to fix YugabyteDB gflag configuration errors", "## Common Causes\n- GFlag not recognized\n- GFlag value out of range\n- GFlag requires restart\n\n## How to Fix\n\n```bash\nyb-tserver --flagfile=/etc/yugabyte/tserver.conf\n```\n\n## Examples\n\n```bash\ncat /etc/yugabyte/tserver.conf | grep -v '^#'\n```"),
    ("yugabyte-placement-error", "YugabyteDB Placement Error", "How to fix YugabyteDB placement and zone errors", "## Common Causes\n- Tablet not placed in expected zone\n- Cloud region mismatch\n- Replica placement policy violated\n\n## How to Fix\n\n```bash\nyb-admin modify_placement_info mydb placement_info=cloud1.datacenter1.rack1:1\n```\n\n## Examples\n\n```bash\nyb-admin get_placement_info mydb\n```"),
    ("yugabyte-ssl-error", "YugabyteDB SSL Error", "How to fix YugabyteDB SSL/TLS errors", "## Common Causes\n- Certificate not trusted\n- Certificate expired\n- SSL not enabled on server\n\n## How to Fix\n\n```bash\nyb-tserver --use_client_to_server_encryption=true\n```\n\n## Examples\n\n```bash\nopenssl s_client -connect yugabyte-host:5433\n```"),
    ("yugabyte-rpc-error", "YugabyteDB RPC Error", "How to fix YugabyteDB RPC errors", "## Common Causes\n- RPC connection refused\n- RPC timeout\n- gRPC message too large\n\n## How to Fix\n\n```bash\nyb-admin list_tablet_servers\n```\n\n## Examples\n\n```bash\ncurl -s http://yugabyte-host:9000/rpcz\n```"),
    ("yugabyte-master-error", "YugabyteDB Master Error", "How to fix YugabyteDB master server errors", "## Common Causes\n- Master not running\n- Master not joined to cluster\n- Master data directory corrupted\n\n## How to Fix\n\n```bash\nyb-admin list_masters\n```\n\n## Examples\n\n```bash\nyb-admin master_leader_status\n```"),
    ("yugabyte-tserver-error", "YugabyteDB TServer Error", "How to fix YugabyteDB tablet server errors", "## Common Causes\n- TServer not running\n- TServer disk full\n- TServer memory exhaustion\n\n## How to Fix\n\n```bash\nyb-admin list_tablet_servers\n```\n\n## Examples\n\n```bash\nyb-admin get_tablet_disk_usage\n```"),
    ("yugabyte-auto-split-error", "YugabyteDB Auto Split Error", "How to fix YugabyteDB automatic tablet splitting errors", "## Common Causes\n- Auto split not enabled\n- Split threshold too high\n- Tablet server out of resources\n\n## How to Fix\n\n```bash\nyb-tserver --automaticYSQL_schema_placement=true\n```\n\n## Examples\n\n```bash\nyb-admin list_tablets mydb mytable 0\n```"),
    ("yugabyte-split-error", "YugabyteDB Tablet Split Error", "How to fix YugabyteDB manual tablet split errors", "## Common Causes\n- Split key not in tablet range\n- Tablet too small to split\n- Concurrent split operations\n\n## How to Fix\n\n```bash\nyb-admin split_tablet mydb.mytable\n```\n\n## Examples\n\n```bash\nyb-admin list_tablets mydb mytable 0\n```"),
    ("yugabyte-tablet-error", "YugabyteDB Tablet Error", "How to fix YugabyteDB tablet errors", "## Common Causes\n- Tablet not running\n- Tablet leader election failed\n- Tablet data corruption\n\n## How to Fix\n\n```bash\nyb-admin list_tablets mydb mytable 0\n```\n\n## Examples\n\n```bash\nyb-admin get_tablet_disk_usage\n```"),
    ("yugabyte-lsm-error", "YugabyteDB LSM Error", "How to fix YugabyteDB LSM tree errors", "## Common Causes\n- LSM compaction falling behind\n- Too many SST files\n- Bloom filter too large\n\n## How to Fix\n\n```bash\nyb-admin dump_tablet_info tablet_id\n```\n\n## Examples\n\n```bash\nyb-admin get_tablet_disk_usage\n```"),
    ("yugabyte-upgrade-error", "YugabyteDB Upgrade Error", "How to fix YugabyteDB upgrade errors", "## Common Causes\n- Rolling upgrade stuck\n- Version mismatch between nodes\n- Schema incompatibility\n\n## How to Fix\n\n```bash\nyb-admin list_masters\n```\n\n## Examples\n\n```bash\nyb-admin master_leader_status\n```"),
    ("yugabyte-clock-error", "YugabyteDB Clock Error", "How to fix YugabyteDB clock skew errors", "## Common Causes\n- Clock skew between nodes too high\n- NTP not synchronized\n- Clock error exceeding threshold\n\n## How to Fix\n\n```bash\nntpq -p\n```\n\n## Examples\n\n```bash\nyb-admin master_leader_status\n```"),
    ("yugabyte-query-error", "YugabyteDB Query Error", "How to fix YugabyteDB query errors", "## Common Causes\n- Query planner choosing wrong plan\n- Missing statistics\n- Query timeout\n\n## How to Fix\n\n```sql\nEXPLAIN ANALYZE SELECT * FROM mytable WHERE id = 1;\n```\n\n## Examples\n\n```sql\nANALYZE mytable;\n```"),
    ("yugabyte-monitoring-error", "YugabyteDB Monitoring Error", "How to fix YugabyteDB monitoring errors", "## Common Causes\n- Metrics endpoint not accessible\n- Prometheus not scraping\n- Grafana dashboard not showing data\n\n## How to Fix\n\n```bash\ncurl http://yugabyte-host:9000/metrics\n```\n\n## Examples\n\n```bash\ncurl http://yugabyte-host:7000/metrics\n```"),
    ("yugabyte-federation-error", "YugabyteDB Federation Error", "How to fix YugabyteDB geo-federation errors", "## Common Causes\n- Federation cluster not connected\n- Region not in federation\n- Replication lag between regions\n\n## How to Fix\n\n```bash\nyb-admin list_tablets mydb mytable 0\n```\n\n## Examples\n\n```bash\nyb-admin get_placement_info mydb\n```"),
    ("yugabyte-dc-error", "YugabyteDB Data Center Error", "How to fix YugabyteDB data center configuration errors", "## Common Causes\n- DC not in placement policy\n- Network between DCs blocked\n- DC replication factor wrong\n\n## How to Fix\n\n```bash\nyb-admin modify_placement_info mydb placement_info=cloud1.dc1.rack1:1\n```\n\n## Examples\n\n```bash\nyb-admin get_placement_info mydb\n```"),
    ("yugabyte-shuffle-error", "YugabyteDB Shuffle Error", "How to fix YugabyteDB tablet shuffle errors", "## Common Causes\n- Tablet balance not achieved\n- Shuffle frequency too high\n- Tablet server overloaded\n\n## How to Fix\n\n```bash\nyb-admin list_tablets mydb mytable 0\n```\n\n## Examples\n\n```bash\nyb-admin get_tablet_disk_usage\n```"),
    ("yugabyte-dr-error", "YugabyteDB Disaster Recovery Error", "How to fix YugabyteDB disaster recovery errors", "## Common Causes\n- xCluster replication lag too high\n- Standby cluster not connected\n- Snapshot for DR failed\n\n## How to Fix\n\n```bash\nyb-admin list_xcluster_configs\n```\n\n## Examples\n\n```bash\nyb-admin get_xcluster_config config_name\n```"),
    ("yugabyte-xdc-error", "YugabyteDB XDC Replication Error", "How to fix YugabyteDB cross-datacenter replication errors", "## Common Causes\n- XDC replication not configured\n- Replication stream failed\n- Target cluster unreachable\n\n## How to Fix\n\n```bash\nyb-admin setup_xcluster replication_name source:target\n```\n\n## Examples\n\n```bash\nyb-admin list_xcluster_configs\n```"),
    ("yugabyte-ddl-error", "YugabyteDB DDL Transaction Error", "How to fix YugabyteDB DDL in transaction errors", "## Common Causes\n- DDL not supported in transaction block\n- DDL blocking other DDLs\n- DDL timeout\n\n## How to Fix\n\n```sql\nCREATE TABLE mytable (id INT PRIMARY KEY);\n```\n\n## Examples\n\n```sql\nSELECT * FROM pg_stat_activity WHERE wait_event_type = 'Lock';\n```"),
]

count = 0
for slug, title, desc, body in PAGES:
    if slug in EXISTING:
        continue
    path = os.path.join(BASE, f'{slug}.md')
    with open(path, 'w') as f:
        f.write(make_page(slug, title, desc, body))
    count += 1

print(f'Generated {count} new YugabyteDB pages (total: {len(EXISTING) + count})')
