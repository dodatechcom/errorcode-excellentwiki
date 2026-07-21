#!/usr/bin/env python3
"""Generate new MariaDB error pages to expand to 100+ total."""
import os

TOOL_DIR = '/home/admin1/projects/ErrorCode.excellentwiki.com/content/tools/mariadb/'
EXISTING = {f.replace('.md', '') for f in os.listdir(TOOL_DIR) if f.endswith('.md')}

PAGES = [
    ("mariadb-connection-refused", "MariaDB Connection Refused Error",
     "Fix MariaDB connection refused error. Resolve TCP connection issues to the database server.",
     "The client cannot connect to the MariaDB server. The connection is actively refused.",
     ["MariaDB service is not running", "Bind address is set to 127.0.0.1 for remote access", "Firewall blocks port 3306"],
     ["sudo systemctl status mariadb",
      "mysql -e \"SHOW VARIABLES LIKE 'bind-address';\"",
      "ss -tlnp | grep 3306"]),

    ("mariadb-access-denied", "MariaDB Access Denied Error",
     "Fix MariaDB access denied error. Resolve user authentication issues.",
     "The client cannot authenticate with the MariaDB server. The username or password is wrong.",
     ["Username or password is incorrect", "User does not exist", "User lacks permission from client host"],
     ["mysql -u root -e \"SELECT user, host FROM mysql.user;\"",
      "mysql -u root -e \"GRANT ALL PRIVILEGES ON *.* TO 'myuser'@'%' IDENTIFIED BY 'password';\""]),

    ("mariadb-unknown-database", "MariaDB Unknown Database Error",
     "Fix MariaDB unknown database error. Resolve missing database issues.",
     "The specified database does not exist. The database was never created or was dropped.",
     ["Database was never created", "Database was dropped", "Database name is misspelled"],
     ["mysql -e \"SHOW DATABASES;\"",
      "mysql -e \"CREATE DATABASE mydb;\""]),

    ("mariadb-table-doesnt-exist", "MariaDB Table Does Not Exist Error",
     "Fix MariaDB table does not exist error. Resolve missing table issues.",
     "The specified table does not exist in the database. The table was never created or was dropped.",
     ["Table was never created", "Table was dropped", "Table name is misspelled or wrong database"],
     ["mysql -e \"SHOW TABLES FROM mydb;\"",
      "mysql -e \"DESCRIBE mydb.mytable;\""]),

    ("mariadb-column-not-found", "MariaDB Column Not Found Error",
     "Fix MariaDB column not found error. Resolve missing column issues.",
     "The specified column does not exist in the table. The column was never created or was renamed.",
     ["Column was never created", "Column was renamed or dropped", "Column name is misspelled"],
     ["mysql -e \"DESCRIBE mydb.mytable;\"",
      "mysql -e \"SHOW COLUMNS FROM mydb.mytable;\""]),

    ("mariadb-duplicate-entry", "MariaDB Duplicate Entry Error",
     "Fix MariaDB duplicate entry error. Resolve UNIQUE or PRIMARY KEY constraint violations.",
     "A duplicate entry violates a UNIQUE or PRIMARY KEY constraint. The INSERT or UPDATE fails.",
     ["INSERT tries to add existing unique value", "UPDATE changes value to duplicate", "Multiple rows with same key"],
     ["mysql -e \"SHOW CREATE TABLE mydb.mytable;\"",
      "mysql -e \"SELECT * FROM mydb.mytable WHERE unique_col = 'value';\""]),

    ("mariadb-data-too-long", "MariaDB Data Too Long Error",
     "Fix MariaDB data too long error. Resolve column length overflow issues.",
     "The data being inserted or updated is too long for the column. The value is truncated.",
     ["String is longer than VARCHAR limit", "BLOB data exceeds column size", "Numeric value overflows column type"],
     ["mysql -e \"DESCRIBE mydb.mytable;\"",
      "mysql -e \"ALTER TABLE mydb.mytable MODIFY mycolumn VARCHAR(500);\""]),

    ("mariadb-truncation-error", "MariaDB Truncation Error",
     "Fix MariaDB truncation error. Resolve data truncation during insert or update.",
     "Data is truncated during the insert or update operation. The value does not fit the column.",
     ["Value is too long for column", "Numeric value is too large", "Date value is out of range"],
     ["mysql -e \"DESCRIBE mydb.mytable;\"",
      "SET sql_mode = '';"]),

    ("mariadb-syntax-error", "MariaDB Syntax Error in Query",
     "Fix MariaDB syntax error in query. Resolve SQL syntax issues.",
     "The SQL query has a syntax error. The query cannot be parsed by MariaDB.",
     ["SQL keyword is misspelled", "Missing quotes around string values", "Wrong SQL syntax for MariaDB version"],
     ["mysql -e \"SELECT VERSION();\"",
      "mysql --help | grep -i syntax"]),

    ("mariadb-foreign-key-constraint", "MariaDB Cannot Add Foreign Key Constraint Error",
     "Fix MariaDB cannot add foreign key constraint error. Resolve foreign key issues.",
     "The foreign key constraint cannot be added. The referenced table, column, or index is missing.",
     ["Referenced table does not exist", "Referenced column is not indexed", "Data type mismatch between columns"],
     ["mysql -e \"SHOW CREATE TABLE mydb.child_table;\"",
      "mysql -e \"SHOW CREATE TABLE mydb.parent_table;\""]),

    ("mariadb-row-size-too-large", "MariaDB Row Size Too Large Error",
     "Fix MariaDB row size too large error. Resolve row size limit issues.",
     "The row size exceeds the maximum allowed. The table has too many or too large columns.",
     ["Row exceeds InnoDB page size limit", "VARCHAR columns use too much space", "TEXT/BLOB columns cause overflow"],
     ["mysql -e \"SELECT AVG(LENGTH(row_data)) FROM mydb.mytable;\"",
      "mysql -e \"SHOW TABLE STATUS LIKE 'mytable';\""]),

    ("mariadb-table-is-full", "MariaDB Table Is Full Error",
     "Fix MariaDB table is full error. Resolve tablespace exhaustion issues.",
     "The table or tablespace is full. No more rows can be inserted.",
     ["Table has reached max_rows limit", "Tablespace file is full", "Disk space is exhausted"],
     ["df -h /var/lib/mysql",
      "mysql -e \"SHOW TABLE STATUS LIKE 'mytable';\""]),

    ("mariadb-out-of-memory", "MariaDB Out of Memory Error",
     "Fix MariaDB out of memory error. Resolve memory exhaustion issues.",
     "MariaDB runs out of memory. A query or operation requires more memory than available.",
     ["Query requires too much memory", "max_heap_table_size is too low", "Too many concurrent connections"],
     ["mysql -e \"SHOW GLOBAL STATUS LIKE 'Threads_connected';\"",
      "mysql -e \"SHOW VARIABLES LIKE 'max_heap_table_size';\""]),

    ("mariadb-too-many-connections", "MariaDB Too Many Connections Error",
     "Fix MariaDB too many connections error. Resolve connection limit issues.",
     "MariaDB has too many connections. New connection attempts are rejected.",
     ["max_connections limit is reached", "Applications are not closing connections", "Connection pooling is not configured"],
     ["mysql -e \"SHOW VARIABLES LIKE 'max_connections';\"",
      "mysql -e \"SHOW GLOBAL STATUS LIKE 'Threads_connected';\""]),

    ("mariadb-lock-wait-timeout", "MariaDB Lock Wait Timeout Error",
     "Fix MariaDB lock wait timeout error. Resolve transaction lock timeout issues.",
     "A transaction waits too long for a lock. The lock wait timeout expires.",
     ["Long-running transaction holds locks", "Deadlock between concurrent transactions", "Lock wait timeout is too short"],
     ["mysql -e \"SHOW PROCESSLIST;\"",
      "mysql -e \"SHOW ENGINE INNODB STATUS;\""]),

    ("mariadb-deadlock-found", "MariaDB Deadlock Found Error",
     "Fix MariaDB deadlock found error. Resolve transaction deadlock issues.",
     "A deadlock is detected. Two or more transactions are waiting for each other to release locks.",
     ["Transactions lock resources in different order", "Long-running queries hold locks", "InnoDB detects cycle"],
     ["mysql -e \"SHOW ENGINE INNODB STATUS;\"",
      "mysql -e \"SHOW PROCESSLIST;\""]),

    ("mariadb-query-cache-disabled", "MariaDB Query Cache Disabled Error",
     "Fix MariaDB query cache disabled error. Resolve query cache configuration issues.",
     "The query cache is disabled. It was removed in MariaDB 10.1.7+.",
     ["Query cache was removed in MariaDB 10.1.7", "query_cache_type is set to OFF", "Query cache is deprecated"],
     ["mysql -e \"SHOW VARIABLES LIKE 'query_cache%';\"",
      "mysql -e \"SELECT VERSION();\""]),

    ("mariadb-binary-log-error", "MariaDB Binary Log Error",
     "Fix MariaDB binary log error. Resolve binary logging issues.",
     "Binary logging encounters errors. Replication or point-in-time recovery may fail.",
     ["Binary log file is corrupted", "Binary log index file is wrong", "Disk space is exhausted"],
     ["mysql -e \"SHOW BINARY LOGS;\"",
      "mysql -e \"SHOW VARIABLES LIKE 'log_bin%';\""]),

    ("mariadb-gtid-consistency", "MariaDB GTID Consistency Error",
     "Fix MariaDB GTID consistency error. Resolve Global Transaction ID issues.",
     "GTID consistency check fails. Non-transactional statements violate GTID consistency.",
     ["Non-transactional table in transaction", "Statement-based replication with GTID", "CREATE TABLE ... SELECT used"],
     ["mysql -e \"SHOW VARIABLES LIKE 'gtid_strict_mode';\"",
      "mysql -e \"SHOW MASTER STATUS;\""]),

    ("mariadb-replication-fail", "MariaDB Replication Fail Error",
     "Fix MariaDB replication fail error. Resolve replication setup and maintenance issues.",
     "Replication fails to start or maintain sync. The slave cannot replicate from the master.",
     ["Master binary logs are missing", "Slave SQL or IO thread is stopped", "Network between master and slave is broken"],
     ["mysql -e \"SHOW SLAVE STATUS\\G\"",
      "mysql -e \"SHOW MASTER STATUS;\""]),

    ("mariadb-slave-not-running", "MariaDB Slave Not Running Error",
     "Fix MariaDB slave not running error. Resolve replication thread issues.",
     "The replication slave threads are not running. Replication is not active.",
     ["Slave SQL thread encountered an error", "Slave IO thread cannot connect to master", "Replication was manually stopped"],
     ["mysql -e \"SHOW SLAVE STATUS\\G\"",
      "mysql -e \"START SLAVE;\""]),

    ("mariadb-master-info-corrupted", "MariaDB Master Info Corrupted Error",
     "Fix MariaDB master info corrupted error. Resolve replication metadata issues.",
     "The master.info file is corrupted. The slave cannot determine replication coordinates.",
     ["master.info file is corrupted", "File was manually edited", "Disk failure corrupted the file"],
     ["ls -la /var/lib/mysql/master.info",
      "mysql -e \"SHOW SLAVE STATUS\\G\""]),

    ("mariadb-relay-log-corrupted", "MariaDB Relay Log Corrupted Error",
     "Fix MariaDB relay log corrupted error. Resolve relay log integrity issues.",
     "The relay log file is corrupted. The slave cannot read relay log entries.",
     ["Relay log file is corrupted", "Disk failure corrupted relay logs", "Incomplete shutdown corrupted logs"],
     ["ls -la /var/lib/mysql/relay-log*",
      "mysql -e \"SHOW SLAVE STATUS\\G\""]),

    ("mariadb-sql-thread-error", "MariaDB SQL Thread Error",
     "Fix MariaDB SQL thread error. Resolve slave SQL thread issues.",
     "The slave SQL thread encounters an error and stops. Replication is interrupted.",
     ["Duplicate key error on slave", "Table does not exist on slave", "Data type mismatch"],
     ["mysql -e \"SHOW SLAVE STATUS\\G\"",
      "mysql -e \"SHOW PROCESSLIST;\""]),

    ("mariadb-io-thread-error", "MariaDB IO Thread Error",
     "Fix MariaDB IO thread error. Resolve slave IO thread issues.",
     "The slave IO thread encounters an error. The slave cannot fetch binary logs from master.",
     ["Cannot connect to master", "Master binary logs are purged", "Network connectivity issue"],
     ["mysql -e \"SHOW SLAVE STATUS\\G\"",
      "mysql -e \"SHOW MASTER STATUS;\""]),

    ("mariadb-server-id-mismatch", "MariaDB Server ID Mismatch Error",
     "Fix MariaDB server ID mismatch error. Resolve replication server ID issues.",
     "The server_id is not unique across replication topology. Replication fails due to ID conflict.",
     ["Server IDs are the same on master and slave", "Server ID was changed without restart", "Multiple slaves have same ID"],
     ["mysql -e \"SHOW VARIABLES LIKE 'server_id';\"",
      "mysql -e \"SHOW SLAVE STATUS\\G\""]),

    ("mariadb-binlog-format", "MariaDB Binlog Format Error",
     "Fix MariaDB binlog format error. Resolve binary logging format issues.",
     "The binary log format is wrong for the replication setup. Mixed or statement format causes issues.",
     ["binlog_format is set to STATEMENT with GTID", "Mixed format causes inconsistencies", "Row format causes large logs"],
     ["mysql -e \"SHOW VARIABLES LIKE 'binlog_format';\"",
      "mysql -e \"SET GLOBAL binlog_format = 'ROW';\""]),

    ("mariadb-aria-storage-engine", "MariaDB Aria Storage Engine Error",
     "Fix MariaDB Aria storage engine error. Resolve Aria table issues.",
     "The Aria storage engine encounters errors. Aria tables may be corrupted or have crash recovery issues.",
     ["Aria table is corrupted", "Aria log file is corrupted", "Disk failure affected Aria files"],
     ["mysql -e \"CHECK TABLE mydb.mytable;\"",
      "mysql -e \"SHOW TABLE STATUS LIKE 'mytable';\""]),

    ("mariadb-aria-recovery", "MariaDB Aria Recovery Error",
     "Fix MariaDB Aria recovery error. Resolve Aria crash recovery issues.",
     "Aria fails to recover after a crash. The transaction log or table may be inconsistent.",
     ["Crash during write to Aria table", "Transaction log is corrupted", "Recovery process failed"],
     ["aria_chk --check /var/lib/mysql/mydb/mytable.aria",
      "mysql -e \"REPAIR TABLE mydb.mytable;\""]),

    ("mariadb-xtradb-corruption", "MariaDB XtraDB Corruption Error",
     "Fix MariaDB XtraDB corruption error. Resolve InnoDB/XtraDB data corruption issues.",
     "XtraDB (InnoDB) data is corrupted. Tables or tablespaces are unreadable.",
     ["Disk failure corrupted data files", "Crash during write operation", "Bug in XtraDB version"],
     ["mysql -e \"CHECK TABLE mydb.mytable;\"",
      "mysql -e \"SHOW ENGINE INNODB STATUS;\""]),

    ("mariadb-innodb-corruption", "MariaDB InnoDB Corruption Error",
     "Fix MariaDB InnoDB corruption error. Resolve InnoDB data corruption issues.",
     "InnoDB detects data corruption. The tablespace or data dictionary is inconsistent.",
     ["Crash during transaction commit", "Disk failure corrupted pages", "InnoDB log is corrupted"],
     ["mysql -e \"SHOW ENGINE INNODB STATUS;\"",
      "mysql -e \"SET GLOBAL innodb_force_recovery = 1;\""]),

    ("mariadb-innodb-full", "MariaDB InnoDB Tablespace Full Error",
     "Fix MariaDB InnoDB tablespace full error. Resolve InnoDB tablespace exhaustion issues.",
     "The InnoDB tablespace is full. New inserts fail.",
     ["Single tablespace file reached max size", "Disk space is exhausted", "innodb_file_per_table limit reached"],
     ["df -h /var/lib/mysql",
      "mysql -e \"SHOW TABLE STATUS LIKE 'mytable';\""]),

    ("mariadb-innodb-log-full", "MariaDB InnoDB Log Full Error",
     "Fix MariaDB InnoDB log full error. Resolve InnoDB redo log exhaustion issues.",
     "The InnoDB redo log is full. Writes are stalled until log space is freed.",
     ["Redo log size is too small", "Long-running transaction holds log space", "Checkpoint is not advancing"],
     ["mysql -e \"SHOW ENGINE INNODB STATUS;\"",
      "mysql -e \"SHOW VARIABLES LIKE 'innodb_log_file_size';\""]),

    ("mariadb-undo-tablespace", "MariaDB Undo Tablespace Error",
     "Fix MariaDB undo tablespace error. Resolve undo tablespace issues.",
     "The undo tablespace is full or corrupted. Transaction rollbacks may fail.",
     ["Undo tablespace is full", "Too many concurrent transactions", "Undo tablespace is corrupted"],
     ["mysql -e \"SHOW VARIABLES LIKE 'innodb_undo%';\"",
      "mysql -e \"SHOW ENGINE INNODB STATUS;\""]),

    ("mariadb-temporary-file-full", "MariaDB Temporary File Full Error",
     "Fix MariaDB temporary file full error. Resolve temp space exhaustion issues.",
     "MariaDB runs out of temporary file space. Queries that need temp space fail.",
     ["Disk space for tmpdir is full", "Large sort or GROUP BY needs temp space", "tmpdir is on small partition"],
     ["df -h /tmp",
      "mysql -e \"SHOW VARIABLES LIKE 'tmpdir';\""]),

    ("mariadb-max-connections-exceeded", "MariaDB Max Connections Exceeded Error",
     "Fix MariaDB max connections exceeded error. Resolve connection limit issues.",
     "MariaDB has reached the max_connections limit. New connections are refused.",
     ["Applications are not closing connections", "Connection pool is too small", "max_connections needs to be increased"],
     ["mysql -e \"SHOW VARIABLES LIKE 'max_connections';\"",
      "mysql -e \"SHOW GLOBAL STATUS LIKE 'Max_used_connections';\""]),

    ("mariadb-max-heap-table-size", "MariaDB Max Heap Table Size Error",
     "Fix MariaDB max heap table size error. Resolve memory table limit issues.",
     "The MEMORY or HEAP table exceeds max_heap_table_size. The table cannot grow further.",
     ["Table data exceeds max_heap_table_size", "Need to increase max_heap_table_size", "Should use InnoDB for large tables"],
     ["mysql -e \"SHOW VARIABLES LIKE 'max_heap_table_size';\"",
      "mysql -e \"ALTER TABLE mydb.mytable ENGINE=InnoDB;\""]),

    ("mariadb-sort-buffer-too-small", "MariaDB Sort Buffer Too Small Error",
     "Fix MariaDB sort buffer too small error. Resolve sort buffer configuration issues.",
     "The sort buffer is too small for the query. MariaDB allocates additional sort buffers.",
     ["sort_buffer_size is too low", "Query requires sorting large result set", "ORDER BY on large table"],
     ["mysql -e \"SHOW VARIABLES LIKE 'sort_buffer_size';\"",
      "mysql -e \"SET SESSION sort_buffer_size = 4194304;\""]),

    ("mariadb-join-buffer-overflow", "MariaDB Join Buffer Overflow Error",
     "Fix MariaDB join buffer overflow error. Resolve join buffer configuration issues.",
     "The join buffer overflows during query execution. The buffer is too small for the join operation.",
     ["join_buffer_size is too low", "Join involves large unindexed result sets", "Query plan uses Block Nested Loop"],
     ["mysql -e \"SHOW VARIABLES LIKE 'join_buffer_size';\"",
      "mysql -e \"SET SESSION join_buffer_size = 4194304;\""]),

    ("mariadb-tmp-table-size", "MariaDB tmp_table_size Error",
     "Fix MariaDB tmp_table_size error. Resolve internal temporary table limit issues.",
     "The internal temporary table exceeds tmp_table_size. MariaDB converts to disk table.",
     ["tmp_table_size is too low", "Query generates large temporary result", "GROUP BY or DISTINCT on many rows"],
     ["mysql -e \"SHOW VARIABLES LIKE 'tmp_table_size';\"",
      "mysql -e \"SHOW GLOBAL STATUS LIKE 'Created_tmp_disk_tables';\""]),

    ("mariadb-table-open-cache", "MariaDB table_open_cache Error",
     "Fix MariaDB table_open_cache error. Resolve table cache configuration issues.",
     "The table_open_cache is too small. MariaDB has to close and reopen tables frequently.",
     ["table_open_cache is too low", "Too many tables are open concurrently", "Opened_tables counter is high"],
     ["mysql -e \"SHOW VARIABLES LIKE 'table_open_cache';\"",
      "mysql -e \"SHOW GLOBAL STATUS LIKE 'Opened_tables';\""]),

    ("mariadb-open-files-limit", "MariaDB open_files_limit Error",
     "Fix MariaDB open_files_limit error. Resolve file descriptor limit issues.",
     "MariaDB has reached the open files limit. New file operations fail.",
     ["open_files_limit is too low", "System ulimit is too low", "Too many tables and log files open"],
     ["mysql -e \"SHOW VARIABLES LIKE 'open_files_limit';\"",
      "ulimit -n"]),

    ("mariadb-thread-cache", "MariaDB Thread Cache Error",
     "Fix MariaDB thread cache error. Resolve thread caching configuration issues.",
     "The thread cache is too small. New threads are created for each connection instead of being cached.",
     ["thread_cache_size is too low", "Too many connections are created", "Thread creation overhead is high"],
     ["mysql -e \"SHOW VARIABLES LIKE 'thread_cache_size';\"",
      "mysql -e \"SHOW GLOBAL STATUS LIKE 'Threads_created';\""]),

    ("mariadb-thread-pool", "MariaDB Thread Pool Error",
     "Fix MariaDB thread pool error. Resolve thread pool configuration issues.",
     "The thread pool encounters errors. Queries are not being dispatched to worker threads.",
     ["Thread pool is not enabled", "thread_pool_size is too low", "Thread pool plugin has bugs"],
     ["mysql -e \"SHOW VARIABLES LIKE 'thread_pool%';\"",
      "mysql -e \"SHOW PLUGINS;\""]),

    ("mariadb-pool-of-threads", "MariaDB Pool of Threads Error",
     "Fix MariaDB pool of threads error. Resolve thread pooling plugin issues.",
     "The pool-of-threads (XtraDB) plugin encounters errors. Worker threads are not functioning.",
     ["Plugin is not installed or enabled", "Pool size is too small", "Plugin configuration is wrong"],
     ["mysql -e \"SHOW PLUGINS;\"",
      "mysql -e \"SHOW VARIABLES LIKE 'thread_pool%';\""]),

    ("mariadb-user-statistics", "MariaDB User Statistics Error",
     "Fix MariaDB user statistics error. Resolve user statistics plugin issues.",
     "The user statistics plugin encounters errors. User activity tracking is not working.",
     ["User statistics plugin is not enabled", "Plugin has resource issues", "Plugin configuration is wrong"],
     ["mysql -e \"SHOW PLUGINS;\"",
      "mysql -e \"SELECT * FROM information_schema.USER_STATISTICS;\""]),

    ("mariadb-xpand-plugin", "MariaDB Xpand Plugin Error",
     "Fix MariaDB Xpand plugin error. Resolve Xpand storage engine plugin issues.",
     "The Xpand plugin encounters errors. Distributed queries are not functioning.",
     ["Xpand plugin is not installed", "Xpand cluster is not connected", "Plugin version is incompatible"],
     ["mysql -e \"SHOW PLUGINS;\""]),

    ("mariadb-spider-storage-engine", "MariaDB Spider Storage Engine Error",
     "Fix MariaDB Spider storage engine error. Resolve Spider distributed table issues.",
     "The Spider storage engine encounters errors. Distributed table operations fail.",
     ["Spider plugin is not installed", "Backend connection fails", "Spider table definition is wrong"],
     ["mysql -e \"SHOW PLUGINS;\"",
      "mysql -e \"SHOW CREATE TABLE mydb.spider_table;\""]),

    ("mariadb-columnstore-error", "MariaDB ColumnStore Error",
     "Fix MariaDB ColumnStore error. Resolve ColumnStore columnar storage issues.",
     "The ColumnStore engine encounters errors. Columnar queries are not functioning.",
     ["ColumnStore module is not running", "PM/UM nodes are not connected", "Storage configuration is wrong"],
     ["mysql -e \"SHOW PLUGINS;\"",
      "csadmin -i status"]),

    ("mariadb-connect-engine", "MariaDB Connect Engine Error",
     "Fix MariaDB Connect engine error. Resolve Connect storage engine issues.",
     "The Connect storage engine encounters errors. External data source access fails.",
     ["Connect plugin is not installed", "External data source is unreachable", "Table type is not supported"],
     ["mysql -e \"SHOW PLUGINS;\""]),

    ("mariadb-s3-storage-engine", "MariaDB S3 Storage Engine Error",
     "Fix MariaDB S3 storage engine error. Resolve S3-backed table issues.",
     "The S3 storage engine encounters errors. S3-backed tables are not accessible.",
     ["S3 plugin is not installed", "AWS credentials are wrong", "S3 bucket is not accessible"],
     ["mysql -e \"SHOW PLUGINS;\""]),

    ("mariadb-oqgraph-error", "MariaDB OQGraph Engine Error",
     "Fix MariaDB OQGraph engine error. Resolve graph query issues.",
     "The OQGraph storage engine encounters errors. Graph queries fail.",
     ["OQGraph plugin is not installed", "Graph data is malformed", "Plugin has bugs"],
     ["mysql -e \"SHOW PLUGINS;\""]),

    ("mariadb-sequence-engine-error", "MariaDB Sequence Engine Error",
     "Fix MariaDB sequence engine error. Resolve sequence generation issues.",
     "The Sequence engine encounters errors. AUTO_INCREMENT or sequence generation fails.",
     ["Sequence engine is not installed", "Sequence value is exhausted", "Engine configuration is wrong"],
     ["mysql -e \"SHOW PLUGINS;\""]),

    ("mariadb-encountered-error", "MariaDB Encountered Error",
     "Fix MariaDB encountered error. Resolve generic server error issues.",
     "MariaDB encounters an internal error. The error may be caused by a bug or misconfiguration.",
     ["Internal server error occurred", "Configuration is wrong", "Bug in MariaDB version"],
     ["mysql -e \"SHOW ERRORS;\"",
      "mysql -e \"SHOW WARNINGS;\""]),

    ("mariadb-galera-cluster", "MariaDB Galera Cluster Error",
     "Fix MariaDB Galera cluster error. Resolve Galera replication issues.",
     "The Galera cluster encounters errors. Cluster operations fail or nodes cannot communicate.",
     ["Galera node is not running", "Cluster is split-brain", "State Transfer is failing"],
     ["mysql -e \"SHOW STATUS LIKE 'wsrep%';\"",
      "galera_recovery"]),

    ("mariadb-node-not-synced", "MariaDB Galera Node Not Synced Error",
     "Fix MariaDB Galera node not synced error. Resolve Galera synchronization issues.",
     "A Galera node is not synchronized with the cluster. The node is in DONOR or JOINER state.",
     ["Node is in state transfer (SST/IST)", "Node is too far behind", "Network is slow between nodes"],
     ["mysql -e \"SHOW STATUS LIKE 'wsrep_cluster_status';\"",
      "mysql -e \"SHOW STATUS LIKE 'wsrep_local_state_comment';\""]),

    ("mariadb-flow-control-paused", "MariaDB Galera Flow Control Paused Error",
     "Fix MariaDB Galera flow control paused error. Resolve Galera backpressure issues.",
     "Galera flow control is activated. The cluster is applying writes slower than receiving them.",
     ["Write set apply is too slow", "Node is overloaded", "Flow control threshold is reached"],
     ["mysql -e \"SHOW STATUS LIKE 'wsrep_flow_control%';\"",
      "mysql -e \"SHOW STATUS LIKE 'wsrep_apply_oooe';\""]),

    ("mariadb-donor-not-found", "MariaDB Galera Donor Not Found Error",
     "Fix MariaDB Galera donor not found error. Resolve Galera state transfer donor issues.",
     "No donor node is available for state transfer. A new node cannot join the cluster.",
     ["All donor nodes are busy", "Donor node is not in synced state", "Donor node is down"],
     ["mysql -e \"SHOW STATUS LIKE 'wsrep_cluster_status';\"",
      "mysql -e \"SHOW STATUS LIKE 'wsrep_cluster_size';\""]),

    ("mariadb-joiner-error", "MariaDB Galera Joiner Error",
     "Fix MariaDB Galera joiner error. Resolve Galera joiner state issues.",
     "A joiner node fails to complete state transfer. The node cannot join the cluster.",
     ["SST transfer failed", "Joiner node disk space is insufficient", "Network interrupted during transfer"],
     ["mysql -e \"SHOW STATUS LIKE 'wsrep_local_state_comment';\"",
      "galera_recovery"]),

    ("mariadb-sst-method", "MariaDB Galera SST Method Error",
     "Fix MariaDB Galera SST method error. Resolve State Snapshot Transfer issues.",
     "The SST method fails. The donor cannot transfer the full state to the joiner.",
     ["SST method (mysqldump, rsync, mariabackup) failed", "Donor or joiner has issues", "SST user credentials are wrong"],
     ["mysql -e \"SHOW STATUS LIKE 'wsrep_sst_method';\"",
      "galera_recovery"]),

    ("mariadb-ist-transfer", "MariaDB Galera IST Transfer Error",
     "Fix MariaDB Galera IST transfer error. Resolve Incremental State Transfer issues.",
     "The IST transfer fails. The joiner cannot apply incremental writesets from the donor.",
     ["Donor does not have required gcache", "gcache size is too small", "Network issue during transfer"],
     ["mysql -e \"SHOW STATUS LIKE 'wsrep_ist%';\"",
      "mysql -e \"SHOW VARIABLES LIKE 'wsrep_provider_options';\""]),

    ("mariadb-gcomm-connection", "MariaDB Galera gcomm Connection Error",
     "Fix MariaDB Galera gcomm connection error. Resolve Galera communication issues.",
     "The gcomm:// connection between nodes fails. Nodes cannot communicate.",
     ["gcomm URL is wrong", "Network firewall blocks Galera ports", "Donor node address is unreachable"],
     ["mysql -e \"SHOW STATUS LIKE 'wsrep_cluster_size';\"",
      "cat /etc/mysql/mariadb.conf.d/galera.cnf"]),

    ("mariadb-evs-suspect", "MariaDB Galera EVS Suspect Error",
     "Fix MariaDB Galera EVS suspect error. Resolve Evs (Virtual Synchrony) issues.",
     "The EVS layer suspects a node is down. The node may be partitioned or slow.",
     ["Node is not responding to EVS heartbeats", "Network latency is high", "Node is overloaded"],
     ["mysql -e \"SHOW STATUS LIKE 'wsrep_evs%';\"",
      "mysql -e \"SHOW STATUS LIKE 'wsrep_cluster_status';\""]),

    ("mariadb-certification-failure", "MariaDB Galera Certification Failure Error",
     "Fix MariaDB Galera certification failure error. Resolve conflict detection issues.",
     "Galera certification fails. Two nodes applied conflicting writesets.",
     ["Write conflict detected on different nodes", "Schema change on one node conflicts", "Data race in application"],
     ["mysql -e \"SHOW STATUS LIKE 'wsrep_cert%';\"",
      "mysql -e \"SHOW STATUS LIKE 'wsrep_local_cert_failures';\""]),

    ("mariadb-group-communication", "MariaDB Galera Group Communication Error",
     "Fix MariaDB Galera group communication error. Resolve Galera group issues.",
     "The Galera group communication layer fails. The cluster cannot form a quorum.",
     ["Group communication network is broken", "Too many nodes are down", "Provider options are wrong"],
     ["mysql -e \"SHOW STATUS LIKE 'wsrep_cluster_status';\"",
      "mysql -e \"SHOW STATUS LIKE 'wsrep_cluster_size';\""]),

    ("mariadb-primary-component", "MariaDB Galera Primary Component Error",
     "Fix MariaDB Galera primary component error. Resolve Galera primary/primary election issues.",
     "The cluster cannot elect a primary component. Read-only mode is activated.",
     ["Cluster is partitioned", "Quorum is lost", "Primary component was manually stopped"],
     ["mysql -e \"SHOW STATUS LIKE 'wsrep_cluster_status';\"",
      "mysql -e \"SHOW STATUS LIKE 'wsrep_cluster_size';\""]),

    ("mariadb-non-primary-component", "MariaDB Galera Non-Primary Component Error",
     "Fix MariaDB Galera non-primary component error. Resolve non-primary cluster state.",
     "The node is in non-primary state. It cannot serve read-write queries.",
     ["Node is partitioned from primary", "Quorum is lost on this node", "Cluster is split-brain"],
     ["mysql -e \"SHOW STATUS LIKE 'wsrep_cluster_status';\"",
      "mysql -e \"SHOW STATUS LIKE 'wsrep_cluster_size';\""]),

    ("mariadb-split-brain", "MariaDB Galera Split-Brain Error",
     "Fix MariaDB Galera split-brain error. Resolve cluster split-brain issues.",
     "The Galera cluster experiences a split-brain scenario. Two separate clusters form.",
     ["Network partition divides cluster", "Too few nodes in majority partition", "Timeouts are too aggressive"],
     ["mysql -e \"SHOW STATUS LIKE 'wsrep_cluster_status';\"",
      "mysql -e \"SHOW STATUS LIKE 'wsrep_cluster_size';\""]),

    ("mariadb-quorum-lost", "MariaDB Galera Quorum Lost Error",
     "Fix MariaDB Galera quorum lost error. Resolve Galera quorum issues.",
     "The cluster has lost quorum. The remaining nodes cannot form a majority.",
     ["Majority of nodes are down", "Network partition isolates majority", "Cluster size is too small"],
     ["mysql -e \"SHOW STATUS LIKE 'wsrep_cluster_size';\"",
      "mysql -e \"SHOW STATUS LIKE 'wsrep_cluster_status';\""]),

    ("mariadb-myisam-error", "MariaDB MyISAM Error",
     "Fix MariaDB MyISAM error. Resolve MyISAM storage engine issues.",
     "MyISAM tables encounter errors. The table may be corrupted or have index issues.",
     ["MyISAM table is corrupted", "Crash during write to MyISAM", "Index file is corrupted"],
     ["mysql -e \"CHECK TABLE mydb.mytable;\"",
      "mysql -e \"REPAIR TABLE mydb.mytable;\""]),

    ("mariadb-myisam-repair", "MariaDB MyISAM Repair Error",
     "Fix MariaDB MyISAM repair error. Resolve MyISAM table repair issues.",
     "The MyISAM table repair fails. The corruption is too severe for automatic repair.",
     ["Table corruption is severe", "myisamchk cannot repair", "Data and index files are both corrupted"],
     ["myisamchk --check /var/lib/mysql/mydb/mytable",
      "myisamchk --recover /var/lib/mysql/mydb/mytable"]),

    ("mariadb-myisam-crash", "MariaDB MyISAM Crash Error",
     "Fix MariaDB MyISAM crash error. Resolve MyISAM crash recovery issues.",
     "MyISAM tables are inconsistent after a crash. The crash recovery did not complete.",
     ["Server crashed during MyISAM write", "Crash recovery was interrupted", "Table was open during crash"],
     ["mysqlcheck --all-databases --check",
      "mysqlcheck --all-databases --repair"]),

    ("mariadb-mysql-upgrade-error", "MariaDB mysql_upgrade Error",
     "Fix MariaDB mysql_upgrade error. Resolve version upgrade issues.",
     "The mysql_upgrade tool fails. System tables are incompatible between versions.",
     ["System tables are incompatible", "mysql_upgrade was interrupted", "Privilege tables need updating"],
     ["mysql_upgrade --force",
      "mariadb-upgrade --force"]),

    ("mariadb-mysqlcheck-error", "MariaDB mysqlcheck Error",
     "Fix MariaDB mysqlcheck error. Resolve table check and repair issues.",
     "The mysqlcheck tool fails. The table is locked or the check encounters errors.",
     ["Table is locked by another process", "Check encounters corruption", "mysqlcheck cannot access table"],
     ["mysqlcheck --all-databases",
      "mysqlcheck --all-databases --check-upgrade"]),

    ("mariadb-mysqlslap-error", "MariaDB mysqlslap Error",
     "Fix MariaDB mysqlslap error. Resolve load testing tool issues.",
     "The mysqlslap load testing tool fails. The test parameters are wrong or the server is unreachable.",
     ["Server is unreachable", "Test SQL is invalid", "Concurrency settings are too high"],
     ["mysqlslap --auto-generate-sql --verbose"]),

    ("mariadb-aria-chk-error", "MariaDB aria_chk Error",
     "Fix MariaDB aria_chk error. Resolve Aria table check issues.",
     "The aria_chk tool finds errors in Aria tables. The table or log may be corrupted.",
     ["Aria table has errors", "Aria log file is corrupted", "aria_chk cannot fix the errors"],
     ["aria_chk --check /var/lib/mysql/mydb/mytable.aria",
      "aria_chk --recover /var/lib/mysql/mydb/mytable.aria"]),

    ("mariadb-aria-pack-error", "MariaDB aria_pack Error",
     "Fix MariaDB aria_pack error. Resolve Aria table compression issues.",
     "The aria_pack tool fails. The table cannot be compressed or the packed table has errors.",
     ["Table is too large to pack", "Table has errors that need fixing first", "Disk space is insufficient"],
     ["aria_pack /var/lib/mysql/mydb/mytable.aria"]),

    ("mariadb-binary-log-corruption", "MariaDB Binary Log Corruption Error",
     "Fix MariaDB binary log corruption error. Resolve binlog integrity issues.",
     "The binary log file is corrupted. Replication or point-in-time recovery fails.",
     ["Binlog file is corrupted on disk", "Disk failure affected binlog", "Incomplete write to binlog"],
     ["mysqlbinlog /var/lib/mysql/mysql-bin.000001 > /dev/null",
      "mysql -e \"SHOW BINARY LOGS;\""]),

    ("mariadb-slow-log-error", "MariaDB Slow Query Log Error",
     "Fix MariaDB slow query log error. Resolve slow query logging issues.",
     "The slow query log is not being written. Logging configuration is wrong.",
     ["Slow query log is not enabled", "Log file is not writable", "log_output is set to NONE"],
     ["mysql -e \"SHOW VARIABLES LIKE 'slow_query_log%';\"",
      "mysql -e \"SET GLOBAL slow_query_log = ON;\""]),

    ("mariadb-general-log", "MariaDB General Log Error",
     "Fix MariaDB general log error. Resolve general query logging issues.",
     "The general query log is not being written or is causing performance issues.",
     ["General log is not enabled", "Log file is too large", "General log impacts performance"],
     ["mysql -e \"SHOW VARIABLES LIKE 'general_log%';\"",
      "mysql -e \"SET GLOBAL general_log = ON;\""]),

    ("mariadb-audit-log", "MariaDB Audit Log Error",
     "Fix MariaDB audit log error. Resolve audit logging plugin issues.",
     "The audit log plugin encounters errors. Audit events are not being recorded.",
     ["Audit plugin is not installed or enabled", "Log file is not writable", "Plugin configuration is wrong"],
     ["mysql -e \"SHOW PLUGINS;\"",
      "mysql -e \"SHOW VARIABLES LIKE 'server_audit%';\""]),

    ("mariadb-plugin-not-loaded", "MariaDB Plugin Not Loaded Error",
     "Fix MariaDB plugin not loaded error. Resolve plugin loading issues.",
     "A MariaDB plugin fails to load. The plugin library is missing or incompatible.",
     ["Plugin .so file is missing", "Plugin version is incompatible", "Plugin has dependency issues"],
     ["mysql -e \"SHOW PLUGINS;\"",
      "ls /usr/lib/mysql/plugin/"]),

    ("mariadb-encrypted-tablespace", "MariaDB Encrypted Tablespace Error",
     "Fix MariaDB encrypted tablespace error. Resolve tablespace encryption issues.",
     "The encrypted tablespace cannot be opened. The encryption key is missing or wrong.",
     ["Encryption key is not available", "Keyring plugin is not loaded", "Tablespace key is corrupted"],
     ["mysql -e \"SHOW VARIABLES LIKE 'innodb_encrypt%';\"",
      "mysql -e \"SHOW PLUGINS;\""]),

    ("mariadb-keyring-plugin", "MariaDB Keyring Plugin Error",
     "Fix MariaDB keyring plugin error. Resolve keyring (key management) issues.",
     "The keyring plugin fails to operate. Encryption keys cannot be managed.",
     ["Keyring plugin is not installed", "Keyring backend is not accessible", "Keyring file is corrupted"],
     ["mysql -e \"SHOW PLUGINS;\"",
      "mysql -e \"SHOW VARIABLES LIKE 'keyring%';\""]),

    ("mariadb-file-key-management", "MariaDB File Key Management Error",
     "Fix MariaDB file key management error. Resolve file-based keyring issues.",
     "The file key management plugin fails. The key file is missing or corrupted.",
     ["Key file does not exist", "Key file is corrupted", "Key file permissions are wrong"],
     ["mysql -e \"SHOW VARIABLES LIKE 'file_key_management%';\"",
      "ls -la /path/to/keyfile"]),

    ("mariadb-vault-key-management", "MariaDB Vault Key Management Error",
     "Fix MariaDB Vault key management error. Resolve HashiCorp Vault keyring issues.",
     "The Vault key management plugin fails. The Vault server is not reachable or the token is wrong.",
     ["Vault server is unreachable", "Vault token is expired or wrong", "Vault path is wrong"],
     ["mysql -e \"SHOW VARIABLES LIKE 'server_audit%';\"",
      "vault status"]),

    ("mariadb-password-validation", "MariaDB Password Validation Error",
     "Fix MariaDB password validation error. Resolve password policy issues.",
     "The password does not meet the validation policy. Password is too weak.",
     ["Password does not meet complexity requirements", "Password is too short", "Password validation plugin is strict"],
     ["mysql -e \"SHOW VARIABLES LIKE 'validate_password%';\"",
      "mysql -e \"SET GLOBAL validate_password.length = 8;\""]),

    ("mariadb-password-expiry", "MariaDB Password Expiry Error",
     "Fix MariaDB password expiry error. Resolve password expiration issues.",
     "The user password has expired. The user must change the password before logging in.",
     ["Password has expired per policy", "password_lifetime has been exceeded", "Password was never changed"],
     ["mysql -u root -e \"ALTER USER 'myuser'@'%' PASSWORD EXPIRE NEVER;\"",
      "mysql -u root -e \"ALTER USER 'myuser'@'%' IDENTIFIED BY 'new_password';\""]),

    ("mariadb-user-lockout", "MariaDB User Lockout Error",
     "Fix MariaDB user lockout error. Resolve account lock issues.",
     "The user account is locked after too many failed login attempts.",
     ["Too many failed login attempts", "Account was manually locked", "Password validation failed repeatedly"],
     ["mysql -u root -e \"ALTER USER 'myuser'@'%' ACCOUNT UNLOCK;\"",
      "mysql -u root -e \"SELECT user, account_locked FROM mysql.user;\""]),

    ("mariadb-failed-login-tracking", "MariaDB Failed Login Tracking Error",
     "Fix MariaDB failed login tracking error. Resolve login failure tracking issues.",
     "Failed login attempts are not being tracked correctly. Security monitoring is impaired.",
     ["Failed login tracking plugin is not enabled", "Tracking table is missing", "Plugin configuration is wrong"],
     ["mysql -e \"SHOW PLUGINS;\"",
      "mysql -e \"SELECT * FROM mysql.failed_login_attempts;\""]),

    ("mariadb-proxy-user", "MariaDB Proxy User Error",
     "Fix MariaDB proxy user error. Resolve proxy user and authentication issues.",
     "The proxy user cannot impersonate another user. The proxy privilege is missing.",
     ["PROXY privilege is not granted", "Proxy user mapping is wrong", "Authentication plugin mismatch"],
     ["mysql -u root -e \"SHOW GRANTS FOR 'proxy_user'@'%';\"",
      "mysql -u root -e \"GRANT PROXY ON 'target_user'@'%' TO 'proxy_user'@'%';\""]),

    ("mariadb-role-not-found", "MariaDB Role Not Found Error",
     "Fix MariaDB role not found error. Resolve role reference issues.",
     "The specified role does not exist. The role was never created or was dropped.",
     ["Role was never created", "Role name is misspelled", "Role was dropped"],
     ["mysql -e \"SELECT * FROM mysql.roles_mapping;\"",
      "mysql -u root -e \"CREATE ROLE 'myrole';\""]),

    ("mariadb-role-grant-error", "MariaDB Role Grant Error",
     "Fix MariaDB role grant error. Resolve role granting issues.",
     "The role cannot be granted to the user. The role does not exist or the grant is invalid.",
     ["Role does not exist", "Role grant is invalid", "Role has conflicting privileges"],
     ["mysql -e \"SHOW GRANTS FOR 'myuser'@'%' USING myrole;\"",
      "mysql -u root -e \"GRANT 'myrole' TO 'myuser'@'%';\""]),

    ("mariadb-dynamic-privilege", "MariaDB Dynamic Privilege Error",
     "Fix MariaDB dynamic privilege error. Resolve dynamic privilege issues.",
     "A dynamic privilege is not available or not granted. The operation requires a specific privilege.",
     ["Dynamic privilege is not recognized", "Privilege was not granted to user", "Plugin providing privilege is not installed"],
     ["mysql -e \"SELECT * FROM mysql.global_priv;\"",
      "mysql -u root -e \"SHOW PRIVILEGES;\""]),

    ("mariadb-secure-transport", "MariaDB Secure Transport Error",
     "Fix MariaDB secure transport error. Resolve SSL/TLS connection requirement issues.",
     "The connection requires SSL/TLS but the client is not using it. The server rejects the connection.",
     ["require_secure_transport is ON", "Client does not use SSL/TLS", "SSL certificate is not configured"],
     ["mysql -e \"SHOW VARIABLES LIKE 'require_secure_transport';\"",
      "mysql -e \"SHOW VARIABLES LIKE '%ssl%';\""]),

    ("mariadb-require-ssl", "MariaDB Require SSL Error",
     "Fix MariaDB require SSL error. Resolve per-user SSL requirement issues.",
     "The user account requires SSL but the client connects without SSL.",
     ["REQUIRE SSL is set on the user", "Client does not support SSL", "SSL is not configured on server"],
     ["mysql -u root -e \"SHOW GRANTS FOR 'myuser'@'%';\"",
      "mysql -u root -e \"ALTER USER 'myuser'@'%' REQUIRE NONE;\""]),

    ("mariadb-x509-subject", "MariaDB X509 Subject Error",
     "Fix MariaDB X509 subject error. Resolve client certificate subject verification issues.",
     "The client certificate subject does not match the REQUIRE X509 subject constraint.",
     ["Certificate subject does not match REQUIRE SUBJECT", "Wrong certificate was used", "Certificate was issued by wrong CA"],
     ["mysql -u root -e \"SHOW GRANTS FOR 'myuser'@'%';\"",
      "openssl x509 -in client.crt -noout -subject"]),

    ("mariadb-cipher-tls", "MariaDB Cipher TLS Error",
     "Fix MariaDB cipher TLS error. Resolve TLS cipher configuration issues.",
     "The TLS cipher suite is not supported or not allowed. The connection fails cipher negotiation.",
     ["Cipher is not allowed by server", "Cipher is not supported by client", "TLS version and cipher mismatch"],
     ["mysql -e \"SHOW VARIABLES LIKE 'ssl_cipher';\"",
      "openssl ciphers -v 'ALL'"]),

    ("mariadb-old-passwords", "MariaDB Old Passwords Error",
     "Fix MariaDB old passwords error. Resolve deprecated password hashing issues.",
     "The old password hashing format is used. This is insecure and deprecated.",
     ["old_passwords is set to 1 or 2", "User was created with old hash", "Client does not support new auth"],
     ["mysql -e \"SHOW VARIABLES LIKE 'old_passwords';\"",
      "mysql -u root -e \"ALTER USER 'myuser'@'%' IDENTIFIED VIA mysql_native_password USING PASSWORD('new_password');\""]),

    ("mariadb-mysql-native-password", "MariaDB mysql_native_password Error",
     "Fix MariaDB mysql_native_password error. Resolve native password authentication issues.",
     "The mysql_native_password authentication fails. The password hash is wrong or the plugin is disabled.",
     ["Password hash is corrupted", "Plugin is not loaded", "Client does not support the plugin"],
     ["mysql -e \"SHOW VARIABLES LIKE 'default_authentication_plugin';\"",
      "mysql -u root -e \"ALTER USER 'myuser'@'%' IDENTIFIED BY 'password';\""]),

    ("mariadb-ed25519-auth", "MariaDB Ed25519 Auth Error",
     "Fix MariaDB Ed25519 auth error. Resolve Ed25519 authentication issues.",
     "Ed25519 authentication fails. The client or server does not support Ed25519.",
     ["Ed25519 plugin is not loaded", "Client does not support Ed25519", "Password hash is wrong"],
     ["mysql -e \"SHOW PLUGINS;\"",
      "mysql -u root -e \"ALTER USER 'myuser'@'%' IDENTIFIED VIA ed25519 USING PASSWORD('password');\""]),

    ("mariadb-unix-socket-auth", "MariaDB Unix Socket Auth Error",
     "Fix MariaDB unix socket auth error. Resolve unix socket authentication issues.",
     "Unix socket authentication fails. The client user does not match the MariaDB user.",
     ["System user does not match MariaDB user", "Socket file path is wrong", "Socket permissions are restricted"],
     ["mysql -e \"SHOW VARIABLES LIKE 'socket';\"",
      "mysql -e \"SELECT user, plugin FROM mysql.user WHERE user = CURRENT_USER();\""]),

    ("mariadb-pam-auth", "MariaDB PAM Auth Error",
     "Fix MariaDB PAM auth error. Resolve PAM authentication issues.",
     "PAM authentication fails. The PAM module is not configured or the PAM backend is unavailable.",
     ["PAM plugin is not installed", "PAM service is not configured", "PAM backend is not accessible"],
     ["mysql -e \"SHOW PLUGINS;\"",
      "cat /etc/pam.d/mysql"]),
]

