import unittest
from unittest.mock import patch
from io import StringIO
import sys

class TestMiniGame(unittest.TestCase):
    def test_invalid_option(self):
        with patch('builtins.input', return_value='invalid'):
            captured_output = StringIO()
            sys.stdout = captured_output
            play_game()
            sys.stdout = sys.__stdout__
            self.assertEqual(captured_output.getvalue().strip(), "Invalid option. Please choose rock, paper, or scissors.")

    def test_player_wins(self):
        with patch('builtins.input', side_effect=['rock', 'scissors']):
            captured_output = StringIO()
            sys.stdout = captured_output
            play_game()
            sys.stdout = sys.__stdout__
            self.assertEqual(captured_output.getvalue().strip(), "You win!")

    def test_player_loses(self):
        with patch('builtins.input', side_effect=['paper', 'scissors']):
            captured_output = StringIO()
            sys.stdout = captured_output
            play_game()
            sys.stdout = sys.__stdout__
            self.assertEqual(captured_output.getvalue().strip(), "You lose!")

    def test_tie(self):
        with patch('builtins.input', side_effect=['rock', 'rock']):
            captured_output = StringIO()
            sys.stdout = captured_output
            play_game()
            sys.stdout = sys.__stdout__
            self.assertEqual(captured_output.getvalue().strip(), "It's a tie!")

    def test_play_again(self):
        with patch('builtins.input', side_effect=['rock', 'yes', 'paper', 'no']):
            captured_output = StringIO()
            sys.stdout = captured_output
            play_game()
            sys.stdout = sys.__stdout__
            self.assertEqual(captured_output.getvalue().strip(), "Do you want to play again? (yes/no): Game over. Your score: 1")

if __name__ == '__main__':
    unittest.main()