"""Used to conduct tests on text analysis module"""
import src.External_API.text_analysis as analysis

# Test Error Cases
class TestCases:
    """Used to conduct test cases on text analysis module"""
    def test_case1(self):
        """Test 1: Checks if module can check input typing"""
        assert analysis.text_analyze(12345, False) == 102

    def test_case2(self):
        """Test 2: Checks if module can detect min text length"""
        assert analysis.text_analyze('at', False) == 103

    def test_case3(self):
        """Test 3: Checks if module can detect max text length"""
        assert analysis.text_analyze("This is the max length of the text", False) == 104

    def test_case4(self):
        """Test 4: Checks if module can do successful execution"""
        assert analysis.text_analyze("Here is test 5!", False) == 0

    def test_case5(self):
        """Test 5: Checks if module can detect missing PDF file"""
        assert analysis.pdf_to_text("nonexistfile.pdf", 'test',  1) == 201

    def test_case6(self):
        """Test 6: Checks if module can detect invalid file format"""
        assert analysis.pdf_to_text("test.txt", 'test', 1) == 202

    def test_case7(self):
        """Test 7: Checks if module can handle PDF reading error"""
        assert analysis.pdf_to_text('test.pdf', 'test', 1) == 203

    def test_case8(self):
        """Test 8: Checks if module can detect PDF with no pages"""
        assert analysis.pdf_to_text('test.pdf', 'test', 0) == 204

    def test_case9(self):
        """Test 7: Checks if module can do successful pdf -> string conversion"""
        assert analysis.pdf_to_text("test.pdf", 'Extracted Text',  1) == 0
