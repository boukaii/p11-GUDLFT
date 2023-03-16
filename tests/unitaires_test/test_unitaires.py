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


@pytest.fixture
def competitions():
    competitions = server.competitions = [
        {
            "name": "Test Festival 2018",
            "date": "2018-03-27 10:00:00",
            "numberOfPlaces": "25"
        },
        {
            "name": "Test Festival_2025",
            "date": "2025-03-27 10:00:00",
            "numberOfPlaces": "25"
        }
        ]
    return competitions


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


def test_valid_email(clubs):
    response = client.post("/showSummary", data={'email': 'test@test.com'})
    assert response.status_code == 200


def test_check_if_a_user_doesnt_exists():
    """
    Véifier si l'adresse email existe
    """
    response = client.post("/showSummary", data={'email': 'dfgfdg'})
    assert response.status_code == 302


def test_empty_email():
    """
    Vérifier si le champs de l'adresse email est pas vide
    """
    response = client.post("/showSummary", data={"email": ""})
    assert response.status_code == 302


def test_logout_url_redirect_to_index():
    """
        vérifier si le code d'état renvoyé est 302 lorsqu'on se déconnecte
    """
    response = client.get("/logout")
    assert response.status_code == 302


def test_competition_booking_url_is_online(competitions):
    """
    DONNÉ une demande sur la page de réservation
    QUAND la page '/book/<competition_name>/<club_name>' reçoit la demande (GET)
    ALORS vérifier si le code d'état renvoyé est 200, et si un texte est dans la réponse
    """
    with client as c:
        response = c.get("/book/Test%20Festival_2025/Test")
        assert response.status_code == 200
        assert b"Test Festival 2025"


def test_booking_a_competition(clubs, competitions):
    """
    DONNÉ à un utilisateur remplissant un formulaire pour réserver un concours
    QUAND la page '/purchasePlaces' reçoit la demande de formulaire (POST)
    ALORS vérifier si le code d'état renvoyé est 200, et si un texte est dans la réponse

    """
    with client as c:
        response = c.post("/purchasePlaces", data={"places": "4",
                                                   "club": clubs[0]["name"],
                                                   "competition": competitions[0]["name"]
                                                   })
        assert response.status_code == 200
        assert b"Great, booking complete!"


def test_booking_more_than_12_places(clubs, competitions):
    """
    DONNÉ un utilisateur remplissant un formulaire pour réserver une compétition, essayant de réserver plus de 12 places
    QUAND la page '/purchasePlaces' reçoit la demande de formulaire (POST)
    ALORS vérifier si le code d'état renvoyé est 200, et si un texte est dans la réponse
    """
    with client as c:
        response = c.post("/purchasePlaces", data={"places": "15",
                                                   "club": clubs[0]["name"],
                                                   "competition": competitions[0]["name"]
                                                   })
        assert response.status_code == 200
        assert b"Vous ne pouvez pas reserver plus de 12 places dans un concours."


def test_3_points_to_book_a_competition(clubs, competitions):

    old_clubs_points = int(clubs[0]["points"])

    with client as c:
        response = c.post("/purchasePlaces", data={"places": "1",
                                                   "club": clubs[0]["name"],
                                                   "competition": competitions[0]["name"]
                                                   })
        assert response.status_code == 200
        assert old_clubs_points - 3 == int(clubs[0]["points"])


def test_purchasePlaces_more_points_allowed(clubs, competitions):
    """
        Lorsque l'utilisateur indique plus d'inscription
        que de points, il ne déduit pas de points.
    """
    response = client.post(
        '/purchasePlaces',
        data={
            'club': 'Test',
            'competition': 'Test Festival 2018',
            'places': '1000'
        }
    )
    assert response.status_code == 200
    assert server.clubs[0]['points'] == "20"
    assert server.competitions[1]['numberOfPlaces'] == "25"


def test_book_places_in_past_competitions(clubs, competitions):

    response = client.get(
        '/book/Test Festival_2025/Test'
    )
    assert response.status_code == 200


def test_purchasePlaces_points_deducted(clubs, competitions):

    POINTS_PER_PLACE = 3

    """
    Vérification de la déduction des points club à l'inscription
    """


    response = client.post(
        '/purchasePlaces',
        data={
            'club': 'Test',
            'competition': 'Test Festival 2018',
            'places': '1'
        }
    )
    assert response.status_code == 200
    assert server.clubs[0]['points'] == 20 - 1 * POINTS_PER_PLACE


def test_ClubsPoints(clubs, competitions):
    response = client.get('/board')
    assert response.status_code == 200

