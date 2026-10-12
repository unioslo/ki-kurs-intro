# Translation (English version of the course)

This repo produces the course in **two languages from one source**. Norwegian
(Bokmål) is the master content in `source/`; the English version is generated
from gettext translation catalogs under `source/locale/en/`.

You never maintain a second copy of the `.rst` files. When you edit the
Norwegian source, a sync command tells you exactly which paragraphs changed and
need re-translating.

---

## TL;DR

```bash
make html            # build Norwegian site  -> _build/html
make html-en         # build English site    -> _build/html/en
make gettext-update  # after editing Norwegian: refresh English catalogs
```

---

## How it works

- Sphinx i18n (`sphinx-intl`) extracts every translatable string from the
  Norwegian source into `.pot` templates, then into per-file English catalogs
  (`.po`) under `source/locale/en/LC_MESSAGES/`.
- Each `.po` entry pairs a Norwegian string (`msgid`) with its English
  translation (`msgstr`).
- Building with `-D language=en` swaps in the translations. Anything not yet
  translated falls back to the Norwegian original.

Relevant config in `source/conf.py`:

```python
language = 'nb'
locale_dirs = ['locale/']
gettext_compact = False            # one .po per source file (easier review)
gettext_additional_targets = ['raw']  # also translate `raw:: html` blocks
```

---

## Prerequisites

```bash
pip install -r requirements.txt    # includes sphinx-intl
```

(If you use the repo's virtualenv, prefix the commands with it, e.g.
`.venv/bin/sphinx-build`, or pass `SPHINXBUILD=.venv/bin/sphinx-build` to `make`.)

---

## Building

| Command | Output | Language |
| --- | --- | --- |
| `make html` | `_build/html/` | Norwegian (default) |
| `make html-en` | `_build/html/en/` | English |

Open `_build/html/en/index.html` to preview the English site.

---

## Keeping the translation in sync

After you edit the Norwegian `.rst` files:

```bash
make gettext-update
```

This re-extracts strings and merges them into `source/locale/en/`. The result:

- **New** Norwegian paragraphs appear as new, untranslated entries (empty
  `msgstr`).
- **Changed** paragraphs are marked **`fuzzy`** — the old translation is kept as
  a hint but flagged as needing review.
- Unchanged paragraphs keep their translations.

Then edit the affected `.po` files: fill in empty `msgstr` entries and fix the
`fuzzy` ones (remove the `#, fuzzy` comment once corrected). Finally rebuild:

```bash
make html-en
```

Find outstanding work quickly:

```bash
# files with untranslated or fuzzy entries
grep -rl 'msgstr ""' source/locale/en/LC_MESSAGES/
grep -rl 'fuzzy'      source/locale/en/LC_MESSAGES/
```

---

## File layout

```
source/
├── conf.py                     # i18n settings
├── module1..6/*.rst            # Norwegian source (the master content)
└── locale/
    └── en/
        └── LC_MESSAGES/
            ├── index.po
            ├── forside.po
            └── module1../*.po  # one catalog per source file
```

Commit `source/locale/` to git. `_build/` is gitignored.

---

## Custom directive titles (for maintainers)

The `uio-*` directives (`uio-colorbox-*`, `uio-task`, `uio-detail`, etc.) take
their heading/summary as a directive argument. A plain node attribute is invisible
to gettext, so `source/_ext/uio_components.py` adds the title to the doctree as a
translatable, source-stamped paragraph node (`_attach_title`) and reads it back
out at render time (`_resolve_title`). This keeps the Norwegian output unchanged
while making the titles translatable.

**If you add a new `uio-*` directive with a title**, use the same two helpers so
the title gets translated:

```python
def run(self):
    node = uio_whatever()
    self.state.nested_parse(self.content, self.content_offset, node)
    _attach_title(self, node, ' '.join(self.arguments) if self.arguments else 'Default')
    return [node]

def html_visit_uio_whatever(self, node):
    title = _resolve_title(node, 'Default')
    ...
```

Directive **default labels** (shown when no argument is given, e.g. `Oppgave`,
`Refleksjon`) come from the extension code in Norwegian, so both languages extract
the same Norwegian string. Their English translations are set as normal entries in
the `.po` catalogs — edit them there if you want different wording.

---

## Caveats

- **Paragraph-for-paragraph.** gettext assumes the English text mirrors the
  Norwegian structure. It is ideal for a faithful translation; it is *not* suited
  to an English version that restructures or re-sequences content.
- **Typographic quotes.** Directive titles now go through Sphinx smartquotes like
  body text, so straight quotes render as guillemets (`«...»`) in Norwegian and
  curly quotes in English.
- **Images with text.** Screenshots that contain Norwegian UI text are not
  translated by this workflow; they must be recaptured separately if an English
  version is wanted.