def make_page(slug, title, desc, body, causes, fixes, examples):
    lines = [
        '---',
        f'title: "[Solution] {title}"',
        f'description: "{desc}"',
        'tools: ["mariadb"]',
        'error-types: ["database-error"]',
        'severities: ["error"]',
        '---',
        '',
        f'# {title}',
        '',
        body,
        '',
        '## Common Causes',
        '',
    ]
    for c in causes:
        lines.append(f'- {c}')
    lines.append('')
    lines.append('## How to Fix')
    lines.append('')
    for i, fix in enumerate(fixes, 1):
        lines.append(f'### Solution {i}')
        lines.append('')
        lines.append('```bash')
        lines.append(fix)
        lines.append('```')
        lines.append('')
    if examples:
        lines.append('## Examples')
        lines.append('')
        for ex in examples:
            lines.append('```bash')
            lines.append(ex)
            lines.append('```')
            lines.append('')
    related = [
        '- [MariaDB Connection Error]({{< relref "/tools/mariadb/mariadb-connection-error" >}})',
        '- [MariaDB InnoDB Error]({{< relref "/tools/mariadb/mariadb-innodb-error" >}})',
        '- [MariaDB Galera Error]({{< relref "/tools/mariadb/mariadb-galera-error" >}})',
    ]
    lines.append('## Related Pages')
    lines.append('')
    lines.extend(related)
    lines.append('')
    return '\n'.join(lines)


count = 0
skipped = 0
for page in PAGES:
    slug, title, desc, body, causes, fixes = page[:6]
    examples = page[6] if len(page) > 6 else []
    if slug in EXISTING:
        print(f"SKIP (exists): {slug}")
        skipped += 1
        continue
    content = make_page(slug, title, desc, body, causes, fixes, examples)
    path = os.path.join(TOOL_DIR, f'{slug}.md')
    with open(path, 'w') as f:
        f.write(content)
    count += 1
    print(f"CREATED: {slug}")

print(f"\nTotal created: {count}")
print(f"Total skipped (existing): {skipped}")
total = len([f for f in os.listdir(TOOL_DIR) if f.endswith('.md')])
print(f"Total .md files in mariadb/: {total}")
