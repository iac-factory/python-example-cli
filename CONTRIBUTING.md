## Usage (Local)

### Development

The *development* approach translates to executing the project's 
entrypoint as a *python module*.

###### Setup

```bash
python -m pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org --upgrade pip build setuptools

python3 -m venv .venv
source .venv/bin/activate
pip install --require-virtualenv .
```

###### Usage

```bash
python3 -m cli
```

### Standard

The *standard* approach translates to executing the project's 
entrypoint as a callable executable (`python-example-cli`).

###### Dependencies 

```bash
pip install --upgrade pip build setuptools
```

###### Build

```bash
python3 -m build
```

###### Install 

```bash
pip install .
```

###### Usage

```bash
python-example-cli
```

## Containerization

### Docker

###### Build

```bash
docker build --tag python-example-cli:latest .
```

###### Usage

```bash
docker run python-example-cli:latest
```

## Adding Python Virtual-Environment to `${PATH}`

In the system's rc file (e.g. `~/.zshrc`):

```bash
if [[ -d "$(pwd)/venv" ]]; then 
    export PATH="${PATH}:$(pwd)/venv/bin"
elif [[ -d "$(pwd)/.venv" ]]; then
    export PATH="${PATH}:$(pwd)/.venv/bin"
fi
```

## Reference(s)

- Python
    - [Dataclasses](https://docs.python.org/3/library/dataclasses.html)
    - [`argparse`](https://docs.python.org/3/library/argparse.html) 
    - Documentation
        - [Types of Docstrings (PEP-257)](https://peps.python.org/pep-0257/)
        - Formats
            - [Google Format](https://github.com/google/styleguide/blob/gh-pages/pyguide.md#38-comments-and-docstrings)
            - [NumPy, SciPy Format](https://numpydoc.readthedocs.io/en/latest/format.html)
            - [Python Official (reStructuredText)](http://docutils.sourceforge.net/rst.html)
  - [Packaging](https://packaging.python.org/en/latest/tutorials/packaging-projects/)
  - [SetupTools](https://setuptools.pypa.io/en/latest/)
  - [Build Backend (`flit`)](https://packaging.python.org/en/latest/key_projects/#flit)
      - [Official `flit` Documentation](https://flit.pypa.io/en/stable/pyproject_toml.html)
  - [Standard 517](https://peps.python.org/pep-0517/)
