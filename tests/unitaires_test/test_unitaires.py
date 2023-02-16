import server
import pytest

client = server.app.test_client()


"""
FIXTURE
"""


@pytest.fixture
def clubs():
    clubs = server.clubs = [
        {
            "name": "Test",
            "email": "test@test.com",
            "points": "20"
        }
        ]
    return clubs


def test_check_if_a_user_exists(clubs):
    """
    Véifier si l'adresse email existe
    si l'e-mail existe et redirigez l'utilisateur("/showSummary")
    """
    response = client.post("/showSummary", data=clubs[0])
    assert response.status_code == 200
    assert b"test@test.com" in response.data


"""
Test unitaires
"""


def test_index_url_is_online():
    """
        vérifier si le code d'état renvoyé est 200 lorsqu'on est sur page "index"
    """
    response = client.get("/")
    assert response.status_code == 200


def test_check_if_a_user_doesnt_exists():
    """
    Véifier si l'adresse email existe
    """
    response = client.post("/showSummary", data={'email': 'dfgfdg'})
    assert response.status_code == 500


def test_empty_email():
    """
    Vérifier si le champs de l'adresse email est pas vide
    """
    response = client.post("/showSummary", data={"email": ""})
    assert response.status_code == 500


def test_logout_url_redirect_to_index():
    """
        vérifier si le code d'état renvoyé est 302 lorsqu'on se déconnecte
    """
    response = client.get("/logout")
    assert response.status_code == 302

