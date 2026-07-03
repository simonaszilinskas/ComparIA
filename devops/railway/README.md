# Railway deployment

The app runs on Railway as five services, mirroring the topology of
`devops/standalone_docker_install/docker-compose.yml`.

```
Internet
   |
   v
caddy  (the only public service, listens :8080)
   |- /counter*  /models/*  /arena/*  -> backend.railway.internal:80   (FastAPI)
   |- everything else                 -> frontend.railway.internal:3000 (SvelteKit)

backend  -> Postgres.DATABASE_URL  +  redis.railway.internal:6379
```

## Why these choices

- **Single public domain via Caddy.** The browser calls the API on
  `window.location.origin` (`frontend/src/lib/fastapi-client.ts`), so frontend and
  backend must share one origin. Caddy fans the API paths out to the backend.
- **IPv6 binding.** Railway's private network is IPv6-only, so the backend binds
  `::` (start command in the root `railway.json`) and the frontend binds `HOST=::`.
- **Bare Redis, no auth.** Mirrors docker-compose: a plain `redis:7-alpine` with
  `--protected-mode no` on the private network. The app's Redis client is
  host-only with no password (`utils/storage/redis.py`), so a managed Railway
  Redis (which forces a password) would need an app change.
- **Managed Postgres.** Full connection URL works directly.
- **Migrations.** `alembic.ini` is copied into the backend image and run as the
  service `preDeployCommand` (`alembic upgrade head`) on every deploy.

## Service config files

| Service  | Build context            | Config              |
|----------|---------------------------|---------------------|
| backend  | repo root                 | `./railway.json` -> `devops/docker/Dockerfile` |
| frontend | `frontend/`               | `frontend/railway.json` -> `frontend/Dockerfile` |
| caddy    | `devops/railway/caddy/`   | `railway.json` + `Caddyfile` + `Dockerfile` |
| redis    | `devops/railway/redis/`   | `railway.json` + `Dockerfile` |
| Postgres | managed plugin            | n/a |

## Required service variables

- **backend**: `COMPARIA_DB_URI=${{Postgres.DATABASE_URL}}`,
  `COMPARIA_REDIS_HOST=redis.railway.internal`, `OPENROUTER_API_KEY`,
  `ALTCHA_HMAC_KEY`, `LOG_FORMAT=JSON`, `DEFAULT_COUNTRY_PORTAL=fr`.
- **frontend**: `PUBLIC_API_LOCAL_URL=http://backend.railway.internal:80`,
  `PUBLIC_API_URL=https://<caddy-domain>`, `PORT=3000`, `HOST=::`,
  `PUBLIC_APP_NAME`, `PUBLIC_BRAND` (see `frontend/.env.example` — used for the
  compar:IA juridique branding).

## Deploying code

Each service is deployed from its build-context directory. With a project token
exported as `RAILWAY_TOKEN` this works non-interactively from any directory:

```bash
export RAILWAY_TOKEN=<project token>
( cd .                          && railway up --service backend  --detach )
( cd frontend                   && railway up --service frontend --detach )
( cd devops/railway/caddy       && railway up --service caddy    --detach )
( cd devops/railway/redis       && railway up --service redis    --detach )
```
