from stackapi import StackAPI


def test_buscar_questoes(tags):
    sopt = StackAPI("pt.stackoverflow")
    sopt.page_size = 100
    sopt.max_pages = 1
    questoes_python = sopt.fetch('questions', min=1, fromdate=1534582800, todate=1534636800)
    assert 1534625951 == questoes_python['items'][0]['creation_date']
