from rich.console import Console
from rich.traceback import install

install()

def dividir(
    num_01: int,
    num_02: int
) -> int:
    return num_01 / num_02

console = Console()

console.print(
    dividir(
        50,
        0
    )
)