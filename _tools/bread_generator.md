---
title: Generate Bread Recipe List
private: true  # This is just a note to yourself — GitHub Pages doesn't use it
category: Bread
---

> ⚠️ This file is not for public viewing — it helps generate the list of bread recipes using Dataview.  
> Copy the rendered output below into `categories/bread.md`.

```dataview
list from "_recipes"
where category = "Bread"
sort title asc
```

