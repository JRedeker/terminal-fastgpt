import typer
import requests
from rich import pretty
from rich.prompt import Prompt
pretty.install()

app = typer.Typer()


@app.command()
def ask(user_query: str):
	# request data from url
	base_url = f"https://labs.kagi.com/fastgpt?query={user_query}"
	request = requests.get("")
	response = request #plus .whatever [value blah]
	typer.echo(f"FastGPT: {response}")


while looping {

	question = Prompt.ask("Ask FastGPT:")

	url =  "https://labs.kagi.com/fastgpt?query={question}".format()

	// Request data from the url, waiting until it loads for the answer


}
