# Progress Tracker Instructions

This is my Capstone project for Future Horizons September 23rd class.

It is a progress tracker that tracks anime you watched. You can add anime, update the watch status of your anime, and even get a progess percentage for level of completion. 

You can search through the anime database as well

### Downloading the files

The program assumes all files are in the same directory, so please place all files in the same directory. That includes all all .sql files, .py files, and .csv files

### Setting up the code

1. Run the Database_Create.sql script

The create script is optimized for MySQL. Though SQL languages aren't particularly different from one another, it works best as a mySQL script. Once you have it open on your mySQL IDE, run it, and it should create an empty database

2. Run the create_database.py script

There are two python files you need, data_cleaning.py, and create_database.py.
Data_Cleaning.py is imported by create_database.py, so you do not have to run Data_Cleaning.py.

In create_database you'll notice some code on line 19
` engine = create_engine("mysqlconnector://username:password@localhost/progress_tracker") `

Please update mysqlconnector to your sql connector, username to the username of your mysql document, and password to your password.

Once that's been updated, you can now run create_database. It should take a minute, but it will automatically run Data_Cleaning and populate the sql documents

### Using the progress tracker

Just like in create_database.py, progress tracker also requires you to update the engine. So please take care of that. 
The code runs in the terminal, so the display might be a bit clunky. 

1. Logging in
Once you press run you should be greeted with output that looks like this
```
Hello! Welcome to your progress tracker! Sign up or log in!
1 - Log in
2 - Sign up
```

If you want to log in, you can use any user in the users.csv. The fourth user has an empty account so you can mess with it if you like (email: mockuser@example.edu, password: badpassword). 
If not feel free to sign up.

2. The Main menu

Once you're in, you should be greeted by a menu

```
Now that you're all logged in, please choose what you wish to do

1 - View complete list of anime
2 - View/Update personal anime list
3 - Log out/switch users 
4 - Update information
5 - Quit program
```

Selecting (1) will show the list of anime, (2) will be the actual progress tracker, (3) allows you to switch users, and (4) will have you update information. (5) ends the program 

We will look at (1) below

3. Adding anime to your list

Choosing 1, should result in output like this

```
You chose to view all anime.

1 - Add anime to list
2 - See next 10 anime
3 - See previous 10 anime
4 - Filter list
5 - Return to menu
anime_id	title	english	title	synopsis	genre	media	episodes	studio	origin	rating	season	releaseyear
(1, 'Cowboy Bebop', 'Cowboy Bebop', "Crime is timeless. By the year 2071, humanity has expanded across the galaxy, filling the surface of other planets with settlements like those on Ear ... (710 characters truncated) ... Spike's past. As a rival's maniacal plot continues to unravel, Spike must choose between life with his newfound family or revenge for his old wounds.", 'Sci-Fi', 'TV', 26, 'Sunrise', 'Original', 'R', 'Spring', 1998)
(2, 'Trigun', 'Trigun', 'Vash the Stampede is the man with a $$60,000,000,000 bounty on his head. The reason: he\'s a merciless villain who lays waste to all those that oppos ... (712 characters truncated) ... summoned to bring about suffering to the trio. Vash\'s agonizing past will be unraveled and his morality and principles pushed to the breaking point.', 'Action', 'TV', 26, 'Madhouse', 'Manga', 'PG-13', 'Spring', 1998)
(3, 'Witch Hunter Robin', 'Witch Hunter Robin', "Robin Sena is a powerful craft user drafted into the STNJ—a group of specialized hunters that fight deadly beings known as Witches. Though her fire p ... (92 characters truncated) ...  partner, Amon. But the truth about the Witches and herself will leave Robin on an entirely new path that she never expected!\n\n(Source: Funimation)", 'Action', 'TV', 26, 'Sunrise', 'Original', 'PG-13', 'Summer', 2002)
(4, 'Bouken Ou Beet', 'Beet the Vandel Buster', "It is the dark century and the people are suffering under the rule of the devil, Vandel, who is able to manipulate monsters. The Vandel Busters are a ... (423 characters truncated) ... have passed since then and the young Vandel Buster, Beet, begins his adventure to carry out the Zenon Squad's will to put an end to the dark century.", 'Adventure', 'TV', 52, 'Toei Animation', 'Manga', 'PG', 'Fall', 2004)
(5, 'Eyeshield 21', 'Eyeshield 21', 'Shy, reserved, and small-statured, Deimon High School student Sena Kobayakawa is the perfect target for bullies. However, as a result of running erra ... (737 characters truncated) ... apon of the Deimon Devil Bats. As he interacts with his teammates, Sena gradually gains more self-confidence and forges valuable bonds along the way.', 'Sports', 'TV', 145, 'Gallop', 'Manga', 'PG-13', 'Spring', 2005)
(6, 'Hachimitsu to Clover', 'Honey and Clover', "Yuuta Takemoto, a sophomore at an arts college, shares a cheap apartment with two seniors—the eccentric Shinobu Morita, who keeps failing to graduate ... (553 characters truncated) ...  heartwarming tale of youth, love, soul-searching, and self-discovery, intricately woven through the complex relationships between five dear friends.", 'Comedy', 'TV', 24, 'J.C.Staff', 'Manga', 'PG-13', 'Spring', 2005)
(7, 'Hungry Heart: Wild Striker', 'Hungry Heart: Wild Striker', "As the younger brother of Japanese soccer star Seisuke Kanou, Kyousuke was always expected to grow as a soccer player at the same pace his brother di ... (504 characters truncated) ... remain steadfast in his decision to abandon the sport he once loved, or allow himself to reignite that flame to become the best striker in the world.", 'Comedy', 'TV', 52, 'Nippon Animation', 'Manga', 'PG-13', 'Fall', 2002)
(8, 'Initial D Fourth Stage', 'Initial D Fourth Stage', 'Takumi Fujiwara finally joins Ryousuke and Keisuke Takahashi to create "Project D." Their goal is twofold: Ryousuke wants to develop his "High-Speed  ... (465 characters truncated) ... tial D details the hardships and successes of the members of Project D as they try to become the best street racing team outside of Gunma Prefecture.', 'Action', 'TV', 24, 'A.C.G.T.', 'Manga', 'PG-13', 'Spring', 2004)
(9, 'Monster', 'Monster', "Dr. Kenzou Tenma, an elite neurosurgeon recently engaged to his hospital director's daughter, is well on his way to ascending the hospital hierarchy. ... (1069 characters truncated) ... comes face to face with the monster he operated on. He must now embark on a quest of pursuit to make amends for the havoc spread by the one he saved.", 'Drama', 'TV', 74, 'Madhouse', 'Manga', 'R+', 'Spring', 2004)
(10, 'Naruto', 'Naruto', "Moments prior to Naruto Uzumaki's birth, a huge demon known as the Kyuubi, the Nine-Tailed Fox, attacked Konohagakure, the Hidden Leaf Village, and w ... (351 characters truncated) ... n the village, while his burning desire to become the Hokage of Konohagakure leads him not only to some great new friends, but also some deadly foes.", 'Action', 'TV', 220, 'Pierrot', 'Manga', 'PG-13', 'Fall', 2002)
Choose here: 

```

