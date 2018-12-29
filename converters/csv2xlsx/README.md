# file-converters
## CSV to XSLX

Compiling to obtain the JAR:

    cd csv2xlsx
    mvn package

You need to copy this content from target:

* File: Csv2Excel-X.X.X.jar
* Directory: lib

in order to execute converting tool:

    java -jar Csv2Excel-X.X.X.jar source.csv

### Example

Report generation from Oracle spooling:

* Creating sql query in `example-file.sql`:

```
alter session set NLS_DATE_FORMAT='DD/MM/YYYY';
alter session set NLS_TIMESTAMP_FORMAT='DD/MM/YYYY';
set colsep ";"
set heading on
set pagesize 0 embedded on
set trimspool off
set linesize 1000

/* Formatting columns (optional) */
/* col COLUMN_NAME format a50 */

set termout off
spool example-file.csv
select .... ;
spool off
```

* Executing spool into `example-file.csv`:

```
$> exit | sqlplus user/pass@server:port/sid @./example-file.sql
```

* CSV to XLSX:

```
$> head -1 example-file.csv > example-tmp.csv
$> tail -n +3 example-file.csv >> example-tmp.csv
$> mv example-tmp.csv example-file.csv
$> java -jar Csv2Excel.jar example-file.csv
```

All previous commands could be written in a [Jenkins](https://jenkins.io/) job to receive your report periodically by email! :bowtie:
