# Jupyter Server for Atlassian Python API

This directory provides utilities for running client notebooks that interact with Jira and Bitbucket using the [`atlassian-python-api`](https://github.com/Cazador0/atlassian-python-api).

## Setup

1. Create and activate a Python virtual environment.
2. Install dependencies:

```bash
pip install -r requirements.txt
# install the library from the repository root
pip install -e ..
```

3. Copy `.env.example` to `.env` and fill in your connection details.

4. Launch Jupyter:

```bash
jupyter notebook
```

## Adding a Client Notebook

Run the helper script with the desired client name:

```bash
python init_client.py CLIENT_NAME
```

This creates `notebooks/CLIENT_NAME/CLIENT_NAME.ipynb` from the template.

## Generating an API Feature Map

To list available methods on the `Jira` and `Bitbucket` classes, run:

```bash
python list_features.py
```

The results will be written to `api_map.md` in this directory.
