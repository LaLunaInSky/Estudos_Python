from rich.console import Console
from rich.style import Style
from rich.panel import Panel

console = Console()

caixa_001 = Panel(
    "[white]Esse aqui é um painel de exemplo[/]",
    title="[white]Ana[/]",
    style=Style( 
        color="green"
    ),
    expand=False,
    padding=1,
    subtitle="[white]14:10[/]",
    subtitle_align="left",
    title_align="rigth"
)

caixa_002 = Panel(
    "[white]Esse aqui é um painel de exemplo[/]",
    title="[white]Julia[/]",
    style=Style( 
        color="red"
    ),
    expand=False,
    padding=1,
    subtitle="[white]14:15[/]",
    subtitle_align="right",
    title_align="left"
)

console.print(caixa_001)
print()
console.print(caixa_002)