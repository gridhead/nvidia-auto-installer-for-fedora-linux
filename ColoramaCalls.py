from colorama import init, Fore, Style

class StatusDecorator(object):
    def __init__(self):
        self.PASS = Style.BRIGHT + Fore.GREEN + "[ ✔ ]" + Style.RESET_ALL
        self.FAIL = Style.BRIGHT + Fore.RED + "[ ✘ ]" + Style.RESET_ALL
        self.WARN = Style.BRIGHT + Fore.YELLOW + "[ ! ]" + Style.RESET_ALL
        self.HEAD = Style.BRIGHT + Fore.CYAN + "[ # ]" + Style.RESET_ALL
        self.STDS = "     "

    def SuccessMessage(self, RequestMessage):
        print(self.PASS + " " + Style.RESET_ALL + RequestMessage)

    def FailureMessage(self, RequestMessage):
        print(self.FAIL + " " + Style.RESET_ALL + RequestMessage)

    def WarningMessage(self, RequestMessage):
        print(self.WARN + " " + Style.RESET_ALL + RequestMessage)

    def SectionHeader(self, RequestMessage):
        print(self.HEAD + " " + Fore.CYAN + RequestMessage + Style.RESET_ALL)

    def NormalMessage(self, RequestMessage):
        print(self.STDS + " " + Style.RESET_ALL + RequestMessage)