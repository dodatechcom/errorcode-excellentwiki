---
title: "[Solution] GCP Cloud Composer Connection Pool Error"
description: "Fix Cloud Composer connection pool errors. Resolve SQLAlchemy pool exhaustion and Airflow metadata database issues in GCP Composer."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

# GCP Cloud Composer Connection Pool Error

The Cloud Composer Connection Pool error occurs when the Airflow metadata database connection pool is exhausted, preventing DAG scheduling.

## Common Causes

- Too many concurrent DAG runs consume all connections
- Long-running database queries hold connections open
- Pool size is smaller than concurrent worker count
- Celery worker connections exceed pool limits
- Connection pool pre_ping is not enabled

## How to Fix

### 1. Increase pool size
```ini
[database]
sql_alchemy_pool_size = 30
sql_alchemy_pool_recycle = 1800
sql_alchemy_pool_pre_ping = True
```

### 2. Check active connections
```bash
gcloud sql connect INSTANCE_NAME --user=root
SHOW PROCESSLIST;
```

### 3. Restart workers to release connections
```bash
gcloud composer environments run ENV_NAME \
  --location=REGION \
  celery worker -- --purge
```

### 4. Update environment variables
```bash
gcloud composer environments update ENV_NAME \
  --location=REGION \
  --update-env-vars=AIRFLOW__CORE__SQL_ALCHEMY_CONN='...'
```

## Examples

### Monitor pool usage
```python
from sqlalchemy.pool import QueuePool
engine = create_engine(url, poolclass=QueuePool, pool_size=20)
print(engine.pool.status())
```

### Check connection count
```sql
SELECT COUNT(*) as connections
FROM information_schema.processlist
WHERE user = 'airflow';
```

## Related Errors

- [GCP Composer Error]({{< relref "/cloud/gcp/gcp-composer-error" >}})
- [GCP Cloud SQL Error]({{< relref "/cloud/gcp/gcp-cloud-sql-error" >}})
