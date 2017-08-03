#! /bin/bash

gunicorn -w 4 -b 0.0.0.0:6060 main:app
