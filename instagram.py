#Imports
from os import close
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import constants as const
import time
import random
from datetime import datetime


class Instagram:
######################################################################
#Constructor
######################################################################
        def __init__(self):
                self.driver = webdriver.Chrome(ChromeDriverManager().install())
                super(Instagram, self).__init__()
                self.driver.implicitly_wait(15)
        def __enter__(self):
                print ('Enter')
                return self
        def __exit__(self, exc_type, exc_value, exc_traceback):
                print('Exit')
        
######################################################################
# Open Instagram Method
#
#This method opens the instagram home page
######################################################################
        def open_instagram(self):
                self.driver.get(const.BASE_URL)
######################################################################
#Login Method
#
#This method will log the user into their instagram account. 
######################################################################
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
######################################################################
#Search Tags Method
#
#This method will accept a list of hastags and will then loop through
#the list of tags. In each loop it will call the open posts method
######################################################################
        def search_tags(self, tags):
                for tag in tags:
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
                        counts = 0
                        counts = self.open_posts(const.COUNT)
                        utc_time = datetime.utcnow()
                        print('***********************************************************')
                        print(f'*     HashTag: {tag}')
                        print(f'*     Posts Liked: {counts[0]}')
                        print(f'*     Comments Posted: {counts[1]}')
                        print(f'*     Accounts Followed: {counts[2]}')
                        print(f'*     Current TimeStamp: {utc_time}')
                print('***********************************************************')
######################################################################
#Open Posts Method
#
#This method will accept a number which represent how many posts to 
#interact with. For each post this method will call the like, comment, 
#and follow method on each post that will be interacted with
#
#Only posts that have never been liked are interacted with
######################################################################
        def open_posts(self, count):
                counter = 0
                like_count = 0
                follow_count = 0
                comment_count = 0
                time.sleep(2)
                post_elements = self.driver.find_elements_by_css_selector(
                        'a[class="H-KQe"]'
                )
                for post in post_elements:
                        if counter < count:
                                time.sleep(2)
                                post.click()
                                liked = None
                                try:
                                        liked = self.driver.find_element_by_css_selector(
                                                'svg[aria-label="Unlike"]'
                                                )
                                except:
                                        self.like_post()
                                        like_count += 1
                                        self.user_post()
                                        commented = self.comment_post()
                                        if commented:
                                                comment_count += 1
                                        followed = self.follow_user()
                                        if followed: follow_count += 1
                                        counter += 1
                                time.sleep(2)
                                self.close_post()
                        else: return [like_count, comment_count, follow_count]
######################################################################
#Notification Enabler Method
#
#When you log into instagram their are two popups. This method is used
#to close one of those.
######################################################################
        def notification_enabler(self):
                try:
                        notification_element = self.driver.find_element_by_css_selector(
                                'button[class="aOOlW  bIiDR  "]'
                        )
                        notification_element.click()
                except:
                        print('Notification Element not present')
######################################################################
#Save Info Popup Method
#
#When you log into instagram their are two popups. This method is used
#to close one of those.
######################################################################                        
        def save_info_popup(self):
                try:
                        save_info_element = self.driver.find_element_by_css_selector(
                                'button[class="sqdOP  L3NKy   y3zKF     "]'
                        )
                        save_info_element.click()
                except:
                        print('Save Info Element Not Present')
######################################################################
#Like Post Method
#
#This method will like each post
######################################################################     
        def like_post(self): 
                like_element = self.driver.find_element_by_css_selector(
                        'span[class="fr66n"]'
                        )     
                like_element.click()    
######################################################################
#Comment Post Method
#
#This method will be used to comment on each post. It clicks on the 
#comment button, then adds a random comment from the comments list 
#into the text field and clicks post.
######################################################################                
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
                comment = comments[random.randint(0, len(comments)-1)]                
                comment_button_element = self.driver.find_element_by_css_selector(
                        'span[class="_15y0l"]'
                )
                try:
                        comment_button_element.click()
                        time.sleep(2)
                        comment_element = self.driver.find_element_by_css_selector(
                                'textarea[data-testid="post-comment-text-area"]'
                        )
                        comment_element.clear()
                        comment_element.send_keys(comment)
                        post_button_element = self.driver.find_element_by_css_selector(
                                'button[data-testid="post-comment-input-button"]'
                        )
                        post_button_element.click()
                        return True
                except:
                        return False
######################################################################
#User Method
#
#This method will get the username of whoever posted the current post
######################################################################               
        def user_post(self):
                user_element = self.driver.find_element_by_css_selector(
                      'a[class="sqdOP yWX7d     _8A5w5   ZIAjV "]'  
                ).text
                return user_element
######################################################################
#Close Post Method
#
#This method will click on the x in the top right corner of the page 
#when a post is open to close the post. 
######################################################################        
        def close_post(self):
                close_element = self.driver.find_element_by_css_selector(
                        'div[class="            qF0y9          Igw0E     IwRSH      eGOV_         _4EzTm                                                                                  BI4qX            qJPeX            fm1AK   TxciK yiMZG"]'
                )
                close_element.click()
######################################################################
#Follow User Method
#
#This method will be used to click on the follow button next to the 
#Users name. Therefor following this user. (If the user is already 
#being followed, nothing happens)
######################################################################               
        def follow_user(self):
                try:
                        follow_element = self.driver.find_element_by_xpath("//*[text()='Follow']")
                        follow_element.click()
                        return True #Followed
                except:
                        return False #No Follow
