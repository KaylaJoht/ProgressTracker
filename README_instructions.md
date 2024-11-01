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
(5069, 'Soukou Kihei Votoms: Pailsen Files Movie', 'Soukou Kihei Votoms: Pailsen Files Movie', 'Alternative release of Armored Trooper Votoms: Pailsen Files OVA. Was aired 2 years later. Created by the original staff of the series, with an all new story about the end of the 100 year war.', 'Sci-Fi', 'Movie', 1, 'The Answer Studio', 'Original', 'R', 'Winter', 2009)
(94, 'Jinki:Extend', 'Jinki: Extend', 'Aoba is a young girl who loves to build models of robots. She lived alone with her grandmother until her grandmother passes away. Shortly after she i ... (143 characters truncated) ...  but the true meaning behind the fights is hidden. Aoba works hard at the base so one day she can pilot one of the robots and discover these secrets.', 'Sci-Fi', 'TV', 12, 'feel.', 'Manga', 'R', 'Winter', 2005)
(6422, 'Jinki:Extend - Sorekara', 'Jinki: Extend', 'Aoba is a young girl who loves to build models of robots. She lived alone with her grandmother until her grandmother passes away. Shortly after she i ... (143 characters truncated) ...  but the true meaning behind the fights is hidden. Aoba works hard at the base so one day she can pilot one of the robots and discover these secrets.', 'Sci-Fi', 'OVA', 1, 'feel.', 'Manga', 'R', 'Winter', 2006)
(4245, 'Tribe Nine', 'Tribe Nine', 'Fed up with society, youngsters all around Neo-Tokyo formed tribes to find their place in the world. However, group loyalty among them grew fierce an ... (877 characters truncated) ... new threat led by the mysterious Oujirou Otori, the Minato Tribe might just need the power of their two new rookies to overcome the clutches of evil.', 'Sci-Fi', 'TV', 12, 'LIDENFILMS', 'Mixed media', 'R', 'Winter', 2022)
(6523, 'Kidou Senshi Gundam SEED Destiny Final Plus: Erabareta Mirai', 'Mobile Suit Gundam SEED Destiny Final Plus: The Chosen Future', "In year 74 of the Cosmic Era, the civil war raging between the earthbound Naturals and space-dwelling Coordinators comes to a close. Suffering a majo ... (532 characters truncated) ... t brawls are waged for the fate of the galaxy, a sprawling war between humans who are incapable of understanding one another draws to its conclusion.", 'Drama', 'OVA', 1, 'Sunrise', 'Original', 'R', 'Winter', 2005)
(1240, 'Shigofumi', 'Shigofumi: Letters from the Departed', 'There are some things that people are unable to say while they are alive; for these, there are "shigofumi," letters carried from the world of the dea ... (497 characters truncated) ... heir deepest secrets revealed. What is unclear, however, are the details of Fumika\'s past. Who was she before she came to be a carrier of shigofumi?', 'Drama', 'TV', 12, 'J.C.Staff', 'Original', 'R', 'Winter', 2008)
(7629, 'Maji', 'Maji', 'Maji is a young hood in the Nagisa criminal organization whose name is synonymous with loyalty and truth. While driving away thugs, he meets and fall ... (88 characters truncated) ...  run into the rival Kikuchi gang looking for trouble. Based on the first four volumes of the gang chivalry manga by Ayumi Tachihara.\n\n(Source: ANN)', 'Drama', 'OVA', 3, 'Nippon Animation', 'Original', 'R', 'Winter', 1990)
(2719, 'Death Parade', 'Death Parade', "After death, either Heaven or Hell awaits most humans. But for a select few, death brings them to Quindecim—a bar where only pairs of people who die  ... (448 characters truncated) ...  wager their souls. Though his methods remain unchanged, the sudden appearance of a black-haired amnesiac causes Decim to reevaluate his own rulings.", 'Drama', 'TV', 12, 'Madhouse', 'Original', 'R', 'Winter', 2015)
(2670, 'Yuri Kuma Arashi', 'Yurikuma Arashi', 'In the past, humanoid bears coexisted with humans. However, a meteor shower that fell onto Earth had a strange effect on bears throughout the world:  ... (865 characters truncated) ... l school, the girls must stand on trial with their love, embarking on a journey of self-discovery en route to attaining true love\'s "promised kiss."', 'Drama', 'TV', 12, 'SILVER LINK.', 'Original', 'R', 'Winter', 2015)
(4021, 'Wonder Egg Priority', 'Wonder Egg Priority', "Following the suicide of her best and only friend, Koito Nagase, Ai Ooto is left grappling with her new reality. With nothing left to live for, she f ... (601 characters truncated) ... arre world of Wonder Egg Priority, a young girl discovers the different inner struggles tormenting humankind and rescues them from their worst fears.", 'Drama', 'TV', 12, 'CloverWorks', 'Original', 'R', 'Winter', 2021)
Choose here: 

```

It's a lot, and requires you to scroll up to see the menu. 
(1) allows you to add anime to your list, 
(2) scrolls to the next 10 anime
(3) scrolls to the previous 10 anime
(4) allows you to filter on the basis of Genres, Studio, Rating, Season, Year, Origin, whether you watched or not, and even search by title.

Let's preview adding

`Please enter the id of the anime you wish to add: `

You can choose any value, and it will add it to your personal list. For fun, let's add "Wonder Egg Priority", type in 4021.

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

Because we added "Wonder Egg Priority", let's filter by shows that are not in our watch list. Press 7.

Notice how "Wonder Egg Priority" is now removed from the list? That's the power of filtering!

You can scroll through the list to search through anime, if you like. Whenever you're ready to explore other features, press 5.

2. Using the progress tracker

After pressing 5, you'll be taken to the menu. Then press 2, and you'll see the progress tracker. If you used one of the preset accounts, you'll see a bunch of anime, if not just a menu and "Wonder Egg Priority"

```
Here is your personal list
Please choose an option

1 - Update status
2 - Update progress
3 - Filter List
4 - Return to menu

anime_id	list_id	title	english title	episodes	watch status	progress in (%)
(4021, 1, 'Wonder Egg Priority', 'Wonder Egg Priority', 12, 'Plan to Watch', 0)
```

The program prints out the first 10 shows, mostly because it's better to filter through the list.
Any show you add automatically gets updated with the status as "Plan to watch" and episodes at 0 

(1) Updates the watch_status of your program. 
(2) Updates the progress
(3) Filter by watch status
(4) Return to the main menu

Let's pretend that we have watched 7 episodes of Wonder Egg Priority, let's update the status
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
(4021, 1, 'Wonder Egg Priority', 'Wonder Egg Priority', 12, 'In-Progress', 0)
```

Let's update our progress to reflect that we watched 7 episodes
`(4021, 40, 'Wonder Egg Priority', 'Wonder Egg Priority', 12, 'In-Progress', 58)`

Look at that, we now have 58% completion.
It would be fun to use the filtering option. If you are using one of the three accounts, then have fun filtering through the 4 statuses.
If not, let's go to the main menu to switch into a different account. 

3. Log out/switch users

This one is simple. It takes you to the login page where you can switch the user, or log back in. 

### And that's it! 
