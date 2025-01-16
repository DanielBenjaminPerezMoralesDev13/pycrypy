# Author: Daniel Benjamin Perez Morales
# GitHub: https://github.com/DanielBenjaminPerezMoralesDev13
# Gitlab: https://gitlab.com/DanielBenjaminPerezMoralesDev13
# Email: danielperezdev@proton.me

from typing import Dict, Any
from toml import loads

falcon: Dict[str, Any] = loads(s = """\
    # falcon colorscheme for alacritty
    # by fenetikm, https//github.com/fenetikm/falcon

    # Default colors
    [colors.primary]
    background = '#020221'
    foreground = '#b4b4b9'

    [colors.cursor]
    text = '#020221'
    cursor = '#ffe8c0'

    # Normal colors
    [colors.normal]
    black   = '#000004'
    red     = '#ff3600'
    green   = '#718e3f'
    yellow  = '#ffc552'
    blue    = '#635196'
    magenta = '#ff761a'
    cyan    = '#34bfa4'
    white   = '#b4b4b9'

    # Bright colors
    [colors.bright]
    black   = '#020221'
    red     = '#ff8e78'
    green   = '#b1bf75'
    yellow  = '#ffd392'
    blue    = '#99a4bc'
    magenta = '#ffb07b'
    cyan    = '#8bccbf'
    white   = '#f8f8ff'
    """
)