"""
SlothSurf CLI Entry Point.
The Zero-Effort Autonomous Browser Agent.
"""

import sys
sys.stdout.reconfigure(encoding='utf-8')

import asyncio
from rich.console import Console
from rich.prompt import Prompt

from slothsurf.config import Config
from slothsurf.presets import PRESET_TASKS
from slothsurf.ui import print_welcome, print_presets, print_result
from slothsurf.agent import execute_task

console = Console()

def main():
    print_welcome()

    if not Config.validate():
        console.print(
            "[bold yellow]Notice:[/bold yellow] No valid [bold]XAI_API_KEY[/bold] detected in [bold].env[/bold].\n"
            "You can still explore the presets or enter custom prompts, but actual browser runs require an xAI key.\n"
        )

    while True:
        print_presets(PRESET_TASKS)
        choice = Prompt.ask("\n[bold yellow]Select a mission (or Q to quit)[/bold yellow]", default="1").strip().upper()

        if choice in ("Q", "QUIT", "EXIT"):
            console.print("[dim green]🦥 Heading back to the tree branch for a nap. Goodbye![/dim green]")
            sys.exit(0)

        task_prompt = ""
        if choice in PRESET_TASKS:
            task_prompt = PRESET_TASKS[choice]["task"]
            console.print(f"\n[cyan]Selected:[/cyan] [bold]{PRESET_TASKS[choice]['title']}[/bold]")
        elif choice == "C":
            task_prompt = Prompt.ask("\n[bold cyan]What chore are you too lazy to do?[/bold cyan]")
            if not task_prompt.strip():
                console.print("[red]Empty task. Conserving energy and doing nothing.[/red]")
                continue
        else:
            console.print("[red]Unknown selection. Conserving energy instead.[/red]")
            continue

        try:
            result = asyncio.run(execute_task(task_prompt))
            print_result(result)
        except KeyboardInterrupt:
            console.print("\n[yellow]Task canceled. Back to resting.[/yellow]")
        except Exception as e:
            console.print(f"\n[bold red]Error during mission:[/bold red] {e}")

        # Pause before showing menu again
        Prompt.ask("\n[dim]Press Enter to return to main menu...[/dim]", default="")

if __name__ == "__main__":
    main()
