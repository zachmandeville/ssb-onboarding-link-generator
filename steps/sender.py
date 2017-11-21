from steps import clear_screen

def main(details, imported_details):
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
    if imported_details['sender']:
        details['sender'] = imported_details['sender']
        print("~*~*~*~ This Email will be signed with '{}' as your name.\n".format(details['sender']))
        finish_this =input("Almost there. press any key to finish!")
    else:
        details['sender'] = input("One last thing: What's your name(or the name the invitee knows  you by?)\n> ")
if __name__ == "__main__":
    main(details, imported_details)
