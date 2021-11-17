# NER by SciSpaCy

## Install package

```sh
python3 -m venv venv
source venv/bin/activate
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

## References

- https://allenai.github.io/scispacy/
- https://github.com/allenai/scispacy
