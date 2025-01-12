import os

import typer
from rich import print
from dotenv import load_dotenv

from dnetochaves_cli_github.cli.repo import repo_app
from dnetochaves_cli_github.cli.user import user_app


if os.path.isfile(".env"):
    load_dotenv()

app = typer.Typer()

app.add_typer(repo_app, name="repo", help="comandos de repositório")
app.add_typer(user_app, name="user", help="comandos de usuários")

if __name__ == "__main__":
    app()
