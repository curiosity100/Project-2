import sys
import pytest
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time

def test_login_01():
    #Positive scenario
    service = Service(executable_path=GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service)
    url = "https://opensource-demo.orangehrmlive.com/"
    driver.get(url)
    time.sleep(3)
    WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//input[@placeholder='Username']")))
    driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
    driver.find_element(By.XPATH, "// input[@placeholder='Password']").send_keys("admin123")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(3)
    # Login success verification
    success_verify = driver.find_element(By.XPATH, "//h6[@class='oxd-text oxd-text--h6 oxd-topbar-header-breadcrumb-module']").text
    if success_verify == 'PIM':
        print("User is logged in successfully")
    else:
        print("Login failed, Try again")


def test_login_02():
    #Negative scenario
    service = Service(executable_path=GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service)
    url = "https://opensource-demo.orangehrmlive.com/"
    driver.get(url)
    time.sleep(3)
    WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//input[@placeholder='Username']")))
    driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
    driver.find_element(By.XPATH, "// input[@placeholder='Password']").send_keys("Invalid password")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(3)
    # Login failed verification
    fail_verify = driver.find_element(By.XPATH, "//div[@class='oxd-alert-content oxd-alert-content--error']").text
    if fail_verify == 'Invalid credentials':
        print("A valid error message for invalid credentials is displayed")
    else:
        print("Negative login testcase failed")


def test_pim_01():
    # to create a account for user with login account
    # USER DETAILS
    # name ="mathew conway", ID =1231, job ="software engineer", role="professional", sub-unit="Adminstration", location="HQ - CA, USA, jobtype="freelance"
    service = Service(executable_path=GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service)
    url = "https://opensource-demo.orangehrmlive.com/"
    driver.get(url)
    # Login
    WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//input[@placeholder='Username']")))
    driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
    driver.find_element(By.XPATH, "// input[@placeholder='Password']").send_keys("admin123")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(3)
    # To Add New User
    driver.find_element(By.LINK_TEXT, "PIM").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "//button[@class='oxd-button oxd-button--medium oxd-button--secondary']").click()
    time.sleep(3)
    # First name and Last name
    driver.find_element(By.XPATH, "//input[@name='firstName']").send_keys("mathew")
    driver.find_element(By.XPATH, "//input[@name='lastName']").send_keys("conway")
    # Id
    driver.find_element(By.XPATH, "//div[@class='oxd-input-group oxd-input-field-bottom-space']//input[@class='oxd-input oxd-input--active']").click()
    driver.find_element(By.XPATH, "//input[@class='oxd-input oxd-input--focus']").send_keys(Keys.BACK_SPACE)
    driver.find_element(By.XPATH, "//input[@class='oxd-input oxd-input--focus']").send_keys(Keys.BACK_SPACE)
    driver.find_element(By.XPATH, "//input[@class='oxd-input oxd-input--focus']").send_keys(Keys.BACK_SPACE)
    driver.find_element(By.XPATH, "//input[@class='oxd-input oxd-input--focus']").send_keys(Keys.BACK_SPACE)
    driver.find_element(By.XPATH, "//input[@class='oxd-input oxd-input--focus']").send_keys(1231)
    time.sleep(3)
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(10)
    # to add job details
    driver.find_element(By.LINK_TEXT, "Job").click()
    time.sleep(3)
    # to select software engineer
    driver.find_element(By.XPATH, "//form/div[1]/div/div[2]/div/div[2]/div/div").click()
    driver.find_element(By.XPATH, ("//*[contains(text(), 'Software Engineer')]")).click()
    # to select professional
    driver.find_element(By.XPATH, "//form/div[1]/div/div[4]/div/div[2]/div/div/div[1]").click()
    driver.find_element(By.XPATH, "//*[contains(text(), 'Professionals')]").click()
    # to select sub unit
    driver.find_element(By.XPATH, "//form/div[1]/div/div[5]/div/div[2]/div/div").click()
    driver.find_element(By.XPATH, "//*[contains(text(), 'Administration')]").click()
    # to select location
    driver.find_element(By.XPATH, "//form/div[1]/div/div[6]/div/div[2]/div/div/div[1]").click()
    driver.find_element(By.XPATH, "//*[contains(text(), 'HQ - CA, USA')]").click()
    # to select job type
    driver.find_element(By.XPATH, "//form/div[1]/div/div[7]/div/div[2]/div/div/div[1]").click()
    driver.find_element(By.XPATH, "//*[contains(text(), 'Freelance')]").click()
    time.sleep(3)
    # to save
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(5)
    # to verify if new employee is created
    driver.find_element(By.LINK_TEXT, "PIM").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "//form/div[1]/div/div[2]/div/div[2]/input").send_keys(1231)  #emp id
    time.sleep(3)
    driver.find_element(By.XPATH, "//button[@type='submit']").click() # to click search
    time.sleep(5)
    employee_details = driver.find_element(By.XPATH, "//div[@class='orangehrm-container']") # to check employee details
    driver.execute_script("arguments[0].scrollIntoView()", employee_details)
    time.sleep(3)
    first_name = driver.find_element(By.XPATH, "//div[@class='oxd-table-card']/div/div[3]").text
    last_name = driver.find_element(By.XPATH, "//div[@class='oxd-table-card']/div/div[4]").text
    if first_name =="mathew" and last_name =="conway":
        print("New employee is successfully created")
    else:
        print("New employee addition failed")


