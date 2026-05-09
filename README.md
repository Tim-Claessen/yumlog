# Tim & Zoe's Yumlog

**Zoe & Tim's favourite recipes**

**Yumlog** is a cookbook for the foods we love making: easy to search, browse by category or protein, or skim A–Z. Built with [Jekyll](https://jekyllrb.com/) and hosted on [GitHub Pages](https://pages.github.com/).

## Table of contents

- [Live site](#live-site)
- [Contributing](#contributing)
- [Local development](#local-development)
- [Layout and theming](#layout-and-theming)
- [Developer tools](#developer-tools)
- [Line endings](#line-endings)
- [To-do](#to-do)
- [Credits](#credits)
- [License](#license)

## Live site

[https://tim-claessen.github.io/yumlog](https://tim-claessen.github.io/yumlog)

## Contributing

Share a recipe via the Google Form:

[Submit a recipe](https://forms.gle/Fj8Szehe23sCvq6GA)

Submissions are reviewed before they appear on the site. Please credit sources when a recipe is adapted or inspired elsewhere.

## Local development

From the repo root:

```bash
bundle exec jekyll serve
```

Then open the URL Jekyll prints (often `http://127.0.0.1:4000/yumlog/` when using the configured `baseurl`).

If you do not use Bundler, `jekyll serve` works once Jekyll is installed. The site uses default GitHub Pages–friendly Jekyll settings (no custom Ruby gems in-repo).

## Layout and theming

| Piece | Role |
|--------|------|
| `_layouts/default.html` | Site shell: header (nav, search, theme toggle), footer, client-side search from `search.json`. |
| `_layouts/home.html` | Home page: hero, search, recent recipes, category/protein chips, optional submit CTA. |
| `_layouts/recipe.html` | Recipe pages: metadata row (category, protein, times, source), then Markdown body. |
| `_includes/recipe-card.html` | Reusable recipe card (used on home and in search results markup). |
| `assets/css/tokens.css` | Design tokens (colours, type scale, motion, elevations). Light defaults on `:root`; `[data-theme="dark"]` overrides. |
| `assets/css/main.css` | Layout and components. |
| `assets/css/print.css` | Print styles for recipes (`media="print"`). |

Copy for the home hero comes from `_config.yml` (`title`, `description`, `home_lead`, `submit_recipe_url`). Prefer new colours as CSS variables in `tokens.css`, not hardcoded in components.

## Developer tools

The `_tools/` directory has Python helpers for search index generation, index pages, form import, and images. See [_tools/README.md](_tools/README.md).

GitHub Actions (`.github/workflows/process_recipes.yml`) can import form submissions and refresh indexes; the live site is still built by GitHub Pages’ Jekyll when you push to `main`.

## Line endings

The repo uses `.gitattributes` with `* text=auto eol=lf` so text files normalize to LF. After cloning on Windows, use `git add --renormalize .` if you see whole-file CRLF diffs.

## To-do

- Improve the AI recipe generator experience (`ai_generator.md`)
- Test and refine GitHub Actions automation
- Optional: brief per-recipe descriptions in front matter

## Credits

Thanks to everyone whose cooking and writing inspired these recipes. Contributor acknowledgments: [Credits.md](Credits.md).

## License

[MIT License](LICENSE).
