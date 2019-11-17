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
        table = elem.caption.list[0].text
        headers = list(map(pf.stringify, elem.header.content))
        headers_sql = ",".join(headers)
        placeholders_sql = ",".join(["?"] * len(headers))
        doc.sql.execute(f"create table {table} ({headers_sql})")
        for row in elem.content:
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
            return pf.TableCell(pf.Para(pf.Str(t)))

        def r(cs):
            return pf.TableRow(*list(map(c, cs)))

        return [pf.Table(*list(map(r, rows)), header=r(headers))]


def finalize(doc):
    pass


def main(doc=None):
    return pf.run_filter(action, prepare=prepare, finalize=finalize, doc=doc)


if __name__ == "__main__":
    main()
