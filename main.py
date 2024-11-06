from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello, World!"}


@app.get("/items/")
async def read_items(request: Request):
    headers = request.headers # un diccionario de los encabezados enviados por el cliente.
    query_params = request.query_params # parámetros de la URL después de ?, como /items?name=book.
    path_params = request.path_params # parámetros dentro de la ruta (si el endpoint tiene parámetros dinámicos).
    url = request.url # URL completa 
    base_url = request.base_url #base de la solicitud.
    method = request.method # método HTTP utilizado en la solicitud (GET, POST, etc.).
    client = request.client # dirección IP del cliente.
    body = await request.body() # método para acceder al cuerpo de la solicitud.

    return {
        "headers": headers,
        "query_params": query_params,
        "path_params": path_params,
        "url": str(url),
        "base_url": base_url,
        "method": method,
        "client": client,
        "body": body,
    }


