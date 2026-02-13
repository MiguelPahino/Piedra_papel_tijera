import pytest
from src.rock_paper_scissors import Game, GameAction


@pytest.fixture
def game():
    """Fixture que crea una instancia de Game para cada test"""
    return Game()


class TestDraw:
    """Pruebas de empate"""
    
    def test_rock_draw(self, game):
        game.assess_game(GameAction.Rock, GameAction.Rock)
    
    def test_paper_draw(self, game):
        game.assess_game(GameAction.Paper, GameAction.Paper)
    
    def test_scissors_draw(self, game):
        game.assess_game(GameAction.Scissors, GameAction.Scissors)


class TestRock:
    """Pruebas con Rock"""
    
    def test_rock_beats_scissors(self, game):
        """Rock gana a Scissors"""
        game.assess_game(GameAction.Rock, GameAction.Scissors)
    
    def test_rock_loses_to_paper(self, game):
        """Rock pierde a Paper"""
        game.assess_game(GameAction.Rock, GameAction.Paper)


class TestPaper:
    """Pruebas con Paper"""
    
    def test_paper_beats_rock(self, game):
        """Paper gana a Rock"""
        game.assess_game(GameAction.Paper, GameAction.Rock)
    
    def test_paper_loses_to_scissors(self, game):
        """Paper pierde a Scissors"""
        game.assess_game(GameAction.Paper, GameAction.Scissors)


class TestScissors:
    """Pruebas con Scissors"""
    
    def test_scissors_beats_paper(self, game):
        """Scissors gana a Paper"""
        game.assess_game(GameAction.Scissors, GameAction.Paper)
    
    def test_scissors_loses_to_rock(self, game):
        """Scissors pierde a Rock"""
        game.assess_game(GameAction.Scissors, GameAction.Rock)
