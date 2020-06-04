import os

def main():
    data = os.geteuid()
    if data == 0:
        return True
    else:
        return False