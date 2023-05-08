"""Used to conduct tests on multithread wrapper"""
import src.Internal_API.multithread as mt
import src.External_API.feed_ingester as fi
import src.External_API.sec_file as sf
import src.External_API.text_analysis as ta


# Test Cases
class TestCases:
    """Used to conduct test cases on multithreading helper module"""
    def test_case1(self):
        """Test 1: Checks if test items can be added to queue"""
        assert mt.test_queue(5) == 0

    def test_case2(self):
        """Test 2: Checks if feed ingester can be added to queue"""
        assert mt.add_to_queue(lambda: fi.filename_server_search("test.pdf", True)) == 0

    def test_case3(self):
        """Test 3: Checks if sec_file can be added to queue"""
        assert mt.add_to_queue(lambda: sf.file_upload("new.pdf")) == 0

    def test_case4(self):
        """Test 4: Checks if text analysis can be added to queue"""
        assert mt.add_to_queue(lambda: ta.pdf_to_text("test.pdf", 'Extracted Text',  1)) == 0

    def test_case5(self):
        """Test 5: Checks if queue can be processed"""
        assert mt.start_threading() == 0
