# README #

This idea was born because of the need for a simple tool in order to automate the execution of simple log analysis obtained from Nokia SROS routers. The tool reads the content of a log in `txt` or `json` format, parses only pre defined variables and does the comparison, thus verifying if there are changes in such variables . The logs are generated by the use of [taskAutom](https://github.com/laimaretto/taskAutom).

# Setup ##

#### System Libraries
These libraries have been tested under Ubuntu 20.04 and Python3.8.

```bash
sudo pip3 install logChecker
```

# Usage

The program needs two mandatory inputs:
  - a folder which contains the parsing templates, either in `textFSM` or `ttp` format;
  - a folder, which contains the logs obtained a router, via [`taskAutom`](https://github.com/laimaretto/taskAutom). Though not mandatory, `taskAutom` is suggested as a way of obtaining the logs, because these can be stored in a `json` file.

### Templates

The templates are stored by default under the `Templates/` folder. logChecker reads either the CSV or the template folder to perform the function of parsing.

To find out a set of Templates that can be used, see [`here`](https://github.com/laimaretto/logTemplates)

It is possible to use a separate file to specify which templates to use, such as.

```csv
show_router_bgp_summary.template
show_router_interface.template
show_service_sdp.template
```
If omitted, all the templates insisde the templates folder, will be used.

# Results

If `logChecker` is invoked only with option `-pre`, reads the specific content in the log folder for a given command and then saves the results in an Excel report. We need to specify format of the logs, either `-json yes|no` and also the parsing engine, either `-te textFSM|ttp`. Also, the folder where the templates are located, with `-tf Folder`.

```bash
$ python3 logChecker.py -csv templateExample.csv -pre folderLogs/ -json yes -te ttp -tf TemplatesTTP/

<_io.TextIOWrapper name='Templates/nokia_sros_show_service_sdp-using.template' mode='r' encoding='UTF-8'>
#####Plantillas Cargadas Exitosamente#####
#########Logs Cargados Exitosamente#########
ROUTER_EXAMPLE_rx.txt nokia_sros_show_service_sdp-using.template
#
#
Saving Excel
#
```
On the other hand, if `logChecker` is invoked with folder `-pre` and `-post`, it compares the content of pre and post log folders, such as if we run checks to see the status of the routers before and after a task, and then saves the results in an Excel report.

```bash
$ python3 logChecker.py -csv templateExample.csv -pre folderLogsBefore/ -post folderLogsAfter/ -json yes --te textFSM -tf TemplatesFSM/

<_io.TextIOWrapper name='Templates/nokia_sros_show_service_sdp-using.template' mode='r' encoding='UTF-8'>
#####Plantillas Cargadas Exitosamente#####
#########Logs Cargados Exitosamente#########
#########Logs Cargados Exitosamente#########
ROUTER_EXAMPLE_rx.txt nokia_sros_show_service_sdp-using.template
ROUTER_EXAMPLE_rx.txt nokia_sros_show_service_sdp-using.template
#
#
Saving Excel
#
```

## Configuration Options

`logChecker` can be configured through CLI as shown below.

```bash
$ python3 logChecker.py -h
usage: PROG [options]

Log Analysis

optional arguments:
  -h, --help            show this help message and exit
  -pre PREFOLDER, --preFolder PREFOLDER
                        Folder with PRE Logs. Must end in "/"
  -post POSTFOLDER, --postFolder POSTFOLDER
                        Folder with POST Logs. Must end in "/"
  -csv CSVTEMPLATE, --csvTemplate CSVTEMPLATE
                        CSV with list of templates names to be used in parsing. If the file is omitted, then all the templates inside --templateFolder, will be considered for parsing. Default=None.
  -json {yes,no}, --formatJson {yes,no}
                        logs in json format: yes or no. Default=yes.
  -tf TEMPLATEFOLDER, --templateFolder TEMPLATEFOLDER
                        Folder where templates reside. Used both for PRE and POST logs. Default=Templates/
  -tf-post TEMPLATEFOLDERPOST, --templateFolderPost TEMPLATEFOLDERPOST
                        If set, use this folder of templates for POST logs. Default=Templates/
  -te {ttp,textFSM}, --templateEngine {ttp,textFSM}
                        Engine for parsing. Default=textFSM.
  -ri {name,ip,both}, --routerId {name,ip,both}
                        Router Id to be used within the tables in the Excel report. Default=name.
  -v, --version         Version
```
