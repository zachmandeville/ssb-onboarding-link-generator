from steps import clear_screen

def main(details):
    ascii_art = """

 ██████╗██╗  ██╗ █████╗ ███╗   ██╗███╗   ██╗███████╗██╗     ███████╗
██╔════╝██║  ██║██╔══██╗████╗  ██║████╗  ██║██╔════╝██║     ██╔════╝
██║     ███████║███████║██╔██╗ ██║██╔██╗ ██║█████╗  ██║     ███████╗
██║     ██╔══██║██╔══██║██║╚██╗██║██║╚██╗██║██╔══╝  ██║     ╚════██║
╚██████╗██║  ██║██║  ██║██║ ╚████║██║ ╚████║███████╗███████╗███████║
 ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝╚══════╝╚══════╝╚══════╝
                                                       """
    clear_screen.main()
    print(ascii_art)
    details['channel-one'] = input("What's a Channel they should check out? (Include the Hash-tag)\n> ")
    details['channel-two'] = input("What's another channel you recommend?\n> ")
    details['channel-three'] = input("And one last channel!\n> ")

if __name__ == "__main__":
    main(details)
