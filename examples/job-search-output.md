# Introduction

This is an adaptation of the document I used to track my last job
search. The names of companies have been scrubbed and I have made a few
modifications to make a better example.

After installing `pandocsql`, you can process this document with:

    $ pandoc job-search.md -F pandocsql -o job-search.html

You can see the output [here](job-search-output.md)

# Data entry

This is the main table tracking jobs you have applied to. I had a URL
pointing to the offer, but faking that data sounded useless so I removed
it. This can handle multiple jobs from the same company. Extra columns
could be added to track job properties, etc.

The other table is for job events. The job column should match the job
column in the table above.

# Reports

This table just lists all events, adding the job headline and days from
the first even and days to
“now”.

| ts         | days\_to\_now | days\_from\_start | job            | event             | company        | headline                                         |
| ---------- | ------------- | ----------------- | -------------- | ----------------- | -------------- | ------------------------------------------------ |
| 2019-11-22 | 66            | 0                 | METACERO       | APPLIED           | METACERO       | Text to display in some reports… status, etc.    |
| 2019-11-25 | 63            | 3                 | CRYPTOBER      | APPLIED           | CRYPTOBER      |                                                  |
| 2019-11-25 | 63            | 3                 | UNILANE        | APPLIED           | UNILANE        |                                                  |
| 2019-11-25 | 63            | 3                 | IDIOZZY        | APPLIED           | IDIOZZY        |                                                  |
| 2019-11-25 | 63            | 3                 | ISOLOO         | APPLIED           | ISOLOO         |                                                  |
| 2019-11-25 | 63            | 3                 | DEMOVUR        | APPLIED           | DEMOVUR        |                                                  |
| 2019-11-25 | 63            | 3                 | AGINTE         | APPLIED           | AGINTE         |                                                  |
| 2019-11-25 | 63            | 3                 | ALBICIOUS      | APPLIED           | ALBICIOUS      |                                                  |
| 2019-11-25 | 63            | 3                 | AMBITRI        | APPLIED           | AMBITRI        |                                                  |
| 2019-11-25 | 63            | 3                 | AMBITRI        | REJECTED          | AMBITRI        |                                                  |
| 2019-11-25 | 63            | 3                 | SYMILE         | APPLIED           | SYMILE         |                                                  |
| 2019-11-25 | 63            | 3                 | YAKILIUMER     | APPLIED           | YAKILIUMER     |                                                  |
| 2019-11-25 | 63            | 3                 | FLEMATE        | APPLIED           | FLEMATE        |                                                  |
| 2019-11-25 | 63            | 3                 | BLUEPOD        | APPLIED           | BLUEPOD        |                                                  |
| 2019-11-25 | 63            | 3                 | YAKILIUMER     | EMAILS            | YAKILIUMER     |                                                  |
| 2019-11-25 | 63            | 3                 | GABORLENOR     | APPLIED           | GABORLENOR     |                                                  |
| 2019-11-25 | 63            | 3                 | ROBOCADRE      | APPLIED           | ROBOCADRE      |                                                  |
| 2019-11-25 | 63            | 3                 | GOOMDOR        | APPLIED           | GOOMDOR        |                                                  |
| 2019-11-26 | 62            | 4                 | ROTEBOTEDO     | APPLIED           | ROTEBOTEDO     |                                                  |
| 2019-11-26 | 62            | 4                 | PEMBROTHER     | APPLIED           | PEMBROTHER     |                                                  |
| 2019-11-26 | 62            | 4                 | BOKEMOKETOPER  | APPLIED           | BOKEMOKETOPER  |                                                  |
| 2019-11-26 | 62            | 4                 | GANO           | APPLIED           | GANO           |                                                  |
| 2019-11-26 | 62            | 4                 | FLEMATE        | EMAILS            | FLEMATE        |                                                  |
| 2019-11-26 | 62            | 4                 | SUCORER        | APPLIED           | SUCORER        |                                                  |
| 2019-11-26 | 62            | 4                 | REPOZOO        | APPLIED           | REPOZOO        |                                                  |
| 2019-11-26 | 62            | 4                 | AVUURA         | APPLIED           | AVUURA         |                                                  |
| 2019-11-26 | 62            | 4                 | UNILANE        | REJECTED          | UNILANE        |                                                  |
| 2019-11-27 | 61            | 5                 | AGINTE         | EMAILS            | AGINTE         |                                                  |
| 2019-11-27 | 61            | 5                 | AVUURA         | REJECTED          | AVUURA         |                                                  |
| 2019-11-27 | 61            | 5                 | UNILANE2       | APPLIED           | UNILANE        |                                                  |
| 2019-11-27 | 61            | 5                 | SUCORER        | REJECTED          | SUCORER        |                                                  |
| 2019-11-27 | 61            | 5                 | ROBEDOBE       | APPLIED           | ROBEDOBE       |                                                  |
| 2019-11-27 | 61            | 5                 | ANOR           | APPLIED           | ANOR           |                                                  |
| 2019-11-27 | 61            | 5                 | LETOPE         | APPLIED           | LETOPE         |                                                  |
| 2019-11-27 | 61            | 5                 | AGUSAPARTE     | APPLIED           | AGUSAPARTE     |                                                  |
| 2019-11-27 | 61            | 5                 | BOKEMOKETOPER  | EXERCISE\_REQUEST | BOKEMOKETOPER  |                                                  |
| 2019-11-27 | 61            | 5                 | NACE           | APPLIED           | NACE           |                                                  |
| 2019-11-27 | 61            | 5                 | ISOLOO         | REJECTED          | ISOLOO         |                                                  |
| 2019-11-27 | 61            | 5                 | IDIOZZY        | REJECTED          | IDIOZZY        |                                                  |
| 2019-11-28 | 60            | 6                 | GANO           | REJECTED          | GANO           |                                                  |
| 2019-11-29 | 59            | 7                 | AGINTE         | INTERVIEW         | AGINTE         |                                                  |
| 2019-11-29 | 59            | 7                 | FOOLAMINASTE   | APPLIED           | FOOLAMINASTE   |                                                  |
| 2019-11-29 | 59            | 7                 | BOOG           | APPLIED           | BOOG           |                                                  |
| 2019-11-29 | 59            | 7                 | COREDUL        | APPLIED           | COREDUL        |                                                  |
| 2019-11-29 | 59            | 7                 | MARTER         | APPLIED           | MARTER         |                                                  |
| 2019-11-29 | 59            | 7                 | POKERCONNOR    | APPLIED           | POKERCONNOR    |                                                  |
| 2019-11-29 | 59            | 7                 | LETOPE         | INTERVIEW         | LETOPE         |                                                  |
| 2019-12-01 | 57            | 9                 | PORESORE       | APPLIED           | PORESORE       |                                                  |
| 2019-12-02 | 56            | 10                | REPOZOO        | REJECTED          | REPOZOO        |                                                  |
| 2019-12-02 | 56            | 10                | LETOPE         | REJECTED          | LETOPE         |                                                  |
| 2019-12-02 | 56            | 10                | COREDUL        | REJECTED          | COREDUL        |                                                  |
| 2019-12-02 | 56            | 10                | ROBOCADRE      | REJECTED          | ROBOCADRE      |                                                  |
| 2019-12-03 | 55            | 11                | NASTIPE        | APPLIED           | NASTIPE        | Interesting, but I don’t like their mission      |
| 2019-12-03 | 55            | 11                | UNILANE2       | REJECTED          | UNILANE        |                                                  |
| 2019-12-03 | 55            | 11                | ANOR           | INTERVIEW         | ANOR           |                                                  |
| 2019-12-04 | 54            | 12                | FLEMATE        | INTERVIEW         | FLEMATE        |                                                  |
| 2019-12-04 | 54            | 12                | NASTIPE        | INTERVIEW         | NASTIPE        | Interesting, but I don’t like their mission      |
| 2019-12-04 | 54            | 12                | GOOMDOR        | REJECTED          | GOOMDOR        |                                                  |
| 2019-12-05 | 53            | 13                | COCOPARNABURN  | APPLIED           | COCOPARNABURN  |                                                  |
| 2019-12-05 | 53            | 13                | ZOOXOR         | APPLIED           | ZOOXOR         |                                                  |
| 2019-12-05 | 53            | 13                | AGINTE2        | APPLIED           | AGINTE         |                                                  |
| 2019-12-05 | 53            | 13                | BOKEMOKETOPER  | EXERCISE\_DONE    | BOKEMOKETOPER  |                                                  |
| 2019-12-06 | 52            | 14                | ARBORPALE      | APPLIED           | ARBORPALE      |                                                  |
| 2019-12-06 | 52            | 14                | WOOBOORT       | APPLIED           | WOOBOORT       |                                                  |
| 2019-12-09 | 49            | 17                | ANOR           | REJECTED          | ANOR           |                                                  |
| 2019-12-09 | 49            | 17                | FLEMATE        | INTERVIEW         | FLEMATE        |                                                  |
| 2019-12-09 | 49            | 17                | FLEMATE        | OFFER             | FLEMATE        |                                                  |
| 2019-12-09 | 49            | 17                | SYLER          | APPLIED           | SYLER          |                                                  |
| 2019-12-09 | 49            | 17                | COCE           | APPLIED           | COCE           |                                                  |
| 2019-12-09 | 49            | 17                | HOOROOPO       | APPLIED           | HOOROOPO       |                                                  |
| 2019-12-10 | 48            | 18                | BOKEMOKETOPER  | REJECTED          | BOKEMOKETOPER  |                                                  |
| 2019-12-10 | 48            | 18                | WOOBOORT       | REJECTED          | WOOBOORT       |                                                  |
| 2019-12-10 | 48            | 18                | MARTER         | EXERCISE\_REQUEST | MARTER         |                                                  |
| 2019-12-10 | 48            | 18                | MARTER         | EXERCISE\_DONE    | MARTER         |                                                  |
| 2019-12-11 | 47            | 19                | SYLER          | INTERVIEW         | SYLER          |                                                  |
| 2019-12-12 | 46            | 20                | SYLER          | INTERVIEW         | SYLER          |                                                  |
| 2019-12-12 | 46            | 20                | NACE2          | APPLIED           | NACE           |                                                  |
| 2019-12-13 | 45            | 21                | PEMBROTHER     | INTERVIEW         | PEMBROTHER     |                                                  |
| 2019-12-13 | 45            | 21                | PEMBROTHER     | EXERCISE\_REQUEST | PEMBROTHER     |                                                  |
| 2019-12-15 | 43            | 23                | PEMBROTHER     | EXERCISE\_DONE    | PEMBROTHER     |                                                  |
| 2019-12-16 | 42            | 24                | SYLER          | REJECTED          | SYLER          |                                                  |
| 2019-12-16 | 42            | 24                | FGHTANIO       | APPLIED           | FGHTANIO       |                                                  |
| 2019-12-16 | 42            | 24                | AVINU          | APPLIED           | AVINU          |                                                  |
| 2019-12-16 | 42            | 24                | BUKULURUPOX    | APPLIED           | BUKULURUPOX    |                                                  |
| 2019-12-16 | 42            | 24                | JUJUP          | APPLIED           | JUJUP          |                                                  |
| 2019-12-17 | 41            | 25                | FRAMEPORCOCO   | APPLIED           | FRAMEPORCOCO   |                                                  |
| 2019-12-17 | 41            | 25                | REPROCA        | APPLIED           | REPROCA        |                                                  |
| 2019-12-17 | 41            | 25                | PUXXONA        | APPLIED           | PUXXONA        |                                                  |
| 2019-12-17 | 41            | 25                | BUKULURUPOX    | INTERVIEW         | BUKULURUPOX    |                                                  |
| 2019-12-17 | 41            | 25                | AVINU          | INTERVIEW         | AVINU          |                                                  |
| 2019-12-17 | 41            | 25                | FLEMATE        | DECLINED          | FLEMATE        |                                                  |
| 2019-12-18 | 40            | 26                | ROTEBOTEDO2    | APPLIED           | ROTEBOTEDO     |                                                  |
| 2019-12-18 | 40            | 26                | PERALTA        | APPLIED           | PERALTA        |                                                  |
| 2019-12-18 | 40            | 26                | DOZENER        | APPLIED           | DOZENER        |                                                  |
| 2019-12-18 | 40            | 26                | BUKULURUPOX    | EXERCISE\_REQUEST | BUKULURUPOX    |                                                  |
| 2019-12-18 | 40            | 26                | AGINTE2        | INTERVIEW         | AGINTE         |                                                  |
| 2019-12-19 | 39            | 27                | REPROCA        | EMAILS            | REPROCA        |                                                  |
| 2019-12-19 | 39            | 27                | BUKULURUPOX    | EXERCISE\_DONE    | BUKULURUPOX    |                                                  |
| 2019-12-19 | 39            | 27                | MARTER         | INTERVIEW         | MARTER         |                                                  |
| 2019-12-19 | 39            | 27                | SOAOK          | APPLIED           | SOAOK          |                                                  |
| 2019-12-20 | 38            | 28                | COCE           | DECLINED          | COCE           |                                                  |
| 2019-12-20 | 38            | 28                | NEXTPUPUS      | APPLIED           | NEXTPUPUS      |                                                  |
| 2019-12-20 | 38            | 28                | DOZENER2       | APPLIED           | DOZENER        |                                                  |
| 2019-12-20 | 38            | 28                | PERALTA        | REJECTED          | PERALTA        |                                                  |
| 2019-12-23 | 35            | 31                | CUCUPORI       | APPLIED           | CUCUPORI       |                                                  |
| 2019-12-26 | 32            | 34                | VIVIZONI       | APPLIED           | VIVIZONI       |                                                  |
| 2019-12-26 | 32            | 34                | FREPULATORING  | APPLIED           | FREPULATORING  |                                                  |
| 2019-12-27 | 31            | 35                | BAKKANT        | APPLIED           | BAKKANT        |                                                  |
| 2019-12-27 | 31            | 35                | REPROCA        | INTERVIEW         | REPROCA        |                                                  |
| 2020-01-03 | 24            | 42                | BUBONICA       | APPLIED           | BUBONICA       |                                                  |
| 2020-01-03 | 24            | 42                | REAITOR        | APPLIED           | REAITOR        |                                                  |
| 2020-01-03 | 24            | 42                | FLIZZOG        | APPLIED           | FLIZZOG        |                                                  |
| 2020-01-03 | 24            | 42                | BOOR           | APPLIED           | BOOR           |                                                  |
| 2020-01-03 | 24            | 42                | FROSTYMAN      | APPLIED           | FROSTYMAN      |                                                  |
| 2020-01-03 | 24            | 42                | PUNNY          | APPLIED           | PUNNY          |                                                  |
| 2020-01-03 | 24            | 42                | XAXAPO         | APPLIED           | XAXAPO         |                                                  |
| 2020-01-03 | 24            | 42                | QOOBAR         | APPLIED           | QOOBAR         |                                                  |
| 2020-01-03 | 24            | 42                | PIXXOTE        | APPLIED           | PIXXOTE        |                                                  |
| 2020-01-03 | 24            | 42                | AZZOOMR        | APPLIED           | AZZOOMR        |                                                  |
| 2020-01-03 | 24            | 42                | NIXX           | APPLIED           | NIXX           |                                                  |
| 2020-01-03 | 24            | 42                | PULE           | APPLIED           | PULE           |                                                  |
| 2020-01-07 | 20            | 46                | FLIZZOG        | INTERVIEW         | FLIZZOG        |                                                  |
| 2020-01-07 | 20            | 46                | BUKULURUPOX    | INTERVIEW         | BUKULURUPOX    |                                                  |
| 2020-01-07 | 20            | 46                | FLUZ           | APPLIED           | FLUZ           |                                                  |
| 2020-01-07 | 20            | 46                | AVINU2         | APPLIED           | AVINU          |                                                  |
| 2020-01-07 | 20            | 46                | WOWAWEWIWUPR   | APPLIED           | WOWAWEWIWUPR   |                                                  |
| 2020-01-07 | 20            | 46                | LEFTR          | APPLIED           | LEFTR          |                                                  |
| 2020-01-07 | 20            | 46                | ZOOXOR         | REJECTED          | ZOOXOR         |                                                  |
| 2020-01-08 | 19            | 47                | REPROCA        | EXERCISE\_REQUEST | REPROCA        |                                                  |
| 2020-01-08 | 19            | 47                | REPROCA        | EXERCISE\_DONE    | REPROCA        |                                                  |
| 2020-01-08 | 19            | 47                | SOAOK          | EMAILS            | SOAOK          |                                                  |
| 2020-01-08 | 19            | 47                | PACKGANO       | APPLIED           | PACKGANO       |                                                  |
| 2020-01-08 | 19            | 47                | CIZZZATROPEX   | APPLIED           | CIZZZATROPEX   | Looking very good, remember to ask Matt about it |
| 2020-01-08 | 19            | 47                | BAKKANT        | INTERVIEW         | BAKKANT        |                                                  |
| 2020-01-08 | 19            | 47                | SOAOK          | REJECTED          | SOAOK          |                                                  |
| 2020-01-09 | 18            | 48                | DOZENER        | REJECTED          | DOZENER        |                                                  |
| 2020-01-09 | 18            | 48                | BUBUCUCURUCUS2 | APPLIED           | BUBUCUCURUCUS2 |                                                  |
| 2020-01-09 | 18            | 48                | FUSTIN         | APPLIED           | FUSTIN         |                                                  |
| 2020-01-09 | 18            | 48                | AVINU2         | INTERVIEW         | AVINU          |                                                  |
| 2020-01-09 | 18            | 48                | VAVIT          | APPLIED           | VAVIT          |                                                  |
| 2020-01-10 | 17            | 49                | CIZZZATROPEX   | INTERVIEW         | CIZZZATROPEX   | Looking very good, remember to ask Matt about it |
| 2020-01-10 | 17            | 49                | LOROPE         | APPLIED           | LOROPE         |                                                  |
| 2020-01-10 | 17            | 49                | BUKULURUPOX    | REJECTED          | BUKULURUPOX    |                                                  |
| 2020-01-10 | 17            | 49                | PULE           | INTERVIEW         | PULE           |                                                  |
| 2020-01-10 | 17            | 49                | PULE           | EXERCISE\_REQUEST | PULE           |                                                  |
| 2020-01-10 | 17            | 49                | CIZZZATROPEX   | EXERCISE\_REQUEST | CIZZZATROPEX   | Looking very good, remember to ask Matt about it |
| 2020-01-12 | 15            | 51                | CIZZZATROPEX   | EXERCISE\_DONE    | CIZZZATROPEX   | Looking very good, remember to ask Matt about it |
| 2020-01-13 | 14            | 52                | LEFTR          | REJECTED          | LEFTR          |                                                  |
| 2020-01-13 | 14            | 52                | FLIZZOG        | REJECTED          | FLIZZOG        |                                                  |
| 2020-01-13 | 14            | 52                | BAKKANT        | EXERCISE\_REQUEST | BAKKANT        |                                                  |
| 2020-01-13 | 14            | 52                | BAKKANT        | EXERCISE\_DONE    | BAKKANT        |                                                  |
| 2020-01-13 | 14            | 52                | REPROCA        | INTERVIEW         | REPROCA        |                                                  |
| 2020-01-13 | 14            | 52                | PULE           | EXERCISE\_DONE    | PULE           |                                                  |
| 2020-01-14 | 13            | 53                | LOGOPOTE       | APPLIED           | LOGOPOTE       |                                                  |
| 2020-01-14 | 13            | 53                | CIZZZATROPEX   | INTERVIEW         | CIZZZATROPEX   | Looking very good, remember to ask Matt about it |
| 2020-01-14 | 13            | 53                | VAVIT          | REJECTED          | VAVIT          |                                                  |
| 2020-01-15 | 12            | 54                | LOROPE         | INTERVIEW         | LOROPE         |                                                  |
| 2020-01-15 | 12            | 54                | WOWAWEWIWUPR   | INTERVIEW         | WOWAWEWIWUPR   |                                                  |
| 2020-01-15 | 12            | 54                | LOGOPOTE       | INTERVIEW         | LOGOPOTE       |                                                  |
| 2020-01-15 | 12            | 54                | BORNEMASTEROR  | APPLIED           | BORNEMASTEROR  |                                                  |
| 2020-01-15 | 12            | 54                | BUBUCUCURUCUS3 | APPLIED           | BUBUCUCURUCUS3 |                                                  |
| 2020-01-15 | 12            | 54                | GHOOPOHOOZU    | APPLIED           | GHOOPOHOOZU    |                                                  |
| 2020-01-15 | 12            | 54                | ESPELUZAN      | APPLIED           | ESPELUZAN      |                                                  |
| 2020-01-16 | 11            | 55                | LOROPE         | EXERCISE\_REQUEST | LOROPE         |                                                  |
| 2020-01-16 | 11            | 55                | LOROPE         | EXERCISE\_DONE    | LOROPE         |                                                  |
| 2020-01-16 | 11            | 55                | REPROCA        | REJECTED          | REPROCA        |                                                  |
| 2020-01-16 | 11            | 55                | CIZZZATROPEX   | INTERVIEW         | CIZZZATROPEX   | Looking very good, remember to ask Matt about it |
| 2020-01-17 | 10            | 56                | BAKKANT        | INTERVIEW         | BAKKANT        |                                                  |
| 2020-01-20 | 7             | 59                | CIZZZATROPEX   | INTERVIEW         | CIZZZATROPEX   | Looking very good, remember to ask Matt about it |
| 2020-01-20 | 7             | 59                | WOWAWEWIWUPR   | REJECTED          | WOWAWEWIWUPR   |                                                  |
| 2020-01-20 | 7             | 59                | PULE           | REJECTED          | PULE           |                                                  |
| 2020-01-20 | 7             | 59                | SLICEMACHINE   | REJECTED          | None           | None                                             |
| 2020-01-21 | 6             | 60                | BAKKANT        | INTERVIEW         | BAKKANT        |                                                  |
| 2020-01-22 | 5             | 61                | CIZZZATROPEX   | OFFER             | CIZZZATROPEX   | Looking very good, remember to ask Matt about it |
| 2020-01-24 | 3             | 63                | AGINTE2        | INTERVIEW         | AGINTE         |                                                  |
| 2020-01-27 | 0             | 66                | PEMBROTHER     | INTERVIEW         | PEMBROTHER     |                                                  |
| 2020-01-28 | \-1           | 67                | AVINU2         | INTERVIEW         | AVINU          |                                                  |

