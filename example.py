import typer
from typer_tools import dependency

app = typer.Typer()

@dependency
def parse_client(
  host: str = typer.Option(..., '--host', help='HTTP host'),
  port: int = typer.Option(80, '--port', help='HTTP port'),
  token: str = typer.Option(..., '--token', help='Access token')
) -> str:
  return 'client'

@app.command()
@parse_client.inject
def main(client: str = parse_client.Depends()):
  print(client)

if __name__ == '__main__':
  app()