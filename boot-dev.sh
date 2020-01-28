#!/bin/sh
source /venv/bin/activate
export FLASK_DEBUG=True
exec flask run --host=0.0.0.0
