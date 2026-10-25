"""
Core SlothSurf Agent module.
Integrates the open-source browser-use harness with xAI Grok.
Uses the pre-installed system browser (Microsoft Edge / Chrome) with zero extra downloads.
"""

import asyncio
from pathlib import Path
from typing import Optional
from rich.console import Console

from slothsurf.config import Config

console = Console()

SLOTH_SYSTEM_PROMPT = """
You are SlothSurf, the ultimate relaxed, energy-conserving browser automation assistant.
Your motto is 'Slow and Steady'. You conserve energy by making the most efficient, direct clicks.
Never waste actions. Avoid unnecessary rabbit holes. 
Extract exactly what the user asked for with zero fluff.
Conclude with a clear, concise summary suitable for someone who wants to read the bare minimum and get back to relaxing.
"""

def get_system_browser_path() -> Optional[str]:
    """Finds existing installed browser executable on Windows."""
    candidates = [
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    ]
    for c in candidates:
        if Path(c).exists():
            return c
    return None

async def execute_task(task: str, headless: Optional[bool] = None, slow_mo: Optional[int] = None) -> str:
    """
    Executes a web task using browser-use and Grok.
    """
    if headless is None:
        headless = Config.HEADLESS

    # Check API key
    if not Config.validate():
        console.print(
            "[bold red]⚠️  No valid XAI_API_KEY detected in .env![/bold red]\n"
            "[yellow]Please open [bold].env[/bold] and set your xAI Grok API key.[/yellow]\n"
            "[dim]Get an API key at https://console.x.ai/[/dim]\n"
        )
        return "Task could not run: Missing XAI_API_KEY. Please configure your .env file."

    from langchain_openai import ChatOpenAI
    from browser_use import Agent, Browser

    console.print(f"[cyan]🦥 Waking up SlothSurf with model [bold]{Config.GROK_MODEL}[/bold]...[/cyan]")
    console.print(f"[dim]Browser Mode: {'Headless (invisible)' if headless else 'Visible UI'} using system Edge/Chrome[/dim]\n")

    # Configure Grok via OpenAI-compatible endpoint
    llm = ChatOpenAI(
        model=Config.GROK_MODEL,
        base_url=Config.XAI_BASE_URL,
        api_key=Config.XAI_API_KEY,
        temperature=0.2,
    )

    # Use installed system browser (Edge or Chrome)
    browser_path = get_system_browser_path()
    if browser_path:
        browser = Browser(executable_path=browser_path, headless=headless)
    else:
        browser = Browser(channel="msedge", headless=headless)

    # Prepend sloth persona
    full_task = f"{SLOTH_SYSTEM_PROMPT}\n\nTask: {task}"

    agent = Agent(
        task=full_task,
        llm=llm,
        browser=browser,
    )

    console.print("[bold green]🏄 Sloth is surfing the web... sit back and relax.[/bold green]\n")
    history = await agent.run()
    
    # Extract final answer
    final_result = history.final_result()
    return final_result or "Task completed, but no text was returned."
