# Bloomb - Financial data retriever

Bloomb is a module that retrieves and outputs fundamental financial data.
Its interface is simple: an HTTP Server to serve the data, and an HTTP client
to retrieve it from Yahoo! Finance.

## How to run it

Using Docker:

```sh
docker-compose up -d
```

Retrieving data:

```sh
GET /get_financial_data/<COMPANY SYMBOL>
```

Updating data in the DB:

Use a file (to be determined) that sends the list of company symbols to be
updated.

```sh
GET /update_financial_data/<COMPANY SYMBOL>
```
