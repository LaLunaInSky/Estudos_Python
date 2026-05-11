from rich.console import Console
from rich.style import Style

console = Console()

danger_style = Style(color="white", bgcolor="red", blink=True, bold=True)

console.print(" Olá, Mundo! :earth_americas: ", style=danger_style)
console.print("Olá,[bold blue on white] Pequeno Gafanhoto [/]:vulcan_salute:")


try:
    do_something()
except Exception:
    console.print_exception(show_locals=False)