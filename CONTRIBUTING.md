# Contributing to Grunnkurs KI

This document provides guidelines for contributing to the Grunnkurs KI course content, with a focus on the custom UiO directives used throughout the project.

## Overview

This project uses Sphinx with the Read the Docs theme to build course content that is compatible with UiO Canvas. The course content is written in reStructuredText (RST) format and located in the `source/episodes/` directory.

## Custom UiO Directives

The project includes custom Sphinx extensions in the `source/_ext/` directory that provide UiO-specific components. These directives generate HTML following UiO design guidelines from [UiO Canvas design elements](https://www.uio.no/for-ansatte/arbeidsstotte/sta/canvas/veiledninger/utnytt-mulighetene/designelementer.html).

### Canvas Tabs (`canvas_tabs.py`)

Canvas-compatible tabs that use HTML with URL fragments (no JavaScript required).



#### `.. canvas-tabs::`

Container directive for creating tabbed content.

**Usage:**

```rst
.. canvas-tabs::

   .. canvas-tab:: Tab Title 1

      Content for tab 1

   .. canvas-tab:: Tab Title 2

      Content for tab 2
```

**Example result**

<img src="div-support-filer/figs/tabs.png" alt="Screenshot tabs" width="500">


-------------------------

#### `.. canvas-tab:: Tab Title`

Individual tab directive. The title is specified as an argument after the directive.

**Usage:**

```rst
.. canvas-tab:: Introduction

   This is the introduction tab content.
```

-------------------------


### UiO Components (`uio_components.py`)

UiO-specific components that follow the University of Oslo's design guidelines.

#### `.. uio-exercise:: Custom Title`

Exercise container with a task icon. Can include a collapsible solution.

**Default title:** `Oppgave`

**Usage:**

```rst
.. uio-exercise:: Practice Prompting

   Try writing a prompt to generate a summary of this text.

   .. uio-solution::

      Here's an example solution...
```

-------------------------


#### `.. uio-reflect:: Custom Title`

Reflection exercise container with a reflection icon. Can include a collapsible solution.

**Default title:** `Refleksjon`

**Usage:**

```rst
.. uio-reflect:: AI Ethics

   Consider the ethical implications of using AI in your daily work.

   .. uio-solution::

      Some points to consider...
```

**Example result**

<img src="div-support-filer/figs/refleksjon.png" alt="Screenshot reflect" width="500">


-------------------------


#### `.. uio-question:: Custom Title`

Question container with a task icon. Can include a collapsible answer.

**Default title:** `Spørsmål`

**Usage:**

```rst
.. uio-question:: What is a language model?

   How would you explain a language model to a colleague?

   .. uio-answer::

      A language model is...
```

**Example result**

<img src="div-support-filer/figs/spm_svar.png" alt="Screenshot spm og svar" width="500">


-------------------------

#### `.. uio-solution::`

Collapsible solution directive (accordion). Must be nested inside `.. uio-exercise::` or `.. uio-reflect::`.

**Usage:**

```rst
.. uio-solution::

   This content will be hidden behind a "Løsning" (Solution) toggle.
```

-------------------------


#### `.. uio-answer::`

Collapsible answer directive (accordion). Must be nested inside `.. uio-question::`.

**Usage:**

```rst
.. uio-answer::

   This content will be hidden behind a "Svar" (Answer) toggle.
```

-------------------------

#### `.. uio-dont:: Custom Title`

Warning/don't container with a warning icon.

**Default title:** `OBS!`

**Usage:**

```rst
.. uio-dont:: Important Warning

   Never share sensitive personal data with public AI tools.
```

**Example result**

<img src="div-support-filer/figs/dont.png" alt="Screenshot dont" width="500">

-------------------------


#### `.. uio-note:: Custom Title`

Note container with a source icon.

**Default title:** `Merk`

**Usage:**

```rst
.. uio-note:: Additional Information

   UiO provides several AI services for staff and students.
```

-------------------------

#### `.. uio-do:: Custom Title`

Tip/do container with a checkmark icon.

**Default title:** `Tips`

**Usage:**

```rst
.. uio-do:: Best Practice

   Always verify AI-generated content before using it in your work.
```

**Example result**

<img src="div-support-filer/figs/do.png" alt="Screenshot do" width="500">

-------------------------


#### `.. uio-icon-box::`

Generic icon box container. Use this when you need a custom-styled container.

**Usage:**

```rst
.. uio-icon-box::

   .. uio-detail:: More Information

      Additional details that can be collapsed.
```

**Example result**

<img src="div-support-filer/figs/info.png" alt="Screenshot info" width="500">


-------------------------


#### `.. uio-detail:: Summary text`

Details/accordion element using HTML `<details>` and `<summary>` tags.

**Default summary:** `Detaljer`

**Usage:**

```rst
.. uio-detail:: Click to expand

   This content is hidden by default and can be expanded by clicking.
```


## Add figures

You can add figures in the following way:

```rst
.. figure:: ../images/ChatGPT_howLLMswork.png
   :align: center
   :width: 60%
   :alt: LLM text generation illustration
```

-------------------------

## Some Sphinx docs 

- [reStructuredText Primer](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html)
- [Read the Docs Theme Documentation](https://sphinx-rtd-theme.readthedocs.io/)


---

## Building the Documentation

To build the documentation locally:

```bash
cd ki-kurs-intro
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
make html
```

The built HTML will be in `_build/html/episodes`.

---

## Workflow

1. Edit RST files in `source/episodes/`
2. Commit changes to GitHub
3. GitHub Actions will automatically build the HTML files
4. HTML files are stored in the `html-pages` branch
5. Update Canvas pages either manually or via the REST API script

For detailed workflow instructions, see the main [README.md](README.md).

---

## Canvas Compatibility

All custom directives are designed to be compatible with UiO Canvas. The generated HTML:
- Uses UiO-specific CSS classes (`uio-icon-box`, `task`, `reflect`, `source`, `do`, `dont`)
- Avoids JavaScript where possible (tabs use URL fragments)
- Follows UiO design guidelines for accessibility and visual consistency








