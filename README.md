# The Agentic Review

Opinionated reviews of agentic software development and software factories, by Itamar Friedman.

**Read the publication:** [coditamar.github.io/the-agentic-review](https://coditamar.github.io/the-agentic-review/)

## Reviews

- [When agents outgrow the infrastructure](https://coditamar.github.io/the-agentic-review/articles/when-agents-outgrow-the-infrastructure.html) — A review of Anthropic’s source-control redesign, and what I would take into a software factory. ([Editable source](articles/when-agents-outgrow-the-infrastructure.html))

## Read, adapt, and challenge

Software factory architecture v14 connects triage, in-session review, decision rationale, portable test/observation plans, and post-deployment verification. It distinguishes local execution from representative verification environments and confirms recovery after corrective deployments. Download the vendor-neutral [SVG](assets/software-factory-architecture-v14.svg) / [PNG](assets/software-factory-architecture-v14.png). The [A4 print edition](assets/software-factory-architecture-v14-a4.pdf) has an overview and five readable detail pages. These are conceptual architectural proposals. They do not describe a company’s internal implementation or product plans.

Each article is a standalone HTML page in `articles/`. The published page has links to propose changes, open an issue, and view revision history. To contribute, see [CONTRIBUTING.md](CONTRIBUTING.md).

## Local preview

Python 3.11 or newer is enough. There are no third-party dependencies.

```sh
python3 scripts/check_site.py
python3 -m http.server 8000
```

Open `http://localhost:8000/`. To assemble an isolated preview of the reading pages and assets:

```sh
python3 scripts/build_site.py
```

The generated `_site/` contains the reading pages and assets for an isolated local preview. GitHub Pages publishes directly from **main / (root)**, using its built-in branch deployment. The `.nojekyll` file preserves the plain HTML site. Accepted article changes publish automatically; run the local checks before merging a pull request. There is no custom Actions workflow or automated PR check in this initial setup.

## License

The repository retains its original [CC0 1.0 Universal license](LICENSE).
