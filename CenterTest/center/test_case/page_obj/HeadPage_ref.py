from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
# import sys
# sys.path.append('..')
from Base import Page
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class CompanyInformation(Page):
    '''企业设置'''

    url = '/'

    # Action
    company_setting_loc = (By.XPATH, '//*[@id="app"]/div/div[1]/div[1]/div[2]/div[2]/span')

    def company_setting(self):
        self.find_element(*self.company_setting_loc).click()

    edit_company_information_loc = (By.XPATH, '//*[@id="app"]/div/div[1]/div[4]/div/div/div[3]/div/button[1]')

    def edit_company_information(self):
        self.find_element(*self.edit_company_information_loc).click()

    close_company_information_loc = (By.XPATH, '//*[@id="app"]/div/div[1]/div[4]/div/div/div[1]/button/i')

    def close_company_information(self):
        self.find_element(*self.close_company_information_loc).click()

    change_company_logo_loc = (By.XPATH, '//*[@id="app"]/div/div[1]/div[4]/div/div/div[2]/form[2]/div[1]/div/div/div[1]')

    def change_company_logo(self):
        self.find_element(*self.change_company_logo_loc).click()

    change_company_name_loc = (By.XPATH, '//*[@id="app"]/div/div[1]/div[4]/div/div/div[2]/form[2]/div[3]/div/div/input')

    def change_company_name(self, company_name):
        self.find_element(*self.change_company_name_loc).send_keys(company_name)

    change_contact_address_loc = (By.XPATH, '//*[@id="provinLink"]')

    def change_contact_address(self):
        self.find_element(*self.change_contact_address_loc).click()

    pick_province_Beijing_loc = (By.XPATH, '//*[@id="_citys0"]/a[1]')

    def pick_province_Beijing(self):
        self.find_element(*self.pick_province_Beijing_loc).click()

    pick_city_Beijing_loc = (By.XPATH, '//*[@id="_citys1"]/a')
    def pick_city_Beijing(self):
        self.find_element(*self.pick_city_Beijing_loc).click()

    change_detail_address_loc = (By.XPATH, '//*[@id="app"]/div/div[1]/div[4]/div/div/div[2]/form[2]/div[7]/div/div/input')

    def change_detail_address(self, detail_address):
        self.find_element(*self.change_detail_address_loc).send_keys(detail_address)

    change_email_address_loc = (By.XPATH, '//*[@id="app"]/div/div[1]/div[4]/div/div/div[2]/form[2]/div[9]/div/div/input')

    def change_email_address(self, email_address):
        self.find_element(*self.change_email_address_loc).send_keys(email_address)

    change_english_name_loc = (By.XPATH, '//*[@id="app"]/div/div[1]/div[4]/div/div/div[2]/form[2]/div[4]/div/div/input')

    def change_english_name(self, english_name):
        self.find_element(*self.change_english_name_loc).send_keys(english_name)

    change_company_manager_name_loc = (By.XPATH, '//*[@id="app"]/div/div[1]/div[4]/div/div/div[2]/form[2]/div[6]/div/div/input')

    def change_company_manager_name(self, company_manager_name):
        self.find_element(*self.change_company_manager_name_loc).send_keys(company_manager_name)

    change_mobilephone_num_loc = (By.XPATH, '//*[@id="app"]/div/div[1]/div[4]/div/div/div[2]/form[2]/div[8]/div/div/input')

    def change_mobilephone_num(self, mobilephone_num):
        self.find_element(*self.change_mobilephone_num_loc).send_keys(mobilephone_num)

    change_telephone_num_loc = (By.XPATH, '//*[@id="app"]/div/div[1]/div[4]/div/div/div[2]/form[2]/div[10]/div/div/input')

    def change_telephone_num(self, telephone_num):
        self.find_element(*self.change_telephone_num_loc).send_keys(telephone_num)

    password_verification_loc = (By.XPATH, '//*[@id="app"]/div/div[1]/div[4]/div/div/div[2]/form[2]/div[11]/div/div/input')

    def password_verification(self, password_verification):
        self.find_element(*self.password_verification_loc).send_keys(password_verification)

    save_information_loc = (By.XPATH, '//*[@id="app"]/div/div[1]/div[4]/div/div/div[3]/div/button[2]')

    def save_information(self):
        self.find_element(*self.save_information_loc).click()

    cancel_information_loc = (By.XPATH, '//*[@id="app"]/div/div[1]/div[4]/div/div/div[3]/div/button[3]')

    def cancel_information(self):
        self.find_element(*self.cancel_information_loc).click()


    # Verification
    company_logo_hint_loc = (By.XPATH, '//*[@id="app"]/div/div[1]/div[4]/div/div/div[2]/form[1]/div[1]/div/div')

    company_name_hint_loc = (By.XPATH, '//*[@id="app"]/div/div[1]/div[4]/div/div/div[2]/form[1]/div[3]/div/div')

    contact_address_hint_loc = (By.XPATH, '//*[@id="provinLinkAddress"]')

    detail_address_hint_loc = (By.XPATH, '//*[@id="app"]/div/div[1]/div[4]/div/div/div[2]/form[1]/div[7]/div/div')

    email_address_hint_loc = (By.XPATH, '//*[@id="app"]/div/div[1]/div[4]/div/div/div[2]/form[1]/div[9]/div/div')

    english_name_hint_loc = (By.XPATH, '//*[@id="app"]/div/div[1]/div[4]/div/div/div[2]/form[1]/div[4]/div/div')

    company_manager_name_hint_loc = (By.XPATH, '//*[@id="app"]/div/div[1]/div[4]/div/div/div[2]/form[1]/div[6]/div/div')

    mobilephone_num_hint_loc = (By.XPATH, '//*[@id="app"]/div/div[1]/div[4]/div/div/div[2]/form[1]/div[8]/div/div')

    telephone_num_hint_loc = (By.XPATH, '//*[@id="app"]/div/div[1]/div[4]/div/div/div[2]/form[1]/div[10]/div/div')

    floating_prompt_hint_loc = (By.XPATH, '/html/body/div[5]/div/p')

    def edit_success_hint(self):
        for i in range(3):
            sleep(0.1)
            a1 = self.find_element(*self.floating_prompt_hint_loc).text
        return a1

    def company_name_hint(self):
        return self.find_element(*self.company_name_hint_loc).text

    def contact_address_hint(self):
        return self.find_element(*self.contact_address_hint_loc).text

    def detail_address_hint(self):
        return self.find_element(*self.detail_address_hint_loc).text

    def telephone_num_hint(self):
        return self.find_element(*self.telephone_num_hint_loc).text

    def english_name_hint(self):
        return self.find_element(*self.english_name_hint_loc).text

    def company_manager_name_hint(self):
        return self.find_element(*self.company_manager_name_hint_loc).text

    def mobilephone_num_hint(self):
        return self.find_element(*self.mobilephone_num_hint_loc).text

    def email_address_hint(self):
        return self.find_element(*self.email_address_hint_loc).text

    empty_company_name_hint_loc = (By.XPATH, '//*[@id="app"]/div/div[1]/div[4]/div/div/div[2]/form[2]/div[3]/div/div[2]')

    empty_detail_address_hint_loc = (By.XPATH, '//*[@id="app"]/div/div[1]/div[4]/div/div/div[2]/form[2]/div[7]/div/div[2]')

    empty_email_address_hint_loc = (By.XPATH, '//*[@id="app"]/div/div[1]/div[4]/div/div/div[2]/form[2]/div[9]/div/div[2]')

    empty_english_name_hint_loc = (By.XPATH, '//*[@id="app"]/div/div[1]/div[4]/div/div/div[2]/form[2]/div[4]/div/div[2]')

    empty_company_manager_name_hint_loc = (By.XPATH, '//*[@id="app"]/div/div[1]/div[4]/div/div/div[2]/form[2]/div[6]/div/div[2]')

    empty_mobilephone_num_hint_loc = (By.XPATH, '//*[@id="app"]/div/div[1]/div[4]/div/div/div[2]/form[2]/div[8]/div/div[2]')

    empty_telephone_num_hint_loc = (By.XPATH, '//*[@id="app"]/div/div[1]/div[4]/div/div/div[2]/form[2]/div[10]/div/div[2]')
    
    empty_password_verification_hint_loc = (By.XPATH, '//*[@id="app"]/div/div[1]/div[4]/div/div/div[2]/form[2]/div[11]/div/div[2]')

    def empty_company_name_hint(self):
        return self.find_element(*self.empty_company_name_hint_loc).text

    def empty_contact_address_hint(self):
        return self.find_element(*self.empty_contact_address_hint_loc).text

    def empty_detail_address_hint(self):
        return self.find_element(*self.empty_detail_address_hint_loc).text

    def empty_telephone_num_hint(self):
        return self.find_element(*self.empty_telephone_num_hint_loc).text

    def empty_english_name_hint(self):
        return self.find_element(*self.empty_english_name_hint_loc).text

    def empty_company_manager_name_hint(self):
        return self.find_element(*self.empty_company_manager_name_hint_loc).text

    def empty_mobilephone_num_hint(self):
        return self.find_element(*self.empty_mobilephone_num_hint_loc).text

    def empty_email_address_hint(self):
        return self.find_element(*self.empty_email_address_hint_loc).text

    def empty_password_verification_hint(self):
        return self.find_element(*self.empty_password_verification_hint_loc).text

    def wrong_password_verification_hint(self):
        for i in range(3):
            a1 = self.find_element(*self.floating_prompt_hint_loc).text
        # print(a1)
        return a1

    def only_space_verification_hint(self):
        for i in range(3):
            a1 = self.find_element(*self.floating_prompt_hint_loc).text
        # print(a1)
        return a1


