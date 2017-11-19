
import os
import shutil

from steps import *

details = {}

def grab_the_details():
    """Run through user input getting specific details to fill into the invite webpage."""
    recipient.main(details)
    pub.main(details)
    invite_code.main(details)
    username.main(details)
    channels.main(details)
    sender.main(details)

def main():
    grab_the_details()
    template.main(details)
    success.main(details)

if __name__ == "__main__":
    main()
