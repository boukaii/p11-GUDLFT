# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.service import Service
# import time
#
# test = Service(ChromeDriverManager().install())
#
#
# def test_story():
#     chrome = webdriver.Chrome()
#     """
#     Permet de naviguer vers un lien
#     en passant par une url en paramètre
#     """
#     chrome.get('http://127.0.0.1:5000')
#     title = chrome.find_element(By.TAG_NAME, 'h1').text
#     assert 'Registration Portal' in title
#     assert chrome.current_url == 'http://127.0.0.1:5000/'
#     time.sleep(1)
#     # on récupère un élément grace a son ID
#     email = chrome.find_element(By.ID, 'email')
#     # on remplit du text sur l'élément selectionné
#     email.send_keys('john@simplylift.co')
#     time.sleep(1)
#     # # on vérifie qu'on est bien redirigé vers la bonne page
#     chrome.find_element(By.TAG_NAME, 'button').click()
#     time.sleep(1)
#     assert chrome.current_url == 'http://127.0.0.1:5000/showSummary'
#     chrome.find_element(By.LINK_TEXT, 'Book Places').click()
#     time.sleep(1)
#     assert chrome.current_url == 'http://127.0.0.1:5000/book/Spring%20Festival/Simply%20Lift'
#     chrome.close()
