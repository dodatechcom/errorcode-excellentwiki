---
title: "[Solution] R gganimate Animation Error"
description: "gganimate animation errors."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R gganimate Animation Error

gganimate animation errors.

### Common Causes
Missing transition; wrong easing

### How to Fix
```r
library(gganimate)
ggplot(mtcars, aes(wt, mpg)) +
  geom_point() +
  transition_states(cyl)
```

### Examples
```r
anim <- ggplot(mtcars, aes(wt, mpg)) +
  geom_point() +
  transition_time(cyl)
anim_save("scatter.gif", anim)
```
