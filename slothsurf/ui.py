"""
Rich terminal UI utilities for SlothSurf.
"""

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.markdown import Markdown

console = Console()

SLOTH_BANNER = r"""[bold green]
  .-""-.
 /      \      ___ _       _   _    ____             __ 
|  o  o  |    / __| |___ _| |_| |_ / ___| _   _ _ __/ _|
|   __   |    \__ \ / _ \_   _| ' \\___ \| | | | '__| |_ 
 \______/     |___/_\___/ |_| |_||_|___) | |_| | |  |  _|
  /|  |\                                 |____/|_|  |_|  
 (_|  |_)     [yellow]The Zero-Effort Autonomous Browser Agent[/yellow]
[/bold green]"""

def print_welcome():
    console.print(SLOTH_BANNER)
    console.print(
        Panel(
            "[bold white]Theme: Slow and Steady (International Sloth Day)[/bold white]\n"
            "[dim]Powered by [bold cyan]browser-use[/bold cyan] (open-source harness) & [bold magenta]Grok API[/bold magenta] (xAI)[/dim]\n"
            "Sit back, relax, and let your sloth agent do the scrolling, clicking, and reading for you.",
            border_style="green",
        )
    )

def print_presets(presets: dict):
    table = Table(title="[bold yellow]Lazy One-Click Preset Missions[/bold yellow]", border_style="dim")
    table.add_column("Key", style="bold cyan", width=6)
    table.add_column("Mission", style="bold white", width=35)
    table.add_column("Description", style="dim", width=45)

    for key, data in presets.items():
        table.add_row(key, data["title"], data["description"])
    table.add_row("C", "✍️  Custom Task", "Type whatever chore you're too lazy to do")
    table.add_row("Q", "💤 Quit & Nap", "Exit SlothSurf")
    console.print(table)

def print_result(result_text: str):
    console.print("\n[bold green]━" * 50 + "[/bold green]")
    console.print("[bold green]🦥 Sloth Mission Accomplished! Here is your lazy briefing:[/bold green]\n")
    console.print(Markdown(result_text))
    console.print("[bold green]━" * 50 + "[/bold green]\n")
