# Introduction

This is an adaptation of the document I used to track my last job search. The
names of companies have been scrubbed and I have made a few modifications to
make a better example.

After installing `pandocsql`, you can process this document with:

```
$ pandoc job-search.md -F pandocsql -o job-search.html
```

You can see the output [here](job-search-output.md)

# Data entry

This is the main table tracking jobs you have applied to. I had a URL pointing
to the offer, but faking that data sounded useless so I removed it. This can
handle multiple jobs from the same company. Extra columns could be added to track
job properties, etc.

| job            | company        |  headline                                           | found_on    |
| -------------- | -------------- |  -------------------------------------------------- | ----------- |
| METACERO       | METACERO       |  Text to display in some reports... status, etc.    | LINKEDIN    |
| CRYPTOBER      | CRYPTOBER      |                                                     |             |
| UNILANE        | UNILANE        |                                                     |             |
| IDIOZZY        | IDIOZZY        |                                                     |             |
| ISOLOO         | ISOLOO         |                                                     |             |
| DEMOVUR        | DEMOVUR        |                                                     |             |
| AGINTE         | AGINTE         |                                                     |             |
| ALBICIOUS      | ALBICIOUS      |                                                     |             |
| AMBITRI        | AMBITRI        |                                                     | WWR         |
| SYMILE         | SYMILE         |                                                     | WWR         |
| YAKILIUMER     | YAKILIUMER     |                                                     | WWR         |
| FLEMATE        | FLEMATE        |                                                     | FRIEND1     |
| BLUEPOD        | BLUEPOD        |                                                     | WWR         |
| GABORLENOR     | GABORLENOR     |                                                     | WWR         |
| ROBOCADRE      | ROBOCADRE      |                                                     | WWR         |
| GOOMDOR        | GOOMDOR        |                                                     | WWR         |
| ROTEBOTEDO     | ROTEBOTEDO     |                                                     | LINKEDIN    |
| PEMBROTHER     | PEMBROTHER     |                                                     | LINKEDIN    |
| BOKEMOKETOPER  | BOKEMOKETOPER  |                                                     | LINKEDIN    |
| GANO           | GANO           |                                                     | LINKEDIN    |
| SUCORER        | SUCORER        |                                                     | SOMEREDDIT  |
| REPOZOO        | REPOZOO        |                                                     | INFOJOBS    |
| AVUURA         | AVUURA         |                                                     | INFOJOBS    |
| UNILANE2       | UNILANE        |                                                     |             |
| ROBEDOBE       | ROBEDOBE       |                                                     | LINKEDIN    |
| ANOR           | ANOR           |                                                     | FRIEND2     |
| LETOPE         | LETOPE         |                                                     |             |
| AGUSAPARTE     | AGUSAPARTE     |                                                     |             |
| NACE           | NACE           |                                                     | RECRUITER   |
| FOOLAMINASTE   | FOOLAMINASTE   |                                                     | LINKEDIN    |
| BOOG           | BOOG           |                                                     | SO          |
| COREDUL        | COREDUL        |                                                     | SO          |
| MARTER         | MARTER         |                                                     | SO          |
| POKERCONNOR    | POKERCONNOR    |                                                     | SO          |
| PORESORE       | PORESORE       |                                                     | LINKEDIN    |
| NASTIPE        | NASTIPE        | Interesting, but I don't like their mission         | RECRUITER2  |
| COCOPARNABURN  | COCOPARNABURN  |                                                     | LINKEDIN    |
| ZOOXOR         | ZOOXOR         |                                                     | LINKEDIN    |
| AGINTE2        | AGINTE         |                                                     |             |
| ARBORPALE      | ARBORPALE      |                                                     | LINKEDIN    |
| WOOBOORT       | WOOBOORT       |                                                     | LINKEDIN    |
| SYLER          | SYLER          |                                                     |             |
| COCE           | COCE           |                                                     |             |
| HOOROOPO       | HOOROOPO       |                                                     | LINKEDIN    |
| NACE2          | NACE           |                                                     | LINKEDIN    |
| FGHTANIO       | FGHTANIO       |                                                     | LINKEDIN    |
| AVINU          | AVINU          |                                                     | LINKEDIN    |
| BUKULURUPOX    | BUKULURUPOX    |                                                     | LINKEDIN    |
| JUJUP          | JUJUP          |                                                     | LINKEDIN    |
| FRAMEPORCOCO   | FRAMEPORCOCO   |                                                     | LINKEDIN    |
| REPROCA        | REPROCA        |                                                     | LINKEDIN    |
| PUXXONA        | PUXXONA        |                                                     | LINKEDIN    |
| ROTEBOTEDO2    | ROTEBOTEDO     |                                                     | LINKEDIN    |
| PERALTA        | PERALTA        |                                                     | LINKEDIN    |
| DOZENER        | DOZENER        |                                                     | LINKEDIN    |
| SOAOK          | SOAOK          |                                                     | SLACK1      |
| NEXTPUPUS      | NEXTPUPUS      |                                                     | LINKEDIN    |
| DOZENER2       | DOZENER        |                                                     | LINKEDIN    |
| CUCUPORI       | CUCUPORI       |                                                     | LINKEDIN    |
| VIVIZONI       | VIVIZONI       |                                                     | LINKEDIN    |
| FREPULATORING  | FREPULATORING  |                                                     | LINKEDIN    |
| BAKKANT        | BAKKANT        |                                                     | FRIEND3     |
| BUBONICA       | BUBONICA       |                                                     | LINKEDIN    |
| REAITOR        | REAITOR        |                                                     | LINKEDIN    |
| FLIZZOG        | FLIZZOG        |                                                     | LINKEDIN    |
| BOOR           | BOOR           |                                                     | LINKEDIN    |
| FROSTYMAN      | FROSTYMAN      |                                                     | LINKEDIN    |
| PUNNY          | PUNNY          |                                                     | LINKEDIN    |
| XAXAPO         | XAXAPO         |                                                     | INFOJOBS    |
| QOOBAR         | QOOBAR         |                                                     | LINKEDIN    |
| PIXXOTE        | PIXXOTE        |                                                     | LINKEDIN    |
| AZZOOMR        | AZZOOMR        |                                                     | LINKEDIN    |
| NIXX           | NIXX           |                                                     | LINKEDIN    |
| PULE           | PULE           |                                                     | SLACK1      |
| FLUZ           | FLUZ           |                                                     | LINKEDIN    |
| AVINU2         | AVINU          |                                                     | LINKEDIN    |
| WOWAWEWIWUPR   | WOWAWEWIWUPR   |                                                     | INFOJOBS    |
| LEFTR          | LEFTR          |                                                     | INFOJOBS    |
| PACKGANO       | PACKGANO       |                                                     | RECRUITER3  |
| CIZZZATROPEX   | CIZZZATROPEX   | Looking very good, remember to ask Matt about it    | RECRUITER3  |
| BUBUCUCURUCUS2 | BUBUCUCURUCUS2 |                                                     | LINKEDIN    |
| FUSTIN         | FUSTIN         |                                                     | LINKEDIN    |
| VAVIT          | VAVIT          |                                                     | ANGELCO     |
| LOROPE         | LOROPE         |                                                     | LINKEDIN    |
| LOGOPOTE       | LOGOPOTE       |                                                     | RECRUITER4  |
| BORNEMASTEROR  | BORNEMASTEROR  |                                                     | SLACK1      |
| BUBUCUCURUCUS3 | BUBUCUCURUCUS3 |                                                     | LINKEDIN    |
| GHOOPOHOOZU    | GHOOPOHOOZU    |                                                     | INFOJOBS    |
| ESPELUZAN      | ESPELUZAN      |                                                     | INDEED      |

