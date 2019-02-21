from aiohttp import web

routes = web.RouteTableDef()


@routes.get("/")
async def root(req):
    return web.json_response({"success": True})
