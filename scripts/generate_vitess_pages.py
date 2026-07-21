#!/usr/bin/env python3
"""Generate Vitess error pages to reach 100+ total."""
import os

BASE = '/home/admin1/projects/ErrorCode.excellentwiki.com/content/tools/vitess'
EXISTING = {f.replace('.md', '') for f in os.listdir(BASE) if f.endswith('.md')}

def make_page(slug, title, desc, body):
    return f'''---
title: "[Solution] {title}"
description: "{desc}"
tools: ["vitess"]
error-types: ["tool-error"]
severities: ["error"]
---

{body}
'''

PAGES = [
    ("vitess-resolve-error", "Vitess VSchema Resolve Error", "How to fix Vitess VSchema resolution errors", "## Common Causes\n\n- VSchema not applied to keyspace\n- Route target not found\n- Sharding key missing\n\n## How to Fix\n\n```bash\nvtctlclient ApplyVSchema -kspace_name myks -vschema_file vschema.json\n```\n\n## Examples\n\n```bash\nvtctlclient GetVSchema myks\n```"),
    ("vitess-tablet-health-error", "Vitess Tablet Health Error", "How to fix Vitess tablet health check errors", "## Common Causes\n\n- Tablet not responding to health checks\n- MySQL process down behind tablet\n- Replication lag too high\n\n## How to Fix\n\n```bash\nvtctlclient ListAllTablets\n```\n\n## Examples\n\n```bash\nvtctlclient GetTablet tablet-alias\n```"),
    ("vitess-transaction-retry-error", "Vitess Transaction Retry Error", "How to fix Vitess transaction retry errors", "## Common Causes\n\n- Transient transaction error\n- Deadlock detected\n- Shard-level conflict\n\n## How to Fix\n\n```bash\nmysql -h vtgate-host -P 15306 -u user -e \"SELECT 1\"\n```\n\n## Examples\n\n```bash\nvtctlclient ShardInfo myks 0\n```"),
    ("vitess-shard-key-error", "Vitess Shard Key Error", "How to fix Vitess shard key and routing errors", "## Common Causes\n\n- Shard key not in VSchema\n- Query missing shard key in WHERE\n- Cross-shard query not supported\n\n## How to Fix\n\n```json\n{\n  \"sharded\": true,\n  \"vindexes\": {\n    \"hash\": {\"type\": \"hash\"}\n  },\n  \"tables\": {\n    \"users\": {\"column_vindexes\": [{\"column\": \"id\", \"name\": \"hash\"}]}\n  }\n}\n```\n\n## Examples\n\n```bash\nvtctlclient VSchemaInfo myks\n```"),
    ("vitess-move-tables-error", "Vitess MoveTables Error", "How to fix Vitess MoveTables workflow errors", "## Common Causes\n\n- Source keyspace not sharded correctly\n- Target keyspace not available\n- Stream lag too high\n\n## How to Fix\n\n```bash\nvtctlclient MoveTables Create --source=unsharded_ks --tables=customer,order --target=sharded_ks\n```\n\n## Examples\n\n```bash\nvtctlclient MoveTables Status --target=sharded_ks\n```"),
    ("vitess-resharding-error", "Vitess Resharding Error", "How to fix Vitess resharding errors", "## Common Causes\n\n- Shard split/merge failing\n- VReplication stream error\n- Target shard not ready\n\n## How to Fix\n\n```bash\nvtctlclient Reshard --skip_start=false myks.0 myks.0-80,80-f0\n```\n\n## Examples\n\n```bash\nvtctlclient Reshard myks.0 myks.0-80,80-f0\n```"),
    ("vitess-vreplication-error", "Vitess VReplication Error", "How to fix Vitess VReplication stream errors", "## Common Causes\n\n- Source MySQL unreachable\n- Binlog position invalid\n- Filter expression error\n\n## How to Fix\n\n```bash\nvtctlclient VReplicationStatus --target=sharded_ks\n```\n\n## Examples\n\n```bash\nvtctlclient VReplicationList\n```"),
    ("vitess-vtgate-error", "Vitess VTGate Error", "How to fix Vitess VTGate connection errors", "## Common Causes\n\n- VTGate not running\n- Max connections reached\n- Routing rules missing\n\n## How to Fix\n\n```bash\nvtgate --port=15306 --mysql_server_port=15306 --log_dir=/var/log/vitess\n```\n\n## Examples\n\n```bash\ncurl http://localhost:15001/debug/status\n```"),
    ("vitess-vttablet-error", "Vitess VTTablet Error", "How to fix Vitess VTTablet errors", "## Common Causes\n\n- MySQL connection failed\n- Tablet role wrong (master vs replica)\n- Schema not loaded\n\n## How to Fix\n\n```bash\nvttablet --port=15100 --tablet_uid=100 --init_db_sql_file=init_db.sql\n```\n\n## Examples\n\n```bash\ncurl http://localhost:15100/debug/status\n```"),
    ("vitess-vtctld-error", "Vitess VTCTlD Error", "How to fix Vitess VTCTlD command errors", "## Common Causes\n\n- VTCTlD not connected to topology\n- TopoServer unreachable\n- Command syntax wrong\n\n## How to Fix\n\n```bash\nvtctldclient --server=localhost:15999 ListAllTablets\n```\n\n## Examples\n\n```bash\nvtctldclient --server=localhost:15999 GetKeyspaces\n```"),
    ("vitess-topo-error", "Vitess Topology Server Error", "How to fix Vitess topology server errors", "## Common Causes\n- TopoServer (etcd/ZooKeeper) unreachable\n- Topo data corrupted\n- Lock acquisition failed\n\n## How to Fix\n\n```bash\netcdctl get --prefix /vitess/\n```\n\n## Examples\n\n```bash\netcdctl get --prefix /vitess/myks/\n```"),
    ("vitess-lookup-vindex-error", "Vitess Lookup Vindex Error", "How to fix Vitess lookup vindex errors", "## Common Causes\n- Lookup table not created\n- Vindex column mismatch\n- Lookup write failing\n\n## How to Fix\n\n```json\n{\n  \"vindexes\": {\n    \"email_vdx\": {\"type\": \"consistent_lookup_unique\", \"params\": {\"table\": \"email_lookup\", \"from\": \"email\", \"to\": \"user_id\"}}\n  }\n}\n```\n\n## Examples\n\n```bash\nvtctlclient GetVSchema myks\n```"),
    ("vitess-charset-error", "Vitess Charset Error", "How to fix Vitess character set errors", "## Common Causes\n- Charset not supported by Vitess\n- Connection charset mismatch\n- Collation mismatch\n\n## How to Fix\n\n```bash\nmysql -h vtgate-host -P 15306 --default-character-set=utf8mb4\n```\n\n## Examples\n\n```bash\nmysql -h vtgate-host -P 15306 -e \"SHOW VARIABLES LIKE 'character_set%'\"\n```"),
    ("vitess-plan-error", "Vitess Query Plan Error", "How to fix Vitess query plan errors", "## Common Causes\n- Query not supported by Vitess planner\n- Cross-shard scatter gather\n- Subquery not supported\n\n## How to Fix\n\n```bash\nmysql -h vtgate-host -P 15306 -e \"EXPLAIN FORMAT=VITESS SELECT * FROM users WHERE id = 1\"\n```\n\n## Examples\n\n```bash\ncurl http://localhost:15001/debug/query_plans\n```"),
    ("vitess-grpc-error", "Vitess gRPC Error", "How to fix Vitess gRPC connection errors", "## Common Causes\n- gRPC port not enabled\n- TLS mismatch\n- Message size exceeded\n\n## How to Fix\n\n```bash\nvtgate --grpc_port=15999\n```\n\n## Examples\n\n```bash\ncurl -k https://localhost:15999/debug/status\n```"),
    ("vitess-gtid-error", "Vitess GTID Error", "How to fix Vitess GTID replication errors", "## Common Causes\n- GTID position out of sync\n- Master failover causing GTID gap\n- Replication not using GTID\n\n## How to Fix\n\n```sql\nSHOW MASTER STATUS;\nSHOW SLAVE STATUS\\G\n```\n\n## Examples\n\n```sql\nSELECT @@global.gtid_mode;\n```"),
    ("vitess-replication-error", "Vitess Replication Error", "How to fix Vitess replication errors", "## Common Causes\n- Replication stopped on replica\n- Network partition between master and replica\n- Binlog corrupted on replica\n\n## How to Fix\n\n```bash\nvtctlclient ReparentShard -force myks 0 master-tablet\n```\n\n## Examples\n\n```bash\nvtctlclient ListTablets\n```"),
    ("vitess-reparent-error", "Vitess Reparent Error", "How to fix Vitess reparent and master failover errors", "## Common Causes\n- Master tablet not responding\n- Semi-sync timeout\n- Ejected master still accepting writes\n\n## How to Fix\n\n```bash\nvtctlclient PlannedReparentShard myks 0\n```\n\n## Examples\n\n```bash\nvtctlclient EmergencyReparentShard myks 0\n```"),
    ("vitess-keyspace-error", "Vitess Keyspace Error", "How to fix Vitess keyspace errors", "## Common Causes\n- Keyspace not found\n- Keyspace not sharded correctly\n- ServedFrom misconfigured\n\n## How to Fix\n\n```bash\nvtctlclient CreateKeyspace myks\n```\n\n## Examples\n\n```bash\nvtctlclient GetKeyspaces\n```"),
    ("vitess-table-error", "Vitess Table Error", "How to fix Vitess table routing errors", "## Common Causes\n- Table not found in any keyspace\n- Routing rules table not configured\n- Target keyspace wrong\n\n## How to Fix\n\n```bash\nvtctlclient GetRoutingRules\n```\n\n## Examples\n\n```bash\nmysql -h vtgate-host -P 15306 -e \"SHOW VSCHEMA TABLES\"\n```"),
    ("vitess-restore-error", "Vitess Restore Error", "How to fix Vitess backup restore errors", "## Common Causes\n- Backup not found\n- Restore path wrong\n- Storage backend unreachable\n\n## How to Fix\n\n```bash\nvtctlclient RestoreFromBackup tablet-alias\n```\n\n## Examples\n\n```bash\nvtctlclient ListBackups myks 0\n```"),
    ("vitess-backup-error", "Vitess Backup Error", "How to fix Vitess backup errors", "## Common Causes\n- Backup storage not configured\n- Backup timeout\n- Too many concurrent backups\n\n## How to Fix\n\n```bash\nvtctlclient Backup tablet-alias\n```\n\n## Examples\n\n```bash\nvtctlclient ListBackups myks 0\n```"),
    ("vitess-stream-error", "Vitess VStream Error", "How to fix Vitess VStream streaming errors", "## Common Causes\n- Stream position invalid\n- Stream lag too high\n- Filter syntax wrong\n\n## How to Fix\n\n```bash\nvtctlclient VStream --keyspace_shard='myks/0' --start_pos='' --timeout=10s\n```\n\n## Examples\n\n```bash\ncurl http://localhost:15001/debug/vstream_events\n```"),
    ("vitess-schema-error", "Vitess Schema Error", "How to fix Vitess schema management errors", "## Common Causes\n- Schema version mismatch\n- Apply schema failing\n- Column type mismatch\n\n## How to Fix\n\n```bash\nvtctlclient ApplySchema -sql-file=changes.sql myks\n```\n\n## Examples\n\n```bash\nvtctlclient GetSchema tablet-alias\n```"),
    ("vitess-user-error", "Vitess User Management Error", "How to fix Vitess user and ACL errors", "## Common Causes\n- User not registered in VTGate\n- ACL rules blocking query\n- Password authentication failing\n\n## How to Fix\n\n```bash\nmysql -h vtgate-host -P 15306 -e \"CREATE USER 'myuser'@'%' IDENTIFIED BY 'pass'\"\n```\n\n## Examples\n\n```bash\nmysql -h vtgate-host -P 15306 -e \"SHOW GRANTS FOR 'myuser'@'%'\"\n```"),
    ("vitess-transaction-error", "Vitess Transaction Error", "How to fix Vitess distributed transaction errors", "## Common Causes\n- 2PC transaction timeout\n- Participant shard unreachable\n- Transaction coordinator failure\n\n## How to Fix\n\n```bash\nmysql -h vtgate-host -P 15306 -e \"SELECT * FROM users WHERE id = 1\"\n```\n\n## Examples\n\n```bash\ncurl http://localhost:15001/debug/tx_stats\n```"),
    ("vitess-health-error", "Vitess Health Check Error", "How to fix Vitess health check errors", "## Common Causes\n- Tablet failing health check\n- MySQL not responding behind tablet\n- Tablet lag too high\n\n## How to Fix\n\n```bash\nvtctlclient ListAllTablets\n```\n\n## Examples\n\n```bash\ncurl http://localhost:15001/debug/status | grep -i health\n```"),
    ("vitess-workflow-error", "Vitess Workflow Error", "How to fix Vitess workflow management errors", "## Common Causes\n- Workflow not started\n- Workflow stream failed\n- Workflow target keyspace wrong\n\n## How to Fix\n\n```bash\nvtctlclient WorkflowStatus myks\n```\n\n## Examples\n\n```bash\nvtctlclient WorkflowList\n```"),
]

count = 0
for slug, title, desc, body in PAGES:
    if slug in EXISTING:
        continue
    path = os.path.join(BASE, f'{slug}.md')
    with open(path, 'w') as f:
        f.write(make_page(slug, title, desc, body))
    count += 1

print(f'Generated {count} new Vitess pages (total: {len(EXISTING) + count})')
