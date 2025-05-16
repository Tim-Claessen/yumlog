---
title: Generate Protein Lists
private: true
---

> ⚠️ This file is not for public viewing — it helps generate the list of recipes for each protein category.  
> 
> Copy the rendered output below into the respective category markdown files (`protein_xxx.md`).
> 
>  Make sure you replace / remove 'app://obsidian.md' from the paths which are pasted and replace with '..' to ensure relative paths are maintained


# Beans

```dataview
LIST WITHOUT ID "[" + title + "]" + "(../recipes/" + file.name + ".md)"
FROM "recipes"
WHERE contains(protein,[[beans]])
SORT title ASC
```

# Cheese

```dataview
LIST WITHOUT ID "[" + title + "]" + "(../recipes/" + file.name + ".md)"
FROM "recipes"
WHERE contains(protein,[[cheese]])
SORT title ASC
```

# Chickpea

```dataview
LIST WITHOUT ID "[" + title + "]" + "(../recipes/" + file.name + ".md)"
FROM "recipes"
WHERE contains(protein,[[chickpea]])
SORT title ASC
```

# Eggs

```dataview
LIST WITHOUT ID "[" + title + "]" + "(../recipes/" + file.name + ".md)"
FROM "recipes"
WHERE contains(protein,[[eggs]])
SORT title ASC
```

# Lentils

```dataview
LIST WITHOUT ID "[" + title + "]" + "(../recipes/" + file.name + ".md)"
FROM "recipes"
WHERE contains(protein,[[lentils]])
SORT title ASC
```

# Mushroom

```dataview
LIST WITHOUT ID "[" + title + "]" + "(../recipes/" + file.name + ".md)"
FROM "recipes"
WHERE contains(protein,[[mushroom]])
SORT title ASC
```

# Nuts & Seeds

```dataview
LIST WITHOUT ID "[" + title + "]" + "(../recipes/" + file.name + ".md)"
FROM "recipes"
WHERE contains(protein,[[nuts_seeds]])
SORT title ASC
```

# Tofu

```dataview
LIST WITHOUT ID "[" + title + "]" + "(../recipes/" + file.name + ".md)"
FROM "recipes"
WHERE contains(protein,[[tofu]])
SORT title ASC
```

# Vegetable

```dataview
LIST WITHOUT ID "[" + title + "]" + "(../recipes/" + file.name + ".md)"
FROM "recipes"
WHERE contains(protein,[[vegetable]])
SORT title ASC
```

# Other

```dataview
LIST WITHOUT ID "[" + title + "]" + "(../recipes/" + file.name + ".md)"
FROM "recipes"
WHERE contains(protein,[[other]])
SORT title ASC
```
