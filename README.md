# Flask Web Project

## Class 1: Challenges to host the application on Azure

- Python version compatibility issues and installing necessary dependencies.
- Every new update of the application needs to be redeployed, which can be time-consuming.

## Database configuration

Set the following environment variables for MySQL connectivity:

- `MYSQL_HOST` (use the MySQL container name when running on the same Docker network)
- `MYSQL_PORT` (optional, defaults to `3306`)
- `MYSQL_DATABASE`
- `MYSQL_USER`
- `MYSQL_PASSWORD`

The app loads a local `.env` file if present. When running in Docker, pass it with `--env-file .env` (or add an env file in Compose) and set `MYSQL_HOST` to the MySQL container/service name rather than `localhost`.

## Endpoints

- `GET /db` returns the current database time as JSON.
