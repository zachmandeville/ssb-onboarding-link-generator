import shutil
import os

def make_directory(details):
    """Make a new folder specific for invitee within this directory, then add an index.html and
    stylesheet.css file for it."""
    name = details['recipient'].replace(" ","-").lower()
    path = 'invites/{}'.format(name)
    if not os.path.exists(path):
        os.makedirs(path)
    shutil.copy2('resources/stylesheet.css', path)
    shutil.copy2('resources/index.html', path)


def filled_out_template(details):
    """Take the details entered in the script and add them to the index.html template."""
    with open('resources/template.html', 'r') as template:
        the_page = template.read()
    return the_page.format(**details)

def create_index_file(details):
    """Convert the filled out template file into the invitees' index.html file"""
    name = details['recipient'].replace(" ","-").lower()
    index_file = 'invites/{}/index.html'.format(name)
    with open(index_file, "w") as target_file:
        target_file.write(filled_out_template(details))

def main(details):
    """Make a new directory for the invitee, then add a stylesheet and custom index.html file to
    this directory."""
    make_directory(details)
    filled_out_template(details)
    create_index_file(details)

if __name__ == "__main__":
    main()
