# Author: Daniel Benjamin Perez Morales
# GitHub: https://github.com/DanielBenjaminPerezMoralesDev13
# Gitlab: https://gitlab.com/DanielBenjaminPerezMoralesDev13
# Email: danielperezdev@proton.me

from typing import Dict, Any
from toml import loads

alabaster_dark: Dict[str, Any] = loads(s = """\
    # Colors (Alabaster Dark)
    # author tonsky

    [colors.primary]
    background = '#0E1415'
    foreground = '#CECECE'

    [colors.cursor]
    text = '#0E1415'
    cursor = '#CECECE'

    [colors.normal]
    black = '#0E1415'
    red = '#e25d56'
    green = '#73ca50'
    yellow = '#e9bf57'
    blue = '#4a88e4'
    magenta = '#915caf'
    cyan = '#23acdd'
    white = '#f0f0f0'

    [colors.bright]
    black = '#777777'
    red = '#f36868'
    green = '#88db3f'
    yellow = '#f0bf7a'
    blue = '#6f8fdb'
    magenta = '#e987e9'
    cyan = '#4ac9e2'
    white = '#FFFFFF'
    """
)