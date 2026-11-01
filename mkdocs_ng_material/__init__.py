"""
Make `import material` load mkdocs-ng-material.

mkdocs-ng-material provides the `material` package, but some plugins depend on
the upstream `mkdocs-material` distribution, which installs a package of the
same name. To keep the two from overwriting each other's files,
mkdocs-ng-material installs its package to
`site-packages/mkdocs_ng_material/material/` instead of
`site-packages/material/`, and runs `install()` at interpreter startup: from
`mkdocs_ng_material.start` on Python 3.15+ (PEP 829), and from the import line
in `mkdocs_ng_material.pth` on older versions. From then on `import material`
finds mkdocs-ng-material first, whether or not the upstream package is
installed too. This is the same mechanism MkDocs NG uses for `mkdocs`.

This module is imported by every Python process in the environment, so it must
stay small and must not import the theme itself.
"""

import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))


def _find_root() -> "str | None":
    """Return the directory that contains mkdocs-ng-material's `material` package."""
    # Installed from a wheel: site-packages/mkdocs_ng_material/material/
    if os.path.isfile(os.path.join(_HERE, "material", "__init__.py")):
        return _HERE
    # Source checkout or editable install: <repo>/material/ next to
    # <repo>/mkdocs_ng_material/
    parent = os.path.dirname(_HERE)
    if os.path.isfile(os.path.join(parent, "pyproject.toml")) and os.path.isfile(
        os.path.join(parent, "material", "__init__.py")
    ):
        return parent
    return None


def _path_finder():
    # The standard path-based finder is already on sys.meta_path. Looking it up
    # there avoids importing importlib.machinery (and warnings) at startup.
    for finder in sys.meta_path:
        if getattr(finder, "__name__", None) == "PathFinder":
            return finder
    from importlib.machinery import PathFinder

    return PathFinder


class MaterialFinder:
    """
    A meta path finder that loads the top-level `material` package from `root`.

    Submodules are then found through the package's `__path__` as usual, so
    they're never mixed with files from another `material` package.
    """

    def __init__(self, root: str) -> None:
        self.root = root

    def find_spec(self, fullname, path=None, target=None):
        if fullname != "material":
            return None
        return _path_finder().find_spec(fullname, [self.root])

    def __repr__(self) -> str:
        return f"{type(self).__name__}({self.root!r})"


def install() -> bool:
    """Put the finder first on `sys.meta_path`. Returns True if it's active."""
    if any(type(f).__name__ == "MaterialFinder" for f in sys.meta_path):
        return True
    root = _find_root()
    if root is None:
        return False
    sys.meta_path.insert(0, MaterialFinder(root))
    return True
