"""Used to conduct tests on file Upload module"""
import src.External_API.sec_file as sf


# Test Cases
class TestCases:
    """Used to conduct test cases on file upload module"""
    def test_case1(self):
        """Test 1: Checks if module can check input typing"""
        assert sf.file_upload(1919810) == 301

    def test_case2(self):
        """Test 2: Checks if program can detect file types"""
        assert sf.file_upload('test.pptx') == 302

    def test_case3(self):
        """Test 3: Checks if a file already exists server-side"""
        assert sf.file_upload("test.pdf") == 303

    def test_case4(self):
        """Test 4: Checks if module can do successful execution"""
        assert sf.file_upload("new.pdf") == 0
