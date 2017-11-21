
import os
import shutil

from steps import *

details = {}
imported_details = {}

def grab_the_details():
    """Run through user input getting specific details to fill into the invite webpage."""
    import_contact_info.main(imported_details)
    recipient.main(details)
    pub.main(details)
    invite_code.main(details)
    username.main(details, imported_details)
    channels.main(details)
    sender.main(details, imported_details)

def main():
    grab_the_details()
    template.main(details)
    success.main(details)

if __name__ == "__main__":
    main()