Table: jobs

The other table is for job events. The job column should match the job column
in the table above.

| job            | event            | ts         |
| -------------- | ---------------- | ---------- |
| METACERO       | APPLIED          | 2019-11-22 |
| CRYPTOBER      | APPLIED          | 2019-11-25 |
| UNILANE        | APPLIED          | 2019-11-25 |
| IDIOZZY        | APPLIED          | 2019-11-25 |
| ISOLOO         | APPLIED          | 2019-11-25 |
| DEMOVUR        | APPLIED          | 2019-11-25 |
| AGINTE         | APPLIED          | 2019-11-25 |
| ALBICIOUS      | APPLIED          | 2019-11-25 |
| AMBITRI        | APPLIED          | 2019-11-25 |
| AMBITRI        | REJECTED         | 2019-11-25 |
| SYMILE         | APPLIED          | 2019-11-25 |
| YAKILIUMER     | APPLIED          | 2019-11-25 |
| FLEMATE        | APPLIED          | 2019-11-25 |
| BLUEPOD        | APPLIED          | 2019-11-25 |
| YAKILIUMER     | EMAILS           | 2019-11-25 |
| GABORLENOR     | APPLIED          | 2019-11-25 |
| ROBOCADRE      | APPLIED          | 2019-11-25 |
| GOOMDOR        | APPLIED          | 2019-11-25 |
| ROTEBOTEDO     | APPLIED          | 2019-11-26 |
| PEMBROTHER     | APPLIED          | 2019-11-26 |
| BOKEMOKETOPER  | APPLIED          | 2019-11-26 |
| GANO           | APPLIED          | 2019-11-26 |
| FLEMATE        | EMAILS           | 2019-11-26 |
| SUCORER        | APPLIED          | 2019-11-26 |
| REPOZOO        | APPLIED          | 2019-11-26 |
| AVUURA         | APPLIED          | 2019-11-26 |
| UNILANE        | REJECTED         | 2019-11-26 |
| AGINTE         | EMAILS           | 2019-11-27 |
| AVUURA         | REJECTED         | 2019-11-27 |
| UNILANE2       | APPLIED          | 2019-11-27 |
| SUCORER        | REJECTED         | 2019-11-27 |
| ROBEDOBE       | APPLIED          | 2019-11-27 |
| ANOR           | APPLIED          | 2019-11-27 |
| LETOPE         | APPLIED          | 2019-11-27 |
| AGUSAPARTE     | APPLIED          | 2019-11-27 |
| BOKEMOKETOPER  | EXERCISE_REQUEST | 2019-11-27 |
| NACE           | APPLIED          | 2019-11-27 |
| ISOLOO         | REJECTED         | 2019-11-27 |
| IDIOZZY        | REJECTED         | 2019-11-27 |
| GANO           | REJECTED         | 2019-11-28 |
| AGINTE         | INTERVIEW        | 2019-11-29 |
| FOOLAMINASTE   | APPLIED          | 2019-11-29 |
| BOOG           | APPLIED          | 2019-11-29 |
| COREDUL        | APPLIED          | 2019-11-29 |
| MARTER         | APPLIED          | 2019-11-29 |
| POKERCONNOR    | APPLIED          | 2019-11-29 |
| LETOPE         | INTERVIEW        | 2019-11-29 |
| PORESORE       | APPLIED          | 2019-12-01 |
| REPOZOO        | REJECTED         | 2019-12-02 |
| LETOPE         | REJECTED         | 2019-12-02 |
| COREDUL        | REJECTED         | 2019-12-02 |
| ROBOCADRE      | REJECTED         | 2019-12-02 |
| NASTIPE        | APPLIED          | 2019-12-03 |
| UNILANE2       | REJECTED         | 2019-12-03 |
| ANOR           | INTERVIEW        | 2019-12-03 |
| FLEMATE        | INTERVIEW        | 2019-12-04 |
| NASTIPE        | INTERVIEW        | 2019-12-04 |
| GOOMDOR        | REJECTED         | 2019-12-04 |
| COCOPARNABURN  | APPLIED          | 2019-12-05 |
| ZOOXOR         | APPLIED          | 2019-12-05 |
| AGINTE2        | APPLIED          | 2019-12-05 |
| BOKEMOKETOPER  | EXERCISE_DONE    | 2019-12-05 |
| ARBORPALE      | APPLIED          | 2019-12-06 |
| WOOBOORT       | APPLIED          | 2019-12-06 |
| ANOR           | REJECTED         | 2019-12-09 |
| FLEMATE        | INTERVIEW        | 2019-12-09 |
| FLEMATE        | OFFER            | 2019-12-09 |
| SYLER          | APPLIED          | 2019-12-09 |
| COCE           | APPLIED          | 2019-12-09 |
| HOOROOPO       | APPLIED          | 2019-12-09 |
| BOKEMOKETOPER  | REJECTED         | 2019-12-10 |
| WOOBOORT       | REJECTED         | 2019-12-10 |
| MARTER         | EXERCISE_REQUEST | 2019-12-10 |
| MARTER         | EXERCISE_DONE    | 2019-12-10 |
| SYLER          | INTERVIEW        | 2019-12-11 |
| SYLER          | INTERVIEW        | 2019-12-12 |
| NACE2          | APPLIED          | 2019-12-12 |
| PEMBROTHER     | INTERVIEW        | 2019-12-13 |
| PEMBROTHER     | EXERCISE_REQUEST | 2019-12-13 |
| PEMBROTHER     | EXERCISE_DONE    | 2019-12-15 |
| SYLER          | REJECTED         | 2019-12-16 |
| FGHTANIO       | APPLIED          | 2019-12-16 |
| AVINU          | APPLIED          | 2019-12-16 |
| BUKULURUPOX    | APPLIED          | 2019-12-16 |
| JUJUP          | APPLIED          | 2019-12-16 |
| FRAMEPORCOCO   | APPLIED          | 2019-12-17 |
| REPROCA        | APPLIED          | 2019-12-17 |
| PUXXONA        | APPLIED          | 2019-12-17 |
| BUKULURUPOX    | INTERVIEW        | 2019-12-17 |
| AVINU          | INTERVIEW        | 2019-12-17 |
| FLEMATE        | DECLINED         | 2019-12-17 |
| ROTEBOTEDO2    | APPLIED          | 2019-12-18 |
| PERALTA        | APPLIED          | 2019-12-18 |
| DOZENER        | APPLIED          | 2019-12-18 |
| BUKULURUPOX    | EXERCISE_REQUEST | 2019-12-18 |
| AGINTE2        | INTERVIEW        | 2019-12-18 |
| REPROCA        | EMAILS           | 2019-12-19 |
| BUKULURUPOX    | EXERCISE_DONE    | 2019-12-19 |
| MARTER         | INTERVIEW        | 2019-12-19 |
| SOAOK          | APPLIED          | 2019-12-19 |
| COCE           | DECLINED         | 2019-12-20 |
| NEXTPUPUS      | APPLIED          | 2019-12-20 |
| DOZENER2       | APPLIED          | 2019-12-20 |
| PERALTA        | REJECTED         | 2019-12-20 |
| CUCUPORI       | APPLIED          | 2019-12-23 |
| VIVIZONI       | APPLIED          | 2019-12-26 |
| FREPULATORING  | APPLIED          | 2019-12-26 |
| BAKKANT        | APPLIED          | 2019-12-27 |
| REPROCA        | INTERVIEW        | 2019-12-27 |
| BUBONICA       | APPLIED          | 2020-01-03 |
| REAITOR        | APPLIED          | 2020-01-03 |
| FLIZZOG        | APPLIED          | 2020-01-03 |
| BOOR           | APPLIED          | 2020-01-03 |
| FROSTYMAN      | APPLIED          | 2020-01-03 |
| PUNNY          | APPLIED          | 2020-01-03 |
| XAXAPO         | APPLIED          | 2020-01-03 |
| QOOBAR         | APPLIED          | 2020-01-03 |
| PIXXOTE        | APPLIED          | 2020-01-03 |
| AZZOOMR        | APPLIED          | 2020-01-03 |
| NIXX           | APPLIED          | 2020-01-03 |
| PULE           | APPLIED          | 2020-01-03 |
| FLIZZOG        | INTERVIEW        | 2020-01-07 |
| BUKULURUPOX    | INTERVIEW        | 2020-01-07 |
| FLUZ           | APPLIED          | 2020-01-07 |
| AVINU2         | APPLIED          | 2020-01-07 |
| WOWAWEWIWUPR   | APPLIED          | 2020-01-07 |
| LEFTR          | APPLIED          | 2020-01-07 |
| ZOOXOR         | REJECTED         | 2020-01-07 |
| REPROCA        | EXERCISE_REQUEST | 2020-01-08 |
| REPROCA        | EXERCISE_DONE    | 2020-01-08 |
| SOAOK          | EMAILS           | 2020-01-08 |
| PACKGANO       | APPLIED          | 2020-01-08 |
| CIZZZATROPEX   | APPLIED          | 2020-01-08 |
| BAKKANT        | INTERVIEW        | 2020-01-08 |
| SOAOK          | REJECTED         | 2020-01-08 |
| DOZENER        | REJECTED         | 2020-01-09 |
| BUBUCUCURUCUS2 | APPLIED          | 2020-01-09 |
| FUSTIN         | APPLIED          | 2020-01-09 |
| AVINU2         | INTERVIEW        | 2020-01-09 |
| VAVIT          | APPLIED          | 2020-01-09 |
| CIZZZATROPEX   | INTERVIEW        | 2020-01-10 |
| LOROPE         | APPLIED          | 2020-01-10 |
| BUKULURUPOX    | REJECTED         | 2020-01-10 |
| PULE           | INTERVIEW        | 2020-01-10 |
| PULE           | EXERCISE_REQUEST | 2020-01-10 |
| CIZZZATROPEX   | EXERCISE_REQUEST | 2020-01-10 |
| CIZZZATROPEX   | EXERCISE_DONE    | 2020-01-12 |
| LEFTR          | REJECTED         | 2020-01-13 |
| FLIZZOG        | REJECTED         | 2020-01-13 |
| BAKKANT        | EXERCISE_REQUEST | 2020-01-13 |
| BAKKANT        | EXERCISE_DONE    | 2020-01-13 |
| REPROCA        | INTERVIEW        | 2020-01-13 |
| PULE           | EXERCISE_DONE    | 2020-01-13 |
| LOGOPOTE       | APPLIED          | 2020-01-14 |
| CIZZZATROPEX   | INTERVIEW        | 2020-01-14 |
| VAVIT          | REJECTED         | 2020-01-14 |
| LOROPE         | INTERVIEW        | 2020-01-15 |
| WOWAWEWIWUPR   | INTERVIEW        | 2020-01-15 |
| LOGOPOTE       | INTERVIEW        | 2020-01-15 |
| BORNEMASTEROR  | APPLIED          | 2020-01-15 |
| BUBUCUCURUCUS3 | APPLIED          | 2020-01-15 |
| GHOOPOHOOZU    | APPLIED          | 2020-01-15 |
| ESPELUZAN      | APPLIED          | 2020-01-15 |
| LOROPE         | EXERCISE_REQUEST | 2020-01-16 |
| LOROPE         | EXERCISE_DONE    | 2020-01-16 |
| REPROCA        | REJECTED         | 2020-01-16 |
| CIZZZATROPEX   | INTERVIEW        | 2020-01-16 |
| BAKKANT        | INTERVIEW        | 2020-01-17 |
| CIZZZATROPEX   | INTERVIEW        | 2020-01-20 |
| WOWAWEWIWUPR   | REJECTED         | 2020-01-20 |
| PULE           | REJECTED         | 2020-01-20 |
| SLICEMACHINE   | REJECTED         | 2020-01-20 |
| BAKKANT        | INTERVIEW        | 2020-01-21 |
| CIZZZATROPEX   | OFFER            | 2020-01-22 |
| AGINTE2        | INTERVIEW        | 2020-01-24 |
| PEMBROTHER     | INTERVIEW        | 2020-01-27 |
| AVINU2         | INTERVIEW        | 2020-01-28 |

