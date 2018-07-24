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

    edit_company_information_loc = (By.XPATH, '//*[@id="app"]/div/div[1]/div[4]/div/div/div[3]/div/button[1]')

    close_company_information_loc = (By.XPATH, '//*[@id="app"]/div/div[1]/div[4]/div/div/div[1]/button/i')

    def edit_company_information(self):
        self.find_element(*self.company_setting_loc).click()
        self.find_element(*self.edit_company_information_loc).click()

    change_company_logo_loc = (By.XPATH, '//*[@id="app"]/div/div[1]/div[4]/div/div/div[2]/form[2]/div[1]/div/div/div[1]')

    change_company_name_loc = (By.XPATH, '//*[@id="app"]/div/div[1]/div[4]/div/div/div[2]/form[2]/div[3]/div/div/input')

    change_contact_address_loc = (By.XPATH, '//*[@id="provinLink"]')

    pick_province_Beijing_loc = (By.XPATH, '//*[@id="_citys0"]/a[1]')

    pick_city_Beijing_loc = (By.XPATH, '//*[@id="_citys1"]/a')

    change_detail_address_loc = (By.XPATH, '//*[@id="app"]/div/div[1]/div[4]/div/div/div[2]/form[2]/div[7]/div/div/input')

    change_email_address_loc = (By.XPATH, '//*[@id="app"]/div/div[1]/div[4]/div/div/div[2]/form[2]/div[9]/div/div/input')

    change_english_name_loc = (By.XPATH, '//*[@id="app"]/div/div[1]/div[4]/div/div/div[2]/form[2]/div[4]/div/div/input')

    change_company_manager_name_loc = (By.XPATH, '//*[@id="app"]/div/div[1]/div[4]/div/div/div[2]/form[2]/div[6]/div/div/input')

    change_mobilephone_num_loc = (By.XPATH, '//*[@id="app"]/div/div[1]/div[4]/div/div/div[2]/form[2]/div[8]/div/div/input')

    change_telephone_num_loc = (By.XPATH, '//*[@id="app"]/div/div[1]/div[4]/div/div/div[2]/form[2]/div[10]/div/div/input')

    password_verification_loc = (By.XPATH, '//*[@id="app"]/div/div[1]/div[4]/div/div/div[2]/form[2]/div[11]/div/div/input')

    save_information_loc = (By.XPATH, '//*[@id="app"]/div/div[1]/div[4]/div/div/div[3]/div/button[2]')

    cancel_information_loc = (By.XPATH, '//*[@id="app"]/div/div[1]/div[4]/div/div/div[3]/div/button[3]')

    def edit_change_company_name(self, companyname):
        self.edit_company_information()
        self.find_element(*self.change_company_name_loc).clear()
        self.find_element(*self.change_company_name_loc).send_keys(companyname)
        self.find_element(*self.password_verification_loc).click()
        self.find_element(*self.password_verification_loc).send_keys('111111')
        self.find_element(*self.save_information_loc).click()
        sleep(2)

    def edit_change_contact_address(self):
        self.edit_company_information()
        #self.find_element(*self.change_contact_address_loc).clear()
        #self.find_element(*self.change_contact_address_loc).send_keys(contactaddress)
        self.find_element(*self.change_contact_address_loc).click()
        self.find_element(*self.pick_province_Beijing_loc).click()
        self.find_element(*self.pick_city_Beijing_loc).click()
        self.find_element(*self.password_verification_loc).send_keys('111111')
        self.find_element(*self.save_information_loc).click()
        sleep(2)

    def edit_change_detail_address(self, detailaddress):
        self.edit_company_information()
        self.find_element(*self.change_detail_address_loc).clear()
        self.find_element(*self.change_detail_address_loc).send_keys(detailaddress)
        self.find_element(*self.password_verification_loc).send_keys('111111')
        self.find_element(*self.save_information_loc).click()
        sleep(2)

    def edit_change_telephone_num(self, telephonenum):
        self.edit_company_information()
        self.find_element(*self.change_telephone_num_loc).clear()
        self.find_element(*self.change_telephone_num_loc).send_keys(telephonenum)
        self.find_element(*self.password_verification_loc).send_keys('111111')
        self.find_element(*self.save_information_loc).click()
        sleep(2)

    def edit_change_english_name(self, englishname):
        self.edit_company_information()
        self.find_element(*self.change_english_name_loc).clear()
        self.find_element(*self.change_english_name_loc).send_keys(englishname)
        self.find_element(*self.password_verification_loc).send_keys('111111')
        self.find_element(*self.save_information_loc).click()
        sleep(2)

    def edit_change_company_manager_name(self, companymanagername):
        self.edit_company_information()
        self.find_element(*self.change_company_manager_name_loc).clear()
        self.find_element(*self.change_company_manager_name_loc).send_keys(companymanagername)
        self.find_element(*self.password_verification_loc).send_keys('111111')
        self.find_element(*self.save_information_loc).click()
        sleep(2)

    def edit_change_mobilephone_num(self, mobilephonenum):
        self.edit_company_information()
        self.find_element(*self.change_mobilephone_num_loc).clear()
        self.find_element(*self.change_mobilephone_num_loc).send_keys(mobilephonenum)
        self.find_element(*self.password_verification_loc).send_keys('111111')
        self.find_element(*self.save_information_loc).click()
        sleep(1)

    def edit_change_email_address(self, emailaddress):
        self.edit_company_information()
        self.find_element(*self.change_email_address_loc).clear()
        self.find_element(*self.change_email_address_loc).send_keys(emailaddress)
        self.find_element(*self.password_verification_loc).send_keys('111111')
        self.find_element(*self.save_information_loc).click()
        sleep(1)

    def input_change_password_verification(self, password):
        self.edit_company_information()
        self.find_element(*self.password_verification_loc).send_keys(password)
        self.find_element(*self.save_information_loc).click()
        sleep(1)

    def empty_edit_change_company_name(self, companyname):
        self.edit_company_information()
        self.find_element(*self.change_company_name_loc).clear()
        self.find_element(*self.change_company_name_loc).send_keys(companyname)
        self.find_element(*self.change_company_name_loc).send_keys(Keys.BACK_SPACE)
        self.find_element(*self.password_verification_loc).click()
        self.find_element(*self.password_verification_loc).send_keys('111111')
        self.find_element(*self.save_information_loc).click()
        sleep(2)

    def empty_edit_change_detail_address(self, detailaddress):
        self.edit_company_information()
        self.find_element(*self.change_detail_address_loc).clear()
        self.find_element(*self.change_detail_address_loc).send_keys(detailaddress)
        self.find_element(*self.change_detail_address_loc).send_keys(Keys.BACK_SPACE)
        self.find_element(*self.password_verification_loc).send_keys('111111')
        self.find_element(*self.save_information_loc).click()
        sleep(2)

    def empty_edit_change_telephone_num(self, telephonenum):
        self.edit_company_information()
        self.find_element(*self.change_telephone_num_loc).clear()
        self.find_element(*self.change_telephone_num_loc).send_keys(telephonenum)
        self.find_element(*self.change_telephone_num_loc).send_keys(Keys.BACK_SPACE)
        self.find_element(*self.password_verification_loc).send_keys('111111')
        self.find_element(*self.save_information_loc).click()
        sleep(2)

    def empty_edit_change_english_name(self, englishname):
        self.edit_company_information()
        self.find_element(*self.change_english_name_loc).clear()
        self.find_element(*self.change_english_name_loc).send_keys(englishname)
        self.find_element(*self.change_english_name_loc).send_keys(Keys.BACK_SPACE)
        self.find_element(*self.password_verification_loc).send_keys('111111')
        self.find_element(*self.save_information_loc).click()
        sleep(2)

    def empty_edit_change_company_manager_name(self, companymanagername):
        self.edit_company_information()
        self.find_element(*self.change_company_manager_name_loc).clear()
        self.find_element(*self.change_company_manager_name_loc).send_keys(companymanagername)
        self.find_element(*self.change_company_manager_name_loc).send_keys(Keys.BACK_SPACE)
        self.find_element(*self.password_verification_loc).send_keys('111111')
        self.find_element(*self.save_information_loc).click()
        sleep(2)

    def empty_edit_change_mobilephone_num(self, mobilephonenum):
        self.edit_company_information()
        self.find_element(*self.change_mobilephone_num_loc).clear()
        self.find_element(*self.change_mobilephone_num_loc).send_keys(mobilephonenum)
        self.find_element(*self.change_mobilephone_num_loc).send_keys(Keys.BACK_SPACE)
        self.find_element(*self.password_verification_loc).send_keys('111111')
        self.find_element(*self.save_information_loc).click()
        sleep(1)

    def empty_edit_change_email_address(self, emailaddress):
        self.edit_company_information()
        self.find_element(*self.change_email_address_loc).clear()
        self.find_element(*self.change_email_address_loc).send_keys(emailaddress)
        self.find_element(*self.change_email_address_loc).send_keys(Keys.BACK_SPACE)
        self.find_element(*self.password_verification_loc).send_keys('111111')
        self.find_element(*self.save_information_loc).click()
        sleep(1)

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
        for i in range(2):
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

    input_current_password_loc = (By.XPATH, '//*[@id="app"]/div/div[1]/div[2]/div/div[2]/form/div[1]/div/div/input')

    input_new_password_loc = (By.XPATH, '//*[@id="app"]/div/div[1]/div[2]/div/div[2]/form/div[2]/div/div/input')

    input_new_password_again_loc = (By.XPATH, '//*[@id="app"]/div/div[1]/div[2]/div/div[2]/form/div[3]/div/div/input')

    enter_change_person_password_loc = (By.XPATH, '//*[@id="app"]/div/div[1]/div[2]/div/div[3]/span/button[1]')

    cancel_change_person_password_loc = (By.XPATH, '//*[@id="app"]/div/div[1]/div[2]/div/div[3]/span/button[2]')

    def change_manager_password(self):
        self.find_element(*person_center_loc).click()
        self.find_element(*change_manager_password_loc).click()

    def input_current_password(self, currentpassword):
        self.find_element(*input_current_password_loc).send_keys(currentpassword)

    def input_new_password(self, newpassword):
        self.find_element(*input_new_password_loc).send_keys(newpassword)

    def input_new_password_again(self, newpasswordagain):
        self.find_element(*input_new_password_again_loc).send_keys(newpasswordagain)

    def enter_change_person_password(self):
        self.find_element(*enter_change_person_password_loc).click()

    def cancel_change_person_password(self):
        self.find_element(*cancel_change_person_password_loc).click()

    # Verification
    error_current_password_hint_loc = (By.XPATH, '//*[@id="app"]/div/div[1]/div[2]/div/div[2]/form/div[1]/div/div[2]')

    error_new_password_hint_loc = (By.XPATH, '//*[@id="app"]/div/div[1]/div[2]/div/div[2]/form/div[2]/div/div[2]')

    error_new_password_again_hint_loc = (By.XPATH, '//*[@id="app"]/div/div[1]/div[2]/div/div[2]/form/div[3]/div/div[2]')

    def error_current_password_hint(self):
        return self.find_element(*error_current_password_hint).text

    def error_new_password_hint(self):
        return self.find_element(*error_new_password_hint_loc).text

    def error_new_password_again_hint(self):
        return self.find_element(*error_new_password_again_hint).text
