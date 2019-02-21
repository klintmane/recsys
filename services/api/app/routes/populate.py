from aiohttp import web, ClientSession

from app.routes import routes
from app.db import insert_movies, insert_ratings, parse_ratings, parse_movies, DBError

session = ClientSession()


base = "https://raw.githubusercontent.com/sidooms/MovieTweetings/master/snapshots/10K/"


@routes.get("/populate/ratings")
async def ratings(req):
    resp = await session.get(base + "ratings.dat")
    data = await resp.text()
    ratings = parse_ratings(data)

    try:
        db = req.app["db"]
        await insert_ratings(db, ratings)
        return web.json_response({"success": True})

    except DBError:
        return web.json_response({"success": False, "error": DBError})


@routes.get("/populate/movies")
async def movies(req):
    resp = await session.get(base + "movies.dat")
    data = await resp.text()
    movies = parse_movies(data)

    try:
        db = req.app["db"]
        await insert_movies(db, movies)
        return web.json_response({"success": True})

    except DBError:
        return web.json_response({"success": False, "error": DBError})
