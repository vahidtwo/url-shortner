### Assignment
#### URL SHORTENER
An app that implements a simple URL shortener designed to handle heavy read loads by using an LRU cache and Redis to minimize database access.

This project is simple code without tests 😔, mainly because I wrote it under time pressure (during a business incident).

I built this project using Django and FastAPI 🙃. However, it doesn't follow best practices in the FastAPI sections, as I'm still new to FastAPI, so have fun with it!

I want to add a benchmark test on Django with mysql and fast with cassandra, 
i think django with correct gunicorn mode its not different so much with fast api **with mysql**
But I think  single django gunicorn instance handle over 15K get request and 2K for write.

#### TODO:
- [ ] test docker composes 
- [ ] write some testcases 
- [ ] find best practices for fastapi blueprint
- [ ] try to write test with pytest instead of TestCase
- [ ] add better documentation to project
- [ ] add drawio for request journey
- [ ] add load balancer configs (maybe in nginx) 
- [ ] add nginx and test to load statics correctly

