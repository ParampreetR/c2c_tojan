import os

def run(**args):
    print("[*] In dirlisting module")
    files = os.listdir(".")
    return str(files)