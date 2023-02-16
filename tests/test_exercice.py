import pytest

"""
FIXTURE
"""


@pytest.fixture
def first_fixture():
    data = {"first_name": "titi",
            "name": "toto"}
    return data


def test_with_first_fixture(first_fixture):
    print(first_fixture)
    assert first_fixture["first_name"] == "titi"
    assert first_fixture["name"] == "toto"


@pytest.fixture
def first_fixtures():
    data = {"first_name": "Ranga",
            "name": "Gonnage"}
    return data


@pytest.fixture
def second_fixtures(first_fixtures):
    first_fixtures["email"] = "test@test.com"
    return first_fixtures


def test_fixture(second_fixtures):
    assert second_fixtures["first_name"] == "Ranga"
    assert second_fixtures["name"] == "Gonnage"
    assert second_fixtures["email"] == "test@test.com"


"""
Tests unitaires:
    > test unitaire sur une classe
    > Operator = class importer (ligne 50)
    > multiplication = fonction importer(ligne 53)

"""


def test_should_make_multiplication():
    sut = Operators()
    operation = "5*5"
    expected_value = 25
    assert sut.multiplication(operation) == expected_value


"""
classe de TEST
"""


class TestClass:

    @classmethod
    def setup_class(cls):
        """ fonction appelée lors de la création de la classe"""

    @classmethod
    def teardown_class(cls):
        """ fonction appelée lors de la destruction de la classe"""

    def test_one(self):
        assert 1 == 1

    def test_two(self):
        assert 2 == 2


"""
tests d’intégration > Les tests d'intégration déterminent
si les unités logicielles développées indépendamment fonctionnent correctement
lorsqu'elles sont connectées les unes aux autres. 
"""


@pytest.mark.django_db
def test_login_route():

    client = Client()

 #Inscrire un utilisateur à l’aide de la vue `signup`afin de l’enregistrer dans la base de données
    credentials = {
        'first_name': 'Test',
        'last_name': 'User',
        'username': 'TestUser',
        'email': 'testuser@testing.com',
        'password1': 'TestPassword',
        'password2': 'TestPassword'
    }
    temp_user = client.post(reverse('signup'), credentials)

    #Connecter cet utilisateur avec la vue `login`
    response = client.post(reverse('login'), {'username': 'TestUser', 'password': 'TestPassword'})

    #Vérifier que la redirection vers la page d’accueil est effectuée
    assert response.status_code == 302
    assert response.url == reverse('home')

    #Vérifier que l’utilisateur est bien authentifié
    user = auth.get_user(client)
    assert user.is_authenticated


"""
Les tests de performance sont des procédures de test qui
 permettent de tester la vitesse,
le temps de réponse,
la stabilité
et l'utilisation des ressources d'une application logicielle
sous une charge de travail particulière.
"""

