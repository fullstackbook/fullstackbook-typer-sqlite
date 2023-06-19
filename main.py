import typer
from commands import todos

app = typer.Typer(
    no_args_is_help=True, context_settings={"help_option_names": ["-h", "--help"]}
)
app.add_typer(todos.app, name="todos")

if __name__ == "__main__":
    app()
