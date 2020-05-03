CREATE DATABASE tsutaya;
ALTER DATABASE tsutaya SET timezone TO 'Asia/Bangkok';

CREATE TYPE genre_list AS ENUM ('action', 'romantic', 'musical' , 'horror', 'drama', 'sci-fi', 'porn');
CREATE TYPE period_list AS ENUM ('1','3','5','7');

CREATE TABLE member(
    id SERIAL PRIMARY KEY,
    name VARCHAR(30) NOT NULL,
    age INTEGER NOT NULL,
    id_card VARCHAR(13) UNIQUE NOT NULL,
    phone_number VARCHAR(10) NOT NULL,
    is_borrow BOOLEAN DEFAULT False, 
    banned BOOLEAN DEFAULT False,
    created_at TIMESTAMP DEFAULT NOW() NOT NULL,
    updated_at TIMESTAMP);

CREATE TABLE movies(
    id SERIAL PRIMARY KEY,
    code VARCHAR(20),
    movie_name VARCHAR(80) NOT NULL,
    genre genre_list NOT NULL,
    is_available BOOLEAN DEFAULT True,
    created_at TIMESTAMP DEFAULT NOW() NOT NULL,
    updated_at TIMESTAMP);

CREATE TABLE borrow(
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES member(id),
    movie_id INTEGER REFERENCES movies(id),
    period period_list NOT NULL,
    borrow_at TIMESTAMP DEFAULT NOW() NOT NULL,
    return_at TIMESTAMP,
    expect_return_date TIMESTAMP NOT NULL);

INSERT INTO movies(movie_name, genre, created_at) VALUES
    ('Avengers: Endgame', 'action', NOW()),
    ('John Wick: Chapter 3 – Parabellum', 'action', NOW()),
    ('Star Wars: The Rise of Skywalker', 'sci-fi', NOW()),
    ('Ad Astra', 'sci-fi', NOW()),
    ('Vagabond', 'romantic', NOW()),
    ('Itaewon Class', 'romantic', NOW()),
    ('whiplash', 'musical', NOW()),
    ('La La Land', 'musical', NOW()),
    ('It Chapter Two', 'horror', NOW()),
    ('Crawl', 'horror', NOW()),
    ('Parasite', 'drama', NOW()),
    ('Marriage Story', 'drama', NOW());

INSERT INTO movies(code ,movie_name, genre, created_at) VALUES
    ('SSNI-360','Love Love', 'porn', NOW()),
    ('SSNI-382','Lust', 'porn', NOW());


ALTER SEQUENCE borrow_id_seq RESTART;
ALTER SEQUENCE member_id_seq RESTART;
ALTER SEQUENCE movies_id_seq RESTART;
TRUNCATE TABLE borrow CASCADE;
TRUNCATE TABLE member CASCADE;
TRUNCATE TABLE movies CASCADE;
DROP TABLE borrow;
DROP TABLE member;
DROP TABLE movies;
