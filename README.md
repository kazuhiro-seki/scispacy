# NER by SciSpaCy

## Virtual environment

```sh
python3 -m venv venv
source venv/bin/activate
```

## Install package

```sh
pip install pip -U
pip install scispacy
```

### Install models

```sh
pip install https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/v0.4.0/en_core_sci_sm-0.4.0.tar.gz # biomedical generic
pip install https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/v0.4.0/en_ner_bionlp13cg_md-0.4.0.tar.gz # NER
```

## Run

```sh
python test.py
```

## Note

Doesn't run on M1 Mac.  Tested on CentOS.

## References

- https://allenai.github.io/scispacy/
- https://github.com/allenai/scispacy
