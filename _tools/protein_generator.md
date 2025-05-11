---
title: Generate Recipe Lists
private: true  # This is just a note to yourself — GitHub Pages doesn't use it
---

> ⚠️ This file is not for public viewing — it helps generate the list of recipes for each category.  
> Copy the rendered output below into the respective category markdown files (`protein_xxx.md`).


# Beans

```dataview
LIST WITHOUT ID "[" + title + "]" + "(" + file.path + ")"
FROM "recipes"
WHERE contains(protein, "Beans")
SORT title ASC
```

# Cheese
```dataview
LIST WITHOUT ID "[" + title + "]" + "(" + file.path + ")"
FROM "recipes"
WHERE contains(protein, "Cheese")
SORT title ASC
```

# Chickpea

```dataview
LIST WITHOUT ID "[" + title + "]" + "(" + file.path + ")"
FROM "recipes"
WHERE contains(protein, "Chickpea")
SORT title ASC
```

# Eggs

```dataview
LIST WITHOUT ID "[" + title + "]" + "(" + file.path + ")"
FROM "recipes"
WHERE contains(protein, "Eggs")
SORT title ASC
```

# Lentils

```dataview
LIST WITHOUT ID "[" + title + "]" + "(" + file.path + ")"
FROM "recipes"
WHERE contains(protein, "Lentils")
SORT title ASC
```

# Mushroom
```dataview
LIST WITHOUT ID "[" + title + "]" + "(" + file.path + ")"
FROM "recipes"
WHERE contains(protein, "Mushroom")
SORT title ASC
```

# Nuts & Seeds

```dataview
LIST WITHOUT ID "[" + title + "]" + "(" + file.path + ")"
FROM "recipes"
WHERE contains(protein, "Nuts & Seeds")
SORT title ASC
```

# Tofu

```dataview
LIST WITHOUT ID "[" + title + "]" + "(" + file.path + ")"
FROM "recipes"
WHERE contains(protein, "Tofu")
SORT title ASC
```
