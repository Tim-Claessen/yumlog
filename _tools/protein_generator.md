---
title: Generate Protein Lists
private: true
---

> ⚠️ This file is not for public viewing — it helps generate the list of recipes for each category.  
> Copy the rendered output below into the respective category markdown files (`protein_xxx.md`).
>  Make sure you replace / remove 'app://obsidian.md' from the paths which are pasted and replace with '..' to ensure relative paths are maintained


# Beans

```dataview
LIST WITHOUT ID "[" + title + "]" + "(../recipes/" + file.name + ".md)"
FROM "recipes"
WHERE contains(protein, "Beans")
SORT title ASC
```

# Cheese

```dataview
LIST WITHOUT ID "[" + title + "]" + "(../recipes/" + file.name + ".md)"
FROM "recipes"
WHERE contains(protein, "Cheese")
SORT title ASC
```

# Chickpea

```dataview
LIST WITHOUT ID "[" + title + "]" + "(../recipes/" + file.name + ".md)"
FROM "recipes"
WHERE contains(protein, "Chickpea")
SORT title ASC
```

# Eggs

```dataview
LIST WITHOUT ID "[" + title + "]" + "(../recipes/" + file.name + ".md)"
FROM "recipes"
WHERE contains(protein, "Eggs")
SORT title ASC
```

# Lentils

```dataview
LIST WITHOUT ID "[" + title + "]" + "(../recipes/" + file.name + ".md)"
FROM "recipes"
WHERE contains(protein, "Lentils")
SORT title ASC
```

# Mushroom

```dataview
LIST WITHOUT ID "[" + title + "]" + "(../recipes/" + file.name + ".md)"
FROM "recipes"
WHERE contains(protein, "Mushroom")
SORT title ASC
```

# Nuts & Seeds

```dataview
LIST WITHOUT ID "[" + title + "]" + "(../recipes/" + file.name + ".md)"
FROM "recipes"
WHERE contains(protein, "Nuts & Seeds")
SORT title ASC
```

# Tofu

```dataview
LIST WITHOUT ID "[" + title + "]" + "(../recipes/" + file.name + ".md)"
FROM "recipes"
WHERE contains(protein, "Tofu")
SORT title ASC
```

# Vegetable

```dataview
LIST WITHOUT ID "[" + title + "]" + "(../recipes/" + file.name + ".md)"
FROM "recipes"
WHERE contains(protein, "Vegetable")
SORT title ASC
```

# Other

```dataview
LIST WITHOUT ID "[" + title + "]" + "(../recipes/" + file.name + ".md)"
FROM "recipes"
WHERE contains(protein, "Other")
SORT title ASC
```
