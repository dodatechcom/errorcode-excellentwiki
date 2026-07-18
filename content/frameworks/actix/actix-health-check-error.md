---
title: "[Solution] Actix Health Check Error — How to Fix"
description: "Fix Actix health check errors. Resolve readiness and liveness probe failures."
frameworks: ["actix"]
error-types: ["monitoring-error"]
severities: ["warning"]
weight: 5
comments: true
---

An Actix health check error occurs when health endpoints fail or return incorrect status.

## Why It Happens

Health check errors happen due to missing health endpoints, incorrect status codes, or missing dependency checks.

## Common Error Messages

```
health check failed
```

```
readiness probe failed
```

```
liveness probe failed
```

```
service unavailable
```

## How to Fix It

### 1. Add Health Endpoints

Create readiness and liveness probes.

```rust
async fn healthz() -> HttpResponse {
    HttpResponse::Ok().json(serde_json::json!({"status": "ok"}))
}

async fn readyz(pool: web::Data<PgPool>) -> HttpResponse {
    if sqlx::query("SELECT 1").execute(pool.get_ref()).await.is_err() {
        return HttpResponse::ServiceUnavailable().json(serde_json::json!({"status": "not ready"}));
    }
    HttpResponse::Ok().json(serde_json::json!({"status": "ready"}))
}
```

### 2. Check Dependencies

Verify database, Redis, etc.

```rust
async fn readyz(data: web::Data<AppState>) -> HttpResponse {
    let checks = serde_json::json!({
        "db": check_db(&data.db).await,
        "redis": check_redis(&data.redis).await,
    });
    HttpResponse::Ok().json(checks)
}
```

### 3. Add Timeout to Health Checks

Don't let health checks hang.

```rust
async fn check_db(pool: &PgPool) -> bool {
    tokio::time::timeout(Duration::from_secs(2), sqlx::query("SELECT 1").execute(pool))
        .await
        .is_ok()
}
```

### 4. Return Proper Status Codes

Use 200 for healthy, 503 for unhealthy.

```rust
HttpResponse::Ok().json(serde_json::json!({"status": "healthy"}))
HttpResponse::ServiceUnavailable().json(serde_json::json!({"status": "unhealthy"}))
```

## Common Scenarios

**Scenario 1: Health check always fails.**
Check dependency availability.

**Scenario 2: Health check slow.**
Add timeouts to checks.

## Prevent It

1. **Implement both liveness and readiness.**


2. **Add dependency checks.**


3. **Set timeouts on health checks.**