It's a lot, and requires you to scroll up to see the menu. 
(1) allows you to add anime to your list, 
(2) scrolls to the next 10 anime
(3) scrolls to the previous 10 anime
(4) allows you to filter on the basis of Genres, Studio, Rating, Season, Year, Origin, whether you watched or not, and even search by title.

Let's preview adding

`Please enter the id of the anime you wish to add: `

You can choose any value, and it will add it to your personal list. For fun, let's add "Witch Hunter Robin", type in 3.

`Successfully added the anime!`

The anime menu runs until you press 5 and return back to the previous menu, but just for fun, let's filter
```
Please choose a filtering option

1 - Genres
2 - Studios
3 - Rating
4 - Season
5 - Year
6 - Origin
7 - Watched
8 - title
```

Because we added "Witch Hunter Robin", let's filter by shows that are not in our watch list. Press 7.

```
(1, 'Cowboy Bebop', 'Cowboy Bebop', "Crime is timeless. By the year 2071, humanity has expanded across the galaxy, filling the surface of other planets with settlements like those on Ear ... (710 characters truncated) ... Spike's past. As a rival's maniacal plot continues to unravel, Spike must choose between life with his newfound family or revenge for his old wounds.", 'Sci-Fi', 'TV', 26, 'Sunrise', 'Original', 'R', 'Spring', 1998)
(2, 'Trigun', 'Trigun', 'Vash the Stampede is the man with a $$60,000,000,000 bounty on his head. The reason: he\'s a merciless villain who lays waste to all those that oppos ... (712 characters truncated) ... summoned to bring about suffering to the trio. Vash\'s agonizing past will be unraveled and his morality and principles pushed to the breaking point.', 'Action', 'TV', 26, 'Madhouse', 'Manga', 'PG-13', 'Spring', 1998)
(4, 'Bouken Ou Beet', 'Beet the Vandel Buster', "It is the dark century and the people are suffering under the rule of the devil, Vandel, who is able to manipulate monsters. The Vandel Busters are a ... (423 characters truncated) ... have passed since then and the young Vandel Buster, Beet, begins his adventure to carry out the Zenon Squad's will to put an end to the dark century.", 'Adventure', 'TV', 52, 'Toei Animation', 'Manga', 'PG', 'Fall', 2004)
(5, 'Eyeshield 21', 'Eyeshield 21', 'Shy, reserved, and small-statured, Deimon High School student Sena Kobayakawa is the perfect target for bullies. However, as a result of running erra ... (737 characters truncated) ... apon of the Deimon Devil Bats. As he interacts with his teammates, Sena gradually gains more self-confidence and forges valuable bonds along the way.', 'Sports', 'TV', 145, 'Gallop', 'Manga', 'PG-13', 'Spring', 2005)
(6, 'Hachimitsu to Clover', 'Honey and Clover', "Yuuta Takemoto, a sophomore at an arts college, shares a cheap apartment with two seniors—the eccentric Shinobu Morita, who keeps failing to graduate ... (553 characters truncated) ...  heartwarming tale of youth, love, soul-searching, and self-discovery, intricately woven through the complex relationships between five dear friends.", 'Comedy', 'TV', 24, 'J.C.Staff', 'Manga', 'PG-13', 'Spring', 2005)
(7, 'Hungry Heart: Wild Striker', 'Hungry Heart: Wild Striker', "As the younger brother of Japanese soccer star Seisuke Kanou, Kyousuke was always expected to grow as a soccer player at the same pace his brother di ... (504 characters truncated) ... remain steadfast in his decision to abandon the sport he once loved, or allow himself to reignite that flame to become the best striker in the world.", 'Comedy', 'TV', 52, 'Nippon Animation', 'Manga', 'PG-13', 'Fall', 2002)
(8, 'Initial D Fourth Stage', 'Initial D Fourth Stage', 'Takumi Fujiwara finally joins Ryousuke and Keisuke Takahashi to create "Project D." Their goal is twofold: Ryousuke wants to develop his "High-Speed  ... (465 characters truncated) ... tial D details the hardships and successes of the members of Project D as they try to become the best street racing team outside of Gunma Prefecture.', 'Action', 'TV', 24, 'A.C.G.T.', 'Manga', 'PG-13', 'Spring', 2004)
(9, 'Monster', 'Monster', "Dr. Kenzou Tenma, an elite neurosurgeon recently engaged to his hospital director's daughter, is well on his way to ascending the hospital hierarchy. ... (1069 characters truncated) ... comes face to face with the monster he operated on. He must now embark on a quest of pursuit to make amends for the havoc spread by the one he saved.", 'Drama', 'TV', 74, 'Madhouse', 'Manga', 'R+', 'Spring', 2004)
(10, 'Naruto', 'Naruto', "Moments prior to Naruto Uzumaki's birth, a huge demon known as the Kyuubi, the Nine-Tailed Fox, attacked Konohagakure, the Hidden Leaf Village, and w ... (351 characters truncated) ... n the village, while his burning desire to become the Hokage of Konohagakure leads him not only to some great new friends, but also some deadly foes.", 'Action', 'TV', 220, 'Pierrot', 'Manga', 'PG-13', 'Fall', 2002)
(11, 'Tennis no Ouji-sama', 'The Prince of Tennis', 'At the request of his father, tennis prodigy Ryouma Echizen has returned from America and is ready to take the Japanese tennis scene by storm. Aiming ... (809 characters truncated) ... tennis in unique ways for their own reasons. Ryouma and his teammates must learn to cooperate if they want to become the champions they aspire to be.', 'Sports', 'TV', 178, 'Trans Arts', 'Manga', 'PG-13', 'Fall', 2001)
``` 

