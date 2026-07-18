@dataclass(slots=True)
class UISettings:
    theme: str = "dark"
    font_family: str = "JetBrains Mono"
    font_size: int = 12
    tab_size: int = 4