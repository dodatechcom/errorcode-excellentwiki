---
title: "[Solution] Erlang Riak Error"
description: "Riak database errors."
languages: ["erlang"]
error-types: ["language-error"]
severities: ["error"]
---

# Erlang Riak Error

Riak database errors.

### Common Causes
Wrong bucket; connection; timeout

### How to Fix
```erlang
{ok, C} = riakc_pb_socket:start_link('127.0.0.1', 8087),
riakc_pb_socket:put(C, riakc_obj:new(bucket, key, value)).
```

### Examples
```erlang
{ok, Obj} = riakc_pb_socket:get(C, bucket, key),
Value = riakc_obj:get_value(Obj).
```
