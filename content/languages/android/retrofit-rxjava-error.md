---
title: "Retrofit RxJava Error"
description: "Fix Retrofit RxJava Observable and Single integration errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Retrofit returns wrong type or RxJava subscription causes memory leak

## Common Causes

- Converter not configured for RxJava types
- Observable not subscribed on correct scheduler
- Disposable not cleared on Activity destroy
- Flowable backpressure not handled

## Fixes

- Add RxJava3ConverterFactory to Retrofit
- Subscribe on IO, observe on Main
- Use CompositeDisposable and clear in onDestroy
- Use Flowable for backpressure-sensitive streams

## Code Example

```kotlin
val retrofit = Retrofit.Builder()
    .baseUrl("https://api.example.com/")
    .addConverterFactory(GsonConverterFactory.create())
    .addCallAdapterFactory(RxJava3CallAdapterFactory.create())
    .build()

// Usage:
interface ApiService {
    @GET("users")
    fun getUsers(): Observable<List<User>>
}

// In ViewModel:
val disposable = CompositeDisposable()
disposable.add(
    apiService.getUsers()
        .subscribeOn(Schedulers.io())
        .observeOn(AndroidSchedulers.mainThread())
        .subscribe({ users -> updateUI(users) })
)

// In onDestroy:
disposable.clear()
```

# RxJava3CallAdapterFactory for Observable/Single/Completable
# Subscribe on IO, observe on MainThread
# Clear CompositeDisposable to prevent leaks
