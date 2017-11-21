import configparser

config = configparser.ConfigParser()

def main(imported_details):
    config.read("contact-info.ini")
    config.sections()
    for key, value in config.items('Contact Info'):
        imported_details[key] = value

if __name__ == "__main__":
    main(imported_details)
