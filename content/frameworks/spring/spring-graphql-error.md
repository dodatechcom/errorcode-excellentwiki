---
title: "DataFetchingException - GraphQL"
description: "Spring for GraphQL throws DataFetchingException when a GraphQL data fetcher fails"
frameworks: ["spring"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

This error occurs when a GraphQL data fetcher throws an exception while resolving a field. Spring for GraphQL wraps it as `DataFetchingException` and returns it in the GraphQL errors array.

## Common Causes

- Data fetcher throws a runtime exception
- N+1 query problem causing performance issues
- Missing data for non-null fields
- Schema definition does not match the data source
- Authorization check fails during data fetching

## How to Fix

1. Implement `DataFetcherExceptionHandler`:

```java
@Component
public class CustomExceptionHandler implements DataFetcherExceptionHandler {

    @Override
    public CompletableFuture<DataFetcherExceptionResult> handleException(
            DataFetcherExceptionHandlerParameters params) {
        Throwable ex = params.getException();

        DataFetcherExceptionResult result = DataFetcherExceptionResult.newResult()
            .errorGRAPHQL_ERROR()
            .message(ex.getMessage())
            .location(params.getField().getSourceLocation())
            .path(params.getPath())
            .build();

        return CompletableFuture.completedFuture(result);
    }
}
```

2. Use `@SchemaMapping` with error handling:

```java
@Controller
public class UserController {

    @SchemaMapping(typeName = "Query", field = "user")
    public User getUser(@Argument Long id) {
        return userRepository.findById(id)
            .orElseThrow(() -> new DataFetchingException("User not found"));
    }
}
```

3. Handle non-null field errors in the schema:

```graphql
type User {
    id: ID!
    name: String!   # Non-null — error propagates to parent
    email: String    # Nullable — error returns null
}
```

## Examples

```java
@SchemaMapping
public User user(@Argument Long id) {
    throw new DataFetchingException("Database connection failed");
}
// GraphQL response: { "errors": [{"message": "Database connection failed"}] }
```

## Related Errors

- [Batch error]({{< relref "/frameworks/spring/spring-batch-error" >}})
- [Retry error]({{< relref "/frameworks/spring/spring-retry-error" >}})
