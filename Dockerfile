FROM python:2.7-onbuild
MAINTAINER Michael Hausenblas
ENV REFRESHED_AT 2017-05-22T14:00
CMD [ "python", "./cwc.py" ]
