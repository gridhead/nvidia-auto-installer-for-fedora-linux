import click
from colorama import Fore, Style

class StatusDecorator(object):
    def __init__(self):
        self.PASS = Style.BRIGHT + Fore.GREEN + "[ ✔ ]" + Style.RESET_ALL
        self.FAIL = Style.BRIGHT + Fore.RED + "[ ✘ ]" + Style.RESET_ALL
        self.WARN = Style.BRIGHT + Fore.YELLOW + "[ ! ]" + Style.RESET_ALL
        self.HEAD = Style.BRIGHT + Fore.CYAN + "[ # ]" + Style.RESET_ALL
        self.STDS = "     "

    def SuccessMessage(self, RequestMessage):
        click.echo(self.PASS + " " + Style.RESET_ALL + RequestMessage)

    def FailureMessage(self, RequestMessage):
        click.echo(self.FAIL + " " + Style.RESET_ALL + RequestMessage)

    def WarningMessage(self, RequestMessage):
        click.echo(self.WARN + " " + Style.RESET_ALL + RequestMessage)

    def SectionHeader(self, RequestMessage):
        click.echo(self.HEAD + " " + Fore.CYAN + Style.BRIGHT + RequestMessage + Style.RESET_ALL)

    def NormalMessage(self, RequestMessage):
        click.echo(self.STDS + " " + Style.RESET_ALL + RequestMessage)