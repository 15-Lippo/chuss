#!/bin/bash

# Installa le dipendenze Python
pip install -r requirements.txt

# Installa le dipendenze Node.js
npm install

# Build delle funzioni serverless
npm run build

# Avvia l'applicazione con gunicorn
gunicorn app:app