import typer

from dnetochaves_cli_github.github import GitHubAPI
from dnetochaves_cli_github.utils import print_beauty
from dnetochaves_cli_github.options import OutputOption


user_app = typer.Typer()


@user_app.command(name="profile")
def profile(
    user: str = typer.Option(..., "--user", "-u", help="github user name"),
):
    """
    obter perfil de usuário

    EXEMPLO

    perfil de usuário do dnetochaves_cli_github -u dnetochaves
    """
    github_api = GitHubAPI()
    repo = github_api.get_all_repositories_for_user(username=user)
    followers = github_api.list_followers_of_user(username=user)
    following = github_api.list_people_user_follows(username=user)

    profile = {
        "repositórios": len(repo) if repo else 0,
        "seguidoras": len(followers) if followers else 0,
        "seguindo": len(following) if following else 0,
    }
    print_beauty([profile], output=OutputOption.table)
