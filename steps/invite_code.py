from steps import clear_screen

def main(details):
    ascii_art = """

██╗███╗   ██╗██╗   ██╗██╗████████╗███████╗     ██████╗ ██████╗ ██████╗ ███████╗
██║████╗  ██║██║   ██║██║╚══██╔══╝██╔════╝    ██╔════╝██╔═══██╗██╔══██╗██╔════╝
██║██╔██╗ ██║██║   ██║██║   ██║   █████╗      ██║     ██║   ██║██║  ██║█████╗  
██║██║╚██╗██║╚██╗ ██╔╝██║   ██║   ██╔══╝      ██║     ██║   ██║██║  ██║██╔══╝  
██║██║ ╚████║ ╚████╔╝ ██║   ██║   ███████╗    ╚██████╗╚██████╔╝██████╔╝███████╗
╚═╝╚═╝  ╚═══╝  ╚═══╝  ╚═╝   ╚═╝   ╚══════╝     ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝
                                                       """
                                                
    clear_screen.main()
    print(ascii_art)
    details['invite-code'] = input("What's their Invite Code?\n> ")

if __name__ == "__main__":
    main(details)
