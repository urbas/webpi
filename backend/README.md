# webpi-web-backend

## Development
Install python of the version defined in [`../.python-version`](../.python-version). You can do that with [pyenv].

Create a virtual environment and activate it:
```bash
python -m venv .venv
source .venv/bin/activate
```

Install dependencies:
```bash
pip install -e .
pip install -r requirements_dev.txt
```

Run development server:
```bash
FLASK_ENV=development FLASK_APP=webpi/app.py flask run
```

Unit-tests:
```bash
# This will watch for changes
pytest-watch

# Watched tests without coverage
pytest-watch -- --no-cov

# This will run tests only once
pytest
```

Linter:
```bash
pylint webpi
```

Formatter:
```bash
black webpi
```


[pyenv]: https://github.com/pyenv/pyenv