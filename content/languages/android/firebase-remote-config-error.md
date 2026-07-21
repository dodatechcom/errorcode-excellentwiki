---
title: "Remote Config Error"
description: "Fix Firebase Remote Config fetch and activation errors in Android"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Firebase Remote Config does not return updated values or fetch fails

## Common Causes

- Config fetch not called before activation
- Minimum fetch interval not configured
- Default values not set in XML
- Fetch interval too short for production

## Fixes

- Call fetch() then activate() in sequence
- Set appropriate minimumFetchInterval
- Define default values in res/xml/remote_config_defaults.xml
- Use 12 hours for production fetch interval

## Code Example

```kotlin
val remoteConfig = Firebase.remoteConfig

val configSettings = remoteConfigSettings {
    minimumFetchIntervalInSeconds = 3600  // 1 hour for dev
}

remoteConfig.setConfigSettingsAsync(configSettings)
remoteConfig.setDefaultsAsync(R.xml.remote_config_defaults)

remoteConfig.fetchAndActivate()
    .addOnSuccessListener { activated ->
        val value = remoteConfig.getString("welcome_message")
    }
```

# res/xml/remote_config_defaults.xml
<?xml version="1.0" encoding="utf-8"?>
<defaultsMap>
    <entry>
        <key>welcome_message</key>
        <value>Welcome!</value>
    </entry>
</defaultsMap>
