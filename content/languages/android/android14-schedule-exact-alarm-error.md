---
title: "Exact Alarm Permission Error"
description: "Fix Android 14 exact alarm permission and AlarmManager scheduling errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Exact alarm does not fire on Android 14 because permission is not granted

## Common Causes

- USE_EXACT_ALARM permission not declared
- CanScheduleExactAlarms check not performed
- Alarm not using setExactAndAllowWhileIdle
- Permission revoked by user in settings

## Fixes

- Declare USE_EXACT_ALARM in manifest
- Check canScheduleExactAlarms before setting
- Use setExactAndAllowWhileIdle for alarms
- Handle permission denial gracefully

## Code Example

```kotlin
<!-- AndroidManifest.xml -->
<uses-permission android:name="android.permission.SCHEDULE_EXACT_ALARM" />

// Check permission:
val alarmManager = getSystemService(AlarmManager::class.java)
if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.S) {
    if (alarmManager.canScheduleExactAlarms()) {
        setExactAlarm(alarmManager)
    } else {
        // Redirect to settings
        val intent = Intent(Settings.ACTION_REQUEST_SCHEDULE_EXACT_ALARM)
        startActivity(intent)
    }
}

// Set exact alarm:
alarmManager.setExactAndAllowWhileIdle(
    AlarmManager.RTC_WAKEUP,
    triggerTime,
    pendingIntent
)
```

# SCHEDULE_EXACT_ALARM: normal apps
# USE_EXACT_ALARM: alarm clock apps only
# canScheduleExactAlarms(): check before setting
