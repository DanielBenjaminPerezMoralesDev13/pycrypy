# Author: Daniel Benjamin Perez Morales
# GitHub: https://github.com/DanielBenjaminPerezMoralesDev13
# Gitlab: https://gitlab.com/DanielBenjaminPerezMoralesDev13
# Email: danielperezdev@proton.me

from typing import Dict, Any
from toml import loads

deep_space: Dict[str, Any] = loads(s = """\
    # Source https//github.com/tyrannicaltoucan/vim-deep-space

    # Default colors
    [colors.primary]
    background = '#1b202a'
    foreground = '#9aa7bd'

    # Colors the cursor will use if `custom_cursor_colors` is true
    [colors.cursor]
    text = '#232936'
    cursor = '#51617d'

    # Normal colors
    [colors.normal]
    black = '#1b202a'
    red = '#b15e7c'
    green = '#709d6c'
    yellow = '#b5a262'
    blue = '#608cc3'
    magenta = '#8f72bf'
    cyan = '#56adb7'
    white = '#9aa7bd'

    # Bright colors
    [colors.bright]
    black = '#232936'
    red = '#b3785d'
    green = '#709d6c'
    yellow = '#d5b875'
    blue = '#608cc3'
    magenta = '#c47ebd'
    cyan = '#51617d'
    white = '#9aa7bd'
    """
)