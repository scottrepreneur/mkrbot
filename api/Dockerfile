FROM python:3.6-alpine

ENV CELERY_BROKER_URL redis://redis:6379/0
ENV CELERY_RESULT_BACKEND redis://redis:6379/0
ENV C_FORCE_ROOT true

ENV HOST 0.0.0.0
ENV PORT 5000
ENV DEBUG true

COPY requirements.txt /api/requirements.txt
WORKDIR /api
# COPY requirements.txt .

# install requirements
RUN pip install -r requirements.txt

# expose the app port
EXPOSE 5000

RUN pip install gunicorn==19.9.0

# run the app server
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "3", "app:app"]
