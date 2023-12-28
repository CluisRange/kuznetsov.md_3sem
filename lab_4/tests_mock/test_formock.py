from unittest.mock import mock_open, patch
import formock

def test_formock():
    with patch("builtins.open", mock_open(read_data="\n\n PASS LOLOLO")) as mock_file:
        formock.formock()
        mock_file.assert_called_once_with("res\primer_faila.txt", 'r')