# Author: Daniel Benjamin Perez Morales
# GitHub: https://github.com/DanielBenjaminPerezMoralesDev13
# Gitlab: https://gitlab.com/DanielBenjaminPerezMoralesDev13
# Email: danielperezdev@proton.me

from typing import Dict, Any
from toml import loads

github_light: Dict[str, Any] = loads(s = """\
    # github Alacritty Colors

    # Default colors
    [colors.primary]
    background = '#ffffff'
    foreground = '#24292f'

    # Normal colors
    [colors.normal]
    black   = '#24292e'
    red     = '#d73a49'
    green   = '#28a745'
    yellow  = '#dbab09'
    blue    = '#0366d6'
    magenta = '#5a32a3'
    cyan    = '#0598bc'
    white   = '#6a737d'

    # Bright colors
    [colors.bright]
    black   = '#959da5'
    red     = '#cb2431'
    green   = '#22863a'
    yellow  = '#b08800'
    blue    = '#005cc5'
    magenta = '#5a32a3'
    cyan    = '#3192aa'
    white   = '#d1d5da'

    [[colors.indexed_colors]]
    index = 16
    color = '#d18616'

    [[colors.indexed_colors]]
    index = 17
    color = '#cb2431'
    """
)