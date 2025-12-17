# Script com Dependências

- [PEP 723](https://peps.python.org/pep-0723/)

- Ferramentas com suporte:
  - [pipx](https://pipx.pypa.io/stable/#walkthrough-running-an-application-in-a-temporary-virtual-environment): `pipx run -- arquivo.py`
  - [uv](https://docs.astral.sh/uv/guides/scripts/): `uv run --script arquivo.py`

```python
#!/usr/bin/env -S pipx run --
#
# /// script
# requires-python = ">=3.12"
# dependencies = [
#   "click >= 8.2.1, < 9",
# ]
# ///
```
