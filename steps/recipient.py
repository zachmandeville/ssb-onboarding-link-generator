from steps import clear_screen

def main(details):
    """Find out who the invite is for."""
    ascii_art = """


██████╗ ███████╗ ██████╗██╗██████╗ ██╗███████╗███╗   ██╗████████╗
██╔══██╗██╔════╝██╔════╝██║██╔══██╗██║██╔════╝████╗  ██║╚══██╔══╝
██████╔╝█████╗  ██║     ██║██████╔╝██║█████╗  ██╔██╗ ██║   ██║   
██╔══██╗██╔══╝  ██║     ██║██╔═══╝ ██║██╔══╝  ██║╚██╗██║   ██║   
██║  ██║███████╗╚██████╗██║██║     ██║███████╗██║ ╚████║   ██║   
╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═══╝   ╚═╝   
    """
    clear_screen.main()
    print(ascii_art)
    details['recipient'] = input("What's the name of the person you are inviting?\n> ")

if __name__ == "__main__":
    main(details)
