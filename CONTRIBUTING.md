# Contribute to The Agentic Review

Challenge an assumption, fix a factual error, improve an explanation, or suggest a useful diagram. A clear disagreement is welcome.

## Propose a change

1. Follow **Suggest a change** on an article, or open the HTML file in `articles/` on GitHub and choose **Edit**. GitHub will guide you through creating a fork if needed.
2. Edit the article's text inside `<article class="prose">`. Keep the surrounding HTML intact. The HTML file is the canonical article source: there is no second copy to synchronize.
3. Open a pull request describing what should change and why. For factual claims, link to a primary source. Distinguish a source's claims from your interpretation.

For a larger disagreement, [open an issue](https://github.com/coditamar/the-agentic-review/issues/new) before rewriting. Contributions remain proposals until accepted by the maintainer.

## Voice and editorial approach

Keep the author's first-person perspective and cohesive paragraphs. Be concrete, explain the implications, and make room for uncertainty where it changes the conclusion. Avoid unsupported claims, invented quotes, private information, and promotional language. Preserve the source and scope note. Disclose relevant conflicts when proposing substantive additions.

## Preview and validate

No package installation or build step is required. From the repository root:

```sh
python3 scripts/check_site.py
python3 -m http.server 8000
```

Open `http://localhost:8000/`. Check desktop and narrow-screen reading, links, keyboard focus, headings, and the print layout. The automated check covers local links, fragments, basic article structure, and preview file selection; it does not verify external sources or judge the writing.

## Add a review

Copy an article under `articles/` using a descriptive, stable filename. Update the title, description, canonical URL, social metadata, author/date, article navigation, source links, revision links, and contribution links. Give each section a stable unique ID, and include a single main heading. Add an entry to `index.html`; newest reviews go first. Shared styles live in `assets/style.css`.

Keep primary sources close to the claims they support. Create original diagrams or use appropriately licensed assets with attribution. Do not reproduce source articles or their illustrations. The repository's existing [CC0 license](LICENSE) applies to contributions.

## Publication

The maintainer should run the local site checks before accepting a pull request. GitHub Pages publishes directly from `main / (root)` after a merge, with no custom workflow or separate generated article copy. All tracked content is public, including documentation and validation scripts. Keep secrets and working context out of the repository. Published changes remain traceable through Git history.
