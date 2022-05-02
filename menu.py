'''
Provides a basic frontend

Kathleen incorporated all changes to users.py
Marcus incorporated all changes to user_status.py code.
'''
# pylint: disable=W1203
import sys
import logging
from datetime import datetime
import main

# Build logger
FILE_FORMAT = "%(asctime)s %(filename)s:%(lineno)-4d %(levelname)s %(message)s"
formatter = logging.Formatter(FILE_FORMAT)
LOG_FILE = f'log_{datetime.today():%d-%m-%Y}.log'
file_handler = logging .FileHandler(LOG_FILE)
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logger.addHandler(file_handler)
# Add launch statement
logger.info(f'Session launched at {datetime.today():%H:%M:%S}.')


def load_users():
    '''
    Loads user accounts from a file
    '''
    filename = input('Enter filename of user file: ')
    main.load_users(filename, user_collection)


def load_status_updates():
    '''
    Loads status updates from a file
    '''
    filename = input('Enter filename for status file: ')
    main.load_status_updates(filename, status_collection)


def add_user():
    '''
    Adds a new user into the database
    '''
    user_id = input('User ID: ')
    email = input('User email: ')
    user_name = input('User name: ')
    user_last_name = input('User last name: ')
    if not main.add_user(user_id,
                         email,
                         user_name,
                         user_last_name,
                         user_collection):
        print("An error occurred while trying to add new user")
    else:
        print("User was successfully added")


def update_user():
    '''
    Updates information for an existing user
    '''
    user_id = input('User ID: ')
    email = input('User email: ')
    user_name = input('User name: ')
    user_last_name = input('User last name: ')
	# Potentially doubling check logic?
    # I think main.update_user should return False if it
    # fails and True if it doesn't already.
    if main.update_user(user_id, email, user_name, user_last_name, user_collection) is True:
        main.update_user(user_id, email, user_name, user_last_name, user_collection)
    elif not user_collection.database:
        logging.warning('Updating user issue.')
        logging.error('File has not been loaded yet so is empty.')
    else:
        logging.warning('Updating user issue.')
        logging.error('User not in file.')


def search_user():
    '''
    Searches a user in the database
    '''
    user_id = input('Enter user ID to search: ')
    result = main.search_user(user_id, user_collection)
	# See search_update. Maybe its similar error?
    try:
        print(f"User ID: {result.user_id}")
        print(f"Email: {result.email}")
        print(f"Name: {result.user_name}")
        print(f"Last name: {result.user_last_name}")
    except AttributeError:
        if not user_collection.database:
            logging.warning('Searching user issue.')
            logging.error('File has not been loaded yet so is empty.')
        else:
            logging.warning('Searching user issue.')
            logging.error('%s does not exist.', user_id)


def delete_user():
    '''
    Deletes user from the database
    '''
    user_id = input('User ID: ')
	# Double check this logic -> Could be duplication?
    if main.delete_user(user_id, user_collection):
        main.delete_user(user_id, user_collection)
    elif not user_collection.database:
        logging.warning('Deleting user issue.')
        logging.error('File has not been loaded yet so is empty.')
    else:
        logging.warning('Searching user issue.')
        logging.error('User not in file.')


def save_users():
    '''
    Saves user database into a file
    '''
    filename = input('Enter filename for users file: ')
    main.save_users(filename, user_collection)


def add_status():
    '''
    Adds a new status into the database
    '''
    user_id = input('User ID: ')
    status_id = input('Status ID: ')
    status_text = input('Status text: ')
    if not main.add_status(user_id, status_id, status_text, status_collection):
        print("An error occurred while trying to add new status")
    else:
        print("New status was successfully added")


def update_status():
    '''
    Updates information for an existing status
    '''
    user_id = input('User ID: ')
    status_id = input('Status ID: ')
    status_text = input('Status text: ')
    if not main.update_status(status_id, user_id, status_text, status_collection):
        print("An error occurred while trying to update status")
    else:
        print("Status was successfully updated")


def search_status():
    '''
    Searches a status in the database
    '''
    status_id = input('Enter status ID to search: ')
    result = main.search_status(status_id, status_collection)
    if not result:
        print("ERROR: Status does not exist")
    else:
        print(f"User ID: {result.user_id}")
        print(f"Status ID: {result.status_id}")
        print(f"Status text: {result.status_text}")


def delete_status():
    '''
    Deletes status from the database
    '''
    status_id = input('Status ID: ')
    if not main.delete_status(status_id, status_collection):
        print("An error occurred while trying to delete status")
    else:
        print("Status was successfully deleted")


def save_status():
    '''
    Saves status database into a file
    '''
    filename = input('Enter filename for status file: ')
    main.save_status_updates(filename, status_collection)


def quit_program():
    '''
    Quits program
    '''
    logging.info('Quitting program.\n\n')
    sys.exit()


if __name__ == '__main__':
    user_collection = main.init_user_collection()
    status_collection = main.init_status_collection()
    menu_options = {
        'A': load_users,
        'B': load_status_updates,
        'C': add_user,
        'D': update_user,
        'E': search_user,
        'F': delete_user,
        'G': save_users,
        'H': add_status,
        'I': update_status,
        'J': search_status,
        'K': delete_status,
        'L': save_status,
        'Q': quit_program
    }
    while True:
        user_selection = input("""
                            A: Load user database
                            B: Load status database
                            C: Add user
                            D: Update user
                            E: Search user
                            F: Delete user
                            G: Save user database to file
                            H: Add status
                            I: Update status
                            J: Search status
                            K: Delete status
                            L: Save status database to file
                            Q: Quit

                            Please enter your choice: """)
        user_selection = user_selection.upper().strip()
        if user_selection in menu_options:
            logging.info(f'User selected {user_selection} ' \
                         f'-> executing {menu_options[user_selection].__name__}.')
            menu_options[user_selection]()
        else:
            logging.info(f'{user_selection} is an invalid option.')
            print("Invalid option")