class IssueCenter(Page):

    url = '/'

    # Action
    issue_center_loc = (By.XPATH, '//*[@id="app"]/div/div[1]/div[1]/div[2]/div[1]')
    pass


class PersonCenter(Page):
    '''个人中心'''

    url = '/'

    # Action
    person_center_loc = (By.XPATH, '//*[@id="app"]/div/div[1]/div[1]/div[2]/div[3]/div/div')

    change_manager_password_loc = (By.XPATH, '/html/body/ul/li[1]')

    change_person_picture_loc = (By.XPATH, '/html/body/ul/li[2]')

    bind_passport_loc = (By.XPATH, '/html/body/ul/li[3]')

    safe_quit_loc = (By.XPATH, '/html/body/ul/li[4]')

    def person_center_loc(self):
        self.find_element(*self.person_center_loc).click()

    def change_manager_password(self):
        self.find_element(*self.change_manager_password_loc).click()

    def change_person_picture(self):
        self.find_element(*self.change_person_picture_loc).click()

    def bind_passport(self):
        self.find_element(*self.bind_passport_loc).click()

    def safe_quit(self):
        self.find_element(*self.safe_quit_loc).click()

#***************************************************************************************

    input_current_password_loc = (By.XPATH, '//*[@id="app"]/div/div[1]/div[2]/div/div[2]/form/div[1]/div/div/input')

    input_new_password_loc = (By.XPATH, '//*[@id="app"]/div/div[1]/div[2]/div/div[2]/form/div[2]/div/div/input')

    input_new_password_again_loc = (By.XPATH, '//*[@id="app"]/div/div[1]/div[2]/div/div[2]/form/div[3]/div/div/input')

    enter_change_person_password_loc = (By.XPATH, '//*[@id="app"]/div/div[1]/div[2]/div/div[3]/span/button[1]')

    cancel_change_person_password_loc = (By.XPATH, '//*[@id="app"]/div/div[1]/div[2]/div/div[3]/span/button[2]')

    def input_current_password(self, currentpassword):
        self.find_element(*self.input_current_password_loc).send_keys(currentpassword)

    def input_new_password(self, newpassword):
        self.find_element(*self.input_new_password_loc).send_keys(newpassword)

    def input_new_password_again(self, newpasswordagain):
        self.find_element(*self.input_new_password_again_loc).send_keys(newpasswordagain)

    def enter_change_person_password(self):
        self.find_element(*self.enter_change_person_password_loc).click()

    def cancel_change_person_password(self):
        self.find_element(*self.cancel_change_person_password_loc).click()

    # Verification
    error_current_password_hint_loc = (By.XPATH, '//*[@id="app"]/div/div[1]/div[2]/div/div[2]/form/div[1]/div/div[2]')

    error_new_password_hint_loc = (By.XPATH, '//*[@id="app"]/div/div[1]/div[2]/div/div[2]/form/div[2]/div/div[2]')

    error_new_password_again_hint_loc = (By.XPATH, '//*[@id="app"]/div/div[1]/div[2]/div/div[2]/form/div[3]/div/div[2]')

    def error_current_password_hint(self):
        return self.find_element(*self.error_current_password_hint).text

    def error_new_password_hint(self):
        return self.find_element(*self.error_new_password_hint_loc).text

    def error_new_password_again_hint(self):
        return self.find_element(*self.error_new_password_again_hint).text
