import sys
from pprint import pprint
import json
import textwrap

import pydantic

from . import core


def main() -> None:
    args = sys.argv[1:]
    model = core.get_model_sdf()
    if len(args):
        for fn in args:
            with open(fn) as fo:
                data = json.load(fo)
                try:
                    core.validate_sdf(data)
                except pydantic.ValidationError as e:
                    print(f"Failed: {fn}")
                    print(textwrap.indent(str(e), " " * 4))
                    continue

                print(f"Passed: {fn}")
    else:
        pprint(model.schema(), indent=2)


main()
