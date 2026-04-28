# znxcpxmf

Minimal FastAPI starter with typed item APIs.

## Run locally

```bash
python -m pip install -r requirements.txt
uvicorn app.main:app --reload
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
