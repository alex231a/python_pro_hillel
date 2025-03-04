"""Asynchronous web server using aiohttp."""

import asyncio

from aiohttp import web


async def handle_hello(request: web.Request) -> web.Response:
    """
    Handle requests to the root ("/") endpoint.
    Returns a simple text response "Hello, World!".
    """
    _ = request  # Explicitly acknowledge the unused parameter
    return web.Response(text="Hello, World!")


async def handle_slow(request: web.Request) -> web.Response:
    """
    Handle requests to the "/slow" endpoint.
    Simulates a long operation with a 5-second delay before responding.
    Returns a text response "Operation completed".
    """
    _ = request  # Explicitly acknowledge the unused parameter
    await asyncio.sleep(5)
    return web.Response(text="Operation completed")


app = web.Application()
app.router.add_get('/', handle_hello)
app.router.add_get('/slow', handle_slow)

if __name__ == '__main__':
    web.run_app(app)
