---
title: Generate Category Lists
private: true
---

> ⚠️ This file is not for public viewing — it helps generate the list of bread recipes using Dataview.  
> Copy the rendered output below into the relevant `category/xxx.md` file. 
> Make sure you replace / remove 'app://obsidian.md' from the paths which are pasted


# Appetisers & Sides

```dataview
LIST WITHOUT ID "[" + title + "]" + "(../recipes/" + file.name + ".md)"
FROM "recipes"
WHERE category = "Appetisers & Sides"
SORT title ASC
```

# Condiment

```dataview
LIST WITHOUT ID "[" + title + "]" + "(../recipes/" + file.name + ".md)"
FROM "recipes"
WHERE category = "Condiment"
SORT title ASC
```

# Curry

```dataview
LIST WITHOUT ID "[" + title + "]" + "(../recipes/" + file.name + ".md)"
FROM "recipes"
WHERE category = "Curry"
SORT title ASC
```

# Dessert

```dataview
LIST WITHOUT ID "[" + title + "]" + "(../recipes/" + file.name + ".md)"
FROM "recipes"
WHERE category = "Dessert"
SORT title ASC
```

# Drink

```dataview
LIST WITHOUT ID "[" + title + "]" + "(../recipes/" + file.name + ".md)"
FROM "recipes"
WHERE category = "Drink"
SORT title ASC
```

# Grains & Rice

```dataview
LIST WITHOUT ID "[" + title + "]" + "(../recipes/" + file.name + ".md)"
FROM "recipes"
WHERE category = "Grains & Rice"
SORT title ASC
```

# Meat

```dataview
LIST WITHOUT ID "[" + title + "]" + "(../recipes/" + file.name + ".md)"
FROM "recipes"
WHERE category = "Meat"
SORT title ASC
```

# Pasta

```dataview
LIST WITHOUT ID "[" + title + "]" + "(../recipes/" + file.name + ".md)"
FROM "recipes"
WHERE category = "Pasta"
SORT title ASC
```

# Salad

```dataview
LIST WITHOUT ID "[" + title + "]" + "(../recipes/" + file.name + ".md)"
FROM "recipes"
WHERE category = "Salad"
SORT title ASC
```

# Seafood

```dataview
LIST WITHOUT ID "[" + title + "]" + "(../recipes/" + file.name + ".md)"
FROM "recipes"
WHERE category = "Seafood"
SORT title ASC
```

# Slow Cooker

```dataview
LIST WITHOUT ID "[" + title + "]" + "(../recipes/" + file.name + ".md)"
FROM "recipes"
WHERE category = "Slow Cooker"
SORT title ASC
```

# Snack

```dataview
LIST WITHOUT ID "[" + title + "]" + "(../recipes/" + file.name + ".md)"
FROM "recipes"
WHERE category = "Snack"
SORT title ASC
```

# Soup

```dataview
LIST WITHOUT ID "[" + title + "]" + "(../recipes/" + file.name + ".md)".name + ".md)"
FROM "recipes"
WHERE category = "Soup"
SORT title ASC
```

# Sourdough

```dataview
LIST WITHOUT ID "[" + title + "]" + "(../recipes/" + file.name + ".md)"
FROM "recipes"
WHERE category = "Sourdough"
SORT title ASC
```

# Special Occasion

```dataview
LIST WITHOUT ID "[" + title + "]" + "(../recipes/" + file.name + ".md)"
FROM "recipes"
WHERE category = "Special Occasion"
SORT title ASC
```