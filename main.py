from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
import time
import os 
from selenium.webdriver.common.action_chains import ActionChains

# 4 0, 5 0, 6 0, 4 1, 6 1, 4 2, 5 2, 6 2; 

#cell size24 hd_closed hd_flag


"""
def counter(driver, mat):
	k = 0
	for y in range(9):
		for x in range(9):
			if mat[y][x] == "1":
				counter = 0
				if x-1 >= 0 and y-1 >= 0 and driver.find_element("id", f"cell_{x-1}_{y-1}").get_attribute('class') == "cell size24 hd_closed hd_flag":
					counter+=1
				if y-1 >= 0 and driver.find_element("id", f"cell_{x}_{y-1}").get_attribute('class') == "cell size24 hd_closed hd_flag":
					counter+=1
				if x+1 <= 8 and y-1 >= 0 and driver.find_element("id", f"cell_{x+1}_{y-1}").get_attribute('class') == "cell size24 hd_closed hd_flag":
					counter+=1
				if x-1 >= 0 and driver.find_element("id", f"cell_{x-1}_{y}").get_attribute('class') == "cell size24 hd_closed hd_flag":
					counter+=1
				if x+1 <= 8 and driver.find_element("id", f"cell_{x+1}_{y}").get_attribute('class') == "cell size24 hd_closed hd_flag":
					counter+=1
				if x-1 >= 0 and y+1 <= 8 and driver.find_element("id", f"cell_{x-1}_{y+1}").get_attribute('class') == "cell size24 hd_closed hd_flag":
					counter+=1
				if y+1 <= 8 and driver.find_element("id", f"cell_{x}_{y+1}").get_attribute('class') == "cell size24 hd_closed hd_flag":
					counter+=1
				if x+1 <= 8 and y+1 <= 8 and driver.find_element("id", f"cell_{x+1}_{y+1}").get_attribute('class') == "cell size24 hd_closed hd_flag":
					counter+=1
				if counter != 0:
					suspis = driver.find_element("id", f"cell_{x}_{y}").click()
					k+=1
	return k





def marking(driver,xlar,ylar):
	actions = ActionChains(driver)
	for j in range(len(xlar)):
		bomb = driver.find_element("id", f"cell_{xlar[j]}_{ylar[j]}")
		if driver.find_element("id", f"cell_{xlar[j]}_{ylar[j]}").get_attribute("class") != "cell size24 hd_closed hd_flag":
			actions.context_click(bomb).perform()


def check1(driver):
	for j in range(9):
		for i in range(9):
			if mat[j][i] == "1":
				counter = 0
				pair = ()
				if j-1 >= 0 and (mat[j-1][i] == "[]" or mat[j-1][i] == "🚩"):
					counter+=1
					pair = (j-1,i)
				if i-1 >= 0 and (mat[j][i-1] == "[]" or mat[j][i-1] == "🚩"):
					counter+=1
					pair = (j,i-1)
				if i-1 >= 0  and j-1 >= 0 and (mat[j-1][i-1] == "[]" or mat[j-1][i-1] == "🚩"):
					counter+=1
					pair = (j-1,i-1)
				if i+1 <= 8 and (mat[j][i+1] == "[]" or mat[j][i+1] == "🚩"):
					counter+=1
					pair = (j,i+1)
				if j+1 <= 8 and (mat[j+1][i] == "[]" or mat[j+1][i] == "🚩"):	
					counter+=1
					pair = (j+1,i)
				if i+1 <= 8 and j+1 <= 8 and (mat[j+1][i+1] == "[]" or mat[j+1][i+1] == "🚩"):
					counter+=1
					pair = (j+1,i+1)
				if i-1 >= 0 and j+1 <= 8 and (mat[j+1][i-1] == "[]" or mat[j+1][i-1] == "🚩"):
					counter+=1
					pair = (j+1,i-1)
				if i+1 <= 8 and j-1 >= 0 and (mat[j-1][i+1] == "[]" or mat[j-1][i+1] == "🚩"):
					counter+=1
					pair = (j-1,i+1)
				if counter == 1:
					#mat[pair[0]][pair[1]] = "B"
					listk.append(pair)
	for j in listk:
		mat[j[0]][j[1]] = "🚩"

	return mat
	
def printing(driver):
	mat = [[0 for j in range(9)] for i in range(9)]
	
	for i in range(0,9):
		for j in range(0,9):
			element = driver.find_element("id", f"cell_{j}_{i}")
			if element.get_attribute('class') == "cell size24 hd_closed":
				print("-", end = '\t')
				mat[i][j] = "[]" 
			elif element.get_attribute('class') == "cell size24 hd_opened hd_type1":
				print("1", end = '\t')
				mat[i][j] = "1"
			elif element.get_attribute('class') == "cell size24 hd_opened hd_type2":
				print("2", end = '\t')
				mat[i][j] = "2"
			elif element.get_attribute('class') == "cell size24 hd_opened hd_type3":
				print("3", end = '\t')
				mat[i][j] = "3"
			elif element.get_attribute('class') == "cell size24 hd_opened hd_type4":
				print("4", end = '\t')
				mat[i][j] = "4"
			elif element.get_attribute('class') == "cell size24 hd_opened hd_type5":
				print("5", end = '\t')
				mat[i][j] = "5"
			elif element.get_attribute('class') == "cell size24 hd_opened hd_type6":
				print("6", end = '\t')
				mat[i][j] = "6"
			elif element.get_attribute('class') == "cell size24 hd_opened hd_type7":
				print("7", end = '\t')
				mat[i][j] = "7"
			elif element.get_attribute('class') == "cell size24 hd_opened hd_type8":
				print("8", end = '\t')
				mat[i][j] = "8"
			elif element.get_attribute('class') == "cell size24 hd_closed start":
				print("x", end = '\t')
				mat[i][j] = "x"
			elif element.get_attribute('class') == "cell size24 hd_opened hd_type0":
				print("0", end = '\t')
				mat[i][j] = "-"
			elif element.get_attribute('class') == "cell size24 hd_closed hd_flag":
				print("🚩", end = '\t')
		print("\n")
	return mat
"""


