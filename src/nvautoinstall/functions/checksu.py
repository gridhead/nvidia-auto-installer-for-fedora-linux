import os


class CollSuperuserCheck:
    @staticmethod
    def main():
        return os.geteuid() == 0


SuperuserCheck: CollSuperuserCheck = CollSuperuserCheck()
