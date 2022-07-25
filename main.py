#287

#imports
import time
import replit

#Variables
YourHp = 10
RachelHp = 20
KnifeDamage = 10
KIBDamage = 9
PlayerInventory = ["Phone"]

#Functions

def RVW():
  replit.clear()
  global YourHp
  global RachelHp
  global KnifeDamage
  global KIBDamage
  print("YourHP:", YourHp)
  Pause()
  print("RachelHP:", RachelHp)
  Pause()
  print("(1) Attack")
  Pause()
  Input = input("Press 1 to attack Rachel with the Knife: ")
  Pause()
  if Input == "1":
    RachelHp = RachelHp - KnifeDamage
    print("You did 10 damage to Rachel HP:  RachelHP -", RachelHp)
    Pause()
  print("Rachel Turn")
  Pause()
  YourHp = YourHp - KIBDamage
  print("Rachel kicks you in the balls and does 9 damage:  YourHP -", YourHp )
  Pause()
  print("Your Turn")
  Pause()
  print("(1) Attack")
  Pause()
  Input1 = input("Press 1 to attack Rachel with the Knife: ")
  Pause()
  if Input1 == "1":
    RachelHp = RachelHp - KnifeDamage
    print("You did 10 damage to Rachel HP:  RachelHP -", RachelHp)

def GC():
  replit.clear()
  print(PlayerInventory)
  Pause()
  if('Car keys' in PlayerInventory):
    Pause()
    print("Rachel sees the car but the keys are not there she hears you coming and makes a run for it.")
    Pause()
    print("You then get in the car using the car keys you found earlier and catch up to her and arrested her for murder.")
    Pause()
    print("You ask her why would she kill her cousin?")
    Pause()
    print("Rachel - Because I was suppose to be the famous poetry in the family not Russell and when he became famous I was just the cousin of Russell my identity was ruin by him. So I killed him to get my identity back and I would do it again.")
    Pause()
    print("You use your phone to call the police to come and take her into custody. Rachel then spent the rest of her life in a cell. You solved the murder mystery and the rest of the family thanks you for your help and you then move on to the next investigation ahead. ")
    Pause()
  else:
    print("Rachel sees the car and see the keys and gets inside and drives off you try to run after her, but she long gone. You call the police to call for a manhunt, but after months of searching Rachel was never found.")
    Pause()
      

  
      
def WKWOK():
  replit.clear()
  print("PlayerInventory:", PlayerInventory)
  Pause()
  print("After hearing all of the suspects answers to your questions it is time to choose who killed Russell Hawkins.")
  Pause()
  if('knife' in PlayerInventory):
    print("(1) Use the knife to kill the murderer  (2) Don't use the knife and try to arrest the murder.")
    Pause()
    Input = input("Select a choice: ")
    Pause()
    if Input == "1":
      print("(1) Jason  (2) Nick  (3) Mike (4) Rachel (5) Isabella")
      Pause()
      Input2 = input("Select a choice: ")
      Pause()
      if Input2 == "1":
        print("You stab Jason in the heart believing he was the murderer of Russell Hawkins. You have completed this murder mystery.")
        Rest()
        print("However Jason was not the murderer that is what the true murderer wanted you to think and when the police found out that Jason was not the murderer of Russell Hawkins from an anonymous tip. You are sentenced to jail for life and the true murderer was never found ending Russell Hawkins case still being ruled as a suicide.")
        Rest()
      if Input2 == "2":
        print("You stab Nick in the heart believing he was the murderer of Russell Hawkins. You have completed this murder mystery.")
        Rest()
        print("However Nick was not the murderer that is what the true murderer wanted you to think and when the police found out that Nick was not the murderer of Russell Hawkins from an anonymous tip. You are sentenced to jail for life and the true murderer was never found ending Russell Hawkins case still being ruled as a suicide.")
        Rest()
      if Input2 == "3":
        print("You stab Mike in the heart believing he was the murderer of Russell Hawkins. You have completed this murder mystery.")
        Rest()
        print("However Mike was not the murderer that is what the true murderer wanted you to think and when the police found out that Mike was not the murderer of Russell Hawkins from an anonymous tip. You are sentenced to jail for life and the true murderer was never found ending Russell Hawkins case still being ruled as a suicide.")
        Rest()
      if Input2 == "4":
        print("You try to stab Rachel in the heart believing she was the murderer of Russell Hawkins, but Rachel dodged the knife. The rest of the family backs away. Then a boss battle starts Rachel vs you.")
        Pause()
        enter = input("Press enter to continue: ")
        RVW()
        Pause()
        print("You stab Rachel in the heart and she dies. Then you call the police and they transport her body away to the morgue. You have solved this murder mystery.")
        Rest()
        print("The rest of the family thanks you for your help and you then move on to the next investigation ahead.")
        Rest()
      if Input2 == "5":
        print("You stab Isabella in the heart believing she was the murderer of Russell Hawkins. You have completed this murder mystery.")
        Rest()
        print("However Isabella was not the murderer that is what the true murderer wanted you to think and when the police found out that Isabella was not the murderer of Russell Hawkins from an anonymous tip. You are sentenced to jail for life and the true murderer was never found ending Russell Hawkins case still being ruled as a suicide.")
        Rest()
        
    if Input == "2":
        print("(1) Jason  (2) Nick  (3) Mike (4) Rachel (5) Isabella")
        Pause()
        Input3 = input("Select a choice: ")
        Pause()
        if Input3 == "1":
          print("You accuse Jason of murder believing he was the murderer of Russell Hawkins and he is sent to jail. You have completed this murder mystery.")
          Rest()
          print("However Jason was not the murderer that is what the true murderer wanted you to think and Jason spent the rest of his life in a cell. The true murderer was never found ending Russell Hawkins case still being ruled as a suicide.")
          Rest()
        if Input3 == "2":
          print("You accuse Nick of murder believing he was the murderer of Russell Hawkins and he is sent to jail. You have completed this murder mystery.")
          Rest()
          print("However Nick was not the murderer that is what the true murderer wanted you to think and Nick spent the rest of his life in a cell. The true murderer was never found ending Russell Hawkins case still being ruled as a suicide.")
          Rest()
        if Input3 == "3":
          print("You accuse Mike of murder believing he was the murderer of Russell Hawkins and he is sent to jail. You have completed this murder mystery.")
          Rest()
          print("However Mike was not the murderer that is what the true murderer wanted you to think and Mike spent the rest of his life in a cell. The true murderer was never found ending Russell Hawkins case still being ruled as a suicide.")
          Rest()
        if Input3 == "4":
          print("You accuse Rachel of murder believing she was the murderer of Russell Hawkins and she runs away heading for the garage.")
          Pause()
          enter = input("Press enter to continue: ")
          GC()
        if Input3 == "5":
          print("You accuse Isabella of murder believing she was the murderer of Russell Hawkins and she is sent to jail. You have completed this murder mystery.")
          Rest()
          print("However Isabella was not the murderer that is what the true murderer wanted you to think and Isabella spent the rest of his life in a cell. The true murderer was never found ending Russell Hawkins case still being ruled as a suicide.")
          Rest()
  else:
    print("(1) Arrest the murder")
    Pause()
    Input = input("Press 1 arrest the murder:  ")
    Pause()
    if Input == "1":
      print("(1) Jason  (2) Nick  (3) Mike (4) Rachel (5) Isabella")
      Pause()
      Input4 = input("Select a choice: ")
      Pause()
      if Input4 == "1":
        print("You accuse Jason of murder believing he was the murderer of Russell Hawkins and he is sent to jail. You have completed this murder mystery.")
        Rest()
        print("However Jason was not the murderer that is what the true murderer wanted you to think and Jason spent the rest of his life in a cell. The true murderer was never found ending Russell Hawkins case still being ruled as a suicide.")
        Rest()
      if Input4 == "2":
        print("You accuse Nick of murder believing he was the murderer of Russell Hawkins and he is sent to jail. You have completed this murder mystery.")
        Rest()
        print("However Nick was not the murderer that is what the true murderer wanted you to think and Nick spent the rest of his life in a cell. The true murderer was never found ending Russell Hawkins case still being ruled as a suicide.")
        Rest()
      if Input4 == "3":
        print("You accuse Mike of murder believing he was the murderer of Russell Hawkins and he is sent to jail. You have completed this murder mystery.")
        Rest()
        print("However Mike was not the murderer that is what the true murderer wanted you to think and Mike spent the rest of his life in a cell. The true murderer was never found ending Russell Hawkins case still being ruled as a suicide.")
        Rest()
      if Input4 == "4":
        print("You accuse Rachel of murder believing she was the murderer of Russell Hawkins and she runs away heading for the garage.")
        Pause()
        enter = input("Press enter to continue: ")
        enter
        GC()
        Rest()
      if Input4 == "5":
        print("You accuse Isabella of murder believing she was the murderer of Russell Hawkins and she is sent to jail. You have completed this murder mystery.")
        Rest()
        print("However Isabella was not the murderer that is what the true murderer wanted you to think and Isabella spent the rest of his life in a cell. The true murderer was never found ending Russell Hawkins case still being ruled as a suicide.")
        Rest()
      
