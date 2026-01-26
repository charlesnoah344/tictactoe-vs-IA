import pytest
from tictactoe import  initial_state, player, actions, result

EMPTY = None
X = "X"
O = "O"

def test_initial_state():
    assert initial_state() == [[EMPTY, EMPTY, EMPTY],
                               [EMPTY, EMPTY, EMPTY],
                               [EMPTY, EMPTY, EMPTY]]
    
def test_player():
    assert player([[EMPTY, EMPTY, EMPTY],
                   [EMPTY, EMPTY, EMPTY],
                   [EMPTY, EMPTY, EMPTY]]) == X
    
    assert player([[EMPTY, EMPTY, EMPTY],
                   [EMPTY, X, EMPTY],
                   [EMPTY, EMPTY, EMPTY]]) == O
    
    assert player([[EMPTY, EMPTY, EMPTY],
                   [EMPTY, X, EMPTY],
                   [EMPTY, EMPTY, O]]) == X
    
def test_actions():
    assert actions([[X, O, O],
                   [EMPTY, X, EMPTY],
                   [X, EMPTY, O]]) == {(1,0), (1,2), (2,1)}

def test_result():
    assert result([[EMPTY, EMPTY, EMPTY],
                   [EMPTY, EMPTY, EMPTY],
                   [EMPTY, EMPTY, EMPTY]], (0,0)) == [[X, EMPTY, EMPTY],
                                                      [EMPTY, EMPTY, EMPTY],
                                                      [EMPTY, EMPTY, EMPTY]]