from steps import clear_screen

def main(details):
    ascii_art = """

███████╗██╗   ██╗ ██████╗ ██████╗███████╗███████╗███████╗██╗
██╔════╝██║   ██║██╔════╝██╔════╝██╔════╝██╔════╝██╔════╝██║
███████╗██║   ██║██║     ██║     █████╗  ███████╗███████╗██║
╚════██║██║   ██║██║     ██║     ██╔══╝  ╚════██║╚════██║╚═╝
███████║╚██████╔╝╚██████╗╚██████╗███████╗███████║███████║██╗
╚══════╝ ╚═════╝  ╚═════╝ ╚═════╝╚══════╝╚══════╝╚══════╝╚═╝
                                                                      
    """
    directory = details['recipient'].replace(" ","-").lower()
    clear_screen.main()
    print(ascii_art)
    print("Invite Site made!\nYou'll find it within the directory invites, in the sub-directory '{}'".format(directory))
    print("\n"*2)

if __name__ == "__main__":
    main(details)
