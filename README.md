# the-agentic-review

This is my personal, blog-like site for reviewing ideas from [The Agentic Review podcast](https://podcasts.apple.com/us/podcast/the-agentic-review/id1895935770), as well as technical news and breakthroughs.

## Sharing reviews as web pages

I plan to share some reviews as rendered HTML pages. A normal GitHub link to an HTML file shows its source, so a rendered page needs to be hosted separately. GitHub Pages is the standard option: once enabled in the repository’s **Settings → Pages**, files published from a selected branch and folder can be viewed at the corresponding Pages URL.

On GitHub’s free plan, the repository must be public, and its Pages site will be public too. Private-repository Pages access may be available on some GitHub Enterprise Cloud plans and can be restricted to organization members. A Pages update usually takes a minute or two to publish.

For a quick, one-off preview of a public repository, services such as [htmlpreview.github.io](https://htmlpreview.github.io/) or [raw.githack.com](https://raw.githack.com/) can render an HTML file without setup. These third-party proxies do not work with private repositories and are not under this project’s control.

Pages-ready reviews should be standalone HTML documents with their required styles and scripts inlined, so each page works as-is. Static reports, explainers, and charts can work well this way. Features that depend on another service—such as Claude artifacts’ shared data, live connectors, or asking Claude questions—will not work on GitHub Pages.
