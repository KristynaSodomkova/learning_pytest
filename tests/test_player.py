from learning_pytest.player import Player
from learning_pytest.guardian import Guardian

def test_player():
    p = Player('Tatiana', 'Jones')
    assert p.first_name == 'Tatiana'
    assert p.last_name == 'Jones'
    assert p.guardians == []

def test_add_guardians():
    g = Guardian('Mary', 'Jones')
    p = Player('Tatiana', 'Jones')
    p.add_guardian(g)
    assert p.guardians == [g]