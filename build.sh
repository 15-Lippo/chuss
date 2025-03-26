#!/bin/bash

# Configura l'ambiente Python
export PYTHON_VERSION=3.9.0
export PIP_VERSION=21.1.2

# Installa Python e pip
curl -L https://raw.githubusercontent.com/pyenv/pyenv-installer/master/bin/pyenv-installer | bash
export PATH="$HOME/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
pyenv install $PYTHON_VERSION
pyenv global $PYTHON_VERSION

# Aggiorna pip alla versione specificata
python -m pip install --upgrade pip==$PIP_VERSION

# Installa le dipendenze Python
pip install -r requirements.txt

# Installa le dipendenze Node.js
npm install

# Build delle funzioni serverless
npm run build

# Avvia l'applicazione con gunicorn
gunicorn app:app