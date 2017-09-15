FROM python:3-onbuild

COPY src/hello.py /usr/src/app/
COPY src/settings.ini /usr/src/app/
COPY src/__init__.py /usr/src/app/

WORKDIR /usr/src/app/

ENTRYPOINT ["python"]

CMD ["hello.py"]
