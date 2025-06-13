---
title: Generate Category Lists
private: true
---

> ⚠️ This file is not for public viewing — it helps generate the list of receipes in alphabetical order for the A-Z page.


```dataview
LIST WITHOUT ID "[" + title + "]" + "(../recipes/" + file.name + ".md)"
FROM "recipes"
SORT title ASC
```
