# Copyright (c) 2016-2025 Martin Donath <martin.donath@squidfunk.com>

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.

import os
import sys

from colorama import Fore, Style
from pathlib import Path
from sys import stderr

# Check if we're running MkDocs (or mkdocs-ng). This theme is now maintained
# as part of the mkdocs-ng ecosystem. The CLI command remains `mkdocs`.
def is_mkdocs():
    path = Path(sys.argv[0])
    return path.name in ("mkdocs", "mkdocs.exe") or (
        path.name == "__main__.py" and path.parent.name == "mkdocs"
    )

# Print a notice about mkdocs-ng maintainership (once per session)
if is_mkdocs() and not os.getenv("NO_MKDOCS_NG_NOTICE"):
    print(
        "\n"
        f"{Fore.GREEN} │  ℹ  Notice from the mkdocs-ng Material team{Style.RESET_ALL}\n"
        f"{Fore.GREEN} │{Style.RESET_ALL}\n"
        f"{Fore.GREEN} │{Style.RESET_ALL}  This theme is now maintained as part of the mkdocs-ng ecosystem.\n"
        f"{Fore.GREEN} │{Style.RESET_ALL}  Install: pip install mkdocs-ng-material\n"
        f"{Fore.GREEN} │{Style.RESET_ALL}  Docs: https://mkdocs-ng.github.io/mkdocs-material/\n"
        f"{Fore.GREEN} │{Style.RESET_ALL}  GitHub: https://github.com/mkdocs-ng/mkdocs-material\n"
        f"{Style.RESET_ALL}",
        file=stderr
    )

# Disable for subsequent imports
os.environ["NO_MKDOCS_NG_NOTICE"] = "true"
