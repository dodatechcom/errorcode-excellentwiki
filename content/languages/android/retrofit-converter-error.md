---
title: "Retrofit Converter Error"
description: "Fix Retrofit converter factory errors for JSON serialization"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Retrofit cannot serialize or deserialize JSON responses

## Common Causes

- Converter factory not added to Retrofit builder
- JSON response does not match data class fields
- Gson/Moshi cannot handle nullable fields
- Wrong converter for response content type

## Fixes

- Add GsonConverterFactory or MoshiConverterFactory to Retrofit builder
- Use @SerializedName or @Json to match field names
- Handle nulls with nullable types in data class
- Verify Content-Type header matches converter

## Code Example

```kotlin
val retrofit = Retrofit.Builder()
    .baseUrl("https://api.example.com/")
    .addConverterFactory(GsonConverterFactory.create())
    .build()

// With Moshi:
val moshi = Moshi.Builder()
    .add(KotlinJsonAdapterFactory())
    .build()

val retrofit = Retrofit.Builder()
    .baseUrl("https://api.example.com/")
    .addConverterFactory(MoshiConverterFactory.create(moshi))
    .build()
```

# For Kotlin data classes, use Moshi with kotlin-codegen
# or Gson with @SerializedName annotations
