---
title: Generate Category Lists
private: true
---

> ⚠️ This file is not for public viewing — it helps generate the list of bread recipes using Dataview.  
> Copy the rendered output below into the relevant `category/xxx.md` file. 
> Make sure you replace / remove 'app://obsidian.md' from the paths which are pasted and replace with '..' to ensure relative paths are maintained


# Appetisers & Sides

```dataview
LIST WITHOUT ID "[" + title + "]" + "(../recipes/" + file.name + ".md)"
FROM "recipes"
WHERE category = [[appetisers_sides]]
SORT title ASC
```

# Condiment

```dataview
LIST WITHOUT ID "[" + title + "]" + "(../recipes/" + file.name + ".md)"
FROM "recipes"
WHERE category = [[condiment]]
SORT title ASC
```

# Curry

```dataview
LIST WITHOUT ID "[" + title + "]" + "(../recipes/" + file.name + ".md)"
FROM "recipes"
WHERE category = [[curry]]
SORT title ASC
```

# Drink

```dataview
LIST WITHOUT ID "[" + title + "]" + "(../recipes/" + file.name + ".md)"
FROM "recipes"
WHERE category = [[drink]]
SORT title ASC
```

# Grains & Rice

```dataview
LIST WITHOUT ID "[" + title + "]" + "(../recipes/" + file.name + ".md)"
FROM "recipes"
WHERE category = [[grains_rice]]
SORT title ASC
```

# Main

```dataview
LIST WITHOUT ID "[" + title + "]" + "(../recipes/" + file.name + ".md)"
FROM "recipes"
WHERE category = [[main]]
SORT title ASC
```

# Noodles

```dataview
LIST WITHOUT ID "[" + title + "]" + "(../recipes/" + file.name + ".md)"
FROM "recipes"
WHERE category = [[noodles]]
SORT title ASC
```

# Meat

```dataview
LIST WITHOUT ID "[" + title + "]" + "(../recipes/" + file.name + ".md)"
FROM "recipes"
WHERE category = [[meat]]
SORT title ASC
```

# Pie

```dataview
LIST WITHOUT ID "[" + title + "]" + "(../recipes/" + file.name + ".md)"
FROM "recipes"
WHERE category = [[pie]]
SORT title ASC
```

# Pasta

```dataview
LIST WITHOUT ID "[" + title + "]" + "(../recipes/" + file.name + ".md)"
FROM "recipes"
WHERE category = [[pasta]]
SORT title ASC
```

# Salad

```dataview
LIST WITHOUT ID "[" + title + "]" + "(../recipes/" + file.name + ".md)"
FROM "recipes"
WHERE category = [[salad]]
SORT title ASC
```

# Savoury Treat

```dataview
LIST WITHOUT ID "[" + title + "]" + "(../recipes/" + file.name + ".md)"
FROM "recipes"
WHERE category = [[savoury]]
SORT title ASC
```

# Seafood

```dataview
LIST WITHOUT ID "[" + title + "]" + "(../recipes/" + file.name + ".md)"
FROM "recipes"
WHERE category = [[seafood]]
SORT title ASC
```

# Slow Cooker

```dataview
LIST WITHOUT ID "[" + title + "]" + "(../recipes/" + file.name + ".md)"
FROM "recipes"
WHERE category = [[slow_cooker]]
SORT title ASC
```

# Soup

```dataview
LIST WITHOUT ID "[" + title + "]" + "(../recipes/" + file.name + ".md)".name + ".md)"
FROM "recipes"
WHERE category = [[soup]]
SORT title ASC
```

# Sourdough

```dataview
LIST WITHOUT ID "[" + title + "]" + "(../recipes/" + file.name + ".md)"
FROM "recipes"
WHERE category = [[sourdough]]
SORT title ASC
```

# Special Occasion

```dataview
LIST WITHOUT ID "[" + title + "]" + "(../recipes/" + file.name + ".md)"
FROM "recipes"
WHERE category = [[special_occasion]]
SORT title ASC
```

# Sweet Treat

```dataview
LIST WITHOUT ID "[" + title + "]" + "(../recipes/" + file.name + ".md)"
FROM "recipes"
WHERE category = [[sweet]]
SORT title ASC
```
