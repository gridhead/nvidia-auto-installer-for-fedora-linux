from colorama import init, Fore, Style

class StatusDecorator(object):
    def __init__(self):
        self.PASS = Style.BRIGHT + Fore.GREEN + "[ ✔ ]" + Style.RESET_ALL
        self.FAIL = Style.BRIGHT + Fore.RED + "[ ✘ ]" + Style.RESET_ALL
        self.WARN = Style.BRIGHT + Fore.YELLOW + "[ ! ]" + Style.RESET_ALL
        self.HEAD = Style.BRIGHT + Fore.CYAN + "[ # ]" + Style.RESET_ALL
        self.STDS = "     "

    def SuccessMessage(self, RequestMessage):
        print(self.PASS + " " + Fore.WHITE + RequestMessage + Style.RESET_ALL)

    def FailureMessage(self, RequestMessage):
        print(self.FAIL + " " + Fore.WHITE + RequestMessage + Style.RESET_ALL)

    def WarningMessage(self, RequestMessage):
        print(self.WARN + " " + Fore.WHITE + RequestMessage + Style.RESET_ALL)

    def SectionHeader(self, RequestMessage):
        print(self.HEAD + " " + Fore.CYAN + RequestMessage + Style.RESET_ALL)

    def NormalMessage(self, RequestMessage):
        print(self.STDS + " " + Fore.WHITE + RequestMessage + Style.RESET_ALL)