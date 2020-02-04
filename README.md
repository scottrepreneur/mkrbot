# Maker Bot

A RocketChat bot for MKR holders and Dai users.

- [Docker Compose](https://docs.docker.com/compose/)
- [Flask](http://flask.pocoo.org/) 
- [Celery](http://www.celeryproject.org/) 
- [Redis](https://redis.io/)

My command list is [available here](https://docs.google.com/spreadsheets/d/1apOxgKIeeCTUnisfSRS0TLxiXsIFFB0xvtYLoxSpYX0/edit#gid=527738112).


Test me out in the [#chakachat]() channel on the MakerDAO RocketChat

### Installation

```bash
git clone https://github.com/scottrepreneur/mkr-bot
```

### Build & Launch

```bash
docker-compose up -d --build
```

This will expose the Flask application's endpoints on port `5000`

To add more workers:
```bash
docker-compose up -d --scale worker=5 --no-recreate
```

To shut down:

```bash
docker-compose down
```

To change the endpoints, update the code in [api/app.py](api/app.py)

Task changes should happen in [queue/tasks.py](celery-queue/tasks.py) 

---

adapted from [https://github.com/itsrifat/flask-celery-docker-scale](https://github.com/itsrifat/flask-celery-docker-scale)
