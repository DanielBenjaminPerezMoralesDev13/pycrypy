# Author: Daniel Benjamin Perez Morales
# GitHub: https://github.com/DanielBenjaminPerezMoralesDev13
# Gitlab: https://gitlab.com/DanielBenjaminPerezMoralesDev13
# Email: danielperezdev@proton.me

from typing import Dict, Any
from toml import loads

kanagawa_wave: Dict[str, Any] = loads(s = """\
    # Colors (Kanagawa Wave)
    # Source https//github.com/rebelot/kanagawa.nvim

    [colors.primary]
    background = '#1f1f28'
    foreground = '#dcd7ba'

    [colors.normal]
    black   = '#090618'
    red     = '#c34043'
    green   = '#76946a'
    yellow  = '#c0a36e'
    blue    = '#7e9cd8'
    magenta = '#957fb8'
    cyan    = '#6a9589'
    white   = '#c8c093'

    [colors.bright]
    black   = '#727169'
    red     = '#e82424'
    green   = '#98bb6c'
    yellow  = '#e6c384'
    blue    = '#7fb4ca'
    magenta = '#938aa9'
    cyan    = '#7aa89f'
    white   = '#dcd7ba'

    [colors.selection]
    background = '#2d4f67'
    foreground = '#c8c093'

    [[colors.indexed_colors]]
    index = 16
    color = '#ffa066'

    [[colors.indexed_colors]]
    index = 17
    color = '#ff5d62'
    """
)