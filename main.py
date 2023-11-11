from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
import time
import os 


def check1(mat):
	for j in range(9):
		for i in range(9):
			if mat[j][i] == "1":
				counter = 0
				pair = ()
				if j-1 >= 0 and mat[j-1][i] == "[]":
					counter+=1
					pair = (j-1,i)
				if i-1 >= 0 and mat[j][i-1] == "[]":
					counter+=1
					pair = (j,i-1)
				if i-1 >= 0  and j-1 >= 0 and mat[j-1][i-1] == "[]":
					counter+=1
					pair = (j-1,i-1)
				if i+1 <= 8 and mat[j][i+1] == "[]":
					counter+=1
					pair = (j,i+1)
				if j+1 <= 8 and mat[j+1][i] == "[]":
					counter+=1
					pair = (j+1,i)
				if i+1 <= 8 and j+1 <= 8 and mat[j+1][i+1] == "[]":
					counter+=1
					pair = (j+1,i+1)
				if i-1 >= 0 and j+1 <= 8 and mat[j+1][i-1] == "[]":
					counter+=1
					pair = (j+1,i-1)
				if i+1 <= 8 and j-1 >= 0 and mat[j-1][i+1] == "[]":
					counter+=1
					pair = (j-1,i+1)
				if counter == 1:
					mat[pair[0]][pair[1]] = "B"
	return mat
				
				
				




def printing(driver):
	mat = [[0 for j in range(9)] for i in range(9)]
	for i in range(0,9):
		for j in range(0,9):
			element = driver.find_element("id", f"cell_{j}_{i}")
			if element.get_attribute('class') == "cell size24 hd_closed":
				print("-", end = ' ')
				mat[i][j] = "[]" 
			elif element.get_attribute('class') == "cell size24 hd_opened hd_type1":
				print("1", end = ' ')
				mat[i][j] = "1"
			elif element.get_attribute('class') == "cell size24 hd_opened hd_type2":
				print("2", end = ' ')
				mat[i][j] = "2"
			elif element.get_attribute('class') == "cell size24 hd_opened hd_type3":
				print("3", end = ' ')
				mat[i][j] = "3"
			elif element.get_attribute('class') == "cell size24 hd_opened hd_type4":
				print("4", end = ' ')
				mat[i][j] = "4"
			elif element.get_attribute('class') == "cell size24 hd_opened hd_type5":
				print("5", end = ' ')
				mat[i][j] = "5"
			elif element.get_attribute('class') == "cell size24 hd_opened hd_type6":
				print("6", end = ' ')
				mat[i][j] = "6"
			elif element.get_attribute('class') == "cell size24 hd_opened hd_type7":
				print("7", end = ' ')
				mat[i][j] = "7"
			elif element.get_attribute('class') == "cell size24 hd_opened hd_type8":
				print("8", end = ' ')
				mat[i][j] = "8"
			elif element.get_attribute('class') == "cell size24 hd_closed start":
				print("x", end = ' ')
				mat[i][j] = "x"
			elif element.get_attribute('class') == "cell size24 hd_opened hd_type0":
				print("0", end = ' ')
				mat[i][j] = "-"
		print("\n")
	return mat


os.system("cls")
driver = webdriver.Firefox()
driver.get("https://minesweeper.online/")
time.sleep(3)
driver.find_element("xpath", "/html/body/header/div/div/div/button[2]").click()
time.sleep(3)
driver.find_element("xpath", '//*[@id="sign_in_username"]').send_keys("ilhamyaqubzade4@gmail.com")
driver.find_element("xpath", '//*[@id="sign_in_password"]').send_keys("ilhaM2004123")
driver.find_element("xpath", '/html/body/div[6]/div/div/form/div[3]/button[2]').click()

#driver.find_element("xpath", '/html/body/div[3]/div[2]/div/div[1]/div[1]/div/ul[1]/li[2]/a')
driver.get("https://minesweeper.online/game/2789868231")
time.sleep(3)

"""
element_with_id = driver.find_element("id","cell_0_0") 
class_name = element_with_id.get_attribute('class')    
print(class_name)
"""
# cell_0_0

printing(driver)

for i in range(0,9):
	for j in range(0, 9):
		element = driver.find_element("id", f"cell_{j}_{i}")
		if element.get_attribute('class') == "cell size24 hd_closed start":
			print("Tapıldı!")
			element.click()

os.system("cls")

mat = printing(driver)

mat = check1(mat)

for i in range(9):
	for j in range(9):
		print(mat[i][j], end = '\t')
	print()


driver.quit()
