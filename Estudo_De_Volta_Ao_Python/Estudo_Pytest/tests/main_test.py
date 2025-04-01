from main import calcularDiviãoPorDois, obterInformações

def test_calcularDiviãoPorDois():
    response = calcularDiviãoPorDois(8)

    assert response == 4
    assert isinstance(response, int)


def test_obterInformações():
    response = obterInformações()

    assert isinstance(response, dict)
    assert "name" in response
    assert "height" not in response
    assert "Luna" in response["name"]