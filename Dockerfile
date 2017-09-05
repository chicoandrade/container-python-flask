FROM python:3-onbuild

WORKDIR /usr/src/app/

ENV FLASK_APP hello.py

ENTRYPOINT ["flask"]

CMD ["run"]