Table: job_events

# Reports

This table just lists all events, adding the job headline and days from the
first even and days to "now".

```pandocsql
with start_date(start_ts) as (select min(ts) from job_events)
select ts,
       (strftime('%s','2020-01-27') - strftime('%s', ts)) / (60*60*24) as days_to_now,
       (strftime('%s',ts) - strftime('%s', start_ts)) / (60*60*24) as days_from_start,
       job,
       event,
       company,
       headline
from (
    select ts, job, event, company, headline
    from job_events
    left join jobs using(job)
) all_events
join start_date
order by ts
```

This lists active jobs (which have an event other than `APPLIED` and which have
not been `REJECTED` or `DECLINED`), with date of the last event and headline.

```pandocsql
select job, company, headline, found_on, max(ts) as last_event 
from jobs
join job_events using (job)
where not exists (
    select 1
    from job_events
    where jobs.job = job_events.job
    and job_events.event in ('REJECTED', 'DECLINED')
)
and job_events.event not in ('APPLIED')
group by job, company, headline, found_on
order by last_event desc
```

This is a referrer report. Shows how many applications done through each referrer
and date of last application (to see if you should check that referrer again).

```pandocsql
select found_on, max(ts) as last_applied, count(*) as applications
from jobs
join job_events using (job)
where event = 'APPLIED'
group by found_on
order by max(ts)
```

Counts applications per week:

```pandocsql
with start_date(start_ts) as (select min(ts) from job_events)
select (strftime('%s',ts) - strftime('%s', start_ts)) / (60*60*24*7) as weeks_from_start, count(*) applications
from job_events
join start_date
where event = 'APPLIED'
group by (strftime('%s',ts) - strftime('%s', start_ts)) / (60*60*24*7)
order by (strftime('%s',ts) - strftime('%s', start_ts)) / (60*60*24*7)
```

Counts event types:

```pandocsql
select event, count(*) as quantity
from job_events
group by event
```

Groups job applications by their "event log". For instance, jobs where you
`APPLY`ed and there was no response, `REJECTED` after `APPLY`, etc.

```pandocsql
select events, count(*) as instances, group_concat(job, ', ') jobs
from (
    select job, group_concat(event, ', ') as events
    from job_events
    group by job
)
group by events
order by count(*) desc
```