def Isabella():
  replit.clear()
  print("(1) Tell me the full story of Rachel finding the body of Russell Hawkins from your point of view?")
  Pause()
  Input = input("Press 1 to ask question: ")
  Pause()
  if Input == "1":
    print("Isabella - Well that night I was in my room reading one of Russell poetry books. Then I heard Rachel call me in a calm tone of voice given the situation she just witnessed.")
    Pause()
    print("(1) What did you do next?")
    Pause()
    Input1 = input("Press 1 to ask question: ")
    Pause()
    if Input1 == "1":
      print("Isabella - When I came to the room I was thinking Russell and Rachel wanted to tell me or show me something and when I went inside and looked to my left and saw Russell dead body and I screamed in agony because my heart just broke into million pieces. I ran to him to see if he was really dead tapping him and asking him if he is ok, but it was no use, but that was all I could do at that moment.")
      Pause()
      print("(1) So did you call the police?")
      Pause()
      Input2 = input("Press 1 to ask question: ")
      Pause()
      if Input2 == "1":
        print("Isabella - No, Rachel did after I told her to then the police came and did their police investigation and ruled it a suicide, but I could not believe it, so I hired you to make sure it was really a suicide.")
        Pause()
        print("(1) You said Rachel called you in a calm voice what did you mean by that?")
        Pause()
        Input3 = input("Press 1 to ask question: ")
        Pause()
        if Input3 == "1":
          print("Isabella - When she called me she acted like she did not just see the dead body of her cousin. It was just not normal. I do not know if she was trying to stay calm for me or situation at hand and not be emotional. I do not know.")
          Pause()
          print("(1) Was there anything else that did not seem right to you?")
          Pause()
          Input4 = input("Press 1 to ask question: ")
          Pause()
          if Input4 == "1":
            print("Isabella - Well when Rachel was telling the police officers what happen she said she open the door and saw his body. Which does not make any sense I had to go in the room to see his dead body I do not know I could be over thinking it.")

def Rachel():
  replit.clear()
  print("(1) Tell me the full story of finding the body of Russell Hawkins?")
  Pause()
  Input = input("Press 1 to ask question: ")
  Pause()
  if Input == "1":
    print("Rachel - Well that night I was walking to my room after going to the kitchen to make me a late night snack. In the corner of my eye I saw Russell with his door half opened and I fully opened the door to say hi I saw him dead with a gu knife in his hand covered in blood.")
    Pause()
    print("(1) What did you do next?")
    Pause()
    Input1 = input("Press 1 to ask question: ")
    Pause()
    if Input1 == "1":
      print("Rachel - I called over Isabella to tell her the terrible news I just found. When she got to the room she screamed in horror. Then ran in the room to see if he was ok tapping him asking him if he is ok over and over, but he was already dead she could not do anything.")
      Pause()
      print("(1) So did you call the police?")
      Pause()
      Input2 = input("Press 1 to ask question: ")
      Pause()
      if Input2 == "1":
        print("Rachel - Yes I did then the police came and did their police investigation and ruled it a suicide, but Isabella could not believe it, so she hired you to make sure it was really a suicide.")
        Pause()
        print("(1) Do you think it was a suicide?")
        Pause()
        Input3 = input("Press 1 to ask question: ")
        Pause()
        if Input3 == "1":
          print("Rachel - I think so.")
          Pause()
          print("(1) Why?")
          Pause()
          Input4 = input("Press 1 to ask question: ")
          Pause()
          if Input4 == "1":
            print("Rachel - Because the police said so and I believe in their decision. I do not think they will say it was a suicide and it could of been really a murder.")
        
      

