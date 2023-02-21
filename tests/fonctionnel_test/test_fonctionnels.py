from selenium import webdriver
from selenium.webdriver.common.by import By


def test_story():
    chrome = webdriver.Chrome()
    """
    Permet de naviguer vers un lien
    en passant par une url en paramètre 
    """
    chrome.get('http://127.0.0.1:5000/')

    title = chrome.find_element(By.TAG_NAME, 'h1').text
    assert 'Welcome to the GUDLFT Registration Portal!' in title
    assert chrome.current_url == 'http://127.0.0.1:5000/'

    name = chrome.find_element(By.ID, 'name')
    name.send_keys('Simply Lift')
    # on récupère un élément grace a son ID
    email = chrome.find_element(By.ID, 'email')
    # on remplit du text sur l'élément selectionné
    email.send_keys('john@simplylift.co')

    # on vérifie qu'on est bien redirigé vers la bonne page
    chrome.find_element(By.TAG_NAME, 'button').click()
    assert chrome.current_url == 'http://127.0.0.1:5000/showSummary'

    chrome.find_element(By.LINK_TEXT, 'Book Places').click()
    assert chrome.current_url == 'http://127.0.0.1:5000/' \
                                 'book/Spring%20Festival/Iron%20Temple'
    chrome.close()
