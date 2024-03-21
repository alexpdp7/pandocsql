I'm not really using this nowadays, so I'm not maintaining it, really.
https://github.com/alexpdp7/pandoc_datalog is what I will focus on when I have some bandwith.

# pandocsql

This is a Pandoc filter to do stuff with SQL.

If you use it like:

```
$ pandoc README.md -F pandocsql -o README.html
```

, tables defined in the document will not appear in the output; however they will be dumped into an SQLite database...

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

You can see further examples in the [examples folder](examples/).

## Installation

```
$ pipx install git+https://github.com/alexpdp7/pandocsql.git
```

## Development

```
$ pandoc README.md -t json | poetry run pandocsql | pandoc -f json -o README.pdf
```