def Mike():
  replit.clear()
  print("(1) Why would your brother commit suicide?   (2) Did your brother have any falling outs with anyone recently?\n(3) How are you feeling right now?             (4) Did you kill your brother? ")
  Pause()
  Input = input("Select a choice: ")
  Pause()
  if Input == "1":
    print("Mike - My brother would not commit suicide if he was dealing with depression or anything like that he would of told me.")
    Pause()
    print("(2) Did your brother have any falling outs with anyone recently? (3) How are you feeling right now?             (4) Did you kill your brother?")
    Pause()
    Input1 = input("Select a choice: ")
    Pause()
    if Input1 == "2":
      print("Mike - The only person I can think of is Nick. He been blowing up my brother phone these past few weeks recently to help him with his gambling problem and my brother told him he did not want to get involved with the mess Nick made.")
      Pause()
      print("(3) How are you feeling right now?   (4) Did you kill your brother?")
      Pause()
      Input2 = input("Select a choice: ")
      Pause()
      if Input2 == "3":
        print("Mike - Please do not ask me that question right now.")
        Pause()
        print("(4) Did you kill your brother?")
        Pause()
        Input3 = input("Select a choice: ")
        Pause()
        if Input3 == "4":
          print("Mike - You really ask me that question what psychopath would kill their own brother. I loved him I would die for my little brother.")
      if Input2 == "4":
        print("Mike - You really ask me that question what psychopath would kill their own brother. I loved him I would die for my little brother.")
        Pause()
        print("(3) How are you feeling right now?")
        Pause()
        Input4 = input("Select a choice: ")
        Pause()
        if Input4 == "3":
          print("Mike - Please do not ask me that question right now.")
    if Input1 == "3":
      print("Mike - Please do not ask me that question right now.")
      Pause()
      print("(2) Did your brother have any falling outs with anyone recently?  (4) Did you kill your brother?")
      Pause()
      Input5 = input("Select a choice: ")
      Pause()
      if Input5 == "2":
        print("Mike - The only person I can think of is Nick. He been blowing up my brother phone these past few weeks recently to help him with his gambling problem and my brother told him he did not want to get involved with the mess Nick made.")
        Pause()
        print("(4) Did you kill your brother?")
        Pause()
        Input6 = input("Select a choice: ")
        Pause()
        if Input6 == "4":
          print("Mike - You really ask me that question what psychopath would kill their own brother. I loved him I would die for my little brother.")
      if Input5 == "4":
        print("Mike - You really ask me that question what psychopath would kill their own brother. I loved him I would die for my little brother.")
        Pause()
        print("(2) Did your brother have any falling outs with anyone recently?")
        Pause()
        Input7 = input("Select a choice: ")
        Pause()
        if Input7 == "2":
          print("Mike - The only person I can think of is Nick. He been blowing up my brother phone these past few weeks recently to help him with his gambling problem and my brother told him he did not want to get involved with the mess Nick made.")
    if Input1 == "4":
      print("Mike - You really ask me that question what psychopath would kill their own brother. I loved him I would die for my little brother.")
      Pause()
      print(" (2) Did your brother have any falling outs with anyone recently? (3) How are you feeling right now?")
      Pause()
      Input8 = input("Select a choice: ")
      Pause()
      if Input8 == "2":
        print("Mike - The only person I can think of is Nick. He been blowing up my brother phone these past few weeks recently to help him with his gambling problem and my brother told him he did not want to get involved with the mess Nick made.")
        Pause()
        print("(3) How are you feeling right now?")
        Pause()
        Input9 = input("Select a choice: ")
        Pause()
        if Input9 == "3":
          print("Mike - Please do not ask me that question right now.")
      if Input8 == "3":
        print("Mike - Please do not ask me that question right now.")
        Pause()
        print("(2) Did your brother have any falling outs with anyone recently?")
        Pause()
        Input10 = input("Select a choice: ")
        Pause()
        if Input10 == "2":
          print("Mike - The only person I can think of is Nick. He been blowing up my brother phone these past few weeks recently to help him with his gambling problem and my brother told him he did not want to get involved with the mess Nick made.")

          
  if Input == "2":
    print("Mike - The only person I can think of is Nick. He been blowing up my brother phone these past few weeks recently to help him with his gambling problem and my brother told him he did not want to get involved with the mess Nick made.")
    Pause()
    print("1) Why would your brother commit suicide?  (3) How are you feeling right now?  (4) Did you kill your brother?")
    Pause()
    Input1 = input("Select a choice: ")
    Pause()
    if Input1 == "1":
      print("Mike - My brother would not commit suicide if he was dealing with depression or anything like that he would of told me.")
      Pause()
      print("(3) How are you feeling right now?  (4) Did you kill your brother?")
      Pause()
      Input2 = input("Select a choice: ")
      Pause()
      if Input2 == "3":
        print("Mike - Please do not ask me that question right now.")
        Pause()
        print("(4) Did you kill your brother?")
        Pause()
        Input3 = input("Select a choice: ")
        Pause()
        if Input3 == "4":
          print("Mike - You really ask me that question what psychopath would kill their own brother. I loved him I would die for my little brother.")
      if Input2 == "4":
        print("Mike - You really ask me that question what psychopath would kill their own brother. I loved him I would die for my little brother.")
        Pause()
        print("(3) How are you feeling right now?")
        Pause()
        Input4 = input("Select a choice: ")
        Pause()
        if Input4 == "3":
          print("Mike - Please do not ask me that question right now.")
    if Input1 == "3":
      print("Mike - Please do not ask me that question right now.")
      Pause()
      print("(1) Why would your brother commit suicide?   (4) Did you kill your brother?")
      Pause()
      Input5 = input("Select a choice: ")
      Pause()
      if Input5 == "1":
        print("Mike - My brother would not commit suicide if he was dealing with depression or anything like that he would of told me.")
        Pause()
        print("(4) Did you kill your brother?")
        Pause()
        Input6 = input("Select a choice: ")
        Pause()
        if Input6 == "4":
          print("Mike - You really ask me that question what psychopath would kill their own brother. I loved him I would die for my little brother.")
      if Input5 == "4":
        print("Mike - You really ask me that question what psychopath would kill their own brother. I loved him I would die for my little brother.")
        Pause()
        print("(1) Why would your brother commit suicide?")
        Pause()
        Input7 = input("Select a choice: ")
        Pause()
        if Input7 == "1":
          print("Mike - My brother would not commit suicide if he was dealing with depression or anything like that he would of told me.")
    if Input1 == "4":
      print("Mike - You really ask me that question what psychopath would kill their own brother. I loved him I would die for my little brother.")
      Pause()
      print("(1) Why would your brother commit suicide? (3) How are you feeling right now?")
      Pause()
      Input8 = input("Select a choice: ")
      Pause()
      if Input8 == "1":
        print("Mike - My brother would not commit suicide if he was dealing with depression or anything like that he would of told me.")
        Pause()
        print("(3) How are you feeling right now?")
        Pause()
        Input9 = input("Select a choice: ")
        Pause()
        if Input9 == "3":
          print("Mike - Please do not ask me that question right now.")
      if Input8 == "3":
        print("Mike - Please do not ask me that question right now.")
        Pause()
        print("(1) Why would your brother commit suicide?")
        Pause()
        Input10 = input("Select a choice: ")
        Pause()
        if Input10 == "1":
          print("Mike - My brother would not commit suicide if he was dealing with depression or anything like that he would of told me.")

          
  if Input == "3":
    print("Mike - Please do not ask me that question right now.")
    Pause()
    print("(1) Why would your brother commit suicide?   (2) Did your brother have any falling outs with anyone recently?      (4) Did you kill your brother?")
    Pause()
    Input1 = input("Select a choice: ")
    Pause()
    if Input1 == "1":
      print("Mike - My brother would not commit suicide if he was dealing with depression or anything like that he would of told me.")
      Pause()
      print("(2) Did your brother have any falling outs with anyone recently?     (4) Did you kill your brother?")
      Pause()
      Input2 = input("Select a choice: ")
      Pause()
      if Input2 == "2":
        print("Mike - The only person I can think of is Nick. He been blowing up my brother phone these past few weeks recently to help him with his gambling problem and my brother told him he did not want to get involved with the mess Nick made.")
        Pause()
        print("(4) Did you kill your brother?")
        Pause()
        Input3 = input("Select a choice: ")
        Pause()
        if Input3 == "4":
          print("Mike - You really ask me that question what psychopath would kill their own brother. I loved him I would die for my little brother.")
      if Input2 == "4":
        print("Mike - You really ask me that question what psychopath would kill their own brother. I loved him I would die for my little brother.")
        Pause()
        print("(2) Did your brother have any falling outs with anyone recently?")
        Pause()
        Input4 = input("Select a choice: ")
        Pause()
        if Input4 == "2":
          print("Mike - The only person I can think of is Nick. He been blowing up my brother phone these past few weeks recently to help him with his gambling problem and my brother told him he did not want to get involved with the mess Nick made.")
    if Input1 == "2":
      print("Mike - The only person I can think of is Nick. He been blowing up my brother phone these past few weeks recently to help him with his gambling problem and my brother told him he did not want to get involved with the mess Nick made.")
      Pause()
      print("(1) Why would your brother commit suicide?     (4) Did you kill your brother?")
      Pause()
      Input5 = input("Select a choice: ")
      Pause()
      if Input5 == "1":
        print("Mike - My brother would not commit suicide if he was dealing with depression or anything like that he would of told me.")
        Pause()
        print("(4) Did you kill your brother?")
        Pause()
        Input6 = input("Select a choice: ")
        Pause()
        if Input6 == "4":
          print("Mike - You really ask me that question what psychopath would kill their own brother. I loved him I would die for my little brother.")
      if Input5 == "4":
        print("Mike - You really ask me that question what psychopath would kill their own brother. I loved him I would die for my little brother.")
        Pause()
        print("(1) Why would your brother commit suicide?")
        Pause()
        Input7 = input("Select a choice: ")
        Pause()
        if Input7 == "1":
          print("Mike - My brother would not commit suicide if he was dealing with depression or anything like that he would of told me.")
    if Input1 == "4":
      print("Mike - You really ask me that question what psychopath would kill their own brother. I loved him I would die for my little brother.")
      Pause()
      print("(1) Why would your brother commit suicide?   (2) Did your brother have any falling outs with anyone recently?")
      Pause()
      Input8 = input("Select a choice: ")
      Pause()
      if Input8 == "1":
        print("Mike - My brother would not commit suicide if he was dealing with depression or anything like that he would of told me.")
        Pause()
        print("(2) Did your brother have any falling outs with anyone recently?")
        Pause()
        Input9 = input("Select a choice: ")
        Pause()
        if Input9 == "2":
          print("Mike - The only person I can think of is Nick. He been blowing up my brother phone these past few weeks recently to help him with his gambling problem and my brother told him he did not want to get involved with the mess Nick made.")
      if Input8 == "2":
        print("Mike - The only person I can think of is Nick. He been blowing up my brother phone these past few weeks recently to help him with his gambling problem and my brother told him he did not want to get involved with the mess Nick made.")
        Pause()
        print("(1) Why would your brother commit suicide?")
        Pause()
        Input10 = input("Select a choice: ")
        Pause()
        if Input10 == "1":
          print("Mike - My brother would not commit suicide if he was dealing with depression or anything like that he would of told me.")


          
  if Input == "4":
    print("Mike - You really ask me that question what psychopath would kill their own brother. I loved him I would die for my little brother.")
    Pause()
    print("(1) Why would your brother commit suicide?  (2) Did your brother have any falling outs with anyone recently? (3) How are you feeling right now?")
    Pause()
    Input1 = input("Select a choice: ")
    Pause()
    if Input1 == "1":
      print("Mike - My brother would not commit suicide if he was dealing with depression or anything like that he would of told me.")
      Pause()
      print("(2) Did your brother have any falling outs with anyone recently? (3) How are you feeling right now?")
      Pause()
      Input2 = input("Select a choice: ")
      Pause()
      if Input2 == "2":
        print("Mike - The only person I can think of is Nick. He been blowing up my brother phone these past few weeks recently to help him with his gambling problem and my brother told him he did not want to get involved with the mess Nick made.")
        Pause()
        print("(3) How are you feeling right now?")
        Pause()
        Input3 = input("Select a choice: ")
        Pause()
        if Input3 == "3":
          print("Mike - Please do not ask me that question right now.")
      if Input2 == "3":
        print("Mike - Please do not ask me that question right now.")
        Pause()
        print("(2) Did your brother have any falling outs with anyone recently?")
        Pause()
        Input4 = input("Select a choice: ")
        Pause()
        if Input4 == "2":
          print("Mike - The only person I can think of is Nick. He been blowing up my brother phone these past few weeks recently to help him with his gambling problem and my brother told him he did not want to get involved with the mess Nick made.")
    if Input1 == "2":
      print("Mike - The only person I can think of is Nick. He been blowing up my brother phone these past few weeks recently to help him with his gambling problem and my brother told him he did not want to get involved with the mess Nick made.")
      Pause()
      print("(1) Why would your brother commit suicide? (3) How are you feeling right now?")
      Pause()
      Input5 = input("Select a choice: ")
      Pause()
      if Input5 == "1":
        print("Mike - My brother would not commit suicide if he was dealing with depression or anything like that he would of told me.")
        Pause()
        print("(3) How are you feeling right now?")
        Pause()
        Input6 = input("Select a choice: ")
        Pause()
        if Input6 == "3":
          print("Mike - Please do not ask me that question right now.")
      if Input5 == "3":
        print("Mike - Please do not ask me that question right now.")
        Pause()
        print("(1) Why would your brother commit suicide?")
        Pause()
        Input7 = input("Select a choice: ")
        Pause()
        if Input7 == "1":
          print("Mike - My brother would not commit suicide if he was dealing with depression or anything like that he would of told me.")
    if Input1 == "3":
      print("Mike - Please do not ask me that question right now.")
      Pause()
      print("(1) Why would your brother commit suicide? (2) Did your brother have any falling outs with anyone recently?")
      Pause()
      Input8 = input("Select a choice: ")
      Pause()
      if Input8 == "1":
        print("Mike - My brother would not commit suicide if he was dealing with depression or anything like that he would of told me.")
        Pause()
        print("(2) Did your brother have any falling outs with anyone recently?")
        Pause()
        Input9 = input("Select a choice: ")
        Pause()
        if Input9 == "2":
          print("Mike - The only person I can think of is Nick. He been blowing up my brother phone these past few weeks recently to help him with his gambling problem and my brother told him he did not want to get involved with the mess Nick made.")
      if Input8 == "2":
        print("Mike - The only person I can think of is Nick. He been blowing up my brother phone these past few weeks recently to help him with his gambling problem and my brother told him he did not want to get involved with the mess Nick made.")
        Pause()
        print("(1) Why would your brother commit suicide?")
        Pause()
        Input10 = input("Select a choice: ")
        Pause()
        if Input10 == "1":
          print("Mike - My brother would not commit suicide if he was dealing with depression or anything like that he would of told me.")


  
