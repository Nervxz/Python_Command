import io
import unittest
import os
from io import StringIO
from unittest.mock import patch
import shutil

# Import the code you want to test
from Command import ls, cd, pwd, find

class Test_Command(unittest.TestCase):
    def setUp(self):
    # Save the original working directory
        self.original_dir = os.getcwd()
    # Create a temporary directory for testing
        self.test_dir = os.path.join(os.getcwd(), 'test_dir')
    # Remove the existing directory if it exists
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)
        os.mkdir(self.test_dir)
        os.chdir(self.test_dir)
        
        import Command
        Command.current_dir = self.test_dir

    def tearDown(self):
    # Change back to the original working directory
        os.chdir(self.original_dir)
    # Remove the temporary directory if it exists
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)

    @patch('sys.stdout', new_callable=StringIO)
    def test_ls(self, mock_stdout):
        # Create some test files and directories
        os.mkdir('subdir')
        open('file1.txt', 'w').close()
        open('file2.txt', 'w').close()

        ls()
        output = mock_stdout.getvalue().strip().split('\n')
        expected_output = ['subdir', 'file1.txt', 'file2.txt']
        self.assertCountEqual(output, expected_output)

    def test_cd(self):
    # Create a subdirectory
        subdir_path = os.path.join(self.test_dir, 'subdir')
        os.mkdir(subdir_path)

    # Change to the subdirectory
        cd('subdir')
        self.assertEqual(os.getcwd(), subdir_path)

    # Change back to the parent directory
        cd('..')
        self.assertEqual(os.getcwd(), self.test_dir)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_pwd(self, mock_stdout):
        # Call the pwd() function
        returned_dir = pwd()

        # Assert that the returned directory matches the expected directory (self.test_dir)
        self.assertEqual(returned_dir, self.test_dir)
    
  
    @patch('sys.stdout', new_callable=StringIO)
    def test_find(self, mock_stdout):
    # Create some test files and directories
        os.mkdir('subdir')
        open('file1.txt', 'w').close()
        subdir_path = os.path.join(self.test_dir, 'subdir')
        open(os.path.join(subdir_path, 'file2.txt'), 'w').close()
        open(os.path.join(subdir_path, 'test_file.txt'), 'w').close()

    # Call the find function
        find('file')

if __name__ == '__main__':
    unittest.main()
