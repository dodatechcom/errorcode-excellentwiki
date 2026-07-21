---
title: "[Solution] Flask Cache Timeout Error"
description: "Fix Flask cache timeout errors when cached data expires too quickly or never expires."
frameworks: ["flask"]
error-types: ["cache-error"]
severities: ["error"]
---

Cache timeout errors occur when cached data is not properly managed, leading to stale data or excessive cache misses.

## Common Causes

- Default timeout too short or too long
- Cache not invalidated on data changes
- Different cache backends with different timeout behaviors
- Timeout not set for specific cache operations
- Cache key collisions causing wrong data return

## How to Fix

### Set Appropriate Timeouts

```python
from flask_caching import Cache

cache = Cache(app, config={
    "CACHE_TYPE": "SimpleCache",
    "CACHE_DEFAULT_TIMEOUT": 300,  # 5 minutes
})

@app.route("/data")
@cache.cached(timeout=60)  # 1 minute
def get_data():
    return expensive_query()
```

### Invalidate Cache on Updates

```python
@app.route("/update", methods=["POST"])
def update_data():
    # Update data
    update_data_in_db()
    # Clear cache
    cache.delete_memoized(get_data)
    return {"status": "updated"}
```

### Use Different Timeouts for Different Data

```python
@app.route("/static-data")
@cache.cached(timeout=3600)  # 1 hour for rarely changing data
def static_data():
    return get_static_data()

@app.route("/dynamic-data")
@cache.cached(timeout=30)  # 30 seconds for frequently changing data
def dynamic_data():
    return get_dynamic_data()
```

## Examples

```python
from flask_caching import Cache

cache = Cache(app)

# Bug -- no cache invalidation
@app.route("/products")
@cache.cached(timeout=300)
def get_products():
    return Product.query.all()

@app.route("/products", methods=["POST"])
def create_product():
    # Cache still has old data
    ...

# Fix -- invalidate cache
@app.route("/products", methods=["POST"])
def create_product():
    product = Product(**request.json)
    db.session.add(product)
    db.session.commit()
    cache.delete_memoized(get_products)
    return {"id": product.id}
```