def test_pim_02():
    # to modify user details with login account
    # USER DETAILS
    # name ="mathew conway", ID =1231, job ="software engineer", role="professional", sub-unit="Adminstratio", location="HQ - CA, USA, jobtype="freelance"
    # modifiying details jobtype = "Freelance" to "Full-Time Contract" and addition of salary details
    service = Service(executable_path=GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service)
    url = "https://opensource-demo.orangehrmlive.com/"
    driver.get(url)
    # Login
    WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//input[@placeholder='Username']")))
    driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
    driver.find_element(By.XPATH, "// input[@placeholder='Password']").send_keys("admin123")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(5)
    # PIM
    driver.find_element(By.LINK_TEXT, "PIM").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "//form/div[1]/div/div[2]/div/div[2]/input").send_keys(1231)  # emp id
    driver.find_element(By.XPATH, "//button[@type='submit']").click()  # to click search
    time.sleep(5)
    employee_details = driver.find_element(By.XPATH, "//div[@class='orangehrm-container']")  # to check employee details
    driver.execute_script("arguments[0].scrollIntoView()", employee_details)
    time.sleep(3)
    first_name = driver.find_element(By.XPATH, "//div[@class='oxd-table-card']/div/div[3]").text
    last_name = driver.find_element(By.XPATH, "//div[@class='oxd-table-card']/div/div[4]").text
    if first_name == "mathew" and last_name == "conway":
        driver.find_element(By.XPATH, "//div[@class='oxd-table-cell-actions']/button[2]").click()
        # to add job details
        driver.find_element(By.LINK_TEXT, "Job").click()
        time.sleep(3)
        # to select job type
        driver.find_element(By.XPATH, "//form/div[1]/div/div[7]/div/div[2]/div/div/div[1]").click()
        driver.find_element(By.XPATH, "//*[contains(text(), 'Full-Time Contract')]").click()
        # to save
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(5)
        # to add salary details
        driver.find_element(By.LINK_TEXT, "Salary").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "//div[@class='orangehrm-edit-employee-content']/div[1]/div/button").click()
        time.sleep(2)
        #salary component (Basic salary)
        driver.find_element(By.XPATH, "//form/div[1]/div/div[1]/div/div[2]/input").send_keys("Basic salary")
        #pay grade (Grade 3)
        driver.find_element(By.XPATH, "//form/div[1]/div/div[2]/div/div[2]/div").click()
        driver.find_element(By.XPATH, "//form/div[1]/div/div[2]/div/div[2]/div/div[2]/div[4]").click()
        time.sleep(3)
        #pay frequency (monthly)
        driver.find_element(By.XPATH, "//form/div[1]/div/div[3]/div/div[2]/div").click()
        driver.find_element(By.XPATH, "//form/div[1]/div/div[3]/div/div[2]/div/div[2]/div[4]").click()
        #currency
        driver.find_element(By.XPATH, "//form/div[1]/div/div[4]/div/div[2]/div/div").click()
        driver.find_element(By.XPATH, "//*[text()= 'United States Dollar']").click()
        #amount
        driver.find_element(By.XPATH, "//form/div[1]/div/div[5]/div/div[2]/input").send_keys(32000)
        #comment
        driver.find_element(By.XPATH, "//form/div[2]/div/div/div/div[2]/textarea").send_keys("Direct deposit not available, contact admin")
        #save
        driver.find_element(By.XPATH, "//form/div[4]/button[2]").click()
        time.sleep(5)
        # to verify if employee details is modified
        driver.find_element(By.LINK_TEXT, "PIM").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "//form/div[1]/div/div[2]/div/div[2]/input").send_keys(1231)  # emp id
        time.sleep(3)
        driver.find_element(By.XPATH, "//button[@type='submit']").click()  # to click search
        time.sleep(5)
        employee_details = driver.find_element(By.XPATH, "//div[@class='orangehrm-container']")  # to check employee details
        driver.execute_script("arguments[0].scrollIntoView()", employee_details)
        time.sleep(3)
        first_name = driver.find_element(By.XPATH, "//div[@class='oxd-table-card']/div/div[3]").text
        last_name = driver.find_element(By.XPATH, "//div[@class='oxd-table-card']/div/div[4]").text
        employment_status = driver.find_element(By.XPATH, "//div[@class='oxd-table-card']/div/div[6]").text
        if first_name == "mathew" and last_name == "conway" and employment_status == "Full-Time Contract":
            print("Employee details modified and salary details added")
        else:
            print("Employee details modification failed")
    else:
        print("Employee information doesn't match, Please verify")