def start(driver):
	for j in range(9):
		for i in range(9):
			if driver.find_element("id", f"cell_{j}_{i}").get_attribute("class") == "cell size24 hd_closed start":
				driver.find_element("id", f"cell_{j}_{i}").click()
				print("Start verildi.!")

def birlerinyerleri(driver,k):
	xlar = []
	ylar = []
	for j in range(9):
		for i in range(9):
			if driver.find_element("id", f"cell_{j}_{i}").get_attribute("class") == f"cell size24 hd_opened hd_type{k}":
				xlar+=[j]
				ylar+=[i]
	return xlar, ylar

def bayraqlama(driver,xlar,ylar,k):

	
	target_xlar = []
	target_ylar = []
		
	for j in range(len(xlar)):
		arr = []
		x = xlar[j]
		y = ylar[j]	
		counter = 0
		counter_flag = 0
		if x-1 >= 0 and y-1 >= 0:
			if driver.find_element("id", f"cell_{x-1}_{y-1}").get_attribute("class") == "cell size24 hd_closed":
				counter+=1
				target_x = x-1
				target_y = y-1
				arr+=[target_x, target_y]
			if driver.find_element("id", f"cell_{x-1}_{y-1}").get_attribute("class") == "cell size24 hd_closed hd_flag":
				counter_flag +=1

		if y-1 >= 0:
			if driver.find_element("id", f"cell_{x}_{y-1}").get_attribute("class") == "cell size24 hd_closed":
				counter+=1
				target_x = x
				target_y = y-1
				arr+=[target_x, target_y]
			if driver.find_element("id", f"cell_{x}_{y-1}").get_attribute("class") == "cell size24 hd_closed hd_flag":
				counter_flag +=1

		if x+1 <= 8 and y-1 >= 0:
			if driver.find_element("id", f"cell_{x+1}_{y-1}").get_attribute("class") == "cell size24 hd_closed":
				counter+=1
				target_x = x+1
				target_y = y-1
				arr+=[target_x, target_y]				
			if driver.find_element("id", f"cell_{x+1}_{y-1}").get_attribute("class") == "cell size24 hd_closed hd_flag":
				counter_flag+=1

		if x-1 >= 0:
			if driver.find_element("id", f"cell_{x-1}_{y}").get_attribute("class") == "cell size24 hd_closed":
				counter+=1
				target_x = x-1
				target_y = y
				arr+=[target_x, target_y]
			if driver.find_element("id", f"cell_{x-1}_{y}").get_attribute("class") == "cell size24 hd_closed hd_flag":
				counter_flag+=1

		if x+1 <= 8:
			if driver.find_element("id", f"cell_{x+1}_{y}").get_attribute("class") == "cell size24 hd_closed":
				counter+=1
				target_x = x+1
				target_y = y
				arr+=[target_x, target_y]
			if driver.find_element("id", f"cell_{x+1}_{y}").get_attribute("class") == "cell size24 hd_closed hd_flag":
				counter_flag+=1

		if x-1>=0 and y+1 <= 8:
			if driver.find_element("id", f"cell_{x-1}_{y+1}").get_attribute("class") == "cell size24 hd_closed":
				counter+=1
				target_x = x-1
				target_y = y+1
				arr+=[target_x, target_y]
			if driver.find_element("id", f"cell_{x-1}_{y+1}").get_attribute("class") == "cell size24 hd_closed hd_flag":
				counter_flag+=1

		if y+1 <= 8:
			if driver.find_element("id", f"cell_{x}_{y+1}").get_attribute("class") == "cell size24 hd_closed":
				counter+=1
				target_x = x
				target_y = y+1
				arr+=[target_x, target_y]
			if driver.find_element("id", f"cell_{x}_{y+1}").get_attribute("class") == "cell size24 hd_closed hd_flag":
				counter_flag+=1

		if x+1 <= 8 and y+1 <= 8:
			if driver.find_element("id", f"cell_{x+1}_{y+1}").get_attribute("class") == "cell size24 hd_closed":
				counter+=1
				target_x = x+1
				target_y = y+1
				arr+=[target_x, target_y]
			if driver.find_element("id", f"cell_{x+1}_{y+1}").get_attribute("class") == "cell size24 hd_closed hd_flag":
				counter_flag+=1

		print(f"{x}, {y} koordinatındakı {k}nın ətrafında {counter} qədər bağlı xana var. Bağlı -> {counter}. Bayraqlı -> {counter_flag}\n")
		if counter + counter_flag == k:
			if counter_flag != k:
				for o in range(0,len(arr),2):
					if driver.find_element("id", f"cell_{arr[o]}_{arr[o+1]}").get_attribute("class") != "cell size24 hd_closed hd_flag":
						actions = ActionChains(driver)
						actions.context_click(driver.find_element("id", f"cell_{arr[o]}_{arr[o+1]}")).perform()
						#target_xlar+=[target_x]
						#target_ylar+=[target_y]
						target_xlar+=[arr[o]]
						target_ylar+=[arr[o+1]]
						time.sleep(2)

	return target_xlar, target_ylar

