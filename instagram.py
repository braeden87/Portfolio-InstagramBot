#Imports
from os import close
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import constants as const
import time
import random


class Instagram:
        def __init__(self):
                self.driver = webdriver.Chrome(ChromeDriverManager().install())
                super(Instagram, self).__init__()
                self.driver.implicitly_wait(15)
        def __enter__(self):
                print ('Enter')
                return self
        def __exit__(self, exc_type, exc_value, exc_traceback):
                time.sleep(30)
                print('Exit')
        
        #Opens the Webpage
        def open_instagram(self):
                self.driver.get(const.BASE_URL)
        #Login 
        def login(self, username, password):
                #Username
                username_element = self.driver.find_element_by_css_selector(
                        'input[name="username"]'
                )
                username_element.clear()
                username_element.send_keys(username)
                #Password
                password_element = self.driver.find_element_by_css_selector(
                        'input[aria-label="Password"]'
                )
                password_element.clear()
                password_element.send_keys(password)
                #Button
                submit_button_element = self.driver.find_element_by_css_selector(
                        'button[type="submit"]'
                )
                submit_button_element.click()

                #PopUp
                self.save_info_popup()
                #Notifications
                self.notification_enabler()
        #Go to search area
        def search_tags(self, tag):
                discover_window_element = self.driver.find_element_by_css_selector(
                        'a[href="/explore/"]'
                )
                discover_window_element.click()
                #Notifications
                self.notification_enabler()
                #Search For First Tag
                search_element = self.driver.find_element_by_css_selector(
                        'input[class="XTCLo x3qfX "]'
                )
                search_element.clear()
                search_element.send_keys(tag)
                search_element_select = self.driver.find_element_by_css_selector(
                        'a[class="-qQT3"]'
                )
                search_element_select.click()
        def open_posts(self, count):
                #post_element = self.driver.find_element_by_css_selector(
                #        'a[href="/p/CVQHItWlU6G/"]'
                #)
                time.sleep(2)
                post_elements = self.driver.find_elements_by_css_selector(
                        'a[class="H-KQe"]'
                )
                for _ in range(count):
                        for post in post_elements:
                                time.sleep(2)
                                post.click()
                                self.like_post()
                                self.user_post()
                                self.comment_post()
                                time.sleep(2)
                                self.close_post()

        #Nested Functions
        def notification_enabler(self):
                try:
                        notification_element = self.driver.find_element_by_css_selector(
                                'button[class="aOOlW  bIiDR  "]'
                        )
                        notification_element.click()
                except:
                        print('Notification Element not present')
        def save_info_popup(self):
                try:
                        save_info_element = self.driver.find_element_by_css_selector(
                                'button[class="sqdOP  L3NKy   y3zKF     "]'
                        )
                        save_info_element.click()
                except:
                        print('Save Info Element Not Present')
        def like_post(self): #Need to Make This recognize when a post is already liked
                like_element = self.driver.find_element_by_css_selector(
                        'span[class="fr66n"]'
                )
                like_element.click()
                print('1 Post Liked')
        def comment_post(self):
                user = self.user_post()
                comments = [f'Nice shot! @{user}',
                        f'I love your profile! @{user}',
                        'Your feed is an inspiration :thumbsup:',
                        'Just incredible :open_mouth:',
                        f'What camera did you use @{user}?',
                        f'Love your posts @{user}',
                        f'Looks awesome @{user}',
                       f'Getting inspired by you @{user}',
                        ':raised_hands: Yes!',
                        f'I can feel your passion @{user} :muscle:']
                comment = comments[random.randint(0, len(comments))]
                
                comment_button_element = self.driver.find_element_by_css_selector(
                        'span[class="_15y0l"]'
                )
                comment_button_element.click()
                time.sleep(2)
                comment_element = self.driver.find_element_by_css_selector(
                        'textarea[data-testid="post-comment-text-area"]'
                )
                comment_element.clear()
                comment_element.send_keys(comment)
                print(comment)
                post_button_element = self.driver.find_element_by_css_selector(
                        'button[data-testid="post-comment-input-button"]'
                )
                post_button_element.click()
        def user_post(self):
                user_element = self.driver.find_element_by_css_selector(
                      'a[class="sqdOP yWX7d     _8A5w5   ZIAjV "]'  
                ).text
                return user_element
        def close_post(self):
                close_element = self.driver.find_element_by_css_selector(
                        'div[class="            qF0y9          Igw0E     IwRSH      eGOV_         _4EzTm                                                                                  BI4qX            qJPeX            fm1AK   TxciK yiMZG"]'
                )
                close_element.click()