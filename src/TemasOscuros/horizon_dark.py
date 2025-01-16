# Author: Daniel Benjamin Perez Morales
# GitHub: https://github.com/DanielBenjaminPerezMoralesDev13
# Gitlab: https://gitlab.com/DanielBenjaminPerezMoralesDev13
# Email: danielperezdev@proton.me

from typing import Dict, Any
from toml import loads

horizon_dark: Dict[str, Any] = loads(s = """\
    # Colors (Horizon Dark)

    # Primary colors
    [colors.primary]
    background = '#1c1e26'
    foreground = '#e0e0e0'

    # Normal colors
    [colors.normal]
    black = '#16161c'
    red = '#e95678'
    green = '#29d398'
    yellow = '#fab795'
    blue = '#26bbd9'
    magenta = '#ee64ac'
    cyan = '#59e1e3'
    white = '#d5d8da'

    # Bright colors
    [colors.bright]
    black = '#5b5858'
    red = '#ec6a88'
    green = '#3fdaa4'
    yellow = '#fbc3a7'
    blue = '#3fc4de'
    magenta = '#f075b5'
    cyan = '#6be4e6'
    white = '#d5d8da'
    """
)