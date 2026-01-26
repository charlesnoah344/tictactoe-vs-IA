import pytest
from tictactoe import  initial_state, player, actions, result, winner, utility

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
    with pytest.raises(RuntimeError):
        result([[EMPTY, EMPTY, EMPTY],
                [EMPTY, EMPTY, EMPTY],
                [EMPTY, EMPTY, EMPTY]], (14,0))
        
    with pytest.raises(RuntimeError):
        result([[X, EMPTY, EMPTY],
                [EMPTY, EMPTY, EMPTY],
                [EMPTY, EMPTY, EMPTY]], (0,0))

    assert result([[EMPTY, EMPTY, EMPTY],
                   [EMPTY, EMPTY, EMPTY],
                   [EMPTY, EMPTY, EMPTY]], (0,0)) == [[X, EMPTY, EMPTY],
                                                      [EMPTY, EMPTY, EMPTY],
                                                      [EMPTY, EMPTY, EMPTY]]
    
def test_winner():
    assert winner([[X, O, O],
                   [EMPTY, X, O],
                   [EMPTY, EMPTY, X]]) == X
    
    assert winner([[O, O, O],
                   [X, X, EMPTY],
                   [X, EMPTY, EMPTY]]) == O
    
    assert winner([[X, O, EMPTY],
                   [EMPTY, O, EMPTY],
                   [X, O, X]]) == O
    
    assert winner([[O, O, X],
                   [O, X, EMPTY],
                   [X, EMPTY, EMPTY]]) == X
    
    assert winner([[EMPTY, EMPTY, EMPTY],
                   [EMPTY, EMPTY, EMPTY],
                   [EMPTY, EMPTY, EMPTY]]) == None
    
    assert winner([[X, O, O],
                   [EMPTY, X, EMPTY],
                   [X, EMPTY, O]]) == None
    
    assert winner([[X, O, O],
                   [O, X, X],
                   [X, O, O]]) == None

def test_utility():
    assert utility([[X, O, O],
                    [EMPTY, X, O],
                    [EMPTY, EMPTY, X]]) == 1
    
    assert utility([[O, O, O],
                    [X, X, EMPTY],
                    [X, EMPTY, EMPTY]]) == -1
    
    assert utility([[X, O, O],
                   [O, X, X],
                   [X, O, O]]) == 0
