---
title: "Glance AppWidget Error"
description: "Fix Glance AppWidget configuration and Compose rendering errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Glance AppWidget does not render or update correctly

## Common Causes

- GlanceAppWidget not properly configured
- Widget layout not updating on data change
- Widget click actions not working
- Widget preview not showing in widget picker

## Fixes

- Implement GlanceAppWidget with proper parameters
- Use updateAppWidgetState to update widget data
- Configure click action with actionStartActivity
- Add preview parameter for widget picker

## Code Example

```kotlin
class MyAppWidget : GlanceAppWidget() {
    override suspend fun provideGlance(context: Context, id: GlanceId) {
        provideContent {
            MyAppWidgetContent()
        }
    }
}

@Composable
fun MyAppWidgetContent() {
    val context = LocalContext.current
    GlanceTheme {
        Column(modifier = GlanceModifier.fillMaxSize()) {
            Text("Widget Title")
            Button(
                text = "Refresh",
                onClick = actionRunCallback<RefreshCallback>()
            )
        }
    }
}

// Update widget state:
suspend fun updateWidget(context: Context, id: GlanceId) {
    updateAppWidgetState(context, id) { prefs ->
        prefs["last_update"] = System.currentTimeMillis()
    }
    MyAppWidget().update(context, id)
}
```

# Glance: Compose for AppWidgets
# provideGlance: define widget content
# actionRunActivity: click to open Activity
# actionRunCallback: click to run callback