This lists active jobs (which have an event other than `APPLIED` and
which have not been `REJECTED` or `DECLINED`), with date of the last
event and
headline.

| job          | company      | headline                                         | found\_on  | last\_event |
| ------------ | ------------ | ------------------------------------------------ | ---------- | ----------- |
| AVINU2       | AVINU        |                                                  | LINKEDIN   | 2020-01-28  |
| PEMBROTHER   | PEMBROTHER   |                                                  | LINKEDIN   | 2020-01-27  |
| AGINTE2      | AGINTE       |                                                  |            | 2020-01-24  |
| CIZZZATROPEX | CIZZZATROPEX | Looking very good, remember to ask Matt about it | RECRUITER3 | 2020-01-22  |
| BAKKANT      | BAKKANT      |                                                  | FRIEND3    | 2020-01-21  |
| LOROPE       | LOROPE       |                                                  | LINKEDIN   | 2020-01-16  |
| LOGOPOTE     | LOGOPOTE     |                                                  | RECRUITER4 | 2020-01-15  |
| MARTER       | MARTER       |                                                  | SO         | 2019-12-19  |
| AVINU        | AVINU        |                                                  | LINKEDIN   | 2019-12-17  |
| NASTIPE      | NASTIPE      | Interesting, but I don’t like their mission      | RECRUITER2 | 2019-12-04  |
| AGINTE       | AGINTE       |                                                  |            | 2019-11-29  |
| YAKILIUMER   | YAKILIUMER   |                                                  | WWR        | 2019-11-25  |

