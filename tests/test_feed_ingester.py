"""Used to conduct tests on feed ingester module"""
import src.External_API.feed_ingester as fi


# Test Cases
class TestCases:
    """Used to conduct test cases on feed ingester module"""
    def test_case1(self):
        """Test 1: Checks if module can detect filename length in search"""
        assert fi.filename_server_search("ExtremelyVeryLongNameTest.pdf", True) == 105

    def test_case2(self):
        """Test 2: Checks if program can detect when a file isn't found"""
        assert fi.filename_server_search("NotFound.pdf", False) == 106

    def test_case3(self):
        """Test 3: Checks if a file search can execute properly"""
        assert fi.filename_server_search("test.pdf", True) == 0
