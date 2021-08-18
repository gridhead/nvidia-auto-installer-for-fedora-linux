from dataclasses import dataclass
from typing import Any
import click


@dataclass
class StatusDecorator(object):
    def __init__(self):
        self.MessageType: dict[str, Any] = {
            "PASS": click.style("[ \u2713 ]", fg="green", bold=True),
            "FAIL": click.style("[ \u2717 ]", fg="red", bold=True),
            "WARN": click.style("[ ! ]", fg="yellow", bold=True),
            "HEAD": click.style("[ \u2605 ]", fg="magenta", bold=True),
            "STDS": "     ",
        }

    def send_message(self, message_type: str, request_message: str, fg: str = "", bold: bool = False):
        click.echo(f"{self.MessageType.get(message_type)} {click.style(request_message, fg=fg, bold=bold)}")


DecoratorObject: StatusDecorator = StatusDecorator()