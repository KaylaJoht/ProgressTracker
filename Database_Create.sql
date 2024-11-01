DROP DATABASE IF EXISTS progress_tracker;
CREATE DATABASE progress_tracker;

use progress_tracker;

CREATE TABLE Genre
(
	genre_id int PRIMARY KEY auto_increment,
    genre varchar(20)
);

CREATE TABLE Origin
(
	Origin_id int PRIMARY KEY auto_increment,
    origin varchar(20)
);

CREATE TABLE Rating
(
	rating_id int PRIMARY KEY auto_increment,
    rating varchar(10)
);

CREATE TABLE Season
(
	season_id int PRIMARY KEY auto_increment,
    season varchar(10)
);

CREATE TABLE Release_Year
(
	release_Year_id int PRIMARY KEY auto_increment,
    release_Year int
);

CREATE TABLE Studio
(
	studio_id int PRIMARY KEY auto_increment,
    studio varchar(100)
);

CREATE TABLE Media
(
	media_id int PRIMARY KEY auto_increment,
    media varchar(10)
);

CREATE TABLE Anime
(
	anime_id int PRIMARY KEY auto_increment,
    title varchar(150),
    english_title varchar(150),
    original_title varchar(100),
    synopsis varchar(5000),
    media_id int,
    episodes int,
    duration varchar(15),
    FOREIGN KEY (media_id) references Media(media_id)
);

CREATE TABLE Users
(
	users_id int PRIMARY KEY auto_increment,
    email varchar(50),
    password varchar(100)
);

CREATE TABLE User_List 
(
	user_list_id int PRIMARY KEY auto_increment,
    users_id int,
    anime_id int,
    list_id int,
    watch_status varchar(100) DEFAULT "Plan to Watch",
    progress int DEFAULT 0,
    FOREIGN KEY (users_id) references Users(users_id),
    FOREIGN KEY (anime_id) references Anime(anime_id)
);

CREATE TABLE Anime_List
(
	anime_list_id int PRIMARY KEY auto_increment,
    anime_id int, 
    genre_id int,
    media_id int,
    studio_id int, 
    origin_id int, 
    rating_id int,
    season_id int,
    release_year_id int,
    FOREIGN KEY (anime_id) references Anime(anime_id),
    FOREIGN KEY (genre_id) references Genre(genre_id),
    FOREIGN KEY (media_id) references Media(media_id),
    FOREIGN KEY (studio_id) references Studio(studio_id),
    FOREIGN KEY (origin_id) references Origin(origin_id),
    FOREIGN KEY (rating_id) references Rating(rating_id),
    FOREIGN KEY (season_id) references Season(season_id),
    FOREIGN KEY (release_year_id) references Release_year(release_year_id)
    
)