def Nick():
  replit.clear()
  print("(1) Why would your best friend commit suicide?   (2) Did your best friend have any falling outs with anyone recently?\n(3) How are you feeling right now?             (4) Did you kill your best friend?")
  Pause()
  Input = input("Select a choice: ")
  Pause()
  if Input == "1":
    print("Nick - I dont know I have not talked to Russell for months. I only came down here to ask him if he can help with a problem I have and I'm not going to tell you what it is because it is none of your business.")
    Pause()
    print("(2) Did your best friend have any falling outs with anyone recently? (3) How are you feeling right now?  (4) Did you kill your best friend?")
    Pause()
    Input1 = input("Select a choice: ")
    Pause()
    if Input1 == "2":
      print("Nick - I do not believe so the only person I can think of is his wife Isabella they was not the happiest couple the last time I talked to Russell.")
      Pause()
      print("(3) How are you feeling right now?  (4) Did you kill your best friend?")
      Pause()
      Input2 = input("Select a choice: ")
      Pause()
      if Input2 == "3":
        print("Nick - I feel like you are wasting my time and everyone else's with these interrogations.")
        Pause()
        print("(4) Did you kill your best friend?")
        Pause()
        Input3 = input("Select a choice: ")
        Pause()
        if Input3 == "4":
          print("Nick - I'm done fuck you Wilson. I'm getting a drink from the dining room do not follow me unless you want to end up just like Russell.")
      if Input2 == "4":
        print("Nick - I'm done fuck you Wilson. I'm getting a drink from the dining room do not follow me unless you want to end up just like Russell.")
    if Input1 == "3":
      print("Nick - I feel like you are wasting my time and everyone else's with these interrogations.")
      Pause()
      print("(2) Did your best friend have any falling outs with anyone recently? (4) Did you kill your best friend?")
      Pause()
      Input4 = input("Select a choice: ")
      Pause()
      if Input4 == "2":
        print("Nick - I do not believe so the only person I can think of is his wife Isabella they was not the happiest couple the last time I talked to Russell.")
        Pause()
        print("(4) Did you kill your best friend?")
        Pause()
        Input5 = input("Select a choice: ")
        Pause()
        if Input5 == "4":
          print("Nick - I'm done fuck you Wilson. I'm getting a drink from the dining room do not follow me unless you want to end up just like Russell.")
      if Input4 == "4":
        print("Nick - I'm done fuck you Wilson. I'm getting a drink from the dining room do not follow me unless you want to end up just like Russell.")
    if Input1 == "4":
      print("Nick - I'm done fuck you Wilson. I'm getting a drink from the dining room do not follow me unless you want to end up just like Russell.")
      

          
  if Input == "2":
    print("Nick - I do not believe so the only person I can think of is his wife Isabella they was not the happiest couple the last time I talked to Russell.")
    Pause()
    print("(1) Why would your best friend commit suicide?  (3) How are you feeling right now?   (4) Did you kill your best friend?")
    Pause()
    Input1 = input("Select a choice: ")
    Pause()
    if Input1 == "1":
      print("Nick - I dont know I have not talked to Russell for months. I only came down here to ask him if he can help with a problem I have and I'm not going to tell you what it is because it is none of your business.")
      Pause()
      print("(3) How are you feeling right now?   (4) Did you kill your best friend?")
      Pause()
      Input2 = input("Select a choice: ")
      Pause()
      if Input2 == "3":
        print("Nick - I feel like you are wasting my time and everyone else's with these interrogations.")
        Pause()
        print("(4) Did you kill your best friend?")
        Pause()
        Input3 = input("Select a choice: ")
        Pause()
        if Input3 == "4":
          print("Nick - I'm done fuck you Wilson. I'm getting a drink from the dining room do not follow me unless you want to end up just like Russell.")
      if Input2 == "4":
        print("Nick - I'm done fuck you Wilson. I'm getting a drink from the dining room do not follow me unless you want to end up just like Russell.")
    if Input1 == "3":
      print("Nick - I feel like you are wasting my time and everyone else's with these interrogations.")
      Pause()
      print("(1) Why would your best friend commit suicide?   (4) Did you kill your best friend?")
      Pause()
      Input5 = input("Select a choice: ")
      Pause()
      if Input5 == "1":
        print("Nick - I dont know I have not talked to Russell for months. I only came down here to ask him if he can help with a problem I have and I'm not going to tell you what it is because it is none of your business.")
        Pause()
        print("(4) Did you kill your best friend?")
        Pause()
        Input6 = input("Select a choice: ")
        Pause()
        if Input6 == "4":
          print("Nick - I'm done fuck you Wilson. I'm getting a drink from the dining room do not follow me unless you want to end up just like Russell.")
      if Input5 == "4":
        print("Nick - I'm done fuck you Wilson. I'm getting a drink from the dining room do not follow me unless you want to end up just like Russell.")
    if Input1 == "4":
      print("Nick - I'm done fuck you Wilson. I'm getting a drink from the dining room do not follow me unless you want to end up just like Russell.")
    
          
  if Input == "3":
    print("Nick - I feel like you are wasting my time and everyone else's with these interrogations.")
    Pause()
    print("(1) Why would your best friend commit suicide?   (2) Did your best friend have any falling outs with anyone recently?     (4) Did you kill your best friend?")
    Pause()
    Input1 = input("Select a choice: ")
    Pause()
    if Input1 == "1":
      print("Nick - I dont know I have not talked to Russell for months. I only came down here to ask him if he can help with a problem I have and I'm not going to tell you what it is because it is none of your business.")
      Pause()
      print("(2) Did your best friend have any falling outs with anyone recently? (4) Did you kill your best friend?")
      Pause()
      Input2 = input("Select a choice: ")
      Pause()
      if Input2 == "2":
        print("Nick - I do not believe so the only person I can think of is his wife Isabella they was not the happiest couple the last time I talked to Russell.")
        Pause()
        print("(4) Did you kill your best friend?")
        Pause()
        Input3 = input("Select a choice: ")
        Pause()
        if Input3 == "4":
          print("Nick - I'm done fuck you Wilson. I'm getting a drink from the dining room do not follow me unless you want to end up just like Russell.")
      if Input2 == "4":
        print("Nick - I'm done fuck you Wilson. I'm getting a drink from the dining room do not follow me unless you want to end up just like Russell.")
    if Input1 == "2":
      print("Nick - I do not believe so the only person I can think of is his wife Isabella they was not the happiest couple the last time I talked to Russell.")
      Pause()
      print("(1) Why would your best friend commit suicide?     (4) Did you kill your best friend?")
      Pause()
      Input5 = input("Select a choice: ")
      Pause()
      if Input5 == "1":
        print("Nick - I dont know I have not talked to Russell for months. I only came down here to ask him if he can help with a problem I have and I'm not going to tell you what it is because it is none of your business.")
        Pause()
        print("(4) Did you kill your best friend?")
        Pause()
        Input6 = input("Select a choice: ")
        Pause()
        if Input6 == "4":
          print("Nick - I'm done fuck you Wilson. I'm getting a drink from the dining room do not follow me unless you want to end up just like Russell.")
      if Input5 == "4":
        print("Nick - I'm done fuck you Wilson. I'm getting a drink from the dining room do not follow me unless you want to end up just like Russell.")
    if Input1 == "4":
      print("Nick - I'm done fuck you Wilson. I'm getting a drink from the dining room do not follow me unless you want to end up just like Russell.")
          
  if Input == "4":
    print("Nick - I'm done fuck you Wilson. I'm getting a drink from the dining room do not follow me unless you want to end up just like Russell.")
    

          
def Jason():
  replit.clear()
  print("(1) Why would your Dad commit suicide?   (2) Did your Dad have any falling outs with anyone recently?\n(3) How are you feeling right now?             (4) Did you kill your Dad? ")
  Pause()
  Input = input("Select a choice: ")
  Pause()
  if Input == "1":
    print("Jason - My Dad would not commit suicide he had too much to live for and he would not leave his son behind with this burden.")
    Pause()
    print("(2) Did your Dad have any falling outs with anyone recently? (3) How are you feeling right now?\n(4) Did you kill your Dad?")
    Pause()
    Input1 = input("Select a choice: ")
    Pause()
    if Input1 == "2":
      print("Jason - I do not think so everyone loved my Dad.")
      Pause()
      print("(3) How are you feeling right now? (4) Did you kill your Dad?")
      Pause()
      Input2 = input("Select a choice: ")
      Pause()
      if Input2 == "3":
        print("Jason - I'm trying to stay strong for my mom, but I miss my Dad and I want him to come back.")
        Pause()
        print("(4) Did you kill your Dad?")
        Pause()
        Input3 = input("Select a choice: ")
        Pause()
        if Input3 == "4":
          print("Jason - No I would never.")
      if Input2 == "4":
        print("Jason - No I would never.")
        Pause()
        print("(3) How are you feeling right now?")
        Pause()
        Input4 = input("Select a choice: ")
        Pause()
        if Input4 == "3":
          print("Jason - I'm trying to stay strong for my mom, but I miss my Dad and I want him to come back.")
    if Input1 == "3":
      print("Jason - I'm trying to stay strong for my mom, but I miss my Dad and I want him to come back.")
      Pause()
      print("(2) Did your Dad have any falling outs with anyone recently? (4) Did you kill your Dad?")
      Pause()
      Input5 = input("Select a choice: ")
      Pause()
      if Input5 == "2":
        print("Jason - I do not think so everyone loved my Dad.")
        Pause()
        print("(4) Did you kill your Dad?")
        Pause()
        Input6 = input("Select a choice: ")
        Pause()
        if Input6 == "4":
          print("Jason - No I would never.")
      if Input5 == "4":
        print("Jason - No I would never.")
        Pause()
        print("(2) Did your Dad have any falling outs with anyone recently?")
        Pause()
        Input7 = input("Select a choice: ")
        Pause()
        if Input7 == "2":
          print("Jason - I do not think so everyone loved my Dad.")
    if Input1 == "4":
      print("Jason - No I would never.")
      Pause()
      print("(2) Did your Dad have any falling outs with anyone recently? (3) How are you feeling right now?")
      Pause()
      Input8 = input("Select a choice: ")
      Pause()
      if Input8 == "2":
        print("Jason - I do not think so everyone loved my Dad.")
        Pause()
        print("(3) How are you feeling right now?")
        Pause()
        Input9 = input("Select a choice: ")
        Pause()
        if Input9 == "3":
          print("Jason - I'm trying to stay strong for my mom, but I miss my Dad and I want him to come back.")
      if Input8 == "3":
        print("Jason - I'm trying to stay strong for my mom, but I miss my Dad and I want him to come back.")
        Pause()
        print("(2) Did your Dad have any falling outs with anyone recently?")
        Pause()
        Input10 = input("Select a choice: ")
        Pause()
        if Input10 == "2":
          print("Jason - I do not think so everyone loved my Dad.")

          
  if Input == "2":
    print("Jason - I do not think so everyone loved my Dad.")
    Pause()
    print("(1) Why would your Dad commit suicide? (3) How are you feeling right now? (4) Did you kill your Dad?")
    Pause()
    Input1 = input("Select a choice: ")
    Pause()
    if Input1 == "1":
      print("Jason - My Dad would not commit suicide he had too much to live for and he would not leave his son behind with this burden.")
      Pause()
      print("(3) How are you feeling right now? (4) Did you kill your Dad?")
      Pause()
      Input2 = input("Select a choice: ")
      Pause()
      if Input2 == "3":
        print("Jason - I'm trying to stay strong for my mom, but I miss my Dad and I want him to come back.")
        Pause()
        print("(4) Did you kill your Dad?")
        Pause()
        Input3 = input("Select a choice: ")
        Pause()
        if Input3 == "4":
          print("Jason - No I would never.")
      if Input2 == "4":
        print("Jason - No I would never.")
        Pause()
        print("(3) How are you feeling right now?")
        Pause()
        Input4 = input("Select a choice: ")
        Pause()
        if Input4 == "3":
          print("Jason - I'm trying to stay strong for my mom, but I miss my Dad and I want him to come back.")
    if Input1 == "3":
      print("Jason - I'm trying to stay strong for my mom, but I miss my Dad and I want him to come back.")
      Pause()
      print("(1) Why would your Dad commit suicide? (4) Did you kill your Dad?")
      Pause()
      Input5 = input("Select a choice: ")
      Pause()
      if Input5 == "1":
        print("Jason - My Dad would not commit suicide he had too much to live for and he would not leave his son behind with this burden.")
        Pause()
        print("(4) Did you kill your Dad?")
        Pause()
        Input6 = input("Select a choice: ")
        Pause()
        if Input6 == "4":
          print("Jason - No I would never.")
      if Input5 == "4":
        print("Jason - No I would never.")
        Pause()
        print("(1) Why would your Dad commit suicide?")
        Pause()
        Input7 = input("Select a choice: ")
        Pause()
        if Input7 == "1":
          print("Jason - My Dad would not commit suicide he had too much to live for and he would not leave his son behind with this burden.")
    if Input1 == "4":
      print("Jason - No I would never.")
      Pause()
      print("(1) Why would your Dad commit suicide? (3) How are you feeling right now?")
      Pause()
      Input8 = input("Select a choice: ")
      Pause()
      if Input8 == "1":
        print("Jason - My Dad would not commit suicide he had too much to live for and he would not leave his son behind with this burden.")
        Pause()
        print("(3) How are you feeling right now?")
        Pause()
        Input9 = input("Select a choice: ")
        Pause()
        if Input9 == "3":
          print("Jason - I'm trying to stay strong for my mom, but I miss my Dad and I want him to come back.")
      if Input8 == "3":
        print("Jason - I'm trying to stay strong for my mom, but I miss my Dad and I want him to come back.")
        Pause()
        print("(1) Why would your Dad commit suicide?")
        Pause()
        Input10 = input("Select a choice: ")
        Pause()
        if Input10 == "2":
          print("Jason - My Dad would not commit suicide he had too much to live for and he would not leave his son behind with this burden.")

          
  if Input == "3":
    print("Jason - I'm trying to stay strong for my mom, but I miss my Dad and I want him to come back.")
    Pause()
    print("(1) Why would your Dad commit suicide? (2) Did your Dad have any falling outs with anyone recently? (4) Did you kill your Dad?")
    Pause()
    Input1 = input("Select a choice: ")
    Pause()
    if Input1 == "1":
      print("Jason - My Dad would not commit suicide he had too much to live for and he would not leave his son behind with this burden.")
      Pause()
      print("(2) Did your Dad have any falling outs with anyone recently? (4) Did you kill your Dad?")
      Pause()
      Input2 = input("Select a choice: ")
      Pause()
      if Input2 == "2":
        print("Jason - I do not think so everyone loved my Dad.")
        Pause()
        print("(4) Did you kill your Dad?")
        Pause()
        Input3 = input("Select a choice: ")
        Pause()
        if Input3 == "4":
          print("Jason - No I would never.")
      if Input2 == "4":
        print("Jason - No I would never.")
        Pause()
        print("(2) Did your Dad have any falling outs with anyone recently?")
        Pause()
        Input4 = input("Select a choice: ")
        Pause()
        if Input4 == "2":
          print("Jason - I do not think so everyone loved my Dad.")
    if Input1 == "2":
      print("Jason - I do not think so everyone loved my Dad.")
      Pause()
      print("(1) Why would your Dad commit suicide? (4) Did you kill your Dad?")
      Pause()
      Input5 = input("Select a choice: ")
      Pause()
      if Input5 == "1":
        print("Jason - My Dad would not commit suicide he had too much to live for and he would not leave his son behind with this burden.")
        Pause()
        print("(4) Did you kill your Dad?")
        Pause()
        Input6 = input("Select a choice: ")
        Pause()
        if Input6 == "4":
          print("Jason - No I would never.")
      if Input5 == "4":
        print("Jason - No I would never.")
        Pause()
        print("(1) Why would your Dad commit suicide?")
        Pause()
        Input7 = input("Select a choice: ")
        Pause()
        if Input7 == "1":
          print("Jason - My Dad would not commit suicide he had too much to live for and he would not leave his son behind with this burden.")
    if Input1 == "4":
      print("Jason - No I would never.")
      Pause()
      print("(1) Why would your Dad commit suicide? (2) Did your Dad have any falling outs with anyone recently?")
      Pause()
      Input8 = input("Select a choice: ")
      Pause()
      if Input8 == "1":
        print("Jason - My Dad would not commit suicide he had too much to live for and he would not leave his son behind with this burden.")
        Pause()
        print("(2) Did your Dad have any falling outs with anyone recently?")
        Pause()
        Input9 = input("Select a choice: ")
        Pause()
        if Input9 == "2":
          print("Jason - I do not think so everyone loved my Dad.")
      if Input8 == "2":
        print("Jason - I do not think so everyone loved my Dad.")
        Pause()
        print("(1) Why would your Dad commit suicide?")
        Pause()
        Input10 = input("Select a choice: ")
        Pause()
        if Input10 == "1":
          print("Jason - My Dad would not commit suicide he had too much to live for and he would not leave his son behind with this burden.")


          
  if Input == "4":
    print("Jason - No I would never.")
    Pause()
    print("(1) Why would your Dad commit suicide? (2) Did your Dad have any falling outs with anyone recently? (3) How are you feeling right now?")
    Pause()
    Input1 = input("Select a choice: ")
    Pause()
    if Input1 == "1":
      print("Jason - My Dad would not commit suicide he had too much to live for and he would not leave his son behind with this burden.")
      Pause()
      print("(2) Did your Dad have any falling outs with anyone recently? (3) How are you feeling right now?")
      Pause()
      Input2 = input("Select a choice: ")
      Pause()
      if Input2 == "2":
        print("Jason - I do not think so everyone loved my Dad.")
        Pause()
        print("(3) How are you feeling right now?")
        Pause()
        Input3 = input("Select a choice: ")
        Pause()
        if Input3 == "3":
          print("Jason - I'm trying to stay strong for my mom, but I miss my Dad and I want him to come back.")
      if Input2 == "3":
        print("Jason - I'm trying to stay strong for my mom, but I miss my Dad and I want him to come back.")
        Pause()
        print("(2) Did your Dad have any falling outs with anyone recently?")
        Pause()
        Input4 = input("Select a choice: ")
        Pause()
        if Input4 == "2":
          print("Jason - I do not think so everyone loved my Dad.")
    if Input1 == "2":
      print("Jason - I do not think so everyone loved my Dad.")
      Pause()
      print("(1) Why would your Dad commit suicide? (3) How are you feeling right now?")
      Pause()
      Input5 = input("Select a choice: ")
      Pause()
      if Input5 == "1":
        print("Jason - My Dad would not commit suicide he had too much to live for and he would not leave his son behind with this burden.")
        Pause()
        print("(3) How are you feeling right now?")
        Pause()
        Input6 = input("Select a choice: ")
        Pause()
        if Input6 == "3":
          print("Jason - I'm trying to stay strong for my mom, but I miss my Dad and I want him to come back.")
      if Input5 == "3":
        print("Jason - I'm trying to stay strong for my mom, but I miss my Dad and I want him to come back.")
        Pause()
        print("(1) Why would your Dad commit suicide?")
        Pause()
        Input7 = input("Select a choice: ")
        Pause()
        if Input7 == "1":
          print("Jason - My Dad would not commit suicide he had too much to live for and he would not leave his son behind with this burden.")
    if Input1 == "3":
      print("Jason - I'm trying to stay strong for my mom, but I miss my Dad and I want him to come back.")
      Pause()
      print("(1) Why would your Dad commit suicide? (2) Did your Dad have any falling outs with anyone recently?")
      Pause()
      Input8 = input("Select a choice: ")
      Pause()
      if Input8 == "1":
        print("Jason - My Dad would not commit suicide he had too much to live for and he would not leave his son behind with this burden.")
        Pause()
        print("(2) Did your Dad have any falling outs with anyone recently?")
        Pause()
        Input9 = input("Select a choice: ")
        Pause()
        if Input9 == "2":
          print("Jason - I do not think so everyone loved my Dad.")
      if Input8 == "2":
        print("Jason - I do not think so everyone loved my Dad.")
        Pause()
        print("(1) Why would your Dad commit suicide?")
        Pause()
        Input10 = input("Select a choice: ")
        Pause()
        if Input10 == "1":
          print("Jason - My Dad would not commit suicide he had too much to live for and he would not leave his son behind with this burden.")
  


def BathRoom():
  replit.clear()
  print("You go to the bathroom, but it occupied. You hear someone talking over the phone in the bathroom about gambling problems, but before you can hear more you hear someone arguing with someone else in the living room and head there.")
  Pause()
  enter = input("Press Enter to go to the Living Room: ")
  enter
  LivingRoom()



def Garage():
  replit.clear()
  print("You enter the Garage and look around and spot car keys on the roof of the car.")
  Pause()
  print("What do you do?")
  Pause()
  print("(1) Pick up the car keys and keep it (2) Leave the car keys there")
  Pause()
  Input = input("Select a choice: ")
  Pause()
  if Input == "1":
    print("Car keys is add to your Inventory.")
    PlayerInventory.append("Car keys")
    Rest()
    print(PlayerInventory)
    Skip()
  if Input == "2":
    print("Car keys are left on the roof of the car>")
    Rest()
  replit.clear()
  if Input == "1" or "2":
    print("(1) Living Room (2) Dining Room (3) Bathroom")
    Pause()
  Input1 = input("Select a choice: ")
  if Input1 == "1":
    LivingRoom() 
  if Input1 == "2":
    DiningRoomAG()
    Pause()
    Input2 = input("Select a choice: ")
    if Input2 == "1":
      LivingRoom()
    if Input2 == "3":
      BathRoom()
  if Input1 == "3":
    BathRoom()

def GarageADR():
  replit.clear()
  print("You enter the Garage and look around and spot car keys on the roof of the car.")
  Pause()
  print("What do you do?")
  Pause()
  print("(1) Pick up the car keys and keep it (2) Leave the car keys there")
  Pause()
  Input = input("Select a choice: ")
  Rest()
  if Input == "1":
    print("Car keys is add to your Inventory.")
    PlayerInventory.append("Car keys")
    Rest()
    print(PlayerInventory)
    Skip()
  if Input == "2":
    print("Car keys are left on the roof of the car")
    Rest()
  replit.clear()
  if Input == "1" or "2":
    print("(1) Living Room (3) Bathroom")
    
 
def DiningRoom():
  replit.clear()
  print("You enter the dining room and look around and spot a knife on the floor.")
  Pause()
  print("What do you do?") 
  Pause()
  print("(1) Pick up the knife and keep it (2) Pick up the knife and put it in the drawer (3) Leave the knife there ")
  Pause()
  Input = input("Select a choice: ")
  Pause()
  if Input == "1":
    print("knife is add to your Inventory.")
    PlayerInventory.append("knife")
    Rest()
    print(PlayerInventory)
    Skip()
  if Input == "2":
    print("Knife is now in the drawer.")
    Rest()
  if Input == "3":
    print("Knife is left on the floor.")
    Rest()
  if Input == "1" or "2" or "3":
    replit.clear()
    print("(1) Living Room (2) Garage (3) Bathroom")
    Pause()
    Input1 = input("Select a choice: ")
    if Input1 == "1":
      LivingRoom()
    if Input1 == "2":
      GarageADR()
      Pause()
      Input2 = input("Select a choice: ")
      if Input2 == "1":
        LivingRoom()
      if Input2 == "3":
        BathRoom()
    if Input1 == "3":
      BathRoom()

def DiningRoomAG():
  replit.clear()
  print("You enter the dining room and look around and spot a knife on the floor.")
  Pause()
  print("What do you do?") 
  Pause()
  print("(1) Pick up the knife and keep it (2) Pick up the knife and put it in the drawer (3) Leave the knife there ")
  Pause()
  Input = input("Select a choice: ")
  Pause()
  if Input == "1":
    print("knife is add to your Inventory.")
    PlayerInventory.append("knife")
    Rest()
    print(PlayerInventory)
    Skip()
  if Input == "2":
    print("Knife is now in the drawer.")
    Rest()
  if Input == "3":
    print("Knife is left on the floor.")
    Rest()
  if Input == "1" or "2" or "3":
    replit.clear()
    print("(1) Living Room (3) Bathroom")
    Pause() 
  
  
    
def LivingRoom():
  replit.clear()
  print("Jason and Mike stop arguing.")
  Rest()
  print("This is everyone Jason is Russell son, Mike is Russell brother, Rachel is Russell cousin, and wait where is Nick?")
  Rest()
  print("Jason - Nick he had to do something real quick before coming to the living room.")
  Rest()
  print("Well Nick is Russell best friend since college and I'm Russell wife Isabella.")
  Rest()
  print("Isabella - There you are Nick. Where were you?")
  Rest()
  print("Nick - None of your business, I'm here right.")
  Rest()
  print("Isabella - Mr.Wilson he should tell us where he was right we can't be having sercets right now with this investigation.")
  Rest()
  print("(1) Yes  (2) No  (3) Let get started with the investigation with Mr.Hawkins")
  Rest()
  Input = input("Select a choice: ")
  Rest()
  if Input == "1":
    print("Isabella - So where were you Nick?")
    Rest()
    print("Nick - I was talking a shit in the bathroom, ok.")
    Rest()
    print("Jason - I knew something stink around here.")
    Rest()
    print("Nick - Shut up see this why I didn't want to say anything. Thanks alot Wilson.")
    Rest()
    print("Isabella - Well we got that situated, let me tell you about my husband and why I feel he didn't commit suicide and that he was murdered instead. Russell was a caring man he donated to the charity when he could, he loved his family very much, and he was about to publish his poerty book he been working on since the past 3 months. It just does not make sense for him to kill himself with so much to live for.")
  if Input == "2":
    print("Isabella - Ok, well let me tell you about my husband and why I feel he didn't commit suicide and that he was murdered instead. Russell was a caring man he donated to the charity when he could, he loved his family very much, and he was about to publish his poerty book he been working on since the past 3 months. It just does not make sense for him to kill himself with so much to live for. ")
  if Input == "3":
    print("Isabella - Ok, let me tell you about my husband and why I feel he didn't commit suicide and that he was murdered instead. Russell was a caring man he donated to the charity when he could, he loved his family very much, and he was about to publish his poerty book he been working on since the past 3 months. It just does not make sense for him to kill himself with so much to live for.")
  Rest()
  print("(1) Who found the body?")
  Pause()
  Input3 = input("Press 1 to ask question: ")
  if Input3 == "1":
    Pause()
    print("Isabella - Rachel found his body last night in his room covered in blood with a knife in his hand when passing by his room to go to her room that is what Rachel says what happened.")
    Pause()
    print("(1) Where was everyone else? ")
    Pause()
    Input4 = input("Press 1 to ask question: ")
    if Input4 == "1":
      Pause()
      print("Isabella - I was in my room Jason, Mike, and Nick was outside hanging out when she found the body.")
      Pause()
      print("(1) Interrogate everyone separately ")
      Pause()
      Input1 = input("Press 1 to interrogate everyone separately: ")
      if Input1 == "1":
        Pause()
        print("Who do you want to interrogate first?")
        Pause()
        print("(1) Jason  (2) Nick  (3) Mike (4) Rachel (5) Isabella")
        Pause()
        Input2 = input("Select a choice: ")
        if Input2 == "1":
          Jason()
          Rest()
          enter = input("Press Enter to continue: ")
          Pause()
          print("You - Ok thank you for answering my questions Jason. Tell Nick to come in.")
          Skip()
          Nick()
          Rest()
          enter = input("Press Enter to continue: ")
          Pause()
          print("You - Ok bye. Tell Mike to come in.")
          Skip()
          Mike()
          Rest()
          enter = input("Press Enter to continue: ")
          Pause()
          print("You - Ok thank you for answering my questions Mike. Tell Rachel to come in.")
          Skip()
          Rachel()
          Rest()
          enter = input("Press Enter to continue: ")
          Pause()
          print("You - Ok thank you for answering my questions Rachel. Tell Isabella to come in.")
          Skip()
          Isabella()
          Rest()
          enter = input("Press Enter to continue: ")
          Pause()
          print("You - Ok thank you for answering my questions Isabella.")
          Skip()

          
        if Input2 == "2":
          Nick()
          Rest()
          enter = input("Press Enter to continue: ")
          Pause()
          print("You - Ok bye. Tell Mike to come in.")
          Skip()
          Mike()
          Rest()
          enter = input("Press Enter to continue: ")
          Pause()
          print("You - Ok thank you for answering my questions Mike. Tell Rachel to come in.")
          Skip()
          Rachel()
          Rest()
          enter = input("Press Enter to continue: ")
          Pause()
          print("You - Ok thank you for answering my questions Rachel. Tell Isabella to come in.")
          Skip()
          Isabella()
          Rest()
          enter = input("Press Enter to continue: ")
          Pause()
          print("You - Ok thank you for answering my questions Isabella. Tell Jason to come in.")
          Skip()
          Jason()
          Rest()
          enter = input("Press Enter to continue: ")
          Pause()
          print("You - Ok thank you for answering my questions Jason.")
          Skip()
          
        if Input2 == "3":
          Mike()
          Rest()
          enter = input("Press Enter to continue: ")
          Pause()
          print("You - Ok thank you for answering my questions Mike. Tell Rachel to come in.")
          Skip()
          Rachel()
          Rest()
          enter = input("Press Enter to continue: ")
          Pause()
          print("You - Ok thank you for answering my questions Rachel. Tell Isabella to come in.")
          Skip()
          Isabella()
          Rest()
          enter = input("Press Enter to continue: ")
          Pause()
          print("You - Ok thank you for answering my questions Isabella. Tell Jason to come in.")
          Skip()
          Jason()
          Rest()
          enter = input("Press Enter to continue: ")
          Pause()
          print("You - Ok thank you for answering my questions Jason. Tell Nick to come in.")
          Skip()
          Nick()
          Rest()
          enter = input("Press Enter to continue: ")
          Pause()
          print("You - Ok bye.")
          Skip()
          
        if Input2 == "4":
          Rachel()
          Rest()
          enter = input("Press Enter to continue: ")
          Pause()
          print("You - Ok thank you for answering my questions Rachel. Tell Isabella to come in.")
          Skip()
          Isabella()
          Rest()
          enter = input("Press Enter to continue: ")
          Pause()
          print("You - Ok thank you for answering my questions Isabella. Tell Jason to come in.")
          Skip()
          Jason()
          Rest()
          enter = input("Press Enter to continue: ")
          Pause()
          print("You - Ok thank you for answering my questions Jason. Tell Nick to come in.")
          Skip()
          Nick()
          Rest()
          enter = input("Press Enter to continue: ")
          Pause()
          print("You - Ok bye. Tell Mike to come in.")
          Skip()
          Mike()
          Rest()
          enter = input("Press Enter to continue: ")
          Pause()
          print("You - Ok thank you for answering my questions Mike.")
          Skip()
          
          
        if Input2 == "5":
          Isabella()
          Rest()
          enter = input("Press Enter to continue: ")
          Pause()
          print("You - Ok thank you for answering my questions Isabella. Tell Jason to come in.")
          Skip()
          Jason()
          Rest()
          enter = input("Press Enter to continue: ")
          Pause()
          print("You - Ok thank you for answering my questions Jason. Tell Nick to come in.")
          Skip()
          Nick()
          Rest()
          enter = input("Press Enter to continue: ")
          Pause()
          print("You - Ok bye. Tell Mike to come in.")
          Skip()
          Mike()
          Rest()
          enter = input("Press Enter to continue: ")
          Pause()
          print("You - Ok thank you for answering my questions Mike. Tell Rachel to come in.")
          Skip()
          Rachel()
          Rest()
          enter = input("Press Enter to continue: ")
          enter
          Pause()
          print("You - Ok thank you for answering my questions Rachel.")
          Skip()
      replit.clear()
      WKWOK()
      for i in range(68):
        print("-", end = "")
      print("The End", end = "")
      for i in range(70):
        print("-", end = "")
      
  
def Pause():
  time.sleep(0.5)
  print()

def Rest():
  time.sleep(3.0)
  print()

def Skip():
  time.sleep(6.0)

def Start():
  replit.clear()
  print("Hello Mr.Wilson thank you for coming I got everyone in the living room. Do you want to meet everyone right now?")
  Pause()
  print("(1) Yes (2) No")
  Pause()
  Input = input("Select a choice: ")
  Pause()
  if Input == "1":
    LivingRoom()
    
  if Input == "2":
    print("Ok well you are free to look around the house if you like and when you are ready just come to the living room to meet everyone.")
    Pause()
    print("(1) Dining Room (2) Garage (3) Bathroom")
    Pause()
    Input1 = input("Select a choice: ")
    if Input1 == "1":
      DiningRoom()
    if Input1 == "2":
      Garage()
    if Input1 == "3":
      BathRoom()
      
def MainMenu():
 print("Who Dunnit")
 Pause()
 print("(1) Start")
 Pause()
 print("(2) How to Play")
 Pause()
 print("(3) Endings")
 Pause()
 MainMenuInput = input("Select a choice: ")
 if MainMenuInput == "1":
   Start()
 if MainMenuInput == "2":
   Pause()
   print("This game is set in the 1980's and you play as a private investigator named Wade Wilson who just arrived at a mansion 30 miles from the nearest town.\nAfter getting hired to investigate Russell Hawkins a famous poet suicide to see if it was really a suicide.\nYour goal is to figure out what really happen and shed light on Russell Hakwins suicide by making the correct choices.")
   Pause()
   enter = input("Press Enter to go Back: ")
   enter
   replit.clear()
   MainMenu()
 if MainMenuInput == "3":
  Pause()
  print("There are five endings to this game: \n1. The Murderer gets arrested and everyone lives.\n2. You kill the Murderer and everyone lives.\n3. You kill an innocent person and you go to jail for that murder and the true murderer of Mr.Hawkins is never found.\n4. You accuse an innocent person and they go to jail for the murder and the true murderer of Mr.Hawkins is never found.\n5. The Murderer gets away.")
  Pause()
  enter = input("Press Enter to go Back: ")
  enter
  replit.clear()
  MainMenu()

   

MainMenu()