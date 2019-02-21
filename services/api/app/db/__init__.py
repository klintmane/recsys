import asyncpg
import os
from datetime import datetime


DBError = asyncpg.PostgresError


async def connect():
    return await asyncpg.create_pool(os.environ["DB_CONN"])


def insert_movies(db, movies):
    return db.executemany(
        "INSERT INTO movies(id, title, genres, year) VALUES($1, $2, $3, $4)", movies
    )


def insert_ratings(db, ratings):
    return db.executemany(
        "INSERT INTO ratings(user_id, movie_id, rating, created_at) VALUES($1, $2, $3, $4)",
        ratings,
    )


def parse_movies(data):
    movies = []
    for d in data.split(sep="\n"):
        movie = d.split(sep="::")
        if len(movie) == 3:
            [id, title, genres] = movie

            title_year = title.split("(")
            title = title_year[0]
            year = title_year[1][:-1]

            genres = genres.split("|")

            movies.append((int(id), title, genres, int(year)))
    return movies


def parse_ratings(data):
    ratings = []
    for d in data.split(sep="\n"):
        rating = d.split(sep="::")
        if len(rating) == 4:
            [user_id, movie_id, rating, timestamp] = rating
            ratings.append(
                (
                    int(user_id),
                    int(movie_id),
                    float(rating),
                    datetime.utcfromtimestamp(int(timestamp)),
                )
            )
    return ratings
