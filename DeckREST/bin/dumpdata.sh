#!/bin/bash
python manage.py dumpdata --indent=2 -e auth -e sessions -e contenttypes
