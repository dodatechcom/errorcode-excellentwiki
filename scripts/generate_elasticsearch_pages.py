#!/usr/bin/env python3
"""Generate new Elasticsearch error pages to expand to 100+ total."""
import os

TOOL_DIR = '/home/admin1/projects/ErrorCode.excellentwiki.com/content/tools/elasticsearch/'
EXISTING = {f.replace('.md', '') for f in os.listdir(TOOL_DIR) if f.endswith('.md')}

PAGES = [
    ("elasticsearch-cluster-health-red", "Elasticsearch Cluster Health Red Error",
     "Fix Elasticsearch cluster health red error. Resolve critical cluster health issues where primary shards are unassigned.",
     "The cluster health is RED, meaning one or more primary shards are unassigned. This indicates data loss or unavailable indices.",
     ["Primary shards cannot be assigned to any node", "A node holding primary shards has left the cluster", "Disk watermark has been exceeded"],
     ["curl -X GET 'localhost:9200/_cluster/health?pretty'",
      "curl -X GET 'localhost:9200/_cat/shards?v&h=index,shard,prirep,state,unassigned.reason'"]),

    ("elasticsearch-cluster-health-yellow", "Elasticsearch Cluster Health Yellow Error",
     "Fix Elasticsearch cluster health yellow error. Resolve replica shard allocation issues.",
     "The cluster health is YELLOW, meaning all primary shards are allocated but some replica shards are not.",
     ["Not enough nodes for replicas", "Replica shards are unassigned due to disk watermarks", "A node recently left the cluster"],
     ["curl -X GET 'localhost:9200/_cat/shards?v&h=index,shard,prirep,state&s=state:desc'",
      "curl -X POST 'localhost:9200/_cluster/reroute' -H 'Content-Type: application/json' -d '{\"commands\":[{\"allocate_replica\":{\"index\":\"myindex\",\"shard\":0,\"node\":\"node-1\"}}]}'"]),

    ("elasticsearch-no-master-node", "Elasticsearch No Master Node Error",
     "Fix Elasticsearch no master node error. Resolve master node election failures.",
     "The cluster cannot elect or maintain a master node. The cluster enters a RED state and cannot serve requests.",
     ["All master-eligible nodes are down", "Network partition prevents election", "Insufficient master-eligible nodes"],
     ["curl -X GET 'localhost:9200/_cat/master?v'",
      "curl -X GET 'localhost:9200/_cat/nodes?v&h=name,master,ip'"]),

    ("elasticsearch-master-not-elected", "Elasticsearch Master Not Elected Error",
     "Fix Elasticsearch master not elected error. Resolve master election timeout issues.",
     "The master election process times out or fails. Nodes cannot agree on a master within the election timeout.",
     ["Election timeout is too low", "Nodes cannot communicate on transport port", "Cluster bootstrapping is incomplete"],
     ["curl -X GET 'localhost:9200/_cat/nodes?v&h=name,master,ip'"]),

    ("elasticsearch-discovery-split-brain", "Elasticsearch Split Brain Error",
     "Fix Elasticsearch split brain error. Resolve master election split-brain scenarios.",
     "A split-brain scenario occurs where two separate master nodes are elected, leading to data inconsistency.",
     ["Minimum master nodes config is incorrect", "Network partition divides the cluster", "Discovery config allows separate quorums"],
     ["grep -i 'minimum_master_nodes\\|discovery.seed_hosts' /etc/elasticsearch/elasticsearch.yml"]),

    ("elasticsearch-minimum-master-nodes", "Elasticsearch Minimum Master Nodes Error",
     "Fix Elasticsearch minimum master nodes error. Resolve quorum configuration issues.",
     "The minimum_master_nodes setting prevents master election because insufficient master-eligible nodes are available.",
     ["Too few master-eligible nodes", "Nodes are down or unreachable", "minimum_master_nodes is too high"],
     ["curl -X GET 'localhost:9200/_cat/nodes?v&h=name,master,ip,role'"]),

    ("elasticsearch-not-enough-nodes", "Elasticsearch Not Enough Nodes Error",
     "Fix Elasticsearch not enough nodes error. Resolve insufficient cluster node issues.",
     "The cluster does not have enough nodes to meet allocation or discovery requirements.",
     ["Cluster needs more nodes for shard allocation", "Replica count exceeds available nodes", "Discovery requires minimum nodes"],
     ["curl -X GET 'localhost:9200/_cat/nodes?v'"]),

    ("elasticsearch-node-left-cluster", "Elasticsearch Node Left Cluster Error",
     "Fix Elasticsearch node left cluster error. Resolve node departure and recovery issues.",
     "A node has left the cluster, leaving shards unassigned and cluster health degraded.",
     ["Node crashed or was shut down ungracefully", "Network issue caused disconnect", "Node was removed via API"],
     ["curl -X GET 'localhost:9200/_cat/nodes?v'",
      "curl -X GET 'localhost:9200/_cat/shards?v&h=index,shard,prirep,state,unassigned.reason'"]),

    ("elasticsearch-shard-not-allocated", "Elasticsearch Shard Not Allocated Error",
     "Fix Elasticsearch shard not allocated error. Resolve shard allocation failures.",
     "A shard cannot be allocated to any node in the cluster. The shard remains in unassigned state.",
     ["All nodes exceed disk watermark", "Shard allocation is disabled", "No node satisfies allocation filters"],
     ["curl -X GET 'localhost:9200/_cluster/allocation/explain?pretty'"]),

    ("elasticsearch-shard-allocation", "Elasticsearch Shard Allocation Error",
     "Fix Elasticsearch shard allocation error. Resolve shard routing and allocation issues.",
     "Shards are not being allocated as expected. The cluster routing and allocation settings may be misconfigured.",
     ["Shard allocation is set to none", "Allocation filtering excludes all nodes", "Rebalancing is disabled"],
     ["curl -X GET 'localhost:9200/_cluster/settings?pretty'"]),

    ("elasticsearch-shard-failed", "Elasticsearch Shard Failed Error",
     "Fix Elasticsearch shard failed error. Resolve shard corruption and recovery issues.",
     "A shard fails during indexing, search, or recovery. The shard may be corrupted or experiencing I/O errors.",
     ["Disk corruption on shard data path", "I/O errors reading segments", "JVM crashes during shard operations"],
     ["curl -X GET 'localhost:9200/_cat/shards?v&h=index,shard,prirep,state,unassigned.reason'"]),

    ("elasticsearch-shard-primary-not-allocated", "Elasticsearch Primary Shard Not Allocated Error",
     "Fix Elasticsearch primary shard not allocated error. Resolve primary shard allocation issues.",
     "A primary shard cannot be allocated. The index is unavailable for indexing until the primary is restored.",
     ["All nodes with shard data are down", "Disk watermarks prevent allocation", "Shard allocation is disabled"],
     ["curl -X GET 'localhost:9200/_cluster/allocation/explain?pretty'"]),

    ("elasticsearch-shard-replica-not-allocated", "Elasticsearch Replica Shard Not Allocated Error",
     "Fix Elasticsearch replica shard not allocated error. Resolve replica allocation failures.",
     "A replica shard cannot be allocated. The index works but is at risk of data loss if the primary fails.",
     ["Not enough data nodes for replicas", "Disk watermarks prevent allocation", "Allocation filtering excludes nodes"],
     ["curl -X GET 'localhost:9200/_cat/shards?v&h=index,shard,prirep,state'"]),

    ("elasticsearch-index-missing", "Elasticsearch Index Missing Error",
     "Fix Elasticsearch index missing error. Resolve missing or deleted index issues.",
     "The requested index does not exist. It may have been deleted or the name is misspelled.",
     ["Index was deleted by retention policy or ILM", "Index name is misspelled", "Index was never created"],
     ["curl -X GET 'localhost:9200/_cat/indices?v&s=index:asc'"]),

    ("elasticsearch-index-read-only", "Elasticsearch Index Read Only Error",
     "Fix Elasticsearch index read only error. Resolve index read-only mode issues.",
     "The index is in read-only mode and rejects write operations. This happens when disk watermarks are exceeded.",
     ["Disk watermark exceeded triggers read-only block", "Index was manually set to read-only", "ILM set read-only phase"],
     ["curl -X GET 'localhost:9200/myindex/_settings?pretty'"]),

    ("elasticsearch-index-blocked", "Elasticsearch Index Blocked Error",
     "Fix Elasticsearch index blocked error. Resolve index block configuration issues.",
     "The index has blocks enabled that prevent certain operations. Writes, metadata changes, or reads may be blocked.",
     ["index.blocks.read_only is true", "index.blocks.write is true", "index.blocks.metadata is true"],
     ["curl -X GET 'localhost:9200/myindex/_settings?pretty'"]),

    ("elasticsearch-index-closed", "Elasticsearch Index Closed Error",
     "Fix Elasticsearch index closed error. Resolve closed index operation issues.",
     "The index is closed and does not accept any operations. A closed index consumes no resources but is inaccessible.",
     ["Index was manually closed", "ILM policy closed the index", "Maintenance operation closed it"],
     ["curl -X POST 'localhost:9200/myindex/_open'"]),

    ("elasticsearch-index-exists", "Elasticsearch Index Already Exists Error",
     "Fix Elasticsearch index already exists error. Resolve index creation conflicts.",
     "The index already exists when trying to create it with create index API.",
     ["Index was already created", "Auto-creation created it first", "Name conflict with data stream"],
     ["curl -X GET 'localhost:9200/_cat/indices?v&s=index:asc'"]),

    ("elasticsearch-alias-not-found", "Elasticsearch Alias Not Found Error",
     "Fix Elasticsearch alias not found error. Resolve index alias reference issues.",
     "The requested alias does not exist. The alias may have been removed or never created.",
     ["Alias was removed", "Alias name is misspelled", "Alias was never created"],
     ["curl -X GET 'localhost:9200/_cat/aliases?v'"]),

    ("elasticsearch-alias-index-missing", "Elasticsearch Alias Index Missing Error",
     "Fix Elasticsearch alias index missing error. Resolve alias pointing to non-existent index.",
     "An alias points to an index that no longer exists. The alias is orphaned and operations fail.",
     ["Index was deleted but alias was not removed", "Alias points to wrong index", "ILM rollover alias update failed"],
     ["curl -X GET 'localhost:9200/_alias/myalias'"]),

    ("elasticsearch-mapping-type-deprecated", "Elasticsearch Mapping Type Deprecated Error",
     "Fix Elasticsearch mapping type deprecated error. Resolve type removal compatibility issues.",
     "The mapping type is deprecated in Elasticsearch 7.x and removed in 8.x. Requests using types will fail.",
     ["Request uses custom type in URL", "Bulk request specifies document types", "Index creation includes type mapping"],
     ["curl -X PUT 'localhost:9200/myindex' -H 'Content-Type: application/json' -d '{\"mappings\":{\"properties\":{\"field\":{\"type\":\"text\"}}}}'"]),

    ("elasticsearch-mapping-conflict", "Elasticsearch Mapping Conflict Error",
     "Fix Elasticsearch mapping conflict error. Resolve field type mapping conflicts.",
     "A field type conflict occurs when a document has a different type for a field than the existing mapping.",
     ["Field indexed as text in one doc and keyword in another", "Dynamic mapping inferred different type", "Bulk indexing sent conflicting types"],
     ["curl -X GET 'localhost:9200/myindex/_mapping?pretty'"]),

    ("elasticsearch-dynamic-mapping-limit", "Elasticsearch Dynamic Mapping Limit Error",
     "Fix Elasticsearch dynamic mapping limit error. Resolve too many dynamic fields issues.",
     "The index exceeds the dynamic field mapping limit. Elasticsearch stops accepting new fields.",
     ["Index has too many dynamically mapped fields (default 1000)", "Application sends many different field names", "Nested objects create deep field paths"],
     ["curl -X PUT 'localhost:9200/myindex/_settings' -H 'Content-Type: application/json' -d '{\"index.mapping.total_fields.limit\":2000}'"]),

    ("elasticsearch-fielddata-disabled", "Elasticsearch Fielddata Disabled Error",
     "Fix Elasticsearch fielddata disabled error. Resolve fielddata usage on text fields.",
     "Fielddata is disabled for text fields. Aggregations and sorting on text fields require fielddata to be enabled.",
     ["Attempting to aggregate on a text field", "Attempting to sort on a text field", "Fielddata is disabled by default on text"],
     ["curl -X GET 'localhost:9200/myindex/_mapping?pretty'"]),

    ("elasticsearch-doc-values-disabled", "Elasticsearch Doc Values Disabled Error",
     "Fix Elasticsearch doc values disabled error. Resolve doc_values usage issues.",
     "Doc values are disabled for a field. Aggregations and sorting on this field require doc values.",
     ["Field was mapped with doc_values: false", "Text fields do not support doc values", "Field type does not support doc values"],
     ["curl -X GET 'localhost:9200/myindex/_mapping?pretty'"]),

    ("elasticsearch-analyzer-not-found", "Elasticsearch Analyzer Not Found Error",
     "Fix Elasticsearch analyzer not found error. Resolve custom analyzer reference issues.",
     "The specified analyzer does not exist. It may not be defined in the index settings or built-in analyzers.",
     ["Custom analyzer is not defined in settings", "Built-in analyzer name is misspelled", "Analyzer is in different index"],
     ["curl -X GET 'localhost:9200/myindex/_settings?pretty'"]),

    ("elasticsearch-char-filter-error", "Elasticsearch Char Filter Error",
     "Fix Elasticsearch char filter error. Resolve custom char filter configuration issues.",
     "A custom char filter fails to initialize or process text. The filter configuration is invalid.",
     ["Char filter type is not recognized", "Pattern is invalid in pattern_replace", "Mapping file is missing"],
     ["curl -X GET 'localhost:9200/myindex/_analyze' -H 'Content-Type: application/json' -d '{\"char_filter\":[\"my_filter\"],\"text\":\"hello\"}'"]),

    ("elasticsearch-tokenizer-error", "Elasticsearch Tokenizer Error",
     "Fix Elasticsearch tokenizer error. Resolve custom tokenizer configuration issues.",
     "A custom tokenizer fails to initialize or tokenize text correctly.",
     ["Tokenizer type is not recognized", "Regex pattern is invalid", "Configuration parameters are wrong"],
     ["curl -X GET 'localhost:9200/myindex/_analyze' -H 'Content-Type: application/json' -d '{\"tokenizer\":\"my_tokenizer\",\"text\":\"hello world\"}'"]),

    ("elasticsearch-filter-configuration", "Elasticsearch Token Filter Configuration Error",
     "Fix Elasticsearch token filter configuration error. Resolve token filter issues.",
     "A token filter is misconfigured or fails during analysis. The filter parameters are invalid.",
     ["Filter type is not recognized", "Stop words list is invalid", "Synonym mapping file is missing"],
     ["curl -X GET 'localhost:9200/myindex/_analyze' -H 'Content-Type: application/json' -d '{\"filter\":[\"my_filter\"],\"text\":\"hello world\"}'"]),

    ("elasticsearch-custom-analyzer-init", "Elasticsearch Custom Analyzer Init Error",
     "Fix Elasticsearch custom analyzer init error. Resolve analyzer initialization failures.",
     "A custom analyzer fails to initialize when creating or updating an index. One of its components is invalid.",
     ["Char filter, tokenizer, or filter has invalid config", "Analyzer references non-existent component", "Circular reference in config"],
     ["curl -X GET 'localhost:9200/myindex/_analyze' -H 'Content-Type: application/json' -d '{\"analyzer\":\"my_analyzer\",\"text\":\"test\"}'"]),

    ("elasticsearch-search-phase-execution", "Elasticsearch Search Phase Execution Error",
     "Fix Elasticsearch search phase execution error. Resolve search phase failure issues.",
     "A search phase fails during execution. The query, fetch, or other phase encounters an error.",
     ["Query phase fails due to invalid syntax", "Fetch phase fails due to memory", "Shard unavailable during search"],
     ["curl -X GET 'localhost:9200/_cat/shards?v&h=index,shard,prirep,state'"]),

    ("elasticsearch-query-timeout", "Elasticsearch Query Timeout Error",
     "Fix Elasticsearch query timeout error. Resolve search timeout issues.",
     "The search query times out before completing. The query is too complex or the cluster is overloaded.",
     ["Query is too complex", "Cluster is under heavy load", "Timeout is set too low"],
     ["curl -X GET 'localhost:9200/myindex/_search?timeout=30s' -H 'Content-Type: application/json' -d '{\"query\":{\"match_all\":{}}}'"]),

    ("elasticsearch-scroll-context-lost", "Elasticsearch Scroll Context Lost Error",
     "Fix Elasticsearch scroll context lost error. Resolve scroll context expiration issues.",
     "The scroll context has expired or been cleared. Subsequent scroll requests fail.",
     ["Scroll context timed out (default 1m)", "Too many scroll contexts open", "Scroll not maintained with keep-alive"],
     ["curl -X DELETE 'localhost:9200/_search/scroll/_all'"]),

    ("elasticsearch-scroll-timeout", "Elasticsearch Scroll Timeout Error",
     "Fix Elasticsearch scroll timeout error. Resolve scroll expiration configuration issues.",
     "The scroll request times out because the scroll context has expired.",
     ["Keep-alive interval is too short", "Scroll not maintained between iterations", "Cluster is slow to respond"],
     ["curl -X GET 'localhost:9200/myindex/_search?scroll=5m' -H 'Content-Type: application/json' -d '{\"query\":{\"match_all\":{}}}'"]),

    ("elasticsearch-search-circuit-breaker", "Elasticsearch Search Circuit Breaker Error",
     "Fix Elasticsearch search circuit breaker error. Resolve memory circuit breaker trips.",
     "The search circuit breaker trips due to excessive memory usage. Searches are rejected to prevent OOM.",
     ["Search loads too much data into memory", "Fielddata uses too much memory", "Circuit breaker limit is too low"],
     ["curl -X GET 'localhost:9200/_nodes/stats/breaker?pretty'"]),

    ("elasticsearch-request-cache-disabled", "Elasticsearch Request Cache Disabled Error",
     "Fix Elasticsearch request cache disabled error. Resolve search caching issues.",
     "The request cache is disabled and searches are not cached. This impacts performance for repeated queries.",
     ["Cache is disabled at index or node level", "Query uses cache-busting features", "Cache was invalidated by writes"],
     ["curl -X GET 'localhost:9200/_nodes/stats/indices.request_cache?pretty'"]),

    ("elasticsearch-field-collapsing-error", "Elasticsearch Field Collapsing Error",
     "Fix Elasticsearch field collapsing error. Resolve search field collapsing issues.",
     "Field collapsing fails during search. The collapse field is missing, unsupported, or has too many groups.",
     ["Collapse field does not exist in mapping", "Collapse field is text without keyword", "Too many unique values"],
     ["curl -X GET 'localhost:9200/myindex/_search' -H 'Content-Type: application/json' -d '{\"query\":{\"match_all\":{}},\"collapse\":{\"field\":\"status.keyword\"}}'"]),

    ("elasticsearch-aggregation-too-complex", "Elasticsearch Aggregation Too Complex Error",
     "Fix Elasticsearch aggregation too complex error. Resolve aggregation performance and resource issues.",
     "The aggregation is too complex or uses too many resources. It may time out or cause memory pressure.",
     ["Aggregation has too many nested levels", "Terms agg has too many buckets", "Aggregation uses high-cardinality fields"],
     ["curl -X PUT 'localhost:9200/_cluster/settings' -H 'Content-Type: application/json' -d '{\"transient\":{\"search.max_buckets\":10000}}'"]),

    ("elasticsearch-result-window-too-large", "Elasticsearch Result Window Too Large Error",
     "Fix Elasticsearch result window too large error. Resolve deep pagination limit issues.",
     "The search result window exceeds the max_result_window limit. Deep pagination is blocked.",
     ["from + size exceeds max_result_window (default 10000)", "Application paginates too deeply", "No search_after or scroll used"],
     ["curl -X PUT 'localhost:9200/myindex/_settings' -H 'Content-Type: application/json' -d '{\"index.max_result_window\":20000}'"]),

    ("elasticsearch-too-many-buckets", "Elasticsearch Too Many Buckets Error",
     "Fix Elasticsearch too many buckets error. Resolve aggregation bucket limit issues.",
     "The aggregation generates more buckets than allowed. The request is rejected.",
     ["Terms agg on high-cardinality field", "Date histogram with very fine granularity", "Multiple nested aggs generate exponential buckets"],
     ["curl -X PUT 'localhost:9200/_cluster/settings' -H 'Content-Type: application/json' -d '{\"transient\":{\"search.max_buckets\":20000}}'"]),

    ("elasticsearch-terms-bucket-overflow", "Elasticsearch Terms Bucket Overflow Error",
     "Fix Elasticsearch terms bucket overflow error. Resolve terms aggregation bucket limit.",
     "The terms aggregation exceeds the bucket limit. Too many unique terms are generated.",
     ["High-cardinality field used in terms agg", "No size parameter to limit buckets", "Aggregation is not filtered enough"],
     ["curl -X GET 'localhost:9200/myindex/_search' -H 'Content-Type: application/json' -d '{\"size\":0,\"aggs\":{\"top_values\":{\"terms\":{\"field\":\"status.keyword\",\"size\":100}}}}'"]),

    ("elasticsearch-date-histogram-error", "Elasticsearch Date Histogram Error",
     "Fix Elasticsearch date histogram error. Resolve date histogram aggregation issues.",
     "The date histogram aggregation fails. The field is not a date type, or the interval is invalid.",
     ["Field is not mapped as date type", "Interval is missing", "Timezone setting is invalid"],
     ["curl -X GET 'localhost:9200/myindex/_search' -H 'Content-Type: application/json' -d '{\"size\":0,\"aggs\":{\"over_time\":{\"date_histogram\":{\"field\":\"@timestamp\",\"calendar_interval\":\"day\"}}}}'"]),

    ("elasticsearch-geo-distance-error", "Elasticsearch Geo Distance Error",
     "Fix Elasticsearch geo distance error. Resolve geo_distance query issues.",
     "The geo_distance query fails due to invalid coordinates or field mapping.",
     ["Geo point field has invalid coordinates", "Distance unit is not recognized", "Field is not mapped as geo_point"],
     ["curl -X GET 'localhost:9200/myindex/_search' -H 'Content-Type: application/json' -d '{\"query\":{\"bool\":{\"must\":{\"match_all\":{}},\"filter\":{\"geo_distance\":{\"distance\":\"200km\",\"location\":{\"lat\":40.73,\"lon\":-74.1}}}}}}'"]),

    ("elasticsearch-nested-query-error", "Elasticsearch Nested Query Error",
     "Fix Elasticsearch nested query error. Resolve nested object query issues.",
     "The nested query fails. The nested path is incorrect or the field is not mapped as nested.",
     ["Nested path does not match mapping", "Field is not mapped as nested", "Query references wrong nested path"],
     ["curl -X GET 'localhost:9200/myindex/_mapping?pretty'"]),

    ("elasticsearch-parent-child-join", "Elasticsearch Parent Child Join Error",
     "Fix Elasticsearch parent/child join error. Resolve join field relationship issues.",
     "The parent/child join query fails. The join field is misconfigured or the relationship is broken.",
     ["Join field is not defined in mapping", "Parent and child are in different indices", "Join field value does not match"],
     ["curl -X GET 'localhost:9200/myindex/_mapping?pretty'"]),

    ("elasticsearch-inner-hits-error", "Elasticsearch Inner Hits Error",
     "Fix Elasticsearch inner hits error. Resolve nested and parent/child inner hits issues.",
     "The inner_hits parameter fails. The nested query or parent/child relationship is not properly configured.",
     ["inner_hits used without nested/has_child/has_parent", "inner_hits size exceeds results", "Source filtering conflicts"],
     ["curl -X GET 'localhost:9200/myindex/_search' -H 'Content-Type: application/json' -d '{\"query\":{\"nested\":{\"path\":\"comments\",\"query\":{\"match_all\":{}},\"inner_hits\":{\"size\":5}}}}'"]),

    ("elasticsearch-suggester-error", "Elasticsearch Suggester Error",
     "Fix Elasticsearch suggester error. Resolve search suggester issues.",
     "The suggester fails to provide suggestions. The suggest field is missing or misconfigured.",
     ["Suggest field is not defined in mapping", "Suggester config is incorrect", "No matching suggestions found"],
     ["curl -X GET 'localhost:9200/myindex/_search' -H 'Content-Type: application/json' -d '{\"suggest\":{\"text\":\"elasticsearch\",\"phrase\":{\"field\":\"suggest\",\"size\":3}}}'"]),

    ("elasticsearch-phrase-suggest", "Elasticsearch Phrase Suggest Error",
     "Fix Elasticsearch phrase suggest error. Resolve phrase suggestion issues.",
     "The phrase suggester fails to generate correct suggestions. The collate query or analyzer is misconfigured.",
     ["Collate query is invalid", "Analyzer does not match suggest field", "Pre-tag and post-tag are wrong"],
     ["curl -X GET 'localhost:9200/myindex/_search' -H 'Content-Type: application/json' -d '{\"suggest\":{\"phrase\":{\"text\":\"lasticsearch\",\"field\":\"body\",\"collate\":{\"query\":{\"match_phrase\":{\"body\":\"{{suggestion}}\"}}}}}}'"]),

    ("elasticsearch-completion-suggest", "Elasticsearch Completion Suggest Error",
     "Fix Elasticsearch completion suggest error. Resolve completion suggestion issues.",
     "The completion suggester fails. The completion field is not mapped or the query is incorrect.",
     ["Completion field is not mapped as completion type", "Suggestions are too expensive", "Fuzzy edits are too many"],
     ["curl -X GET 'localhost:9200/myindex/_search' -H 'Content-Type: application/json' -d '{\"suggest\":{\"name-suggest\":{\"prefix\":\"ela\",\"completion\":{\"field\":\"suggest\",\"size\":5}}}}'"]),

    ("elasticsearch-bulk-partially-failed", "Elasticsearch Bulk Partially Failed Error",
     "Fix Elasticsearch bulk partially failed error. Resolve bulk request partial failures.",
     "Some operations in the bulk request failed while others succeeded. Check the response for individual errors.",
     ["Individual document indexing failed", "Document is too large", "Index does not exist for some operations"],
     ["curl -X POST 'localhost:9200/_bulk' -H 'Content-Type: application/json' --data-binary @bulk_request.json"]),

    ("elasticsearch-bulk-queue-full", "Elasticsearch Bulk Queue Full Error",
     "Fix Elasticsearch bulk queue full error. Resolve bulk indexing queue overflow issues.",
     "The bulk indexing queue is full. Indexing requests are rejected or throttled.",
     ["Indexing rate exceeds bulk thread pool capacity", "Bulk queue size is too small", "Cluster is under heavy indexing load"],
     ["curl -X GET 'localhost:9200/_cat/thread_pool/bulk?v&h=node_name,queue,active,completed'"]),

    ("elasticsearch-indexing-too-slow", "Elasticsearch Indexing Too Slow Error",
     "Fix Elasticsearch indexing too slow error. Resolve slow indexing performance issues.",
     "Indexing performance is degraded. Documents take too long to be indexed.",
     ["Too many segments need merging", "Refresh interval is too frequent", "Disk I/O is slow"],
     ["curl -X PUT 'localhost:9200/myindex/_settings' -H 'Content-Type: application/json' -d '{\"index.refresh_interval\":\"30s\"}'"]),

    ("elasticsearch-document-too-large", "Elasticsearch Document Too Large Error",
     "Fix Elasticsearch document too large error. Resolve document size limit issues.",
     "The document exceeds the maximum allowed size. The indexing request is rejected.",
     ["Document size exceeds http.max_content_length", "Document contains very large fields", "Bulk payload is too large"],
     ["grep http.max_content_length /etc/elasticsearch/elasticsearch.yml"]),

    ("elasticsearch-id-too-long", "Elasticsearch Document ID Too Long Error",
     "Fix Elasticsearch document ID too long error. Resolve document ID length limit issues.",
     "The document ID exceeds the maximum length of 512 bytes.",
     ["Auto-generated ID is too long", "ID contains encoded characters", "Application generates long IDs"],
     ["curl -X PUT 'localhost:9200/myindex/_doc/short-id' -H 'Content-Type: application/json' -d '{\"field\":\"value\"}'"]),

    ("elasticsearch-routing-missing", "Elasticsearch Routing Missing Error",
     "Fix Elasticsearch routing missing error. Resolve routing parameter issues.",
     "The routing parameter is required but not provided. The document cannot be correctly routed to a shard.",
     ["Index requires routing but not provided", "Routing needed for parent/child", "_routing is mandatory in mapping"],
     ["curl -X PUT 'localhost:9200/myindex/_doc/1?routing=user123' -H 'Content-Type: application/json' -d '{\"field\":\"value\"}'"]),

    ("elasticsearch-parent-id-not-set", "Elasticsearch Parent ID Not Set Error",
     "Fix Elasticsearch parent ID not set error. Resolve parent document reference issues.",
     "The child document does not specify a parent ID. The parent/child relationship cannot be established.",
     ["Child indexed without parent parameter", "Parent document does not exist", "Routing does not match parent"],
     ["curl -X PUT 'localhost:9200/myindex/_doc/child1?routing=parent1' -H 'Content-Type: application/json' -d '{\"join_field\":{\"name\":\"child\",\"parent\":\"parent1\"}}'"]),

    ("elasticsearch-dynamic-scripting-disabled", "Elasticsearch Dynamic Scripting Disabled Error",
     "Fix Elasticsearch dynamic scripting disabled error. Resolve script execution permission issues.",
     "Dynamic scripting is disabled. Inline scripts and script queries cannot execute.",
     ["Scripting is disabled for security", "script.inline is false in elasticsearch.yml", "Security plugin blocks scripts"],
     ["grep 'script.inline\\|script.stored' /etc/elasticsearch/elasticsearch.yml"]),

    ("elasticsearch-painless-script-error", "Elasticsearch Painless Script Error",
     "Fix Elasticsearch Painless script error. Resolve Painless scripting language issues.",
     "A Painless script fails to compile or execute. The script has syntax errors or references invalid variables.",
     ["Script has syntax errors", "Script references unavailable classes", "Script attempts restricted operations"],
     ["curl -X POST 'localhost:9200/_scripts/painless/_execute' -H 'Content-Type: application/json' -d '{\"script\":{\"source\":\"return 1 + 1;\"}}'"]),

    ("elasticsearch-script-compilation", "Elasticsearch Script Compilation Error",
     "Fix Elasticsearch script compilation error. Resolve script syntax and compilation issues.",
     "The script fails to compile. The syntax is invalid or the script uses unavailable features.",
     ["Script syntax is incorrect", "Script uses deprecated features", "Script references non-existent fields"],
     ["curl -X POST 'localhost:9200/_scripts/painless/_execute' -H 'Content-Type: application/json' -d '{\"script\":{\"source\":\"return params.x + params.y;\",\"params\":{\"x\":1,\"y\":2}}}'"]),

    ("elasticsearch-script-execution-timeout", "Elasticsearch Script Execution Timeout Error",
     "Fix Elasticsearch script execution timeout error. Resolve script performance issues.",
     "The script execution times out. The script is too complex or processes too many documents.",
     ["Script is computationally expensive", "Script processes too many iterations", "Timeout is set too low"],
     ["curl -X PUT 'localhost:9200/_cluster/settings' -H 'Content-Type: application/json' -d '{\"transient\":{\"script.max_compilations_rate\":\"100/1m\"}}'"]),

    ("elasticsearch-reindex-failed", "Elasticsearch Reindex Failed Error",
     "Fix Elasticsearch reindex failed error. Resolve reindex task failure issues.",
     "The reindex task fails during execution. The source index may be unavailable or the target mapping conflicts.",
     ["Source index is not available", "Target mapping conflicts", "Task was cancelled due to resources"],
     ["curl -X GET 'localhost:9200/_tasks?detailed=true&actions=*reindex*'"]),

    ("elasticsearch-update-by-query-error", "Elasticsearch Update By Query Error",
     "Fix Elasticsearch update by query error. Resolve update by query failure issues.",
     "The update_by_query task fails. Some documents cannot be updated due to conflicts.",
     ["Documents modified by another process", "Script fails for some documents", "Index is read-only"],
     ["curl -X POST 'localhost:9200/myindex/_update_by_query?conflicts=proceed' -H 'Content-Type: application/json' -d '{\"query\":{\"match_all\":{}}}'"]),

    ("elasticsearch-delete-by-query-error", "Elasticsearch Delete By Query Error",
     "Fix Elasticsearch delete by query error. Resolve delete by query failure issues.",
     "The delete_by_query task fails. Documents cannot be deleted due to conflicts or index issues.",
     ["Documents modified during delete", "Index is read-only", "Query matches no documents"],
     ["curl -X POST 'localhost:9200/myindex/_delete_by_query?conflicts=proceed' -H 'Content-Type: application/json' -d '{\"query\":{\"match\":{\"status\":\"inactive\"}}}'"]),

    ("elasticsearch-task-cancelled", "Elasticsearch Task Cancelled Error",
     "Fix Elasticsearch task cancelled error. Resolve task cancellation and timeout issues.",
     "A background task was cancelled. This may be due to timeout, manual cancellation, or resource constraints.",
     ["Task exceeded its timeout", "Task was manually cancelled", "Cluster is under resource pressure"],
     ["curl -X GET 'localhost:9200/_tasks?detailed=true'"]),

    ("elasticsearch-task-not-found", "Elasticsearch Task Not Found Error",
     "Fix Elasticsearch task not found error. Resolve task reference issues.",
     "The requested task does not exist. It may have completed, been cancelled, or the task ID is wrong.",
     ["Task already completed", "Task ID is incorrect", "Task was cancelled and removed"],
     ["curl -X GET 'localhost:9200/_tasks?detailed=true'"]),

    ("elasticsearch-pending-tasks", "Elasticsearch Pending Tasks Error",
     "Fix Elasticsearch pending tasks error. Resolve cluster pending task queue issues.",
     "Too many pending cluster tasks. The cluster cannot process tasks fast enough.",
     ["Cluster state updates are slow", "Too many index operations", "Master node is overloaded"],
     ["curl -X GET 'localhost:9200/_cluster/pending_tasks?pretty'"]),

    ("elasticsearch-snapshot-not-found", "Elasticsearch Snapshot Not Found Error",
     "Fix Elasticsearch snapshot not found error. Resolve snapshot reference issues.",
     "The requested snapshot does not exist. The snapshot may have been deleted or the name is wrong.",
     ["Snapshot was deleted by retention policy", "Snapshot name is misspelled", "Repository does not contain snapshot"],
     ["curl -X GET 'localhost:9200/_snapshot/myrepo/_all?pretty'"]),

    ("elasticsearch-snapshot-in-progress", "Elasticsearch Snapshot In Progress Error",
     "Fix Elasticsearch snapshot in progress error. Resolve concurrent snapshot operation issues.",
     "A snapshot operation is already in progress. Concurrent snapshot operations are not allowed.",
     ["Previous snapshot not completed", "Snapshot restore is in progress", "Delete waiting for snapshot"],
     ["curl -X GET 'localhost:9200/_snapshot/myrepo/_status?pretty'"]),

    ("elasticsearch-snapshot-failed", "Elasticsearch Snapshot Failed Error",
     "Fix Elasticsearch snapshot failed error. Resolve snapshot creation failures.",
     "The snapshot creation fails. The repository may be corrupted, full, or inaccessible.",
     ["Repository storage is full", "Repository is corrupted", "Snapshot includes unsnapshottable indices"],
     ["curl -X GET 'localhost:9200/_snapshot/myrepo/_verify?pretty'"]),

    ("elasticsearch-restore-failed", "Elasticsearch Restore Failed Error",
     "Fix Elasticsearch restore failed error. Resolve snapshot restore failures.",
     "The snapshot restore fails. The indices may already exist, the mapping conflicts, or the repository is unavailable.",
     ["Index already exists", "Mapping conflicts with snapshot", "Repository is unreachable"],
     ["curl -X GET 'localhost:9200/_snapshot/myrepo/_status?pretty'"]),

    ("elasticsearch-repository-not-found", "Elasticsearch Repository Not Found Error",
     "Fix Elasticsearch repository not found error. Resolve snapshot repository reference issues.",
     "The snapshot repository does not exist. The repository was never created or was deleted.",
     ["Repository was never created", "Repository name is misspelled", "Repository was deleted"],
     ["curl -X GET 'localhost:9200/_snapshot/_all'"]),

    ("elasticsearch-repository-verification", "Elasticsearch Repository Verification Error",
     "Fix Elasticsearch repository verification error. Resolve repository connectivity issues.",
     "The repository verification fails. The storage backend is not accessible or the credentials are wrong.",
     ["Storage backend is not accessible", "Credentials are wrong", "Bucket or path does not exist"],
     ["curl -X GET 'localhost:9200/_snapshot/myrepo/_verify?pretty'"]),

    ("elasticsearch-repository-azure", "Elasticsearch Repository Azure Error",
     "Fix Elasticsearch repository Azure error. Resolve Azure Blob Storage repository issues.",
     "The Azure repository fails. The Azure account or container is not accessible.",
     ["Azure account name or key is wrong", "Container does not exist", "Network connectivity to Azure is broken"],
     ["curl -X GET 'localhost:9200/_snapshot/myazure/_verify?pretty'"]),

    ("elasticsearch-repository-gcp", "Elasticsearch Repository GCP Error",
     "Fix Elasticsearch repository GCP error. Resolve GCS repository issues.",
     "The GCS repository fails. The bucket or credentials are not configured correctly.",
     ["GCP bucket does not exist", "Service account key is invalid", "GCP API is not accessible"],
     ["curl -X GET 'localhost:9200/_snapshot/mygcs/_verify?pretty'"]),

    ("elasticsearch-repository-aws", "Elasticsearch Repository AWS Error",
     "Fix Elasticsearch repository AWS error. Resolve S3 repository issues.",
     "The S3 repository fails. The bucket or credentials are not configured correctly.",
     ["S3 bucket does not exist", "AWS credentials are invalid", "IAM role is not configured"],
     ["curl -X GET 'localhost:9200/_snapshot/mys3/_verify?pretty'"]),

    ("elasticsearch-encryption-key-error", "Elasticsearch Encryption Key Error",
     "Fix Elasticsearch encryption key error. Resolve index encryption issues.",
     "The encryption key for encrypted indices is missing or invalid. Encrypted data cannot be read.",
     ["Encryption key is not configured", "Key is wrong for the encrypted index", "Key management plugin is not installed"],
     ["grep 'xpack.security.encryption' /etc/elasticsearch/elasticsearch.yml"]),

    ("elasticsearch-license-expired", "Elasticsearch License Expired Error",
     "Fix Elasticsearch license expired error. Resolve license expiration issues.",
     "The Elasticsearch license has expired. Some features are no longer available.",
     ["License has expired", "License was not renewed", "Trial license expired"],
     ["curl -X GET 'localhost:9200/_license'"]),

    ("elasticsearch-security-not-enabled", "Elasticsearch Security Not Enabled Error",
     "Fix Elasticsearch security not enabled error. Resolve security plugin configuration issues.",
     "Security features are not enabled. The cluster is running without authentication or authorization.",
     ["Security plugin is not enabled", "xpack.security.enabled is false", "Security features are disabled in config"],
     ["grep 'xpack.security.enabled' /etc/elasticsearch/elasticsearch.yml"]),

    ("elasticsearch-user-not-found", "Elasticsearch User Not Found Error",
     "Fix Elasticsearch user not found error. Resolve user authentication issues.",
     "The specified user does not exist in Elasticsearch. The user was never created or was deleted.",
     ["User was never created", "User was deleted", "Username is misspelled"],
     ["curl -X GET 'localhost:9200/_security/_authenticate'"]),

    ("elasticsearch-role-not-found", "Elasticsearch Role Not Found Error",
     "Fix Elasticsearch role not found error. Resolve role configuration issues.",
     "The specified role does not exist. The role was never created or was deleted.",
     ["Role was never created", "Role was deleted", "Role name is misspelled"],
     ["curl -X GET 'localhost:9200/_security/role/myrole'"]),

    ("elasticsearch-privilege-missing", "Elasticsearch Privilege Missing Error",
     "Fix Elasticsearch privilege missing error. Resolve permission issues.",
     "The user does not have the required privilege to perform the action.",
     ["Role does not include the required privilege", "Index pattern does not match", "Application privilege is missing"],
     ["curl -X GET 'localhost:9200/_security/_authenticate'"]),

    ("elasticsearch-api-key-expired", "Elasticsearch API Key Expired Error",
     "Fix Elasticsearch API key expired error. Resolve API key lifecycle issues.",
     "The API key has expired and can no longer be used for authentication.",
     ["API key has expired", "API key was not renewed", "Expiration was set too short"],
     ["curl -X GET 'localhost:9200/_security/_authenticate'"]),

    ("elasticsearch-tls-config-invalid", "Elasticsearch TLS Config Invalid Error",
     "Fix Elasticsearch TLS config invalid error. Resolve TLS configuration issues.",
     "The TLS configuration is invalid. Certificates or keys are misconfigured.",
     ["Certificate file is missing or wrong", "Key file does not match certificate", "TLS protocol version is wrong"],
     ["grep 'xpack.security.transport.ssl' /etc/elasticsearch/elasticsearch.yml"]),

    ("elasticsearch-certificate-expired", "Elasticsearch Certificate Expired Error",
     "Fix Elasticsearch certificate expired error. Resolve certificate lifecycle issues.",
     "The TLS certificate has expired. Nodes cannot establish secure connections.",
     ["Certificate has expired", "Certificate was not renewed", "Certificate validity period is too short"],
     ["openssl x509 -in /etc/elasticsearch/certs/http.crt -noout -dates"]),

    ("elasticsearch-realm-not-configured", "Elasticsearch Realm Not Configured Error",
     "Fix Elasticsearch realm not configured error. Resolve authentication realm issues.",
     "The authentication realm is not configured. Users cannot authenticate against the specified realm.",
     ["Realm is not defined in elasticsearch.yml", "Realm order is wrong", "Realm type is not recognized"],
     ["grep 'xpack.security.authc.realms' /etc/elasticsearch/elasticsearch.yml"]),

    ("elasticsearch-native-realm-error", "Elasticsearch Native Realm Error",
     "Fix Elasticsearch native realm error. Resolve native user store issues.",
     "The native realm encounters errors. Users stored in Elasticsearch are not accessible.",
     ["Native realm is not enabled", "Users index is corrupted", "Security index is not available"],
     ["curl -X GET 'localhost:9200/_security/_authenticate'"]),

    ("elasticsearch-ldap-realm", "Elasticsearch LDAP Realm Error",
     "Fix Elasticsearch LDAP realm error. Resolve LDAP authentication issues.",
     "The LDAP realm fails to authenticate users. The LDAP server is unreachable or the configuration is wrong.",
     ["LDAP server is unreachable", "Bind DN or password is wrong", "User search base is incorrect"],
     ["grep 'xpack.security.authc.realms.ldap' /etc/elasticsearch/elasticsearch.yml"]),

    ("elasticsearch-active-directory", "Elasticsearch Active Directory Error",
     "Fix Elasticsearch Active Directory error. Resolve AD authentication issues.",
     "The Active Directory realm fails. Users cannot authenticate against AD.",
     ["AD server is unreachable", "Domain name is wrong", "Group search filter is incorrect"],
     ["grep 'xpack.security.authc.realms.active_directory' /etc/elasticsearch/elasticsearch.yml"]),

    ("elasticsearch-saml-auth", "Elasticsearch SAML Authentication Error",
     "Fix Elasticsearch SAML authentication error. Resolve SSO authentication issues.",
     "SAML authentication fails. The Identity Provider is not reachable or the SAML response is invalid.",
     ["IdP metadata URL is wrong", "SP entityId does not match", "SAML response signature verification failed"],
     ["grep 'xpack.security.authc.realms.saml' /etc/elasticsearch/elasticsearch.yml"]),

    ("elasticsearch-openid-connect", "Elasticsearch OpenID Connect Error",
     "Fix Elasticsearch OpenID Connect error. Resolve OIDC authentication issues.",
     "OpenID Connect authentication fails. The OIDC provider is not reachable or the configuration is wrong.",
     ["OIDC issuer URL is wrong", "Client ID or secret is wrong", "OIDC provider is not accessible"],
     ["grep 'xpack.security.authc.realms.oidc' /etc/elasticsearch/elasticsearch.yml"]),

    ("elasticsearch-anonymous-access", "Elasticsearch Anonymous Access Error",
     "Fix Elasticsearch anonymous access error. Resolve anonymous user configuration issues.",
     "The anonymous user is not configured correctly. Unauthenticated requests are rejected or allowed unexpectedly.",
     ["Anonymous auth is not enabled", "Anonymous role does not have correct permissions", "Anonymous user is misconfigured"],
     ["grep 'xpack.security.authc.anonymous' /etc/elasticsearch/elasticsearch.yml"]),

    ("elasticsearch-audit-log-error", "Elasticsearch Audit Log Error",
     "Fix Elasticsearch audit log error. Resolve audit logging issues.",
     "Audit logging is not working. Audit events are not being recorded.",
     ["Audit logging is not enabled", "Audit log destination is not writable", "Audit event filters are wrong"],
     ["grep 'xpack.security.audit' /etc/elasticsearch/elasticsearch.yml"]),

    ("elasticsearch-watcher-error", "Elasticsearch Watcher Error",
     "Fix Elasticsearch Watcher error. Resolve Watcher execution issues.",
     "Watcher fails to execute or trigger watches. The Watcher service has errors.",
     ["Watcher service is not running", "Watch definition has errors", "Webhook action URL is unreachable"],
     ["curl -X GET 'localhost:9200/_watcher/stats?pretty'"]),

    ("elasticsearch-watch-not-found", "Elasticsearch Watch Not Found Error",
     "Fix Elasticsearch watch not found error. Resolve watch reference issues.",
     "The requested watch does not exist. The watch was deleted or the ID is wrong.",
     ["Watch was deleted", "Watch ID is misspelled", "Watch was never created"],
     ["curl -X GET 'localhost:9200/_watcher/watch/my_watch?pretty'"]),

    ("elasticsearch-alerting-failure", "Elasticsearch Alerting Failure Error",
     "Fix Elasticsearch alerting failure error. Resolve watch trigger and action failures.",
     "Watch triggers or actions fail. The alert conditions are not met or the action endpoint is unreachable.",
     ["Condition is never met", "Action webhook endpoint is down", "Watch schedule is wrong"],
     ["curl -X GET 'localhost:9200/_watcher/watch/my_watch?pretty'"]),

    ("elasticsearch-monitoring-export", "Elasticsearch Monitoring Export Error",
     "Fix Elasticsearch monitoring export error. Resolve monitoring data collection issues.",
     "Monitoring data fails to export to the monitoring cluster. The monitoring exporter is misconfigured.",
     ["Monitoring cluster is unreachable", "Exporter credentials are invalid", "Monitoring index template is missing"],
     ["curl -X GET 'localhost:9200/_cat/indices/.monitoring-*?v'"]),

    ("elasticsearch-ccr-leader-not-found", "Elasticsearch CCR Leader Not Found Error",
     "Fix Elasticsearch CCR leader not found error. Resolve cross-cluster replication leader issues.",
     "The CCR follower cannot connect to the leader cluster. The leader cluster is unreachable or the index does not exist.",
     ["Leader cluster is not accessible", "Remote cluster connection not configured", "Leader index does not exist"],
     ["curl -X GET 'localhost:9200/_remote/info?pretty'"]),

    ("elasticsearch-ccr-follower", "Elasticsearch CCR Follower Error",
     "Fix Elasticsearch CCR follower error. Resolve follower replication issues.",
     "The CCR follower index falls behind or stops replicating. The follower cannot keep up with the leader.",
     ["Follower is lagging behind leader", "Network to leader is lost", "Follower settings are incorrect"],
     ["curl -X GET 'localhost:9200/myindex/_ccr/stats?pretty'"]),

    ("elasticsearch-ccs-remote-cluster", "Elasticsearch Cross Cluster Search Error",
     "Fix Elasticsearch cross-cluster search error. Resolve CCS configuration issues.",
     "Cross-cluster search fails. The remote cluster is not connected or the index name is wrong.",
     ["Remote cluster is not configured", "Remote connection timed out", "Index pattern does not match"],
     ["curl -X GET 'localhost:9200/_remote/info?pretty'"]),

    ("elasticsearch-remote-cluster-not-connected", "Elasticsearch Remote Cluster Not Connected Error",
     "Fix Elasticsearch remote cluster not connected error. Resolve remote cluster connectivity issues.",
     "The remote cluster connection is not established. Nodes cannot communicate across clusters.",
     ["Remote seed nodes are unreachable", "Firewall blocks connection", "Cluster credentials are invalid"],
     ["curl -X GET 'localhost:9200/_remote/info?pretty'"]),

    ("elasticsearch-ilm-policy-not-found", "Elasticsearch ILM Policy Not Found Error",
     "Fix Elasticsearch ILM policy not found error. Resolve index lifecycle management issues.",
     "The ILM policy does not exist. Indices cannot follow a lifecycle without a valid policy.",
     ["ILM policy was never created", "Policy name is misspelled", "Policy was deleted"],
     ["curl -X GET 'localhost:9200/_ilm/policy?pretty'"]),

    ("elasticsearch-rollover-failed", "Elasticsearch Rollover Failed Error",
     "Fix Elasticsearch rollover failed error. Resolve ILM rollover issues.",
     "The ILM rollover action fails. The write alias is missing or the rollover conditions are not met.",
     ["Index does not have a write alias", "Rollover conditions not met", "Index is not in hot phase"],
     ["curl -X GET 'localhost:9200/myindex/_ilm/explain?pretty'"]),

    ("elasticsearch-shrink-index-error", "Elasticsearch Shrink Index Error",
     "Fix Elasticsearch shrink index error. Resolve index shrink operation issues.",
     "The shrink index operation fails. The source index is not read-only or has non-relocatable shards.",
     ["Source index is not read-only", "Source index has replicas", "Not enough disk space on target"],
     ["curl -X POST 'localhost:9200/myindex/_shrink/myindex-shrunk' -H 'Content-Type: application/json' -d '{\"settings\":{\"index.number_of_replicas\":0,\"index.number_of_shards\":1,\"index.blocks.write\":true}}'"]),

    ("elasticsearch-force-merge-error", "Elasticsearch Force Merge Error",
     "Fix Elasticsearch force merge error. Resolve force merge operation issues.",
     "The force merge operation fails or takes too long. The index may be too large or the node is under load.",
     ["Index has too many segments", "Node is under heavy load", "Force merge on busy index"],
     ["curl -X POST 'localhost:9200/myindex/_forcemerge?max_num_segments=1'"]),

    ("elasticsearch-freeze-index", "Elasticsearch Freeze Index Error",
     "Fix Elasticsearch freeze index error. Resolve frozen index issues.",
     "The freeze index operation fails. The index may be in a state that cannot be frozen.",
     ["Index is already frozen", "Index has open searches", "Index is part of a data stream"],
     ["curl -X POST 'localhost:9200/myindex/_freeze'"]),

    ("elasticsearch-unfreeze-index", "Elasticsearch Unfreeze Index Error",
     "Fix Elasticsearch unfreeze index error. Resolve unfreeze operation issues.",
     "The unfreeze operation fails. The index may not be frozen or is in an invalid state.",
     ["Index is not frozen", "Index is corrupted", "Unfreeze conflicts with ILM actions"],
     ["curl -X POST 'localhost:9200/myindex/_unfreeze'"]),

    ("elasticsearch-cold-data-node", "Elasticsearch Cold Data Node Error",
     "Fix Elasticsearch cold data node error. Resolve cold tier node issues.",
     "Data cannot be moved to the cold tier. The cold tier nodes are unavailable or misconfigured.",
     ["Cold tier nodes are not available", "ILM cold phase not configured", "Node roles do not include data_cold"],
     ["curl -X GET 'localhost:9200/_cat/nodes?v&h=name,node.role,attr'"]),

    ("elasticsearch-frozen-data-node", "Elasticsearch Frozen Data Node Error",
     "Fix Elasticsearch frozen data node error. Resolve frozen tier node issues.",
     "Data cannot be moved to the frozen tier. The frozen tier nodes are unavailable or misconfigured.",
     ["Frozen tier nodes are not available", "ILM frozen phase not configured", "Searchable snapshots not configured"],
     ["curl -X GET 'localhost:9200/_cat/nodes?v&h=name,node.role'"]),

    ("elasticsearch-deprecation-warning", "Elasticsearch Deprecation Warning Error",
     "Fix Elasticsearch deprecation warning error. Resolve API deprecation issues.",
     "Deprecated API usage generates warnings. The application uses APIs that will be removed in future versions.",
     ["Using deprecated mapping types", "Using deprecated query syntax", "Using deprecated settings"],
     ["curl -X GET 'localhost:9200/_nodes/stats/indices.deprecation?pretty'"]),

    ("elasticsearch-upgrade-assistant", "Elasticsearch Upgrade Assistant Error",
     "Fix Elasticsearch upgrade assistant error. Resolve version upgrade issues.",
     "The upgrade assistant finds issues that prevent upgrading to a newer version.",
     ["Index mappings use deprecated features", "Settings are incompatible", "Plugins are not compatible"],
     ["curl -X GET 'localhost:9200/_migration/assistant?pretty'"]),

    ("elasticsearch-feature-migration", "Elasticsearch Feature Migration Error",
     "Fix Elasticsearch feature migration error. Resolve feature migration issues.",
     "Feature migration fails. System features need to be migrated to a new format before upgrading.",
     ["Feature migration is in progress", "Migration encounters incompatible data", "Migration plugin is not installed"],
     ["curl -X GET 'localhost:9200/_migration/feature?pretty'"]),
]

def make_page(slug, title, desc, body, causes, fixes, examples):
    lines = [
        '---',
        f'title: "[Solution] {title}"',
        f'description: "{desc}"',
        'tools: ["elasticsearch"]',
        'error-types: ["tool-error"]',
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
        '- [Elasticsearch Cluster Error]({{< relref "/tools/elasticsearch/elasticsearch-cluster-error" >}})',
        '- [Elasticsearch Index Error]({{< relref "/tools/elasticsearch/elasticsearch-index-error" >}})',
        '- [Elasticsearch Query Error]({{< relref "/tools/elasticsearch/elasticsearch-query-error" >}})',
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
print(f"Total .md files in elasticsearch/: {total}")
