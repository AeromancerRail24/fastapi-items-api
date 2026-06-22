# fastapi-items-api

A minimal FastAPI service with typed item APIs.

## Install dependencies

```bash
python -m pip install -r requirements.txt
```

## Run locally

```bash
uvicorn app.main:app --reload
```

## Run tests

```bash
pytest
```

Once running, open: `http://127.0.0.1:8000/docs`

## API examples

```bash
curl http://127.0.0.1:8000/health
curl -X POST http://127.0.0.1:8000/items -H 'Content-Type: application/json' -d '{"name":"Notebook","description":"Blue cover","price":19.5}'
curl http://127.0.0.1:8000/items
curl http://127.0.0.1:8000/items/1
curl -X DELETE http://127.0.0.1:8000/items/1
```
