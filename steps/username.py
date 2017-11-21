from steps import clear_screen

def main(details, imported_details):
    ascii_art = """

██╗   ██╗███████╗███████╗██████╗ ███╗   ██╗ █████╗ ███╗   ███╗███████╗
██║   ██║██╔════╝██╔════╝██╔══██╗████╗  ██║██╔══██╗████╗ ████║██╔════╝
██║   ██║███████╗█████╗  ██████╔╝██╔██╗ ██║███████║██╔████╔██║█████╗  
██║   ██║╚════██║██╔══╝  ██╔══██╗██║╚██╗██║██╔══██║██║╚██╔╝██║██╔══╝  
╚██████╔╝███████║███████╗██║  ██║██║ ╚████║██║  ██║██║ ╚═╝ ██║███████╗
 ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝
                                                                      
    """
    clear_screen.main()
    print(ascii_art)
    if imported_details['username']:
        details['username'] = imported_details['username']
        print("~*~*~*~* Your username is set to {}\n".format(details['username']))
    else:
        details['username'] = input("What username can they find you under?\n(Note: you can fill this out in 'contact-info.ini' so you don't have to enter it each time.) ")
    if  imported_details['public-key']:
        details['public-key'] = imported_details['public-key']
        print("*~*~*~* Your public key is set to {}\n".format(details['public-key']))
        keep_going = input("~*~*~*~ Hit any key to continue.")
    else:
        details['public-key'] = input("What is your public key?\n(This can also be set in the 'contact-info.ini')\n> ")


if __name__ == "__main__":
    main(details)
