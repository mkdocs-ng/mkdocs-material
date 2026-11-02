<p align="center">
  <a href="https://mkdocs-ng.github.io/mkdocs-material/">
    <img src="https://raw.githubusercontent.com/mkdocs-ng/mkdocs-material/main/.github/assets/logo.svg" width="320" alt="MkDocs NG Material">
  </a>
</p>

<p align="center">
  <strong>MkDocs NG Material</strong><br>
  Material for MkDocs, maintained for
  <a href="https://github.com/mkdocs-ng/mkdocs">MkDocs NG</a>
</p>

<p align="center">
  <a href="https://github.com/mkdocs-ng/mkdocs-material/actions/workflows/build.yml"><img
    src="https://github.com/mkdocs-ng/mkdocs-material/actions/workflows/build.yml/badge.svg"
    alt="Build"
  /></a>
  <a href="https://pypi.org/project/mkdocs-ng-material"><img
    src="https://img.shields.io/pypi/v/mkdocs-ng-material.svg"
    alt="Python Package Index"
  /></a>
  <a href="https://pypistats.org/packages/mkdocs-ng-material"><img
    src="https://img.shields.io/pypi/dm/mkdocs-ng-material.svg"
    alt="Downloads"
  /></a>
</p>

MkDocs NG Material is a community-maintained fork of [Material for MkDocs] by
Martin Donath, published on PyPI as `mkdocs-ng-material` and part of the
[MkDocs NG] project.
It exists so that sites built on MkDocs keep getting security and bug fixes.

How it differs from upstream:

- **Security, bug and compatibility fixes.** Upstream fixes are ported as
  they are released; there are no new features of its own.
- **Installs alongside upstream.** The theme lives in its own package, so it
  does not clash with `mkdocs-material` when a plugin pulls that in.
- **Built on MkDocs NG.** It depends on `mkdocs-ng` and requires Python 3.10
  or newer.
- `mkdocs-redirects` stays in the `[recommended]` extra.

Everything else, including configuration and the `material` theme name, is the
same as upstream, so switching is a one-line change in your requirements.

  [Material for MkDocs]: https://github.com/squidfunk/mkdocs-material
  [MkDocs NG]: https://github.com/mkdocs-ng

## Everything you would expect

### It's just Markdown

Focus on the content of your documentation and create a professional static site
in minutes. No need to know HTML, CSS or JavaScript – let Material for MkDocs do
the heavy lifting for you.

### Works on all devices

Serve your documentation with confidence – Material for MkDocs automatically
adapts to perfectly fit the available screen estate, no matter the type or size
of the viewing device. Desktop. Tablet. Mobile. All great.

### Made to measure

Make it yours – change the colors, fonts, language, icons, logo, and more with
a few lines of configuration. Material for MkDocs can be easily extended and
provides many options to alter appearance and behavior.

### Fast and lightweight

Don't let your users wait – get incredible value with a small footprint by using
one of the fastest themes available with excellent performance, yielding optimal
search engine rankings and happy users that return.

### Maintain ownership

Own your documentation's complete sources and outputs, guaranteeing both
integrity and security – no need to entrust the backbone of your product
knowledge to third-party platforms. Retain full control.

### Open Source

You're in good company – choose a mature and actively maintained solution built
with state-of-the-art Open Source technologies, used by tens of thousands of
projects. Licensed under MIT.

## Quick start

Material for MkDocs can be installed with `pip`:

``` sh
pip install mkdocs-ng-material
```

Add the following lines to `mkdocs.yml`:

``` yaml
theme:
  name: material
```

For detailed installation instructions, configuration options, and a demo, visit
[mkdocs-ng.github.io/mkdocs-material][Material for MkDocs]

  [Material for MkDocs]: https://mkdocs-ng.github.io/mkdocs-material/

## License

MkDocs NG Material is a community-maintained fork of Material for MkDocs.

**MIT License**

Copyright (c) 2016-2025 Martin Donath

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to
deal in the Software without restriction, including without limitation the
rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
sell copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
IN THE SOFTWARE.
