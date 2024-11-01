# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 12:41:40 2024

@author: kayla

This is the program that actually runs the progress tracker
"""

class UserNotFoundError(Exception): pass
class NumberNotListed(Exception): pass
class EmailError(Exception): pass

from sqlalchemy import create_engine
from sqlalchemy import text
from sqlalchemy.orm import Session, DeclarativeBase


engine = create_engine("mysql+pymysql://root:root@localhost/progress_tracker")

class Base(DeclarativeBase): pass

Base.metadata.reflect(bind=engine)

with Session(engine) as session:
    
    def start():
        print("Hello! Welcome to your progress tracker! Sign up or log in!")
        print("1 - Log in\n2 - Sign up")
        while (True):
            try:
                choice = int(input())
                if (choice < 1) or (choice > 2): raise NumberNotListed("invalid input")
                
                if choice == 1: user_id = login()
                if choice == 2: user_id = create_account()
                menu(user_id)
                break
            except NumberNotListed:
                print("Please enter a value between 1 and 2")
            except Exception as e:
                print(f"Please enter a number\nOr remedy this error, {e}")
        return user_id

    def login():
        #Function for handling logging in
        username = input("Please enter your username: ").lower()
        password = input("Please enter your password: ") 
        try:
            stmt = text(f"SELECT users_id FROM users WHERE email = '{username}' AND password = '{password}'")
            
            ans = session.execute(stmt)
            results = ans.fetchone()
            if(not results): raise UserNotFoundError("Account not found")
            user_id = results[0]
            return user_id
            
        except UserNotFoundError:
            print("Your username or password is not correct")
            user_id = start()
                     
    def create_account():
        #Function for creating an account
        while(True):
            try:
                username = input("Please enter your username: ").lower()
                stmt = text(f"SELECT users_id FROM users WHERE email = '{username}'")
                ans = session.execute(stmt)
                results = ans.fetchone()
                if(results): raise EmailError("Account has been found")
                password = input("Please enter your password: ") 
                
                session.execute(text(f"INSERT INTO users (email, password) VALUES('{username}', '{password}')"))
                session.commit()
                
                stmt = text(f"SELECT users_id FROM users WHERE email = '{username}'")
                
                ans = session.execute(stmt)
                results = ans.fetchone()
                user_id = results[0]
                return user_id
            except EmailError:
                print("You already registered with this Email")
                      
    def user_info(user_id):
        #Function for letting the user update their information
        while (True):
            stmt = text(f"SELECT email, password from users WHERE users_id = {user_id}")
            ans = session.execute(stmt)
            result = ans.fetchall()
            print(result)
            
            print("Update email and/or password")
            print("\n1 - Change email\n2 - Change password\n3 - Delete account\n4 - Return to menu")
            try:
                choice = int(input())
                if(choice < 1 or choice > 4): raise NumberNotListed("Invalid input")
            except NumberNotListed:
                print("Please enter a value between 1 and 4")
            except Exception as e:
                print(f"Please enter a number\nOr remedy this error, {e}")
            if(choice == 1):
                #Update email address
                new_email = input("Enter new email here ").lower()
                session.execute(text(f"UPDATE users SET email = '{new_email}' WHERE users_id = {user_id}"))
                session.commit()
            if(choice == 2):
                #Change password
                new_password = input("Enter new password here: ")            
                session.execute(text(f"UPDATE users SET password = '{new_password}' WHERE users_id = {user_id}"))
                session.commit()
                
            if(choice == 3):
                #Delete account
                session.execute(text(f"DELETE FROM user_list WHERE users_id = {user_id}"))
                session.execute(text(f"DELETE FROM users WHERE users_id = {user_id}"))
                print("Deleted data!")
                session.commit()
                user_id = start()
                break
            
            if(choice == 4):
                #Return to menu
                menu(user_id)
                break
            
    def get_list(user_id):
        #Function for updating personal list_id
        list_stmt = text(f"SELECT max(list_id) from user_list WHERE users_id = {user_id}")
        ans = session.execute(list_stmt)
        list_length = ans.fetchall()
        
        if list_length[0][0] == None: return 0
        return list_length[0][0]
        
    def menu(user_id):
        #Basically the starting menu
        print("\n1 - View complete list of anime\n2 - View/Update personal anime list\n3 - Log out/switch users \n4 - Update information\n5 - Quit program")
        while(True):
            try:
                choice = int(input())
                if(choice < 1 or choice > 5): raise NumberNotListed("Invalid input")
            except NumberNotListed:
                print("Please enter a value between 1 and 4")
            except Exception as e:
                print(f"Please enter a valid number, {e}")
            if(choice == 1):
                anime_list()
                break
            if(choice == 2):
                users_list(user_id)
                break
            if(choice == 3):
                user_id = 0
                user_id = start()
                break
            if(choice == 4):
                user_info(user_id)
                break
            if(choice == 5):
                return
                break
    
    def anime_list():
        #Function for displaying the anime ist
        print("You chose to view all anime.")  
            
        stmt = text(f"SELECT anime.anime_id, title, english_title, synopsis, genre, media, episodes, studio, origin, rating, season, release_year FROM anime_list as al INNER JOIN anime ON al.anime_id = anime.anime_id INNER JOIN genre ON al.genre_id = genre.genre_id INNER JOIN studio ON al.studio_id = studio.studio_id INNER JOIN origin ON al.origin_id = origin.origin_id INNER JOIN rating ON al.rating_id = rating.rating_id INNER JOIN season ON al.season_id = season.season_id INNER JOIN media ON al.media_id = media.media_id INNER JOIN release_year ON al.release_year_id = release_year.release_year_id")
        order_by = text("ORDER BY anime.anime_id asc")
        fullstmt = text(str(stmt) + " " + str(order_by))
        ans = session.execute(fullstmt)
        results = ans.fetchall()
        id_list = len(results)
        i = 0
        j = 10
        
        while(True):
            
            if len(results) < 10: j = len(results)
            print(f"\n1 - Add anime to list\n2 - See next 10 anime\n3 - See previous 10 anime\n4 - Filter list\n5 - Return to menu")
            
            print("anime_id\ttitle\tenglish\ttitle\tsynopsis\tgenre\tmedia\tepisodes\tstudio\torigin\trating\tseason\treleaseyear")
            for k in range(i,j):
                print(results[k])
                
            try:
                choice = int(input("Choose here: "))
                if (choice < 1) or (choice > 5): raise NumberNotListed("Number out of range")
            except NumberNotListed:
                print("Please enter a value between 1 and 5")
            except Exception as e:
                print(f"Please enter a number\nOr remedy this error, {e}")
                
            #Adding an anime to your list
            if(choice == 1):
                while(True):
                    try:
                        anime = int(input("Please enter the id of the anime you wish to add: "))
                        if(anime < 1) or (anime > id_list): raise NumberNotListed("Number out of range")
                        list_length = get_list(user_id)
                        
                        session.execute(text(f"INSERT INTO user_list (users_id, anime_id, list_id) VALUES ({user_id}, {anime}, {list_length+1})"))
                        session.commit()
                        print("Successfully added the anime!")
                        break
                        
                    except NumberNotListed:
                        print(f"Not valid id, id should be between 1 and {len(results)}")
                    except Exception as e:
                        print(f"Please enter a number\nOr remedy this error, {e}")
                
            #Loop forward through anime list
            if(choice == 2):
                if(j - i < 10): 
                    print("Restarting list")
                    i = -10
                i = i + 10
                j = i + 10
                if(j > len(results)): j = len(results)
                
            #Loop backwards throught anime list
            if(choice == 3):
                if(i == 0): 
                    print("Cannot scroll back")
                else:
                    j = i
                    i = i - 10
                
            #Filter anime based on criteris
            if(choice == 4):
                while(True):
                    try:
                        print("Please choose a filtering option")
                        print("\n1 - Genres\n2 - Studios\n3 - Rating\n4 - Season\n5 - Year\n6 - Origin\n7 - Watched\n8 - Title\n")
                        filt = int(input())
                        if (filt < 1) or (filt > 8): raise NumberNotListed("Number out of range")
                    except NumberNotListed:
                        print("Please enter a value between 1 and 4")
                    except Exception as e:
                        print(f"Please enter a number\nOr remedy this error, {e}")
                        
                    options = {1:"genre", 2:"studio", 3:"rating",4:"season",5:"release_year",6:"origin", 7:"watched", 8:"title"}
        
                    print(f"You chose {options[filt]}")
                    #These options are rather simple, so they are grouped together.
                    if(filt < 7):
                        while(True):
                            try:
                                filt_stmt = text(f"SELECT * FROM {options[filt]}")
                                ans = session.execute(filt_stmt)
                                res = ans.fetchall()
                                for r in res:
                                    print(r)
                                
                                filt_more = int(input("Please choose a filter option by typing the id: "))
                                if (filt_more < 1) or (filt_more > len(res)): raise NumberNotListed("Number out of range")
                                stmt_two = text(f"WHERE {options[filt]}.{options[filt]}_id = {filt_more}")
                                search_stmt = text(str(stmt) + " " + str(stmt_two) + " " + str(order_by))
                                ans = session.execute(search_stmt)
                                results = ans.fetchall()
                                break
                            except NumberNotListed:
                                print(f"Please enter a value between 1 and {len(res)}")
                            except Exception as e:
                                print(f"Please enter a number\nOr remedy this error, {e}")
                        break
                    else:
                        #Removing shows that are in your watch list
                        if(filt == 7): 
                            print("Now displaying all shows that are not in your watch list")
                            stmt_two = text(f"WHERE anime.anime_id NOT in (SELECT anime_id from user_list where users_id = {user_id})")
                            search_stmt = text(str(stmt) + " " + str(stmt_two) + " " + str(order_by))
                            ans = session.execute(search_stmt)
                            results = ans.fetchall()
                            break
                        #Allowing you to search based on Text
                        if(filt == 8):
                            filt_more = input("Please input the phrase you're looking for (Note, we search both titles): ")
                            stmt_two = text(f"WHERE english_title LIKE '%{filt_more}%' OR title LIKE '%{filt_more}%'")
                            search_stmt = text(str(stmt) + " " + str(stmt_two) + " " + str(order_by))
                            ans = session.execute(search_stmt)
                            results = ans.fetchall()
                            break
            #Quit    
            if(choice == 5):
                menu(user_id)
                break
        
    def users_list(user_id):
        #Displaying your personal list
        print("Here is your personal list")
        stmt = text(f"SELECT anime.anime_id, list_id, title, english_title, episodes, watch_status, progress FROM anime INNER JOIN user_list ON anime.anime_id = user_list.anime_id INNER JOIN users ON users.users_id = user_list.users_id WHERE users.users_id = {user_id}")
        ans = session.execute(stmt)
        tot_ans = session.execute(stmt)
        user_results = ans.fetchall()
        total_results = tot_ans.fetchall()
        i = 10
        list_id = len(user_results)
             
        
        while(True):
            statuses = {1: "Plan to watch", 2:"In-Progress", 3:"Completed", 4:"Dropped"}
        
        #Pulls up your personal list, and lets you change the status/update watch amount 
            print("Please choose an option")
            print("\n1 - Update status\n2 - Update progress\n3 - Filter List\n4 - Return to menu")
            print("anime_id\tlist_id\ttitle\tenglish title\tepisodes\twatch status\tprogress in (%)")
            if list_id < 10 : i = list_id  
            for k in range(0,i):
                print(user_results[k])
                
            try:        
                choice = int(input())
                if(choice < 1) or (choice > 4): raise NumberNotListed("invalid input")
            except NumberNotListed:
                print("Please enter a value between 1 and 4")
            except Exception as e:
                print(f"Please enter a number\nOr remedy this error, {e}")
            
            #Update the status of your show    
            if(choice == 1):
                try:
                   
                    print("Choose an entry based on the list id")
                    entry_id = int(input())
                    if(entry_id > list_id) or (entry_id < 0): raise NumberNotListed("entry_id not in list")
                except NumberNotListed:
                    print(f"Please enter a value between 1 and {list_id}")
                except Exception as e:
                    print(f"Please enter a number\nOr remedy this error, {e}")
                    
                try:
                    print("To update it's status, please choose an option from the list:\n1 - Plan to watch\n2 - In-Progress\n3 - Completed\n4 - Dropped")
                    status_id = int(input())
                    if(status_id < 1) or (status_id > 4): raise NumberNotListed("invalid input")
                    update_stmt = text(f"UPDATE user_list SET watch_status = '{statuses[status_id]}' WHERE list_id = {entry_id} and users_id = {user_id}")
                    ans = session.execute(update_stmt)
                    session.commit()
                    if(status_id == 3):
                        update_stmt = text(f"UPDATE user_list SET progress = 100 WHERE list_id = {entry_id} and users_id = {user_id}")
                        ans = session.execute(update_stmt)
                        session.commit()
                    print("Successfully updated!")
                except NumberNotListed:
                    print("Please enter a value between 1 and 4")
                except Exception as e:
                    print(f"Please enter a number\nOr remedy this error, {e}")
                
                ans = session.execute(stmt)
                user_results = ans.fetchall()
                i = 10
            
            #Update the the amount of episodes you watched    
            if(choice == 2):
                try: 
                    print("Choose an entry based on the list_id")
                    entry_id = int(input())
                    if(entry_id > list_id) or (entry_id < 1): raise NumberNotListed("entry_id not in list")
                
                    eps = int(input("Please update the amount of episodes you watched: "))
                    
                    total_eps = total_results[entry_id - 1][4]
                    if(eps < 0) or (eps > total_eps): raise NumberNotListed("Impossible amount of episodes")
                    progress = (eps / total_eps) * 100
                    update_stmt = text(f"UPDATE user_list SET progress = {progress} WHERE list_id = {entry_id} and users_id = {user_id}")
                    ans = session.execute(update_stmt)
                    session.commit()
                
                    ans = session.execute(stmt)
                    user_results = ans.fetchall() 
                    i = 10
                except NumberNotListed:
                    print(f"Please enter a value between 1 and {list_id}")
                except Exception as e:
                    print(f"Please enter a number\nOr remedy this error, {e}")
             
            #Filter your personal list based on status    
            if(choice == 3):
                try:
                    print("Please choose a status to filter as:\n1 - Plan to watch\n2 - In-Progress\n3 - Completed\n4 - Dropped")
                    status_id = int(input())
                    if(status_id < 1) or (status_id > 4): raise NumberNotListed("invalid input")
                    stmt_two = text(f"AND watch_status LIKE '%{statuses[status_id]}%'")
                    filt_stmt = text(str(stmt) + " " + str(stmt_two))
                    ans = session.execute(filt_stmt)
                    user_results = ans.fetchall()
                    i = len(user_results)
                except NumberNotListed:
                    print("Please enter a value between 1 and 4")
                except Exception as e:
                    print(f"Please enter a number\nOr remedy this error, {e}")
            
            if(choice == 4):
                menu(user_id)
                break
        
        
    #Logging in/Creating a new account
    user_id = start()
      

session.close()
print("Thank you for using the progress tracker!")
