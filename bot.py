from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, UnexpectedAlertPresentException
import random
import threading

class Bot:
	KAHOOT_URL = 'https://kahoot.it/'
	GAME_ID_ID = 'game-input'
	NICKNAME_ID = 'nickname'
	SUBMIT_ID_XPATH = '/html/body/div/div[1]/div/div[2]/main/div/form/input'
	SUBMIT_NICKNAME_XPATH = '/html/body/div/div[1]/div/div[2]/main/div/form/button'
	BUTTON_XPATH = '/html/body/div/div[1]/main/div[2]/div/div/button'
	PODIUM_URL = 'https://kahoot.it/v2/ranking'

	def __init__(self, idd, nick):
		chrome_options = Options()
		chrome_options.add_argument("--disable-popup-blocking")
		chrome_options.add_argument('--disable-notifications')
		chrome_options.add_argument('--ignore-ssl-errors')
		chrome_options.add_argument("--headless") 
		self.nick = nick
		self.id = idd
		self.driver = webdriver.Chrome(chrome_options=chrome_options)
		self.driver.get(self.KAHOOT_URL)
		self.start()

	def start(self):
		try:
			game_id = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, self.GAME_ID_ID)))
			game_id.clear()
			game_id.send_keys(self.id)
			game_id.send_keys(Keys.RETURN)

			nickname = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, self.NICKNAME_ID)))
			nickname.clear()
			nickname.send_keys(self.nick)
			nickname.send_keys(Keys.RETURN)

			while True:
				try:
					if self.driver.current_url == self.PODIUM_URL:
						self.driver.close()	
						exit(1)
					buttons = self.driver.find_elements_by_xpath(self.BUTTON_XPATH)
					buttons[random.randint(0, len(buttons)-1)].click()
				except:
					pass

		except TimeoutException:
			self.driver.close()
			return "Timed Out"

def start(idd, basename, amount):
	for i in range(amount):
		thread = threading.Thread(target=Bot, args=(idd, f'{basename}{i}'))
		thread.start()