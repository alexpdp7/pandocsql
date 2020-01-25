import io
import json
import pandocsql


def test():
    input = {
        "blocks": [
            {
                "t": "Table",
                "c": [
                    [{"t": "Str", "c": "sample"}],
                    [{"t": "AlignDefault"}, {"t": "AlignDefault"}],
                    [0, 0],
                    [
                        [{"t": "Plain", "c": [{"t": "Str", "c": "foo"}]}],
                        [{"t": "Plain", "c": [{"t": "Str", "c": "bar"}]}],
                    ],
                    [
                        [
                            [{"t": "Plain", "c": [{"t": "Str", "c": "a"}]}],
                            [{"t": "Plain", "c": [{"t": "Str", "c": "1"}]}],
                        ]
                    ],
                ],
            },
            {
                "t": "CodeBlock",
                "c": [["", ["pandocsql"], []], "select bar, foo\nfrom sample"],
            },
        ],
        "pandoc-api-version": [1, 17, 5, 1],
        "meta": {},
    }
    input_stream = io.StringIO(json.dumps(input))
    output_stream = io.StringIO()
    pandocsql.main(input_stream=input_stream, output_stream=output_stream)
    assert json.loads(output_stream.getvalue()) == {
        "pandoc-api-version": [1, 17, 5, 1],
        "meta": {},
        "blocks": [
            {
                "t": "Table",
                "c": [
                    [],
                    [{"t": "AlignDefault"}, {"t": "AlignDefault"}],
                    [0.0, 0.0],
                    [
                        [{"t": "Para", "c": [{"t": "Str", "c": "bar"}]}],
                        [{"t": "Para", "c": [{"t": "Str", "c": "foo"}]}],
                    ],
                    [
                        [
                            [{"t": "Para", "c": [{"t": "Str", "c": "1"}]}],
                            [{"t": "Para", "c": [{"t": "Str", "c": "a"}]}],
                        ]
                    ],
                ],
            }
        ],
    }
