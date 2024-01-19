# SDF Validator

This code base uses the `pydantic` library to validate SDF schemas encoded in
JSON.  Install with either `poetry` (`pyproject.toml`) or `pip`
(`requirements.txt`).

## Usage

To validate a schema:
```
python -m sdfval schema.json
python -m sdfval schema1.json schema2.json
```

To print the SDF format definition:
```
python -m sdfval
```
