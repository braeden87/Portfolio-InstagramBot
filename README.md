# Instagram Bot
## Skills Utilized
- Python
- Pygame
- Selenium
## Project Description
This Instagram Bot project is intended to be used for automating your social media interactions with the goal of gaining followers. For this project I utilized the Selenium library to automate the interactions with the browser. When run, the program will do the following:
- Open the browser
- Go to Instagram.com
- Log the user in
- Search for a specific Hashtag
- Open a post
- Check if the post has already been liked
  - If the post hasn't been liked:
    - Like the post
    - Comment on the post
    - Follow the user who posted
  - If the post had already been liked:
    - Move onto the next post
   
All of the features described above can be monitored using the window opened with Selenium. To make this project as user friendly as possible I created a GUI, using pygame, that will allow the user to input all of their information to the program before the program begins to interact with instagram. For the program to run succesfully, the user will need to input the following:
- Username
- Password
- At least 1 Hashtag (each tag should be seperated by a -)
- Email
- Password for Email

Once done inputting this information, the user has to click the submit button. After all of this, the browser will open and Instagram Automation will begin. The program is currently set to like 2 posts from each tag. But this can be changed to any number. After the program is finished, an email will be sent from the users email that they provided to that same email with a report of how many posts were interacted with.

## Inspiration For Project Creation
I was inspired to make this project after hearing about the Instapy library. The library boasts that it is a tool to 'automate social media interaction in order to "farm" likes. I originally attempted to use the library and it was clear that there were some major bugs in the open source code and the project was not currently funcitonal. Instead of trying to fix the already created library, I wanted to see if I could do it myself. 

## Project In Action


https://user-images.githubusercontent.com/59823288/141715773-4f88160c-c7c6-4965-8093-826d174da558.mov