def test_pim_03():
    # to delete a employee record (emp id = 1231, name = "mathew conway")
    service = Service(executable_path=GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service)
    url = "https://opensource-demo.orangehrmlive.com/"
    driver.get(url)
    # Login
    WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//input[@placeholder='Username']")))
    driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
    driver.find_element(By.XPATH, "// input[@placeholder='Password']").send_keys("admin123")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(5)
    # PIM
    driver.find_element(By.LINK_TEXT, "PIM").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "//form/div[1]/div/div[2]/div/div[2]/input").send_keys(1231)  # emp id
    driver.find_element(By.XPATH, "//button[@type='submit']").click()  # to click search
    time.sleep(5)
    employee_details = driver.find_element(By.XPATH, "//div[@class='orangehrm-container']")  # to check employee details
    driver.execute_script("arguments[0].scrollIntoView()", employee_details)
    time.sleep(3)
    first_name = driver.find_element(By.XPATH, "//div[@class='oxd-table-card']/div/div[3]").text
    last_name = driver.find_element(By.XPATH, "//div[@class='oxd-table-card']/div/div[4]").text
    if first_name == "mathew" and last_name == "conway":
        driver.find_element(By.XPATH, "//div[@class='oxd-table-cell-actions']/button[1]").click()
        driver.find_element(By.XPATH, "//div[@role ='document']/div[3]/button[2]").click()
        time.sleep(5)
    else:
        print("Employee details doesn't match")
    # to verify if employee details deleted
    driver.find_element(By.LINK_TEXT, "PIM").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "//form/div[1]/div/div[2]/div/div[2]/input").send_keys(1231)  # emp id
    driver.find_element(By.XPATH, "//button[@type='submit']").click()  # to click search
    time.sleep(5)
    total_record = driver.find_element(By.XPATH, "//div[@class='orangehrm-background-container']/div[2]/div[2]/div/span").text
    if total_record == "No Records Found":
        print("Employee details deleted successfully")
    else:
        print("Employee details deletion failed")
        



