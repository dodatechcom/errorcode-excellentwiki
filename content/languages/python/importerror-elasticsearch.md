---
title: "[Solution] Python ImportError: No module named 'elasticsearch' — Fix"
description: "Fix Python ImportError: No module named 'elasticsearch'. Install the elasticsearch-py client with pip and resolve dependency conflicts."
languages: ["python"]
severities: ["error"]
error-types: ["runtime"]
weight: 323
---

# Python ImportError: No module named 'elasticsearch'

The `elasticsearch` package is the official Python client for Elasticsearch. This error means Python cannot locate the package in the current environment.

## Common Causes

```python
# Cause 1: elasticsearch-py not installed
from elasticsearch import Elasticsearch  # ImportError: No module named 'elasticsearch'

# Cause 2: Wrong package name
import elastic_search  # ImportError — no such package exists

# Cause 3: Version mismatch between client and server
# elasticsearch-py 7.x installed but connecting to Elasticsearch 8.x

# Cause 4: Virtual environment mismatch
# Package installed in a different venv than the one activated

# Cause 5: Using async client without dependencies
from elasticsearch import AsyncElasticsearch  # ImportError if aiohttp missing
```

## How to Fix

### Fix 1: Install elasticsearch-py with pip

```bash
pip install elasticsearch

# For a specific version
pip install elasticsearch==8.12.0

# For Elasticsearch 7.x compatibility
pip install elasticsearch==7.17.9
```

### Fix 2: Install in the correct virtual environment

```bash
source venv/bin/activate
pip install elasticsearch
python -c "import elasticsearch; print(elasticsearch.__versionstr__)"
```

### Fix 3: Install with async extras

```bash
pip install elasticsearch[async]
```

## Examples

```python
from elasticsearch import Elasticsearch

es = Elasticsearch("http://localhost:9200")
print(es.info())
```

## Related Errors

- {{< relref "importerror-kibana" >}} — Related Kibana issues
- {{< relref "importerror-requests" >}} — ImportError: requests
- {{< relref "importerror-urllib3" >}} — ImportError: urllib3
