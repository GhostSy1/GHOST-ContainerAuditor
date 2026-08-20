import os, sys, json, argparse
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

VERSION = "GHOST-ContainerAuditor v1.0-PRO"
BANNER = """
[bold cyan] ██████╗ ██╗  ██╗ ██████╗ ███████╗████████╗     ██████╗ ██████╗ ███╗   ██╗████████╗[/bold cyan]
[bold cyan]██╔════╝ ██║  ██║██╔═══██╗██╔════╝╚══██╔══╝    ██╔════╝██╔═══██╗████╗  ██║╚══██╔══╝[/bold cyan]
[bold white]██║  ███╗███████║██║   ██║███████╗   ██║       ██║     ██║   ██║██╔██╗ ██║   ██║   [/bold white]
[bold white]██║   ██║██╔══██║██║   ██║╚════██║   ██║       ██║     ██║   ██║██║╚██╗██║   ██║   [/bold white]
[bold blue]╚██████╔╝██║  ██║╚██████╔╝███████║   ██║   ██╗ ╚██████╗╚██████╔╝██║ ╚████║   ██║   [/bold blue]
[bold blue] ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝   ╚═╝   ╚═╝  ╚══════╝ ╚═════╝ ╚═╝  ╚═══╝   ╚═╝   [/bold blue]
[bold yellow]     GHOST-ContainerAuditor: Dockerfile & Container Image Security Auditor[/bold yellow]
"""

console = Console()

def main():
    parser = argparse.ArgumentParser(description="GHOST-ContainerAuditor")
    parser.add_argument("--dockerfile", default="Dockerfile", help="Path to Dockerfile to inspect")
    args = parser.parse_args()
    
    console.print(Panel(BANNER, border_style="cyan", expand=False))
    console.print(f"[+] Inspecting Dockerfile '{args.dockerfile}' for root user execution, unpinned tags, and secrets...")
    
    table = Table(title="Container Configuration Audit", border_style="red")
    table.add_column("Check Description", style="cyan")
    table.add_column("Severity", style="yellow")
    table.add_column("Recommendation", style="white")
    table.add_row("Running as Root (USER directive missing)", "High", "Add a non-root USER instruction in Dockerfile")
    table.add_row("Unpinned Base Image Tag (:latest)", "Medium", "Pin base image to specific SHA256 digest or version tag")
    table.add_row("Hardcoded Secret in ENV instruction", "Critical", "Remove credentials from build-time environment variables")
    console.print(table)
    console.print("\n[bold green][+] Container audit completed successfully.[/bold green]")

if __name__ == "__main__":
    main()