Notice how "Witch Hunter Robin" is now removed from the list? That's the power of filtering!

You can scroll through the list to search through anime, if you like. Whenever you're ready to explore other features, press 5.

2. Using the progress tracker

After pressing 5, you'll be taken to the menu. Then press 2, and you'll see the progress tracker. If you used one of the preset accounts, you'll see a bunch of anime, if not just a menu and "Witch Hunter Robin"

```
Here is your personal list
Please choose an option

1 - Update status
2 - Update progress
3 - Filter List
4 - Return to menu

anime_id	list_id	title	english title	episodes	watch status	progress in (%)
(3, 1, 'Witch Hunter Robin', 'Witch Hunter Robin', 26, 'Plan to Watch', 0)
```

The program prints out the first 10 shows, mostly because it's better to filter through the list.
Any show you add automatically gets updated with the status as "Plan to watch" and episodes at 0 

(1) Updates the watch_status of your program. 
(2) Updates the progress
(3) Filter by watch status
(4) Return to the main menu

Let's pretend that we have watched 7 episodes of Witch Hunter Robin, let's update the status
First, add the list_id. 

```
1 - Plan to watch
2 - In-Progress
3 - Completed
4 - Dropped
```

Since we have only watched 7 episodes, we choose in-progress

Now we are back to the menu, and we can see that it's values have updates
```
(3, 1, 'Witch Hunter Robin', 'Witch Hunter Robin', 26, 'In-Progress', 0)
```

Let's update our progress to reflect that we watched 7 episodes
```
(3, 1, 'Witch Hunter Robin', 'Witch Hunter Robin', 26, 'In-Progress', 26)
```

Look at that, we now have 26% completion.
It would be fun to use the filtering option. If you are using one of the three accounts, then have fun filtering through the 4 statuses.
If not, let's go to the main menu to switch into a different account. 

3. Log out/switch users

This one is simple. It takes you to the login page where you can switch the user, or log back in. 

### And that's it! 
