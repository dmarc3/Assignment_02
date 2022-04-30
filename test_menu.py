'''
Unittest module.
Disable "Too many public methods" pylint message.
'''
# pylint: disable=R0904
import unittest
import os
import pdb
from mock import patch
import users
import user_status
import main
import menu

class TestMenu(unittest.TestCase):
    '''
    Test class for menu.py
    '''
    def setUp(self):
        '''
        setUp method to initialize collections.
        '''
        menu.user_collection = main.init_user_collection()
        menu.status_collection = main.init_status_collection()

    def test_load_users(self):
        '''
        Test load_users method
        Author: Kathleen Wong
        '''
        pass

    @patch('main.load_status_updates')
    def test_load_status_updates(self, mock_load):
        '''
        Test load_status_updates method
        Author: Marcus Bakke
        '''
        test_file = os.path.join('test_files',
                                 'test_good_status_updates.csv')
        with patch('builtins.input', return_value=test_file):
            menu.load_status_updates()
        self.assertTrue(mock_load.called)

    def test_add_user(self):
        '''
        Test add_users method
        Author: Kathleen Wong
        '''
        pass

    def test_update_user(self):
        '''
        Test update_users method
        Author: Kathleen Wong
        '''
        pass

    def test_search_user(self):
        '''
        Test search_users method
        Author: Kathleen Wong
        '''
        pass

    def test_delete_user(self):
        '''
        Test delete_users method
        Author: Kathleen Wong
        '''
        pass

    def test_save_user(self):
        '''
        Test save_users method
        Author: Kathleen Wong
        '''
        pass

    def test_add_status(self):
        '''
        Test add_status method
        Author: Marcus Bakke
        '''
        pass

    def test_udpate_status(self):
        '''
        Test update_status method
        Author: Marcus Bakke
        '''
        pass

    def test_search_status(self):
        '''
        Test search_status method
        Author: Marcus Bakke
        '''
        pass

    def test_delete_status(self):
        '''
        Test delete_status method
        Author: Marcus Bakke
        '''
        pass

    def test_save_status(self):
        '''
        Test save_status method
        Author: Marcus Bakke
        '''
        pass

    @patch('sys.exit')
    def test_quit_program(self, mock_exit):
        '''
        Test quit_program method
        Author: Marcus Bakke
        '''
        menu.quit_program()
        self.assertTrue(mock_exit.called)

if __name__ == '__main__':
    unittest.main()
