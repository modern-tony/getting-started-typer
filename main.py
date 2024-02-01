import typer

app = typer.Typer()

@app.command()
def hello(name: str, iq: int, display_iq: bool = True):
    typer.echo(f"Hello World {name}")
    if display_iq:
        typer.echo(f"Your IQ is {iq}")

@app.command()
def goodbye(name: str):
    typer.echo(f"Goodbye {name}")

if __name__ == "__main__":
    app()