from aiohttp import web
import app.populate as populate

routes = web.RouteTableDef()


@routes.get("/")
async def root(req):
    return web.json_response({"success": True})


@routes.get("/populate/ratings")
async def ratings(req):
    err = await populate.ratings(req.app["db_conn"])
    if err is None:
        return web.json_response({"success": True})
    return web.json_response({"success": False, "error": str(err)})


@routes.get("/populate/movies")
async def movies(req):
    err = await populate.movies(req.app["db_conn"])
    if err is None:
        return web.json_response({"success": True})
    return web.json_response({"success": False, "error": str(err)})
