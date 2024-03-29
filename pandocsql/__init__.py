import sqlite3

import panflute as pf


def bp():
    import sys

    sys.stdin = open("/dev/tty")
    import pdb

    pdb.set_trace()


def prepare(doc):
    doc.sql = sqlite3.connect(":memory:")


def action(elem, doc):
    if isinstance(elem, pf.Table):
        table = elem.caption.content[0].content[0].text
        headers = list(map(pf.stringify, elem.head.content[0].content))
        headers_sql = ",".join(headers)
        placeholders_sql = ",".join(["?"] * len(headers))
        doc.sql.execute(f"create table {table} ({headers_sql})")
        for row in elem.content[0].content:
            row_values = [pf.stringify(cell) for cell in row.content]
            doc.sql.execute(
                f"insert into {table}({headers_sql}) values ({placeholders_sql})",
                row_values,
            )
        return []
    if isinstance(elem, pf.CodeBlock):
        if elem.classes != ["pandocsql"]:
            return
        table = doc.sql.execute(elem.text)
        headers = [col[0] for col in table.description]
        rows = list(table)

        def c(t):
            return pf.TableCell(pf.Para(pf.Str(str(t))))

        def r(cs):
            return pf.TableRow(*list(map(c, cs)))

        return [
            pf.Table(
                pf.TableBody(*list(map(r, rows))),
                head=pf.TableHead(r(headers)),
                caption=pf.Caption(),
            )
        ]


def finalize(doc):
    pass


def main(doc=None, input_stream=None, output_stream=None):
    return pf.run_filter(
        action,
        prepare=prepare,
        finalize=finalize,
        doc=doc,
        input_stream=input_stream,
        output_stream=output_stream,
    )


if __name__ == "__main__":
    main()
