## Url Shortener In FastAPI

An app that implements a simple URL shortener designed to handle heavy read loads by using an `LRU cache`
and `Redis cache` to minimize database access.

### Notes

**I’m new to `FastAPI` and `Cassandra`, but I prefer to try them. While I may not follow all the best practices, I’m doing
my best.**

#### TODO:

- [ ] get secrets from vault instead of env file
- [ ] write some test and consider to mock other units
- [ ] uncomment volumes 

