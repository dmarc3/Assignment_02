'''
Classes for user information for the social network project
All edits made by Kathleen Wong to incorporate logging issues.
'''
# pylint: disable=R0903
import logging

class Users():
    '''
    Contains user information
    '''

    def __init__(self, user_id, email, user_name, user_last_name):
        self.user_id = user_id
        self.email = email
        self.user_name = user_name
        self.user_last_name = user_last_name


class UserCollection():
    '''
    Contains a collection of Users objects
    '''

    def __init__(self):
        self.database = {}

    def add_user(self, user_id, email, user_name, user_last_name):
        '''
        Adds a new user to the collection
        '''
        if user_id in self.database:
            # Rejects new status if status_id already exists
            logging.error(f'Unable to modify {user_id} because it ' \
                           'does not exist in UserCollection.')
            logging.debug("UserCollection contains following users': " +
                          ', '.join(self.database.keys()))
            return False
        new_user = Users(user_id, email, user_name, user_last_name)
        self.database[user_id] = new_user
        logging.info(f'Successfully added user {user_id}!')
        return True

    def modify_user(self, user_id, email, user_name, user_last_name):
        '''
        Modifies an existing user
        '''
        if user_id not in self.database:
            logging.error(f'Unable to modify {user_id} because it ' \
                           'does not exist in UserCollection.')
            logging.debug("UserCollection contains following status': " +
                          ', '.join(self.database.keys()))
            return False
        self.database[user_id].email = email
        self.database[user_id].user_name = user_name
        self.database[user_id].user_last_name = user_last_name
        logging.info(f'Successfully modified status {user_id}!')
        return True

    def delete_user(self, user_id):
        '''
        Deletes an existing user
        '''
        if user_id not in self.database:
            # Fails if status does not exist
            logging.error(f'Unable to delete {user_id} because it ' \
                          'does not exist in UserCollection.')
            logging.debug("UserCollection contains following status': " +
                          ', '.join(self.database.keys()))
            return False
        del self.database[user_id]
        logging.info(f'Successfully deleted status {user_id}!')
        return True

    def search_user(self, user_id):
        '''
        Searches for user data
        '''
        if user_id not in self.database:
            logging.error(f'Unable to find {user_id} in UserCollection.')
            logging.debug("UserCollection contains following users': " +
                          ', '.join(self.database.keys()))
            return Users(None, None, None, None)
        return self.database[user_id]
