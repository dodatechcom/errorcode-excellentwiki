---
title: "ElasticsearchException - Spring Data Elasticsearch"
description: "Spring Data Elasticsearch throws ElasticsearchException when an Elasticsearch operation fails"
frameworks: ["spring"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

This error occurs when Spring Data Elasticsearch fails to execute a query, create an index, or communicate with the Elasticsearch cluster. It throws `ElasticsearchException` with details about the failure.

## Common Causes

- Elasticsearch cluster is unreachable or down
- Index does not exist or mapping is incorrect
- Query DSL syntax error in custom queries
- Document field type mismatch with index mapping
- Cluster health status is RED

## How to Fix

1. Verify Elasticsearch connection in `application.yml`:

```yaml
spring:
  elasticsearch:
    uris: http://localhost:9200
    username: elastic
    password: changeme
```

2. Use repository methods correctly:

```java
public interface ProductRepository extends ElasticsearchRepository<Product, String> {
    List<Product> findByNameContaining(String name);

    @Query("{\"match\": {\"description\": \"?0\"}}")
    List<Product> searchByDescription(String query);
}
```

3. Handle connection failures gracefully:

```java
@Service
public class SearchService {

    private final ProductRepository repository;

    public List<Product> search(String query) {
        try {
            return repository.findByNameContaining(query);
        } catch (ElasticsearchException e) {
            log.error("Search failed: {}", e.getMessage());
            return Collections.emptyList();
        }
    }
}
```

## Examples

```java
// Mapping type mismatch
@Document(indexName = "products")
public record Product(
    @Id String id,
    @Field(type = FieldType.Integer) int price, // mapped as integer
    String name
) { }
// ElasticsearchException: failed to parse field [price]
```

## Related Errors

- [Cache error]({{< relref "/frameworks/spring/cache-error" >}})
- [Data JPA error]({{< relref "/frameworks/spring/data-jpa-error" >}})
