# Author: Daniel Benjamin Perez Morales
# GitHub: https://github.com/DanielBenjaminPerezMoralesDev13
# Gitlab: https://gitlab.com/DanielBenjaminPerezMoralesDev13
# Email: danielperezdev@proton.me

from typing import Dict, Any
from toml import loads

flexoki: Dict[str, Any] = loads(s = """\
    # based on https//stephango.com/flexoki and https//github.com/kepano/flexoki/tree/main/alacritty

    # Default colors
    [colors.primary]
    background = '#282726'
    foreground = '#FFFCF0'
    dim_foreground = '#FFFCF0'
    bright_foreground = '#FFFCF0'

    # Cursor colors
    [colors.cursor]
    text = '#FFFCF0'
    cursor = '#FFFCF0'

    # Normal colors
    [colors.normal]
    black = '#100F0F'
    red = '#AF3029'
    green = '#66800B'
    yellow = '#AD8301'
    blue = '#205EA6'
    magenta = '#A02F6F'
    cyan = '#24837B'
    white = '#FFFCF0'

    # Bright colors
    [colors.bright]
    black = '#100F0F'
    red = '#D14D41'
    green = '#879A39'
    yellow = '#D0A215'
    blue = '#4385BE'
    magenta = '#CE5D97'
    cyan = '#3AA99F'
    white = '#FFFCF0'

    # Dim colors
    [colors.dim]
    black = '#100F0F'
    red = '#AF3029'
    green = '#66800B'
    yellow = '#AD8301'
    blue = '#205EA6'
    magenta = '#A02F6F'
    cyan = '#24837B'
    white = '#FFFCF0'
    """
)