This is a referrer report. Shows how many applications done through each
referrer and date of last application (to see if you should check that
referrer again).

| found\_on  | last\_applied | applications |
| ---------- | ------------- | ------------ |
| FRIEND1    | 2019-11-25    | 1            |
| WWR        | 2019-11-25    | 7            |
| SOMEREDDIT | 2019-11-26    | 1            |
| FRIEND2    | 2019-11-27    | 1            |
| RECRUITER  | 2019-11-27    | 1            |
| SO         | 2019-11-29    | 4            |
| RECRUITER2 | 2019-12-03    | 1            |
|            | 2019-12-09    | 13           |
| FRIEND3    | 2019-12-27    | 1            |
| RECRUITER3 | 2020-01-08    | 2            |
| ANGELCO    | 2020-01-09    | 1            |
| RECRUITER4 | 2020-01-14    | 1            |
| INDEED     | 2020-01-15    | 1            |
| INFOJOBS   | 2020-01-15    | 6            |
| LINKEDIN   | 2020-01-15    | 45           |
| SLACK1     | 2020-01-15    | 3            |

Counts applications per week:

| weeks\_from\_start | applications |
| ------------------ | ------------ |
| 0                  | 29           |
| 1                  | 10           |
| 2                  | 6            |
| 3                  | 11           |
| 4                  | 5            |
| 5                  | 1            |
| 6                  | 21           |
| 7                  | 6            |

