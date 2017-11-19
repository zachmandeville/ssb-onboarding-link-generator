from steps import clear_screen

def main(details):
    ascii_art = """

███████╗███████╗███╗   ██╗██████╗ ███████╗██████╗ 
██╔════╝██╔════╝████╗  ██║██╔══██╗██╔════╝██╔══██╗
███████╗█████╗  ██╔██╗ ██║██║  ██║█████╗  ██████╔╝
╚════██║██╔══╝  ██║╚██╗██║██║  ██║██╔══╝  ██╔══██╗
███████║███████╗██║ ╚████║██████╔╝███████╗██║  ██║
╚══════╝╚══════╝╚═╝  ╚═══╝╚═════╝ ╚══════╝╚═╝  ╚═╝
                                                  
                                                      """
    clear_screen.main()
    print(ascii_art)
    details['sender'] = input("One last thing: What's your name(or what they know you by?)\n> ")

if __name__ == "__main__":
    main(details)
