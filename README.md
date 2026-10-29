# Pantry Pal

A free, responsive kitchen inventory app for tracking what you have, finding recipe ideas and building grocery lists. Built with **React 18 (UMD + Babel Standalone), IndexedDB, Tailwind CSS and Chart.js**.

**Live demo:** https://tabitha-dev.github.io/Pantry_Pal/  
**Source:** https://github.com/tabitha-dev/Pantry_Pal

## Features

- Track quantities and optional expiration dates in your **Pantry**, **Fridge** and **Freezer**.
- Search and filter inventory, add/edit/delete items and see when food is expired or due in seven days.
- Explore recipes from **TheMealDB**, view rough ingredient name matches and add potentially missing ingredients to your shopping list.
- Manually add, check off and remove groceries; review a location-based inventory quantity chart with a text summary.
- Download or restore a JSON backup of your pantry and shopping list.
- Responsive desktop navigation and four-tab mobile navigation, improved keyboard labels and modal behavior.
- Local-first storage: the existing IndexedDB database `pantry-pal-db`, version `1`, with the original `inventory` and `shoppingList` stores is preserved.

## Storage and privacy

Pantry Pal saves your inventory and shopping list **locally on your device in your current browser**. It does not automatically synchronize between phones, desktops or browsers. A JSON backup can be downloaded and restored in another browser. Clearing browser site data, using incognito/private browsing or storage restrictions may lose your data.

Recipe searches are sent to TheMealDB; the app and its CDN-delivered libraries may request internet resources. The first page load and recipe search require network access. **This is not a guaranteed offline-installable PWA.** No account, server database or subscription is required.

Recipe ingredient matching is a simple name comparison, not a nutritional or allergen checker. Always check actual food freshness and food safety rather than relying solely on a date in the app.

## Accessibility, SEO, AEO

- Mobile/desktop responsive layout and navigation, touch-friendly controls, visible focus indicators, keyboard-accessible dialogs with Escape and focus management, form labels, text analytics and reduced motion.
- Descriptive page title, canonical URL, summary metadata, share image, sitemap/robots.txt, WebApplication schema and static explanatory FAQs.
- Automated browser tests across five widths validate representative workflows. A full manual WCAG 2.2 AA and assistive-technology review remains necessary. SEO metadata and FAQ copy do not guarantee indexing or inclusion in AI-generated answers.

## Run locally

```bash
git clone https://github.com/tabitha-dev/Pantry_Pal.git
cd Pantry_Pal
python -m http.server 8000
```

Open http://localhost:8000. No application build step is required, but this version uses Babel Standalone to compile JSX in the browser, so several external CDN scripts must load before the app renders.

## Development notes

The responsive redesign preserves data compatibility with the original IndexedDB schema. The visual refresh uses lightweight CSS-based food art as a fallback until final OpenArt renders are reviewed and optimized; generated mockups are not represented as functional app screenshots.

See [LICENSE](LICENSE).
