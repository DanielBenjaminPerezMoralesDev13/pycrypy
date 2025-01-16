# Author: Daniel Benjamin Perez Morales
# GitHub: https://github.com/DanielBenjaminPerezMoralesDev13
# Gitlab: https://gitlab.com/DanielBenjaminPerezMoralesDev13
# Email: danielperezdev@proton.me

from typing import Dict, Any
from toml import loads

meliora: Dict[str, Any] = loads(s = """\
    [colors.primary]
    background = '#1c1917'
    foreground = '#d6d0cd'
    # Bright and dim foreground colors
    dim_foreground = '#d6d0cd'
    bright_foreground = '#d6d0cd'

    # Cursor colors
    [colors.cursor]
    text = '#1c1917'
    cursor = '#d6d0cd'

    [colors.vi_mode_cursor]
    text = '#1c1917'
    cursor = '#d6d0cd'

    # Search colors
    [colors.search]
    matches = { foreground = '#1c1917', background = '#24201e' }
    focused_match = { foreground = '#1c1917', background = '#2a2522' }

    [colors.footer_bar]
    foreground = '#1c1917'
    background = '#b8aea8'

    # Keyboard regex hints
    [colors.hints]
    start = { foreground = '#1c1917', background = '#c4b392' }
    end = { foreground = '#1c1917', background = '#24201e' }

    # Selection colors
    [colors.selection]
    text = '#d6d0cd'
    background = '#2a2522'

    # Normal colors
    [colors.normal]
    black = '#2a2421'
    red = '#d49191'
    green = '#b6b696'
    yellow = '#c4b392'
    blue = '#9e96b6'
    magenta = '#b696b1'
    cyan = '#98acc8'
    white = '#ddd9d6'

    # Bright colors
    [colors.bright]
    black = '#2e2622'
    red = '#d89393'
    green = '#b9b99b'
    yellow = '#c8b692'
    blue = '#a299b9'
    magenta = '#b997b4'
    cyan = '#9bb0ca'
    white = '#e1dbd9'

    # Dim colors
    [colors.dim]
    black = '#2a2421'
    red = '#d18989'
    green = '#727246'
    yellow = '#c1b090'
    blue = '#9b92b3'
    magenta = '#b393ad'
    cyan = '#95a9c5'
    white = '#e3d5ce'

    [[colors.indexed_colors]]
    index = 16
    color = '#c4b392'

    [[colors.indexed_colors]]
    index = 17
    color = '#ddd9d6'
    """
)