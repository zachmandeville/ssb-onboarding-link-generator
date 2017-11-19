from steps import clear_screen

def main(details):
    """Add the specific pub they'll be joining."""
    ascii_art = """

██████╗ ██╗   ██╗██████╗ 
██╔══██╗██║   ██║██╔══██╗
██████╔╝██║   ██║██████╔╝
██╔═══╝ ██║   ██║██╔══██╗
██║     ╚██████╔╝██████╔╝
╚═╝      ╚═════╝ ╚═════╝ 
    
    """
    clear_screen.main()
    print(ascii_art)
    details['pub'] = input("What pub are you inviting them to?\n> ")

if __name__ == "__main__":
    main(details)
