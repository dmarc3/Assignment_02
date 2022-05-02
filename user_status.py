'''
classes to manage the user status messages

All edits by Marcus Bakke.

Disabling W1201 and W1203 in order to not have to re-format all of my logger strings
The benefit of implementing "lazy % formatting" would be a performance boost
since the string formatting would be executed only if the logger message is
emitted. In current state, string formatting is always executed even if message
is not emitted.

'''
# pylint: disable=R0903
# pylint: disable=W1201
# pylint: disable=W1203
import logging

class UserStatus():
    '''
    class to hold status message data
    '''

    def __init__(self, status_id, user_id, status_text):
        logging.info(f'{status_id} status initialized.')
        self.status_id = status_id
        self.user_id = user_id
        self.status_text = status_text


class UserStatusCollection():
    '''
    Collection of UserStatus messages
    '''

    def __init__(self):
        logging.info('UserStatusCollection initialized.')
        self.database = {}

    def add_status(self, status_id, user_id, status_text):
        '''
        add a new status message to the collection
        '''
        logging.info(f'Attempting to add status {status_id} to UserStatusCollection...')
        if status_id in self.database:
            # Rejects new status if status_id already exists
            logging.error(f'Unable to add {status_id} because it ' \
                           'already exists in UserStatusCollection.')
            logging.debug("UserStatusCollection contains following status': " +
                          ', '.join(self.database.keys()))
            return False
        new_status = UserStatus(status_id, user_id, status_text)
        self.database[status_id] = new_status
        logging.info(f'Successfully added status {status_id}!')
        return True

    def modify_status(self, status_id, user_id, status_text):
        '''
        Modifies a status message

        The new user_id and status_text are assigned to the existing message
        '''
        logging.info(f'Attempting to modify status {status_id}...')
        if status_id not in self.database:
            # Rejects update is the status_id does not exist
            logging.error(f'Unable to modify {status_id} because it ' \
                           'does not exist in UserStatusCollection.')
            logging.debug("UserStatusCollection contains following status': " +
                          ', '.join(self.database.keys()))
            return False
        self.database[status_id].user_id = user_id
        self.database[status_id].status_text = status_text
        logging.info(f'Successfully modified status {status_id}!')
        return True

    def delete_status(self, status_id):
        '''
        deletes the status message with id, status_id
        '''
        logging.info(f'Attempting to delete status {status_id} from UserStatusCollection...')
        if status_id not in self.database:
            # Fails if status does not exist
            logging.error(f'Unable to delete {status_id} because it ' \
                           'does not exist in UserStatusCollection.')
            logging.debug("UserStatusCollection contains following status': " +
                          ', '.join(self.database.keys()))
            return False
        del self.database[status_id]
        logging.info(f'Successfully deleted status {status_id}!')
        return True

    def search_status(self, status_id):
        '''
        Find and return a status message by its status_id

        Returns an empty UserStatus object if status_id does not exist
        '''
        logging.info(f'Attempting to find status {status_id} in UserStatusCollection...')
        if status_id not in self.database:
            # Fails if the status does not exist
            logging.error(f'Unable to find {status_id} in UserStatusCollection.')
            logging.debug("UserStatusCollection contains following status': " +
                          ', '.join(self.database.keys()))
            return UserStatus(None, None, None)
        logging.info(f'Successfully found status {status_id}!')
        return self.database[status_id]
