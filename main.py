#ANTHONY COOPER
#TROJAN HORSE ATTACK SIMULATION

#For this assignment, I chose a Trojan Horse attack. I have experience with dealing with pop up-ads, which I get all the time on my laptop, so I thought it would be appropriate to choose this kind of attack for this assignment. I figured that most Trojan Horse attacks stereotypically begin with an attacker sending a pop-up ad to a users computer, the user being gullible enough to click on it. From there, the user has to choose whether they click on it, but risk being attacked, or ignore it, but risk missing out on what the pop up ad has to offer. In this simulation the user has to deal with those kinds of decisions as they are encountered by an oppourtunity for a discount, something similar to a pop up ad. In this simulation, the user can also update the computer, considering that regularly updating a computer can prevent Trojan Horse attacks. In this simulation, updating can allow the computer to let the user know what it beleives the best option would be, making the users decision more safer and less risky. The computer may be mostly accurate, although, to make things more interesting, not completely.

import random #import random
#make procedures that let the user know whether they have been attacked, avoided an attack, received a genuine coupon, or missed out on a genuine coupon; also let the user know if they ever updated the computer
def Attacked(updated): 
 print('You clicked on the link in the email only to find out that the whole thing was a Trojan Horse attack...')
 print('')
 print('...you just got horseplayed...')
 print('')
 print(' _(\ ')
 print('/_ .|')
 print('  \_|')  
 print('')
 print('RESULTS:')
 print('')
 print('OUTCOME: ATTACKED')
 print('UPDATED:',updated)

def Authentic(updated):
 print('You clicked on the link in the email to find out that the coupon was authentic after all...')
 print('')
 print('...not a bad deal...')
 print('')
 print('$$$')
 print('')
 print('RESULTS:')
 print('')
 print('OUTCOME: RECEIVED GENUINE COUPON')
 print('UPDATED:',updated)

def Avoided(updated):
 print('You ignored the email and avoided, what really was, a Trojan Horse attack...')
 print('')
 print('...that was a close one...')
 print('')
 print(' _________ ')
 print('|         |')
 print('|         |')
 print(' \       / ')
 print('  \_____/ ') 
 print('')
 print('RESULTS:')
 print('')
 print('OUTCOME: ATTACK AVOIDED')
 print('UPDATED:',updated)

def Missed_Out(updated):
 print('You ignored the email and missed out on, what really was, an authentic coupon...')
 print('')
 print('...missed out on a sweet new deal...')
 print('')
 print('XXX')
 print('')
 print('RESULTS:')
 print('')
 print('OUTCOME: MISSED OUT ON GENUINE COUPON')
 print('UPDATED:',updated)

print('TROJAN HORSE SIMULATION') #provide user with directions on what to do
print('')
print('DIRECTIONS:')
print('You just finished an email conversation with your favorite store about a huge discount on a new product that they plan to email to you as a thank you for you being a long-time customer, which you are. However, this may or may not be an attacker in disguise and when you finally get the email with the link to the coupon, you are unsure if it would be safe to proceed.')
print('') 
print('YOUR OPTIONS ON WHAT TO DO ARE LISTED BLOW:')
print('OPTION 1: click the link in the email')
print('OPTION 2: ignore the email')
print('OPTION 3: update the computer to inspect for malware')
print('') #provide the user with options of clicking on the link, ignoring the email, or updating the computer
print("ENTER '1' FOR OPTION 1")
print("ENTER '2' FOR OPTION 2")
print("ENTER '3' FOR OPTION 3")
print("ENTER BELOW:")
choice = input() #have the user select an option
chances = random.randrange(1,3) #randomly select a number between 1-2
updated = False #updated = False
if choice == '1': #if the user chooses to click the link
 if chances == 1: #if the random number is 1
  Attacked(updated) #the user is attacked
 elif chances == 2: #if the random number is 2
  Authentic(updated) #the user receives a genuine coupon
   
elif choice == '2': #if the user chooses to avoid the link
  if chances == 1: #if the random number is 1
   Avoided(updated) #the user avoided an attack
  elif chances == 2: #if the random number is 2
   Missed_Out(updated) #the user missed out on an authentic coupon
    
elif choice == '3': #if te user chooses to update the computer
 updated = True #updated = True
 update = random.randrange(1,3) #choose a random number between 1-2
 if update == 1: #if the random number is 1
  print('')
  print('You updated your computer. After doing a quick scan, it suggests that the email might be a setup for an Trojan Horse attack.') #let the user know that the update suggests that the email might be a setup for an Trojan Horse attack
 elif update == 2:
  print('')
  print('You updated your computer. After doing a quick scan, it suggests that the coupon might be authentic.') #let the user know that the update suggests that the coupon might be genuine
 print('')
 print('YOUR OPTIONS ON WHAT TO DO NEXT ARE LISTED BLOW:') #provide the user with the same options
 print('OPTION 1: click the link in the email')
 print('OPTION 2: ignore the email')
 print('***COMPUTER ALREADY UPDATED***')
 print('') #provide the user with options of clicking on the link and ignoring the email; also let the user know that the computer has already been updated
 print("ENTER '1' FOR OPTION 1")
 print("ENTER '2' FOR OPTION 2")
 print("ENTER BELOW:")
 choice_2 = input() #have the user select an option
 updated_chances = random.randrange(1,4) #randomly select a number between 1-3
 if choice_2 == '1': #if the user chooses to click the link
  if update == 1: #if the computer suspects an attack
   if updated_chances <= 2: #if the random number is 1 or 2
    Attacked(updated) #the user is attacked
   elif updated_chances == 3: #if the random number is 3
    Authentic(updated) #the user received a genuine coupon
  elif update == 2: #if the computer beleives that the coupon is authentic
   if updated_chances == 1: #if the random number is 1
    Attacked(updated) #the user is attacked
   elif updated_chances >= 2: #if the random number is 2 or 3
    Authentic(updated) #the user received a genuine coupon
  
 elif choice_2 == '2': #if the user chooses to ignore the email
  if update == 1: #if the computer suspects an attack
   if updated_chances <= 2: #if the random number is 1 or 2
    Avoided(updated) #the user avoided an attack
   elif updated_chances == 3: #if the random number is 3
    Missed_Out(updated) #the user missed out on a genuine coupon
  elif update == 2: #if the computer beleives that the coupon is authentic
   if updated_chances == 1: #if the random number is 1
    Avoided(updated) #the user avoided an attack
   elif updated_chances >= 2: #if the random number is 2 or 3
    Missed_Out(updated) #the user missed out on a genuine coupon

 else: 
   print('Sorry, that is not an option. Please try again...')
else:
   print('Sorry, that is not an option. Please try again...')
#if the user enters any unaccepted input; let the user know and tell them to try again

    
   ###
   ###
   ###
   
 
  
