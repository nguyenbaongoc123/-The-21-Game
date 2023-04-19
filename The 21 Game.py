#!/usr/bin/env python
# coding: utf-8

# Trò chơi 21 là trò chơi số đếm được bắt đầu từ 0, hai người chơi lần lượt có thể thêm 1, 2 hoặc 3, vào tổng số. Tổng số không được vượt quá 21 và người chơi đếm tới 21 sẽ thua. Ở bài tập này, chúng ta sẽ giả định cho máy làm người chơi thứ 2.
# 

# In[5]:


import random
while True:
    wf=random.randint(0,1)
    if wf==0:
        current_player="human"
    else:
        current_player="computer"
    current_number=0
    if current_player=="human":
        print("You play first!")
    else:
        print("Computer play first!")
    while current_number<=21:  
        if current_player=="human":
            print("Current number is: ",current_number)
            while True:
                player_choice=input("enter your choice (from 1 to 3) : ")
                if player_choice in['1','2','3']:
                    break
                else:
                    print("Your choice is not valid!")
            player_choice=int(player_choice)
            current_number+=player_choice
            if current_number>=21:
                print("Current number is: ",current_number)
                print("You lose!")
                break
            else:
                current_player="computer"
        if current_player=="computer":
            computer_choice=random.randint(1,3)
            print("Computer's choice is: ",computer_choice)
            current_number+=computer_choice
            if current_number>=21:
                print("Current number is: ",current_number)
                print("You win!")
            else:
                current_player="human"
    
    print(f"Enter 'Y' if you want to play again")
    play_again=input()
    if play_again!="Y":
        break
        


# In[ ]:




