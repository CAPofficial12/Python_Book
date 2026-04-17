#TODO make sure everything logs and sublogs - USER ADMIN
#TODO make sure all timestamp operations r the same
#------------------------------------------------------------VARIABLES SECTION-----------------------------------------------------------------------
#just some variables i kinda needed to declare first
#no worries here
import time
import random
counter = 0
counter_2 = 0
password = "password"
access = 0
logs = []
sublog = []
choice = "0"
run = True
command_run = False
first_boot = True
help_choice = ""
help_run = True
admin_help_run = True
user_message = 0
admin_message = 0
maintenance_message = 0
owner_message = 0
message_error = False
maint_run = False
owner_run = False
admin_run = False
um = "<Q> Users"
am = "<Q> Admin"
mm = "<Q> Maintenance"
alm = "<CQ> All"
user_dm = []
admin_dm = []
maint_dm = []
owner_dm = []
umrun = False
amrun = False
mmrun = False
omrun = False
system_fail = False
is_critical = False
needs_maintenance = False
base_online = False
maintenance_soon = False
system_nominal = False
version = 4.4

#-----------------------------------------------------------DIRECT MESSAGE SECTION--------------------------------------------------------------------
#---USER MESSAGE FUNCTION---
#we can just keep this the exact same for every person's, right?
#nope
def user_direct_messages():
    global umrun
    umrun = True
    clear_screen()
    while umrun:
        print("\n---MESSAGES---")
        print("1 - SEND A MESSAGE")
        print("2 - CHECK DM INBOX")
        print("3 - CLEAR INBOX")
        print("4 - QUIT")
        message_choice = input("SELECT HOW TO CONTINUE: ")
        if message_choice == "1":
            print("\n--WHO TO MESSAGE--")
            print("1 - ADMIN")
            print("2 - MAINTENANCE")
            print("3 - OWNER")
            who_message = input("WHO DO YOU WANT TO MESSAGE?: ")
            what_message = input("WHAT MESSAGE DO YOU WANT TO SEND?: ")
            if who_message == "1":
                admin_dm.append(f"{timestamp()} " + what_message + " - USER")
                print("MESSAGE SENT")
                sublog.append(f"{timestamp()} USER SENDS MESSAGE TO ADMIN")
                go_back()
                
            elif who_message == "2":
                maint_dm.append(f"{timestamp()} " + what_message + " - USER")
                print("MESSAGE SENT")
                sublog.append(f"{timestamp()} USER SENDS MESSAGE TO MAINTENANCE")
                go_back()
                
            elif who_message == "3":
                owner_dm.append(f"{timestamp()} " + what_message + " - USER")
                sublog.append(f"{timestamp()} USER SENDS MESSAGE TO OWNER")
                go_back()
        
            else:
                print("INVALID INPUT - TRY AGAIN")
            
        elif message_choice == "2":
            if len(user_dm) > 5:
                user_dm.pop(0)
                for i, entry in enumerate(user_dm, start=1):
                    print(f"{i} - {entry}")
                
            elif len(user_dm) == 0:
                print("INBOX EMPTY")
                go_back()

            else:
                for i, entry in enumerate(user_dm, start=1):
                    print(f"{i} - {entry}")
                go_back()
                    
        elif message_choice == "3":
            print("CLEARING...")
            user_dm.clear()
            time.sleep(5)
            sublog.append(f"{timestamp()} USER CLEARS MESSAGE INBOX")
            clear_screen()
            
        elif message_choice == "4":
            print("EXITING...")
            time.sleep(2)
            umrun = False
            clear_screen()
            
        else:
            print("INVALID INPUT - TRY AGAIN")
            go_back()
            
#---ADMIN MESSAGE FUNCTION---
#its easy to just copy paste ig
def admin_direct_messages():
    global amrun
    amrun = True
    clear_screen()
    while amrun:
        print("\n---MESSAGES---")
        print("1 - SEND A MESSAGE")
        print("2 - CHECK DM INBOX")
        print("3 - CLEAR INBOX")
        print("4 - QUIT")
        message_choice = input("SELECT HOW TO CONTINUE: ")
        if message_choice == "1":
            print("\n--WHO TO MESSAGE--")
            print("1 - USERS")
            print("2 - MAINTENANCE")
            print("3 - OWNER")
            who_message = input("WHO DO YOU WANT TO MESSAGE?: ")
            what_message = input("WHAT MESSAGE DO YOU WANT TO SEND?: ")
            if who_message == "1":
                user_dm.append(f"{timestamp()} " + what_message + " - ADMIN")
                print("MESSAGE SENT")
                sublog.append(f"{timestamp()} ADMIN SENDS MESSAGE TO USER")
                go_back()
                
            elif who_message == "2":
                maint_dm.append(f"{timestamp()} " + what_message + " - ADMIN")
                print("MESSAGE SENT")
                sublog.append(f"{timestamp()} ADMIN SENDS MESSAGE TO MAINTENANCE")
                go_back()
        
            elif who_message == "3":
                owner_dm.append(f"{timestamp()} " + what_message + " - ADMIN")
                print("MESSAGE SENT")
                sublog.append(f"{timestamp()} ADMIN SENDS MESSAGE TO OWNER")
                go_back()
        
            else:
                print("INVALID INPUT - TRY AGAIN")
                
        elif message_choice == "2":
            if len(admin_dm) > 5:
                admin_dm.pop(0)
                for i, entry in enumerate(admin_dm, start=1):
                    print(f"{i} - {entry}")
                go_back() 
            elif len(admin_dm) == 0:
                print("INBOX EMPTY")
                go_back()
                
            else:
                for i, entry in enumerate(admin_dm, start=1):
                    print(f"{i} - {entry}")
                go_back()
        
        elif message_choice == "3":
            print("CLEARING...")
            admin_dm.clear()
            time.sleep(5)
            sublog.append(f"{timestamp()} ADMIN CLEARS MESSAGE INBOX")
            clear_screen()
        
        elif message_choice == "4":
            print("EXITING...")
            time.sleep(2)
            amrun = False
            clear_screen()
            
        else:
            print("INVALID INPUT - TRY AGAIN")
            go_back()
        
#---MAINTENANCE MESSAGE FUNCTION---
#poor maintainers
#we can't catch a break
        
def maint_direct_messages():
    global mmrun
    mmrun = True
    clear_screen()
    while mmrun:
        print("\n---MESSAGES---")
        print("1 - SEND A MESSAGE")
        print("2 - CHECK DM INBOX")
        print("3 - CLEAR INBOX")
        print("4 - QUIT")
        message_choice = input("SELECT HOW TO CONTINUE: ")
        if message_choice == "1":
            print("\n--WHO TO MESSAGE--")
            print("1 - ADMIN")
            print("2 - USERS")
            print("3 - OWNER")
            who_message = input("WHO DO YOU WANT TO MESSAGE?: ")
            what_message = input("WHAT MESSAGE DO YOU WANT TO SEND?: ")
            if who_message == "1":
                admin_dm.append(f"{timestamp()} " + what_message + " - MAINTENANCE")
                print("MESSAGE SENT")
                sublog.append(f"{timestamp()} MAINTENANCE SENDS MESSAGE TO ADMIN")
                go_back()
                
            elif who_message == "2":
                user_dm.append(f"{timestamp()} " + what_message + " - MAINTENANCE")
                print("MESSAGE SENT")
                sublog.append(f"{timestamp()} MAINTENANCE SENDS MESSAGE TO USER")
                go_back()
                
            elif who_message == "3":
                owner_dm.append(f"{timestamp()} " + what_message + " - MAINTENANCE")
                print("MESSAGE SENT")
                sublog.append(f"{timestamp()} MAINTENANCE SENDS MESSAGE TO OWNER")
                go_back()
                
            else:
                print("INVALID INPUT - TRY AGAIN")
                
        elif message_choice == "2":
            if len(maint_dm) > 5:
                maint_dm.pop(0)
                for i, entry in enumerate(maint_dm, start=1):
                    print(f"{i} - {entry}")
                go_back()
            elif len(maint_dm) == 0:
                print("INBOX EMPTY")
                go_back()
                
            else:
                for i, entry in enumerate(maint_dm, start=1):
                    print(f"{i} - {entry}")
                go_back()
        
        elif message_choice == "3":
            print("CLEARING...")
            maint_dm.clear()
            time.sleep(3)
            sublog.append(f"{timestamp()} MAINTENANCE CLEARS MESSAGE INBOX")
            clear_screen()
            
        elif message_choice == "4":
            print("EXITING...")
            time.sleep(2)
            clear_screen()
            mmrun = False
            
        else:
            print("INVALID INPUT - TRY AGAIN")
            go_back()
    footer()
#---OWNER MESSAGE FUNCTION---
#FOR MR BIG BOSS OWNERMAN
def owner_direct_messages():
    global omrun
    omrun = True
    clear_screen()
    while omrun:
        print("\n---MESSAGES---")
        print("1 - SEND A MESSAGE")
        print("2 - CHECK DM INBOX")
        print("3 - CLEAR INBOX")
        print("4 - QUIT")
        message_choice = input("SELECT HOW TO CONTINUE: ")
        if message_choice == "1":
            print("\n--WHO TO MESSAGE--")
            print("1 - ADMIN")
            print("2 - MAINTENANCE")
            print("3 - USERS")
            who_message = input("WHO DO YOU WANT TO MESSAGE?: ")
            what_message = input("WHAT MESSAGE DO YOU WANT TO SEND?: ")
            if who_message == "1":
                admin_dm.append(f"{timestamp()} " + what_message + " - OWNER")
                print("MESSAGE SENT")
                sublog.append(f"{timestamp()} OWNER SENDS MESSAGE TO ADMIN")
                go_back()
                
            elif who_message == "2":
                maint_dm.append(f"{timestamp()} " + what_message + " - OWNER")
                print("MESSAGE SENT")
                sublog.append(f"{timestamp()} OWNER SENDS MESSAGE TO MAINTENANCE")
                go_back()
                
            elif who_message == "3":
                user_dm.append(f"{timestamp()} " + what_message + " - OWNER")
                print("MESSAGE SENT")
                sublog.append(f"{timestamp()} OWNER SENDS MESSAGE TO USER")
                go_back()
                
            else:
                print("INVALID INPUT - TRY AGAIN")
                go_back()
                
        elif message_choice == "2":
            if len(owner_dm) > 5: #you can have max 5 messages, like old mobile phones! cool huh?
                owner_dm.pop(0)
                for i, entry in enumerate(owner_dm, start=1):
                    print(f"{i} - {entry}")
                go_back()
            elif len(owner_dm) == 0:
                print("INBOX EMPTY")
                go_back()
            else:
                for i, entry in enumerate(owner_dm, start=1):
                    print(f"{i} - {entry}")
                go_back()
        
        elif message_choice == "3":
            print("CLEARING...")
            time.sleep(3)
            owner_dm.clear()
            sublog.append(f"{timestamp()} OWNER CLEARS MESSAGE INBOX")
            clear_screen()
            
        elif message_choice == "4":
            print("EXITING...")
            time.sleep(2)
            omrun = False
            clear_screen()
            
        else:
            print("INVALID INPUT - TRY AGAIN")
            go_back()
        
#------------------------------------------------SMALL SUBROUTINES SECTION------------------------------------------------------
#---TIMESTAMP---
            #i hated printing that every time so this makes life easy
def timestamp():
    return time.strftime("%d/%m/%Y %H:%M:%S")

#--ALL LOCK FUNCTION--
            #basically a small thing that makes life easy
def ask_all_lock():
    return input("LOGGING OUT ADMIN - ALL LOCK y/N?: ")

#---CLEAR SCREEN---
#helps keep life simple
def clear_screen():
    print("\033[2J\033[H", end = "")
    header()

#----GO BACK----
#simple thingy that quits you so easy life
def go_back():
    global quit_it
    quit_it = input("PRESS ANY KEY TO GO BACK: ")
    if quit_it == "":
        clear_screen()
    else:
        clear_screen()
        
#---HEADER---
#this is gonna appear at the top of every page
#not anymore
#it just may again
#i'm lost now HOW in hell do i make it work
#yuck
def header():
    global version
    print("BENTRAYS TERMINAL SYSTEM, VERSION BETA",version)
    print("_" * 41)
        
#--------------------------------------------------------------COMMAND PORTAL SECTION----------------------------------------------------------------
#----FAQ----
            #FAQ portal for the command portal
            #you come here if you pressed 1
            #look here to edit FAQs ig
def FAQ():
    clear_screen()
    print("\n----FAQ----")
    print("1 - WHAT IS COMMAND PORTAL?")
    print("2 - WHAT COMMANDS CAN I USE?")
    print("3 - MY COMMANDS WON'T WORK")
    FAQ_ask = input("SELECT A QUESTION TO VIEW: ")
    if FAQ_ask == "1":
        print("1 - WHAT IS COMMAND PORTAL?")
        print("THE COMMAND PORTAL IS SOMETHING I MADE TO GIVE YOU THE ABILITY TO ACCESS COMMANDS THAT ARE UNSEEN IN THE MENUS. IT MAY TAKE A LITTLE KNOWHOW, BUT IN THE END IT  SHOULD MAKE SENSE - YOUR FRIENDLY NEIGHBORHOOD CODEBUILDER ☺")
        go_back()
        
    elif FAQ_ask == "2":
        print("2 - WHAT COMMANDS CAN I USE?")
        print("YOU CAN USE VARIOUS COMMANDS - YOU CAN VIEW LOGS, ADD THEM, EDIT THEM, DOESN'T MATTER WHAT, AND THE BEST PART IS IT'S ALL OFF THE RECORDS. SOME ARE log.wipe, sublog.wipe, log.add, sublog.add ETC ETC - YOUR FRIENDLY NEIGHBOURHOOD CODEBUILDER ☺")
        go_back()
        
    elif FAQ_ask == "3":
        print("3 - MY COMMANDS WON'T WORK")
        print("IF YOUR COMMANDS WON'T WORK, CHECK THEY'VE BEEN FORMATTED CORRECTLY. THERE SHOULD BE NO SPACES, A '.' BETWEEN THE TWO WORDS, THE ONLY START SHOULD BE 'log' OR 'sublog' AS THESE ARE THE ONLY OPTIONS TO EDIT, AND THE END SHOULD BE 'wipe', 'add', 'remove' OR 'view' - YOUR FRIENDLY NEIGHBOURHOOD CODEBUILDER ☺")
        go_back()
        
    else:
        print("SORRY PAL, THAT DOESN'T SEEM TO BE AN OPTION, DO TRY AGAIN - YOUR FRIENDLY NEIGHBOURHOOD CODEBUILDER ☺")
        go_back()
        
#---COMMAND PORTAL---
            #the actual command portal
            #use admin or maint shortcut to get here
            #not quite sure how i got it to work but imma leave it alone
def command_portal():
    global command_run
    global admin_run
    global maint_run
    global access
    global owner_run
    command_run = True
    clear_screen()
    while command_run:
        print("WELCOME TO COMMAND PORTAL")
        print("\n----PORTAL----")
        print("1 - FAQ")
        print("2 - ENTER COMMAND")
        print("3 - QUIT")
        command_choice = input("SELECT HOW TO PROCEED: ")
        if command_choice == "1":
            FAQ()
        elif command_choice == "2":
            command = input("ENTER A COMMAND TO USE: ")
            if command == "log.wipe":
                logs.clear()
                print("WIPING...")
                time.sleep(3)
                print("COMMAND EXECUTED SUCCESSFULLY")
                clear_screen()
                
            elif command == "log.add":
                what_use = input("DO YOU WANT TO A: USE CURRENT TIME OR B: INPUT A TIME?: ")
                if what_use == "A" or what_use == "a":
                    add_new_log_from_command = input("ENTER NEW LOG TO ADD: ")
                    logs.append(f"{timestamp()} " + add_new_log_from_command)
                    print("COMMAND EXECUTED SUCCESSFULLY")
                    go_back()
                    
                elif what_use == "B" or what_use == "b":
                    add_new_log_from_command = input("ENTER NEW LOG TO ADD: ")
                    day_for_log = input("ENTER DAY OF LOG: ")
                    month_for_log = input("ENTER MONTH OF LOG: ")
                    year_for_log = input("ENTER YEAR OF LOG: ")
                    hour_for_log = input("ENTER HOUR OF LOG: ")
                    minute_for_log = input("ENTER MINUTE OF LOG: ")
                    second_for_log = input("ENTER SECOND OF LOG: ")
                    log_timestamp = day_for_log + "/" + month_for_log + "/" + year_for_log + " " + hour_for_log + ":" + minute_for_log + ":" + second_for_log
                    logs.append(log_timestamp + " " + add_new_log_from_command)
                    print("COMMAND EXECUTED SUCCESSFULLY")
                    go_back()
                    
                else:
                    print("INVALID INPUT - TRY AGAIN")
                    go_back()
            
            elif command == "log.remove":
                view_logs()
                try:
                    logwipe = int(input("WHICH LOG DO YOU WANT TO REMOVE?: "))
                    reallogwipe = logwipe - 1
                    logs.pop(reallogwipe)
                    print("COMMAND EXECUTED SUCCESSFULLY")
                    go_back()
                    
                except ValueError:
                    print("INVALID INPUT RECEIVED")
                    go_back()
                    
            elif command == "log.view":
                view_logs()
        
            elif command == "sublog.wipe":
                sublog.clear()
                print("WIPING...")
                sublog.append(f"{timestamp()} SUBLOGS WIPED BY [Command_Portal]")
                time.sleep(2)
                print("COMMAND EXECUTED SUCCESSFULLY")
                clear_screen()
                
            elif command == "sublog.add":
                what_use = input("DO YOU WANT TO A: USE CURRENT TIME OR B: INPUT A TIME?: ")
                if what_use == "A" or what_use == "a":
                    add_new_log_from_command = input("ENTER NEW SUBLOG TO ADD: ")
                    sublog.append(f"{timestamp()} " + add_new_log_from_command)
                    print("COMMAND EXECUTED SUCCESSFULLY")
                    go_back()
                    
                elif what_use == "B" or what_use == "b":
                    add_new_log_from_command = input("ENTER NEW SUBLOG TO ADD: ")
                    day_for_log = input("ENTER DAY OF SUBLOG: ")
                    month_for_log = input("ENTER MONTH OF SUBLOG: ")
                    year_for_log = input("ENTER YEAR OF SUBLOG: ")
                    hour_for_log = input("ENTER HOUR OF SUBLOG: ")
                    minute_for_log = input("ENTER MINUTE OF SUBLOG: ")
                    second_for_log = input("ENTER SECOND OF SUBLOG: ")
                    log_timestamp = day_for_log + "/" + month_for_log + "/" + year_for_log + " " + hour_for_log + ":" + minute_for_log + ":" + second_for_log
                    sublog.append(log_timestamp + " " + add_new_log_from_command)
                    print("COMMAND EXECUTED SUCCESSFULLY")
                    go_back()
                    
                else:
                    print("INVALID INPUT - TRY AGAIN")
                    go_back()
        
            elif command == "sublog.remove":
                if len(sublog) == 0:
                    print("LOGS EMPTY")
                    go_back()
                else:
                    print("\n----SUBLOG FILE----")

                    for i, entry in enumerate(sublog, start=1):
                        print(f"{i} - {entry}")
                    try:
                        sublogwipe = int(input("WHICH LOG DO YOU WANT TO REMOVE?: "))
                        realsubwipe = sublogwipe - 1
                        sublog.pop(realsubwipe)
                        print("COMMAND EXECUTED SUCCESSFULLY")
                        go_back()
                        
                    except ValueError:
                        print("INVALID INPUT")
                        go_back()
                        
            elif command == "sublog.view":
                if len(sublog) == 0:
                    print("LOGS EMPTY")
                    go_back()
                else:
                    print("\n----SUBLOG FILE----")

                    for i, entry in enumerate(sublog, start=1):
                        print(f"{i} - {entry}")
                    go_back()
            elif command == "access.user":
                admin_run = False
                maint_run = False
                access = 1
                command_run = False
            elif command == "access.admin":
                maint_run = False
                access = 0
                admin_run = True
                command_run = False
            elif command == "access.maintenance":
                maint_run = True
                admin_run = False
                access = 0
                command_run = False
            elif command == "access.owner":
                maint_run  = False
                admin_run = False
                access = 0
                owner_run = True
                command_run = False
            else:
                print("SORRY PAL, DON'T THINK THAT'S AN OPTION")
                go_back()
                
        elif command_choice == "3":
            print("GOODBYE!")
            sublog.append(f"{timestamp()} " + "ADMIN EXITS COMMAND PORTAL")
            time.sleep(2)
            clear_screen()
            command_run = False
            
        else:
            print("SORRY PAL, DON'T THINK THAT'S AN OPTION")
            go_back()
#------------------------------------------------------------------MENU SECTION-----------------------------------------------------------------------
#---OWNER MENU---
            #see this? this is why we seperate with comments
            #i almost lost this under the command portal
def owner_menu():
    global user_message
    global admin_message
    global maintenance_message
    global password
    global owner_run
    global owner_message
    global first_boot
    owner_run = True
    clear_screen()
    while owner_run:
        print("\n----OWNER MENU----")
        print("1 - SEND MESSAGE")
        print("2 - CHANGE PASSWORD")
        print("3 - VIEW LOGS")
        print("4 - ADD LOG")
        print("5 - INBOX")
        print("6 - DIRECT MESSAGES")
        print("7 - QUIT")
        if message_error == True:
            print("ERROR: YOUR MESSAGE IN LOG FAILED TO SEND")
        else:
            print(">")
        owner_choice = input ("SELECT HOW TO PROCEED: ")
        if owner_choice == "1":
            print("1 - USERS")
            print("2 - ADMIN")
            print("3 - MAINTENANCE")
            print("4 - ALL")
            print("5 - GO BACK")
            who_message = input("WHO WOULD YOU LIKE TO SEND A MESSAGE TO?: ")
            if who_message == "1":
                user_message = user_message + 1
                sublog.append(f"{timestamp()} OWNER SENDS A LOG MESSAGE TO USERS")
            elif who_message == "2":
                admin_message = admin_message + 1
                sublog.append(f"{timestamp()} OWNER SENDS A LOG MESSAGE TO ADMIN")
            elif who_message == "3":
                maintenance_message = maintenance_message + 1
                sublog.append(f"{timestamp()} OWNER SENDS A LOG MESSAGE TO MAINTENANCE")
            elif who_message == "4":
                user_message = user_message + 1
                admin_message = admin_message + 1
                maintenance_message = maintenance_message + 1
                sublog.append(f"{timestamp()} OWNER SENDS A LOG MESSAGE TO ALL")
            elif who_message == "5":
                clear_screen()
            else:
                print("INVALID OPTION")
                
            what_message = input("WHAT IS YOUR MESSAGE?: ")
            if who_message == "1":
                logs.append(f"{timestamp()} [MESSAGE FROM OWNER] --- " + um + " " + what_message)
                print("MESSAGE SENT")
                go_back()
                
            elif who_message == "2":
                logs.append(f"{timestamp()} [MESSAGE FROM OWNER] --- " + am + " " + what_message)
                print("MESSAGE SENT")
                go_back()
                
            elif who_message == "3":
                logs.append(f"{timestamp()} [MESSAGE FROM OWNER] --- " + mm + " " + what_message)
                print("MESSAGE SENT")
                go_back()
                
            else:
                logs.append(f"{timestamp()} [MESSAGE FROM OWNER] --- " + alm + " " + what_message)
                print("MESSAGE SENT")
                go_back()
                
        elif owner_choice == "2":
            new_password = input("WHAT WOULD YOU LIKE TO CHANGE THE PASSWORD TO?: ")
            also_new = input("PLEASE RETYPE PASWORD: ")
            if new_password == also_new:
                sublog.append(f"{timestamp()} OWNER CHANGES PASSWORD TO {new_password} FROM {password}")
                password = new_password
                print("PASSWORD CHANGED SUCCESSFULLY")
                sublog.append(f"{timestamp()} OWNER CHANGES PASSWORD")
                go_back()
                
            else:
                print("PASSWORDS DO NOT MATCH - TRY AGAIN")
                go_back()
                
        elif owner_choice == "3":
            view_logs()
            sublog.append(f"{timestamp()} OWNER VIEWS LOGS")
            
        elif owner_choice == "4":
            add_log()
            sublog.append(f"{timestamp()} OWNER ADDS LOG")
            
        elif owner_choice == "5":
            sublog.append(f"{timestamp()} OWNER VIEWS INBOX")
            print("YOU HAVE ", owner_message, "MESSAGE(S)")
            if owner_message > 0:
                print("CHECK LOGS FOR <Q>")
                owner_message = 0
                go_back()
                
            else:
                print("INBOX EMPTY")
                go_back()
                
        elif owner_choice == "6":
            owner_direct_messages()
            sublog.append(f"{timestamp()} OWNER OPENS DM PORTAL")
            
        elif owner_choice == "BIOS":
            bios()
            sublog.append(f"{timestamp()} OWNER OPENS BIOS")
            
        elif owner_choice == "7":
            print("GOODBYE, OWNER")
            time.sleep(2)
            clear_screen()
            first_boot = False
            owner_run = False
            sublog.append(f"{timestamp()} OWNER LOGS OUT")
            
        else:
            print("INVALID INPUT, TRY AGAIN")
            go_back()

#---ADMIN MENU---
            #SEE ABOVE!!! I almost lost this!
            #admins and hackers come here
            #i miss when this was the most complicated part of my code
def admin_menu():
    global access
    global admin_message
    global first_boot
    global admin_run
    clear_screen()
    admin_run = True
    while admin_run:
        print("\n----ADMIN----")
        print("PRESS 1 TO VIEW LOGS")
        print("PRESS 2 TO ADD LOGS")
        print("PRESS 3 TO DELETE LOGS")
        print("PRESS 4 TO EDIT PASSWORD")
        print("PRESS 5 FOR HELP")
        print("PRESS 6 FOR INBOX")
        print("PRESS 7 FOR DIRECT MESSAGES")
        print("PRESS 8 TO QUIT")
        if message_error == True:
            print("ERROR: YOUR MESSAGE IN LOG FAILED TO SEND")
        else:
            print(">")
        admin_choice = input("SELECT HOW TO PROCEED: ")
        print("------------\n")
        if admin_choice == "1":
            view_logs()
            sublog.append(f"{timestamp()} ADMIN VIEWS LOGS")
        elif admin_choice == "2":
            add_log()
            sublog.append(f"{timestamp()} ADMIN ADDS LOG")
        elif admin_choice == "3":
            logs.clear()
            print("LOGS CLEARED")
            sublog.append(f"{timestamp()} ADMIN CLEARS LOGS")
            go_back()
            
        elif admin_choice == "4":
            global password
            password = input("WHAT WOULD YOU LIKE TO CHANGE YOUR PASSWORD TO?: ")
            logs.append(f"{timestamp()} PASSWORD UPDATED BY ADMIN")
            sublog.append(f"{timestamp()} ADMIN CHANGES PASSWORD")
            print("PASSWORD CHANGED SUCCESSFULLY")
            time.sleep(2)
            clear_screen()
        elif admin_choice == "5":
            admin_help_menu()
            #line 683
        elif admin_choice == "6":
            print("YOU HAVE ", admin_message ,"MESSAGE(S)")
            sublog.append(f"{timestamp()} ADMIN VIEWS INBOX")
            if admin_message > 0:
                print("CHECK LOGS FOR <Q>")
                admin_message = 0
                go_back()
            else:
                print("INBOX EMPTY")
                go_back()
                
        elif admin_choice == "7":
            admin_direct_messages()
            #This is on line 107 - you'll thank me later
        elif admin_choice == "BIOS":
            bios()
            sublog.append(f"{timestamp()} ADMIN OPENS BIOS")
        elif admin_choice == "8":
            result = ask_all_lock()
            sublog.append(f"{timestamp()} ADMIN LOGS OUT")
            access = 0
            first_boot = False
            if result == "y":
                print("ALL ACCESS SUSPENDED")
                password = "srwdfghjkjhgfdsdfghjkoiuy76t54retwsgxdcfvgbhnjoki098utdbnlkijuygtvfbhnjkioiuytr563789;''l'l,.l;p;oityhjfgvbhnjklokijuhygf"
                #this is genuinely ridiculous. never again.
                logs.append(f"{timestamp()} ADMIN LOGGED OUT, ALL ACCESS SUSPENDED ADMIN'S ORDERS")
                sublog.append(f"{timestamp()} ADMIN SUSPENDS ACCESS")
                admin_run = False

            elif result == "N":
                print("ADMIN LOGGED OUT")
                break
                admin_run = False
                sublog.append(f"{timestamp()} ADMIN LOGS OUT")
                
            elif result == "n":
                print("ADMIN LOGGED OUT")
                break
                admin_run = False
                sublog.append(f"{timestamp()} ADMIN LOGS OUT")
                
            else:
                print("INVALID OPTION - ACCESS RESUMED")
                sublog.append(f"{timestamp()} ADMIN ENTERS INVALID OPTION")
                sublog.append(f"{timestamp()} ADMIN LOGS OUT")
                admin_run = False
                
        elif admin_choice == "Open Command Portal":
            command_portal()
            sublog.append(f"{timestamp()} ADMIN ENTERS COMMAND PORTAL")
                
        else:
            print("INVALID OPTION")
            sublog.append(f"{timestamp()} ADMIN ENTERS INVALID OPTION")
            clear_screen()

#---ADMIN HELP---
            #oh admins
            #soft sweet little admins
            #help is on the way
def admin_help_menu():
    global admin_help_run
    global admin_help_choice
    admin_help_run = True
    clear_screen()
    sublog.append(f"{timestamp()} ADMIN OPENS HELP MENU")
    while admin_help_run:
        print("\n----HELP----")
        print("1 - WORDING")
        print("2 - ACCESS ISSUE")
        print("3 - OTHER")
        print("4 - QUIT")
        admin_help_choice = input("PICK WHAT YOU NEED HELP WITH: ")
        if admin_help_choice == "1":
            print("WORDING CAN BE A TRICKY THING - LOGS CAN BE INFORMAL, AND IF ADMIN SAYS OTHERWISE THEY ARE INCORRECT. TO SEND A MESSAGE, USE <Q> THEN THE RECIPIENT (Admin, [example username], Maintenance_Team OR Owner) AND IT WILL SEND THEM A PING TO CHECK LOGS. TO PING EVERY USER, USE <CQ>.")
            sublog.append(f"{timestamp()} ADMIN ASKS FOR WORDING HELP")
            go_back()
            
        elif admin_help_choice == "2":
            print("IF YOU'VE GOT AN ACCESS ISSUE, YOUR ACCESS LEVEL HAS LIKELY BEEN CHANGED BY ADMIN. IF YOU CAN'T PING THEM A <Q> MESSAGE, SPEAK TO THEM IN PERSON AND THEY SHOULD GIVE YOU BACK ACCESS.")
            sublog.append(f"{timestamp()} ADMIN ASKS FOR ACCESS HELP")
            go_back()
            
        elif admin_help_choice == "3":
            print("IF YOU'VE GOT ANOTHER ISSUE, IT WILL LIKELY BE A BUG SO LOG IT, SEND A <Q> TO Maintenance WITH A LOG OF YOUR ISSUE AND LET THEM FIX IT")
            sublog.append(f"{timestamp()} ADMIN ASKS FOR OTHER HELP")
            go_back()
            
        elif admin_help_choice == "4":
            admin_help_run = False
            sublog.append(f"{timestamp()} ADMIN EXITS HELP MENU")
            print("EXITING...")
            time.sleep(2)
            clear_screen()
        else:
            print("INVALID OPTION")
            sublog.append(f"{timestamp()} ADMIN INPUTS INVALID OPTION")
            go_back()

#---HELP MENU---
            #get stuffed normal useres
            #if you wanted priviledge, you shouldve been important enough to become an admin
def help_menu():
    global help_run
    global help_choice
    help_run = True
    clear_screen()
    sublog.append(f"{timestamp()} USER OPENS HELP MENU")
    while help_run:
        print("\n----HELP----")
        print("1 - WORDING")
        print("2 - ACCESS ISSUE")
        print("3 - OTHER")
        print("4 - QUIT")
        help_choice = input("PICK WHAT YOU NEED HELP WITH: ")
        if help_choice == "1":
            print("WORDING CAN BE A TRICKY THING - LOGS CAN BE INFORMAL, AND IF ADMIN SAYS OTHERWISE THEY ARE INCORRECT. TO SEND A MESSAGE, USE <Q> THEN THE RECIPIENT (Admin, [example username], Maintenance_Team OR Owner) AND IT WILL SEND THEM A PING TO CHECK LOGS. TO PING EVERY USER, USE <CQ>.")
            sublog.append(f"{timestamp()} USER ASKS FOR WORDING HELP")
            go_back()
        elif help_choice == "2":
            print("IF YOU'VE GOT AN ACCESS ISSUE, YOU HAVE LIKELY BEEN LOCKED OUT BY ADMIN. IF YOU CAN'T PING THEM A <Q> MESSAGE, SPEAK TO THEM IN PERSON AND THEY SHOULD GIVE YOU BACK ACCESS.")
            sublog.append(f"{timestamp()} USER ASKS FOR ACCESS HELP")
            go_back()
        elif help_choice == "3":
            print("IF YOU'VE GOT ANOTHER ISSUE, IT WILL LIKELY BE A BUG SO LOG IT, SEND A <Q> TO Maintenance WITH A LOG OF YOUR ISSUE AND LET THEM FIX IT")
            sublog.append(f"{timestamp()} USER ASKS FOR OTHER HELP")
            go_back()
            
        elif help_choice == "4":
            print("EXITING...")
            time.sleep(2)
            clear_screen()
            help_run = False
            sublog.append(f"{timestamp()} USER EXITS HELP MENU")
            
        else:
            print("INVALID OPTION")
            sublog.append(f"{timestamp()} USER INPUTS INVALID OPTION")

#---MAINT MENU---
            #tell me now
            #why in gods name wasn't this seperated
            #like at all, it's a wonder running user help didnt open the maint menu
            #not even a single line? don't do that ever again please
def maintenance_menu():
    global access
    global maint_choice
    global maint_run
    global password
    global maintenance_message
    global first_boot
    maint_run = True
    clear_screen()
    while maint_run:
        print("\n---MAINTENANCE MENU---")
        print("1 - SHUT DOWN PROGRAM")
        print("2 - VIEW LOGS")
        print("3 - ADD LOG")
        print("4 - INBOX")
        print("5 - VIEW SUBLOGS")
        print("6 - ADD SUBLOG")
        print("7 - WIPE LOGS")
        print("8 - WIPE SUBLOGS")
        print("9 - CHANGE PASSWORD")
        print("10 - LOCKOUT AND EXIT")
        print("11 - OPEN COMMAND PORTAL")
        print("12 - DIRECT MESSAGES")
        print("13 - QUIT")
        if message_error == True:
            print("ERROR: YOUR MESSAGE IN LOG FAILED TO SEND")
        else:
            print(">")
        maint_choice = input("SELECT HOW TO PROCEED: ")
        if maint_choice == "1":
            yes_or_no = input("WARNING - SHUTTING DOWN PROGRAM WILL CAUSE ALL LOG DATA SINCE LAST SAVE TO BE WIPED AND WILL TERMINATE PROGRAM FOR ALL USERS, CAUSING BIOS TO NEED TO REBOOT. DO YOU WISH TO CONTINUE y/N?: ")
            if yes_or_no == "y":
                print("SHUTTING DOWN")
                maint_run = False
                sublog.append(f"{timestamp()} MAINTENANCE SHUTS DOWN PROGRAM}")
                exit()
            elif yes_or_no == "N":
                print("CANCELLING...")
                time.sleep(2)
                clear_screen()
            else:
                print("INVALID RESPONSE - TRY AGAIN")
                go_back()
                
        elif maint_choice == "2":
            view_logs()
            sublog.append(f"{timestamp()} MAINTENANCE TEAM VIEWS LOGS")
        elif maint_choice == "3":
            add_log()
            sublog.append(f"{timestamp()} MAINTENANCE TEAM ADDS LOG")
        elif maint_choice == "4":
            print("YOU HAVE ", maintenance_message, "MESSAGES")
            if maintenance_message > 0:
                print("CHECK LOGS FOR <Q>")
                maintenance_message = 0
                go_back()
                
            else:
                print("INBOX EMPTY")
                go_back()
                
        elif maint_choice =="5":
            clear_screen()
            if len(sublog) == 0:
                    print("SUBLOGS EMPTY")
                    go_back()
            else:
                print("\n----SUBLOG FILE----")
                for i, entry in enumerate(sublog, start=1):
                    print(f"{i} - {entry}")
                go_back()
                
        elif maint_choice == "6":
            newsublog = input("INPUT LOG TO APPEND HERE: ")
            sublog.append(f"{timestamp()} " + newsublog)
            print("SUBLOG ADDED")
            sublog.append(f"{timestamp()} MAINTENANCE TEAM ADDS SUBLOG")
            go_back()
            
        elif maint_choice == "7":
            logs.clear()
            print("LOGS EMPTIED")
            sublog.append(f"{timestamp()} MAINTENANCE TEAM CLEARS LOGS")
            go_back()
            
        elif maint_choice == "8":
            sublog.clear()
            print("SUBLOGS EMPTIED")
            sublog.append(f"{timestamp()} MAINTENANCE TEAM CLEARS SUBLOGS")
            go_back()
            
        elif maint_choice == "9":
            new_password = input("ENTER NEW PASSWORD HERE: ")
            other_new_password = input("RETYPE PASSWORD HERE: ")
            if new_password == other_new_password:
                password = new_password
                print("PASSWORD UPDATED SUCCESSFULLY")
                sublog.append(f"{timestamp()} MAINTENANCE TEAM UPDATE PASSWORD")
                go_back()
                
            else:
                print("PASSWORDS DO NOT MATCH, TRY AGAIN")
                go_back()
                
        elif maint_choice == "10": #jesus there's a lot of choices for a maintainence guy
            password = "aesdxcfvgl;kjghtfoiuy7gfvbiehfwury983yr09poi]jwhdu3hru';.;poikj,3.;'[pol,k.;[qp0owikjm,edlpoikujhnm,.l;'[pod9i23,kl.e;p0ol"
            #you just had to do it again didn't you
            print("ACCESS LOCKED - LOGGING OUT")
            time.sleep(2)
            maint_run = False
            clear_screen()
            
        elif maint_choice == "11":
            print("ACCESSING COMMAND PORTAL", end="", flush=True)

            for i in range(3):
                time.sleep(1)
                print(".", end="", flush=True)
            
            print("COMMAND PORTAL ACCESSED")
            time.sleep(2)
            clear_screen()
            command_portal()
        elif maint_choice == "12":
            maint_direct_messages()
        elif maint_choice == "13":
            print("LOGGING OUT")
            sublog.append(f"{timestamp()} MAINTENANCE TEAM LOGS OUT")
            maint_run = False
            first_boot = False
            clear_screen()
        elif maint_choice == "BIOS":
            bios()
            sublog.append(f"{timestamp()} MAINTENANCE TEAM OPENS BIOS")
        else:
            print("INVALID OPTION - TRY AGAIN")
            go_back()
            
#---HACKER MENU---
            #why do we even have this
            #isnt this a major security breach
            #or is it just a cheap party trick for admins because really this is just a complicated admin logon
def hack_in_menu():
    global counter
    global counter_2
    print("ACCESSING BACK_DOOR", end="", flush=True)
    sublog.append(f"{timestamp()} UNKNOWN USER ACCESSING BACKDOOR ENTRANCE")
    for i in range(3):
        time.sleep(1)
        print(".", end="", flush=True)
    time.sleep(1)
    print("\nERROR - UNRECOGNISED USER")
    time.sleep(3)
    clear_screen()
    logs.append(f"{timestamp()} UNAUTHORISED USER LOGON - UNRECOGNISED TERMINAL ACCESS")
    sublog.append(f"{timestamp()} UNAUTHORISED USER LOGGING ON - LOCKOUT SEQUENCE INITIATED")
    time.sleep(1)
    print("ten SECONDS TO LOCKOUT", end = "\r")
    time.sleep(1)
    print("nine SECONDS TO LOCKOUT", end = "\r")
    time.sleep(1)
    print("eight SECONDS TO LOCKOUT", end = "\r")
    time.sleep(1)
    print("seven SECONDS TO LOCKOUT", end = "\r")
    time.sleep(1)
    print("six SECONDS TO LOCKOUT     ", end = "\r")
    time.sleep(1)
    print("five SECONDS TO LOCKOUT    ", end = "\r")
    time.sleep(1)
    print("four SECONDS TO LOCKOUT     ", end = "\r")
    time.sleep(1)
    print("three SECONDS TO LOCKOUT     ", end = "\r")
    time.sleep(1)
    print("two SECONDS TO LOCKOUT     ", end = "\r")
    time.sleep(1)
    print("one SECONDS TO LOCKOUT     ", end = "\r")
    time.sleep(1)
    final_block = input("ENTER TERMINAL KEY NOW OR SUSPEND ACCESS: ")
    if final_block == "Lockout_Block - do<try$% enter > *^Use^* string; -{ administrator }- @Root":
        sublog.append(f"{timestamp()} TERMINAL KEY INPUTTED - LOCKOUT SEQUENCE SHUT DOWN - USER STILL UNRECOGNISED")
        print("FIREWALL BREACH - SECURITY DECRYPTION")
        sublog.append(f"{timestamp()} FIREWALL BREACHED, SECURITY CODE BEING DECRYPTED")
        print("░░░░░░░░░░", counter,"% DECRYPT", end = "\r")
        for i in range (11):
            time.sleep(1)
            counter = counter + 10
            counter_2 = counter_2 + 1
            if counter_2 == 1:
                print("▓░░░░░░░░░", counter,"%", end = "\r")
            elif counter_2 == 2:
                counter_3 = counter - 3
                print("▓▒░░░░░░░░", counter_3,"%", end = "\r")
            elif counter_2 == 3:
                counter_4 = counter + 6
                time.sleep(0.4)
                print("▓▓▓▒░░░░░░", counter_4,"%", end = "\r")
            elif counter_2 == 4:
                counter_5 = counter +9
                time.sleep(0.9)
                print("▓▓▓▓▒░░░░░", counter_5,"%", end = "\r")
            elif counter_2 == 5:
                counter_6 = counter+6
                time.sleep(0.6)
                print("▓▓▓▓▓▒░░░░", counter_6,"%", end = "\r")
            elif counter_2 == 6:
                counter_7 = counter + 3
                print("▓▓▓▓▓▓▒░░░", counter_7,"%", end = "\r")
            elif counter_2 == 7:
                counter_8 = counter - 1
                print("▓▓▓▓▓▓▒░░░", counter_8,"%", end = "\r")
            elif counter_2 == 8:
                counter_9 = counter - 2
                print("▓▓▓▓▓▓▓▒░░", counter,"%", end = "\r")
            elif counter_2 == 9:
                counter_10 = counter + 5
                time.sleep(0.5)
                print("▓▓▓▓▓▓▓▓▓▒", counter_10,"%", end = "\r")
            elif counter_2 == 10:
                counter_11 = counter - 1
                print("▓▓▓▓▓▓▓▓▓▒", counter_11,"%", end = "\r")
            elif counter_2 == 11:
                counter_12 = counter - 10
                time.sleep(3)
                print("▓▓▓▓▓▓▓▓▓▓", counter_12,"% ", end = "\r")
                counter = 0
                counter_2 = 0
        time.sleep(0.5)
        print("FIREWALL BREACHED!!!  ")
        sublog.append(f"{timestamp()} FIREWALL BREACHED, SECURITY PROTOCOLS DECRYPTED, TAKING 'DRASTIC MEASURES'")
        time.sleep(1)
        print("User_Terminal Access CHANGE $%Unfamiliar$% ----------> $%Admin$%")
        time.sleep(2)
        print("Terminal_Change_PROGRESS - SUCCESSFUL ☺")
        sublog.append(f"{timestamp()} UNAUTHORISED TERMINAL RECOGNISED ADMIN, INCORRECT SERVER LOGON CODE, SUSPECT TERMINAL KEY CHANGE, ACTIVATING 'DRASTIC MEASURE' DDoS ATTACK ON TERMINAL")
        logs.append(f"{timestamp()} UNAUTHORISED TERMINAL DDoS ATTEMPTED")
        time.sleep(1)
        print("User_Terminal DDoS Request BLOCKED --- *%^ User -> System_IDENT")
        sublog.append(f"{timestamp()} DDoS UNSUCCESSFUL")
        time.sleep(6)
        print("User_Terminal System_IDENT SUCCESSFUL -> IDENT Admin SYSTEM Logon 'Admin'")
        sublog.append(f"{timestamp()} SYSTEM IDENTIFIED AS ADMIN< AWAITING SERVER KEY")
        logs.append(f"{timestamp()} ADMIN LOGGED ON")
        sublog.append(f"{timestamp()} USER RECOGNISED AS ADMIN, KEY ACCEPTED - ADMIN LOGS ON")
        tempinput = input("ADMIN enter passcode -> Back_Door : ")
        if tempinput == "Admin":
            print("WELCOME ADMINISTRATOR")
            time.sleep(3)
            clear_screen()
            admin_menu()
        else:
            while tempinput != "Admin":
                print("TRY AGAIN ADMIN PASSWORD NOT RECOGNISED")
                tempinput = input("ADMIN enter passcode -> Back_Door : ")
            
            clear_screen()
            admin_menu()
                
    else:
        print("USER NOT RECOGNISED - LOCKING SYSTEM")
        sublog.append(f"{timestamp()} UNAUTHORISED USER BLOCKED FROM SYSTEM SUCCESSFULLY")
            
#---MAIN MENU---
            #it's all a lie
            #there is no BIOS
            #i should probably seperate some stuff
            
def open_menu():
    global access
    global first_boot
    sublog.append(f"{timestamp()} " + "MAINFRAME OPENED")
    #right here i go
    #seperating
    #again
    #lucky lucky me
    #here's the first boot if
    clear_screen()
    if first_boot == True:
        print("LOADING BIOS...")
        time.sleep(3)
        print("BIOS LOAD SUCCESSFUL!")
        time.sleep(1)
        print("BOOTING TERMINAL MAINFRAME LOGIN PORTAL")
        time.sleep(5)
        print("BOOT SUCCESSFUL!")
        time.sleep(3)
        clear_screen()
        print("\n----MAINFRAME----")
        print("ENTER PASSWORD TO LOGIN")
        first_boot = False
    #and here's the else
    #tada
    #proud of me yet?
    else:
        time.sleep(1)
        print("\n----MAINFRAME----")
        print("ENTER PASSWORD TO LOGIN")
    
    user_code = input("> ")
    
    #normal user logon:
    
    if user_code == password:
        print("Access Granted - enter Main Menu")
        sublog.append(f"{timestamp()} " + "USER LOGS ON")
        access = 1
    
    #admin logon
        
    elif user_code == "Admin":
        sublog.append(f"{timestamp()} " + "ADMIN LOGS ON")
        print("ACCESSING ADMIN PORTAL", end="", flush=True)

        for i in range(3):
            time.sleep(1)
            print(".", end="", flush=True)

        print("\nADMIN PORTAL ACCESSED")
        time.sleep(1)
        print("WELCOME ADMINISTRATOR")
        admin_menu()
        
    #maintenance logon
    #again, not even a single bit of seperation. really? have a heart for us poor maintainers
        
    elif user_code == "Maintenance Logon":
        sublog.append(f"{timestamp()} " + "MAINTENANCE TEAM LOGS ON")
        print("ACCESSING MAINTENANCE PORTAL", end="", flush=True)

        for i in range(3):
            time.sleep(1)
            print(".", end="", flush=True)

        print("\nMAINTENANCE PORTAL ACCESSED")
        time.sleep(1)
        print("WELCOME CODE ENGINEER")
        time.sleep(5)
        clear_screen()
        maintenance_menu()
        
    #owner logon
    #jeez, the owner too? not even a blank line? I'll have that sorted
        
    elif user_code == "owner logon i own it":
        sublog.append(f"{timestamp()} " + "OWNER LOGS ON")
        time.sleep(1)
        print("WELCOME OWNER")
        time.sleep(2)
        owner_menu()
        
    #hacker logon
    #now why oh why do i have this
    #this could probably be a function
    #it is now!
    
    elif user_code == "BreakIn - back_door = True %$hack$% add enter TRY: AllPassCode -{Digitize} plus <,ATTEMPT_,>":
        hack_in_menu()
        
    else:
        print("PASSWORD INCORRECT - TRY AGAIN")
        sublog.append(f"{timestamp()} " + "INCORRECT PASSWORD ATTEMPTED")
        return False

#---USER MENU---
    #why is it the user menu and not the main menu?
    #right, because open_menu() is the main menu
    #i dont see why that's just silly
    
def secondary_menu():
    clear_screen()
    print("\n----MENU----")
    print("PRESS 1 TO VIEW LOGS")
    print("PRESS 2 TO ADD LOGS")
    print("PRESS 3 FOR HELP")
    print("PRESS 4 FOR INBOX")
    print("PRESS 5 FOR DIRECT MESSAGES")
    print("PRESS 6 TO QUIT")
    if message_error == True:
        print("ERROR: YOUR MESSAGE IN LOG FAILED TO SEND")
    else:
        print(">")
    global choice
    choice = input("SELECT HOW TO PROCEED: ")
    print("------------\n")
    what_next()

def what_next():
    global choice
    global access
    global user_message
    global first_boot
    if choice == "1":
        view_logs()
        sublog.append(f"{timestamp()} " + "USER VIEWS LOGS")

    elif choice == "2":
        add_log()
        sublog.append(f"{timestamp()} " + "USER ADDS LOG")
        
    elif choice == "3":
        help_menu()
        
    elif choice == "4":
        print("YOU HAVE ",user_message,"MESSAGE(S)")
        if user_message > 0:
            print("CHECK LOGS FOR <Q>")
            user_message = 0
            go_back()
        else:
            print("INBOX EMPTY")
            go_back()
    elif choice == "5":
        user_direct_messages()
        
    elif choice == "6":
        print("LOGGING OUT")
        sublog.append(f"{timestamp()} USER LOGS OUT")
        access = 0
        first_boot = False
        
    elif choice == "447260103":
        print("LOGS CLEARED")
        logs.clear()
        sublog.append(f"{timestamp()} USER CLEARS LOGS")
        go_back()
        
    elif choice == "Change Passcode Authorisation Alpha Theta Delta 6":
        global password
        password = input("WHAT WOULD YOU LIKE TO CHANGE YOUR PASSWORD TO?: ")
        sublog.append(f"{timestamp()} USER CHANGES PASSWORD")
        go_back()
        
    elif choice == "BIOS":
        bios()
        sublog.append(f"{timestamp()} USER OPENS BIOS")
    else:
        print("INVALID OPTION")
        go_back()
#---VIEW LOGS---
        #just a shortcut really
        
def view_logs():
    clear_screen()
    if len(logs) == 0:
        print("LOGS EMPTY")
        go_back()
    else:
        print("\n----LOG FILE----")
        for i, entry in enumerate(logs, start=1):
            print(f"{i} - {entry}")
        go_back()

#---ADD LOG---
            #another just shortcut
            
