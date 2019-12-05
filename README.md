# pandocsql

This is a Pandoc filter to do stuff with SQL.

Tables defined in the document will not appear in the output; however they will be dumped into an SQLite database...

| code | description | priority |
| ---- | ----------- | -------- |
| Q1   | Banana      | 7        |
| B2   | Apple       | 1        |
| R7   | Orange      | 3        |

Table: table_1

And you can run queries which will be displayed as tables:

```pandocsql
select *
from table_1
order by priority desc
```

## Installation

```
$ pipx install --spec git+https://github.com/alexpdp7/pandocsql.git pandocsql
```

## Development

```
$ pandoc README.md -t json | poetry run pandocsql | pandoc -f json -o README.pdf
```
