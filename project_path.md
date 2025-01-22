# [FROM HERE](https://tda-api.readthedocs.io/en/latest/getting-started.html)

## python version

```bash
python3 --version
Python 3.11.2
```

# [install venv — Creation of virtual environments](https://docs.python.org/3/library/venv.html)

## create venv

```bash
python3 -m venv .venv
```

## activate venv

```bash
# source <venv>/bin/activate
source .venv/bin/activate
```

## install packages - inside .venv

```bash
pip3 install  tda-api
```

## hello world connect thingorswim

```python
import tda

```

**ABORT** 

Unfortunately, the TD Ameritrade API does not seem to expose any endpoints around the papermoney simulated trading product. tda-api can only be used to perform real trades using a TD Ameritrade account. Note: trades made through the API appear in thinkorswim and vice versa.