Counts event types:

| event             | quantity |
| ----------------- | -------- |
| APPLIED           | 89       |
| DECLINED          | 2        |
| EMAILS            | 5        |
| EXERCISE\_DONE    | 9        |
| EXERCISE\_REQUEST | 9        |
| INTERVIEW         | 32       |
| OFFER             | 2        |
| REJECTED          | 29       |

Groups job applications by their “event log”. For instance, jobs where
you `APPLY`ed and there was no response, `REJECTED` after `APPLY`,
etc.

| events                                                                                        | instances | jobs                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| --------------------------------------------------------------------------------------------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| APPLIED                                                                                       | 47        | AGUSAPARTE, ALBICIOUS, ARBORPALE, AZZOOMR, BLUEPOD, BOOG, BOOR, BORNEMASTEROR, BUBONICA, BUBUCUCURUCUS2, BUBUCUCURUCUS3, COCOPARNABURN, CRYPTOBER, CUCUPORI, DEMOVUR, DOZENER2, ESPELUZAN, FGHTANIO, FLUZ, FOOLAMINASTE, FRAMEPORCOCO, FREPULATORING, FROSTYMAN, FUSTIN, GABORLENOR, GHOOPOHOOZU, HOOROOPO, JUJUP, METACERO, NACE, NACE2, NEXTPUPUS, NIXX, PACKGANO, PIXXOTE, POKERCONNOR, PORESORE, PUNNY, PUXXONA, QOOBAR, REAITOR, ROBEDOBE, ROTEBOTEDO, ROTEBOTEDO2, SYMILE, VIVIZONI, XAXAPO |
| APPLIED, REJECTED                                                                             | 18        | AMBITRI, AVUURA, COREDUL, DOZENER, GANO, GOOMDOR, IDIOZZY, ISOLOO, LEFTR, PERALTA, REPOZOO, ROBOCADRE, SUCORER, UNILANE, UNILANE2, VAVIT, WOOBOORT, ZOOXOR                                                                                                                                                                                                                                                                                                                                        |
| APPLIED, INTERVIEW, REJECTED                                                                  | 4         | ANOR, FLIZZOG, LETOPE, WOWAWEWIWUPR                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| APPLIED, INTERVIEW                                                                            | 3         | AVINU, LOGOPOTE, NASTIPE                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| APPLIED, INTERVIEW, INTERVIEW                                                                 | 2         | AGINTE2, AVINU2                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| APPLIED, DECLINED                                                                             | 1         | COCE                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| APPLIED, EMAILS                                                                               | 1         | YAKILIUMER                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| APPLIED, EMAILS, INTERVIEW                                                                    | 1         | AGINTE                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| APPLIED, EMAILS, INTERVIEW, EXERCISE\_REQUEST, EXERCISE\_DONE, INTERVIEW, REJECTED            | 1         | REPROCA                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| APPLIED, EMAILS, INTERVIEW, INTERVIEW, OFFER, DECLINED                                        | 1         | FLEMATE                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| APPLIED, EMAILS, REJECTED                                                                     | 1         | SOAOK                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| APPLIED, EXERCISE\_REQUEST, EXERCISE\_DONE, INTERVIEW                                         | 1         | MARTER                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| APPLIED, EXERCISE\_REQUEST, EXERCISE\_DONE, REJECTED                                          | 1         | BOKEMOKETOPER                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| APPLIED, INTERVIEW, EXERCISE\_REQUEST, EXERCISE\_DONE                                         | 1         | LOROPE                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| APPLIED, INTERVIEW, EXERCISE\_REQUEST, EXERCISE\_DONE, INTERVIEW                              | 1         | PEMBROTHER                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| APPLIED, INTERVIEW, EXERCISE\_REQUEST, EXERCISE\_DONE, INTERVIEW, INTERVIEW                   | 1         | BAKKANT                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| APPLIED, INTERVIEW, EXERCISE\_REQUEST, EXERCISE\_DONE, INTERVIEW, INTERVIEW, INTERVIEW, OFFER | 1         | CIZZZATROPEX                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| APPLIED, INTERVIEW, EXERCISE\_REQUEST, EXERCISE\_DONE, INTERVIEW, REJECTED                    | 1         | BUKULURUPOX                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| APPLIED, INTERVIEW, EXERCISE\_REQUEST, EXERCISE\_DONE, REJECTED                               | 1         | PULE                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| APPLIED, INTERVIEW, INTERVIEW, REJECTED                                                       | 1         | SYLER                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| REJECTED                                                                                      | 1         | SLICEMACHINE                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
