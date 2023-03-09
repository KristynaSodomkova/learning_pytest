from learning_pytest.guardian import Guardian
def test_construction():
    g = Guardian('Mary', 'Jones')
    assert g.first_name == 'Mary'
    assert g.first_name == 'Jones'