def add_log():
    global message
    global user_message
    global admin_message
    global maintenance_message
    global owner_message
    global message_error
    #got enough globals?
    send_message = False
    log = input("ENTER LOG HERE: ")
    if "<Q>" in log:
        send_message = True
        if "Admin" in log:
            logs.append((f"{timestamp()} " + log))
            print("LOG ADDED")
            admin_message = admin_message + 1
            sublog.append(f"{timestamp()} ADMIN MESSAGE PINGED")
        elif "User" in log:
            logs.append((f"{timestamp()} " + log))
            print("LOG ADDED")
            user_message = user_message + 1
            sublog.append(f"{timestamp()} USER MESSAGE PINGED")
        elif "Maintenance" in log:
            logs.append((f"{timestamp()} " + log))
            print("LOG ADDED")
            maintenance_message = maintenance_message + 1
            sublog.append(f"{timestamp()} MAINTENANCE MESSAGE PINGED")
        elif "Owner" in log:
            logs.append((f"{timestamp()} " + log))
            print("LOG ADDED")
            owner_message = owner_message + 1
            sublog.append(f"{timestamp()} " + "OWNER MESSAGE PINGED")
        else:
            message_error = True
    elif "<CQ>" in log:
        logs.append((f"{timestamp()} " + log))
        print("LOG ADDED")
        send_message = True
        user_message = user_message + 1
        admin_message = admin_message + 1
        maintenance_message = maintenance_message + 1
        owner_message = owner_message + 1
        sublog.append(f"{timestamp()} ALL MESSAGE PINGED")
    else:
        logs.append((f"{timestamp()} " + log))
        print("LOG ADDED")
    go_back()

def bios():
    global first_boot
    global system_fail
    global is_critical
    global needs_maintenance
    global base_online
    global maintenance_soon
    global system_nominal
    global access
    global admin_run
    global maint_run
    global owner_run
    global version
    #evidently not
    clear_screen()
    bios_run = True
    while bios_run:
        print("\n----BASIC INPUT OUTPUT SYSTEM----")
        print("SYSTEM ONLINE")
        print(f"IS_FIRST_BOOT = {first_boot}")
        print("1 - RUN SYSTEM TEST")
        print("2 - RESTART BIOS")
        print("3 - UPDATE SYSTEM VERSION")
        print("4 - QUIT")
        bios_choice = input("SELECT HOW TO PROCEED: ")
    
        if bios_choice == "1":
            line_length = 50
            sublog.append(f"{timestamp()} SYSTEM BIOS TEST RUN")
            print("INITIATING SYSTEM TEST...")
            time.sleep(2)
            print("SYSTEM TEST READY")
            time.sleep(1)
            print("RUNNING SYSTEM TEST", end = "\r")
            time.sleep(1)
            print("RUNNING SYSTEM TEST.", end = "\r")
            time.sleep(1)
            print("RUNNING SYSTEM TEST..", end = "\r")
            time.sleep(1)
            print("RUNNING SYSTEM TEST...", end = "\r")
            time.sleep(1)
            print("RUNNING SYSTEM TEST   ", end = "\r")
            time.sleep(1)
            print("RUNNING SYSTEM TEST.", end = "\r")
            time.sleep(1)
            print("RUNNING SYSTEM TEST..", end = "\r")
            time.sleep(1)
            print("RUNNING SYSTEM TEST...", end = "\r")
            time.sleep(1)
            print("RUNNING SYSTEM TEST   ", end = "\r")
            time.sleep(1)
            print("RUNNING SYSTEM TEST.", end = "\r")
            time.sleep(1)
            print("RUNNING SYSTEM TEST..", end = "\r")
            time.sleep(1)
            print("RUNNING SYSTEM TEST...")
            if system_fail == True:
                print("CRITICAL SYSTEM FAILURE")
                print("RESTART BIOS IMMEDIATELY")
                go_back()
            elif is_critical == True:
                print("SYSTEM CRITICAL")
                print("IMMEDIATE MAINTENANCE NEEDED")
                go_back()
            elif needs_maintenance == True:
                print("SYSTEM REQUIRES MAINTENANCE")
                print("CONTACT MAINTENANCE TO CLOSE SERVER")
                go_back()
            elif base_online == True:
                print("SYSTEM BASE FUNCTIONS ONLINE")
                print("DEBUG CODE SOON")
                go_back()
            elif maintenance_soon == True:
                print("SYSTEM REQUIRES MAINTENANCE SOON")
                print("DEBUG NEEDED IN  6  DAYS")
                go_back()
            elif system_nominal:
                print("SYSTEM NOMINAL")
                print("ALL FUNCTIONS NORMAL")
                go_back()
            else:
                num = random.randint(0,100)
                if num == 0:
                    print("CRITICAL SYSTEM FAILURE")
                    print("RESTART BIOS IMMEDIATELY")
                    system_fail = True
                    go_back()
                elif num >= 1 and num < 10:
                    print("SYSTEM CRITICAL")
                    print("IMMEDIATE MAINTENANCE NEEDED")
                    is_critical = True
                    go_back()
                elif num >= 11 and num < 25:
                    print("SYSTEM REQUIRES MAINTENANCE")
                    print("CONTACT MAINTENANCE TO CLOSE SERVER")
                    needs_maintenance = True
                    go_back()
                elif num >= 26 and num < 50:
                    print("SYSTEM BASE FUNCTIONS ONLINE")
                    print("DEBUG CODE SOON")
                    base_online = True
                    go_back()
                elif num >= 51 and num < 70:
                    print("SYSTEM REQUIRES MAINTENANCE SOON")
                    print("DEBUG NEEDED IN  6  DAYS")
                    maintenance_soon = True
                    go_back()
                else:
                    print("SYSTEM NOMINAL")
                    print("ALL FUNCTIONS NORMAL")
                    system_nominal = True
                    go_back()
        
        elif bios_choice == "2":
            cont = input("WARNING - CONTINUING WILL RESTART INTERNAL BIOS, SHUT DOWN BACKEND AND LOG OUT ALL USERS. DO YOU WISH TO CONTINUE y/N?: ")
            if cont == "y" or cont == "Y":
                sublog.append(f"{timestamp()} BIOS RESTARTED")
                print("RESTARTING BIOS...")
                time.sleep(2)
                bios_run = False
                access = 0
                admin_run = False
                maint_run = False
                owner_run = False
                first_boot = False
                clear_screen()
                print("LOADING BIOS...")
                time.sleep(3)
                print("BIOS LOAD SUCCESSFUL!")
                time.sleep(1)
                print("BOOTING TERMINAL MAINFRAME LOGIN PORTAL")
                time.sleep(5)
                print("BOOT SUCCESSFUL!")
                time.sleep(3)
                clear_screen()
                
            elif cont == "n" or cont == "N":
                print("CANCELLING...")
                time.sleep(2)
                clear_screen()
            else:
                print("INVALID INPUT")
                go_back()
                
        elif bios_choice == "3":
            try:
                version = float(input("WHAT IS THE NEW VERSION NUMBER?: "))
                sublog.append(f"{timestamp()} VERSION UPDATED")
                go_back()
                
            except ValueError:
                print("INVALID CHOICE")
                go_back()
                
        elif bios_choice == "4":
            print("EXITING...")
            time.sleep(2)  
            clear_screen()
            bios_run = False
            
        else:
            print("INVALID INPUT - TRY AGAIN")
            go_back()
            
#-THE THING YOU MUST NEVER TOUCH-
        #just leave it alone, please
        #THIS is the entire code sequence --------------------------------------------------¬
        #literally everything else is just functions                                        |
        #this is the only non def or declaration code here                                  |
        #so this really boils down to the shoulders of one while loop? wow. loops upon loops|
        #   ┌-------------------------------------------------------------------------------┘
        #  \|/
        #   V
        
while run:
    if access == 1:
        secondary_menu()
    else:
        open_menu()
#1568 lines is 1567 too many. all i need is print("Hello world!") and i'm satisfied.  