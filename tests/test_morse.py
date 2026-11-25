from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from main import translate

class MorseTests(unittest.TestCase):
    def test_original_encoding_convention(self):
        self.assertEqual(translate('sOs'), '...---...')
        self.assertEqual(translate('A B'), '.-/-...')
        self.assertEqual(translate('а?'), '.-..--..')
        self.assertEqual(translate('🙂'), '')
    def test_script_works_outside_repository(self):
        script = Path(__file__).resolve().parents[1] / 'main.py'
        with tempfile.TemporaryDirectory() as directory:
            result = subprocess.run([sys.executable, str(script)], input='SOS\n', cwd=directory, text=True, capture_output=True)
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout.strip(), '...---...')
