# Markdown Cheatsheet

<small>[_back to resources_](README.md)</small>


Every `README.md`, `AI_USAGE.md`, and lab writeup you submit this semester
is Markdown. It's also what renders GitHub file previews, R Markdown/Quarto
prose, and Jupyter notebook text cells. This page is a short intro plus a
basic syntax reference — not exhaustive, just what you'll actually use.

## What is Markdown?

Markdown is a plain-text formatting syntax: you write a few extra
characters around your text (`#`, `*`, `` ` ``, etc.), and a renderer turns
it into formatted output (headings, bold text, lists, links, code blocks)
without you touching a WYSIWYG editor or writing HTML by hand. It was
created in 2004 by John Gruber (with Aaron Swartz), with two goals that
still hold: it should be easy to write, and a raw, unrendered `.md` file
should already be readable as plain text.

That second goal is why it's the default for READMEs and documentation:
a Markdown file is useful whether or not anything ever renders it.

## Cheatsheet

### Headings

```markdown
# Heading 1
## Heading 2
### Heading 3
```

### Emphasis

```markdown
*italic*   or   _italic_
**bold**   or   __bold__
`inline code`
```

### Lists

```markdown
- Unordered item
- Another item
  - Nested item (indent 2 spaces)

1. Ordered item
2. Another item
```

### Links and images

```markdown
[link text](https://example.com)
![alt text](path/to/image.png)
```

### Code blocks

Fenced code blocks (three backticks) preserve formatting and, with a
language tag, get syntax highlighting — use these for any command or code
snippet longer than a few words:

````markdown
```bash
git status
```
````

### Blockquotes

```markdown
> A quoted line, e.g. for calling out a note or caveat.
```

### Tables

```markdown
| Column A | Column B |
|---|---|
| value 1  | value 2  |
```

### Horizontal rule

```markdown
---
```

### Line breaks

Markdown collapses single newlines — a line break in your source doesn't
become one in the rendered output. Leave a **blank line** between
paragraphs to actually start a new paragraph.

## Where you'll use this

- Every lab's `README.md` (and `AI_USAGE.md`) — plain Markdown.
- R Markdown (`.Rmd`) and Jupyter notebook text cells — same Markdown
  syntax, embedded alongside code cells (R Markdown/Quarto add a few
  extensions on top, covered when we get there in Week 3).
- GitHub itself renders `.md` files automatically in the file browser —
  it's why your repo's `README.md` is the first thing a grader (or you,
  six months from now) sees.

## Further reading

- [Daring Fireball: Markdown](https://daringfireball.net/projects/markdown/) —
  John Gruber's original syntax description and philosophy; still the
  reference for "classic" Markdown.
- [CommonMark Spec](https://commonmark.org/) and its interactive
  [Try CommonMark](https://spec.commonmark.org/dingus/) — a precise,
  unambiguous specification for what most modern renderers (including
  GitHub) actually implement.
- [GitHub Flavored Markdown
  Spec](https://github.github.com/gfm/) and [GitHub's own Markdown
  guide](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax) —
  GitHub's extensions (task lists, tables, strikethrough) beyond plain
  Markdown, and how it renders in READMEs, issues, and PRs specifically.
- [The Markdown Guide](https://www.markdownguide.org/) — a more thorough,
  example-heavy reference than this page, including "extended syntax"
  we don't use in this course.

---

*This page draws on [Daring Fireball's original Markdown
syntax](https://daringfireball.net/projects/markdown/syntax) by John
Gruber and the [CommonMark](https://commonmark.org/) and [GitHub Flavored
Markdown](https://github.github.com/gfm/) specifications, condensed to
the syntax used in this course.*
