# pokex
Proxy-like server that improves X links appearance on Pocket

## Development

```bash
$ functions-framework-python --target pokex --port=8888
$ curl -A "PocketParser/2.0 (+https://getpocket.com/pocketparser_ua)" "http://localhost:8888/?url=https%3A%2F%2Fx.com%2Fexample%2Fstatus%2F99999999"
```

## Deploy

```bash
gcloud functions deploy pokex \
  --gen2 \
  --runtime=python312 \
  --region=us-west1 \
  --source=. \
  --entry-point=pokex \
  --trigger-http \
  --allow-unauthenticated
```
