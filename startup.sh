#!/bin/bash

source /root/venv/bin/activate
flask --app /root/dateapp/1.py run --host=0.0.0.0 --port=5000
