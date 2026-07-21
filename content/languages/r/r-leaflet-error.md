---
title: "[Solution] R leaflet Map Error"
description: "leaflet interactive map errors."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R leaflet Map Error

leaflet interactive map errors.

### Common Causes
Invalid coords; missing package

### How to Fix
```r
library(leaflet)
leaflet() %>%
  addTiles() %>%
  addMarkers(lng = -73.99, lat = 40.73)
```

### Examples
```r
leaflet() %>%
  addTiles() %>%
  addCircleMarkers(lng = lon, lat = lat, data = df)
```