def clicking(driver):
	n = [1,2,3,4,5,6]
	for j in range(9):
		for i in range(9):
			for k in n:
				if driver.find_element("id", f"cell_{j}_{i}").get_attribute("class") == f"cell size24 hd_opened hd_type{k}":
					driver.find_element("id", f"cell_{j}_{i}").click()
					break

"""
def clicking(driver,target_xlar,target_ylar,k):
	for j in range(len(target_xlar)):
		x = target_xlar[j]
		y = target_ylar[j]
		if x-1 >= 0 and y-1 >= 0:
			if driver.find_element("id", f"cell_{x-1}_{y-1}").get_attribute("class") == f"cell size24 hd_opened hd_type{k}":
				driver.find_element("id", f"cell_{x-1}_{y-1}").click()
				time.sleep(2)
		if y-1 >= 0:
			if driver.find_element("id", f"cell_{x}_{y-1}").get_attribute("class") == f"cell size24 hd_opened hd_type{k}":
				driver.find_element("id", f"cell_{x}_{y-1}").click()
				time.sleep(2)
		if x+1 <= 8 and y-1 >= 0:
			if driver.find_element("id", f"cell_{x+1}_{y-1}").get_attribute("class") == f"cell size24 hd_opened hd_type{k}":
				driver.find_element("id", f"cell_{x+1}_{y-1}").click()
				time.sleep(2)
		if x-1 >= 0:
			if driver.find_element("id", f"cell_{x-1}_{y}").get_attribute("class") == f"cell size24 hd_opened hd_type{k}":
				driver.find_element("id", f"cell_{x-1}_{y}").click()
				time.sleep(2)
		if x+1 <= 8:
			if driver.find_element("id", f"cell_{x+1}_{y}").get_attribute("class") == f"cell size24 hd_opened hd_type{k}":
				driver.find_element("id", f"cell_{x+1}_{y}").click()
				time.sleep(2)
		if x-1 >= 0 and y+1 <= 8:
			if driver.find_element("id", f"cell_{x-1}_{y+1}").get_attribute("class") == f"cell size24 hd_opened hd_type{k}":
				driver.find_element("id", f"cell_{x-1}_{y+1}").click()
				time.sleep(2)
		if y+1 <= 8:
			if driver.find_element("id", f"cell_{x}_{y+1}").get_attribute("class") == f"cell size24 hd_opened hd_type{k}":
				driver.find_element("id", f"cell_{x}_{y+1}").click()
				time.sleep(2)
		if x+1 <= 8 and y+1 <= 8:
			if driver.find_element("id", f"cell_{x+1}_{y+1}").get_attribute("class") == f"cell size24 hd_opened hd_type{k}":
				driver.find_element("id", f"cell_{x+1}_{y+1}").click()
				time.sleep(2)
		print(f"XLAR -> {x}; YLAR -> {y}")
"""






os.system("cls")
driver = webdriver.Firefox()
driver.get("https://minesweeper.online/")
time.sleep(3)
driver.find_element("xpath", "/html/body/header/div/div/div/button[2]").click()
time.sleep(3)
driver.find_element("xpath", '//*[@id="sign_in_username"]').send_keys("ilhamyaqubzade5@gmail.com")
driver.find_element("xpath", '//*[@id="sign_in_password"]').send_keys("ilham2004123")
driver.find_element("xpath", '/html/body/div[6]/div/div/form/div[3]/button[2]').click()
driver.get("https://minesweeper.online/game/2798763689")
time.sleep(5)


xlar = []
ylar = []

start(driver)

time.sleep(1)
for i in range(1,7):
	for j in range(1,i+1):
		xlar, ylar = birlerinyerleri(driver,j)
		target_xlar, target_ylar = bayraqlama(driver,xlar,ylar,j)
		#clicking(driver,target_xlar,target_ylar,j)
		clicking(driver)
		print(f"{j}lər bitdi!\n")

input()
driver.quit()