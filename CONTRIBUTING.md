## Usage (Local)

### Development

The *development* approach translates to executing the project's 
entrypoint as a *python module*.

###### Setup

```bash
pip install --upgrade pip build setuptools

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
