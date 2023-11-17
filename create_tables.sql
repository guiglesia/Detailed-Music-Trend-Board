CREATE TABLE spotify.albums (album_id varchar(22) PRIMARY KEY,
artist_id varchar(22),
name varchar(50),
tracks int,
release date,
album_type varchar(15),
FOREIGN KEY (artist_id) REFERENCES spotify.artists (artist_id));

CREATE TABLE spotify.artists (
artist_id varchar(22) PRIMARY KEY,
name varchar(100),
genre varchar(50),
popularity int,
followers bigint);

CREATE TABLE spotify.tracks (
track_id varchar(22) PRIMARY KEY,
album_id varchar(22),
artist_id varchar(22),
name varchar(150),
release date,
duration bigint,
popularity int,
album_type varchar(15),
FOREIGN KEY (artist_id) REFERENCES spotify.artists (artist_id),
FOREIGN KEY (album_id) REFERENCES spotify.albums (album_id));
