[4.5.3 - 2024-11-25]
- Remove function `searchDiffOnly`, parameter `showResults`, variables related to `showDiffColumns`
- Fix bug: update `ValueKeys` considering `filterColumns` when using filters
- Update `GENERAL_TEMPL_LINES`
- Add total time to run

[4.5.2 - 2024-11-24]

- When reading the parsgin textFSM templates, whenever a variable is identified as `Required` or `Filldown`, we consider such variable as a key column to color-identify it when looking for differences.

[4.5.0 - 2024-11-22]
- New parameter `ic` with default = no. If `ic` = yes, when running pre-post comparision, a new column `Idx Pre/Post` is added in the tables changes detected and major errors for specific templates, relating with the index from pre-post table. For generic templates, the column `Idx Pre/Post` is added regardless of the parameter `ic`.
- Changes in `searchDiffAll`:
    - For specific template: New function `obtain_idx_pre_post` to create new column in `dfCompl`. `obtain_idx_pre_post` detects the matching index from `dfPre` (when `Where` column equal to `left_only`) or `dfPost` (when `Where` equal to `right_only`);
    - For `general.template`: `tempComp` `level_0` renamed to `Idx Pre/Post`.
- `findMajor`: `reset_index` to maintain the standard with the other tables (pre-post side by side and changes detected).

[4.4.1 - 2024-10-22]
- Fix bug for assessment (only using -pre)

[4.4.0 - 2024-10-18]
- Creation of `diff_colors`, within `constructExcel`.
    - Equivalent lines (pre-post pair) are compared, and the cells that have different values are highlighted in red. 
    - Borders were added to the line pairs to make it easier to immediately identify which line corresponds to the "pre" and its "paired" post line.
- Added the option to create #Keys in the templates to activate the `diff_colors` function in the "changes detected" table. 
    - `ValueKeys` was added to the default template.

[4.3.3 - 2024-09-04]
- New function `mixAll()` in order to clean up the code.

[4.3.2 - 2024-09-03]
- Update `NO_MATCH`.
- Update the function detParseStatus to use Regex for identifying `No Matching Entries Found`.
- Update the `no_parsing` in `D_STATUS` from `Can't Parsing` to `Can't Parse`.

[4.3.1 - 2024-09-03]
- Update version (-v)

[4.3.0 - 2024-09-02]
- Introduced `matched_templates` list to accumulate matching templates during execution.
- Adjusted the logic for removing commands from `noMatchedCmdPerRtr` to ensure removal only occurs when applicable.
- Added a processing step to iterate over `matched_templates`, ensuring all matched templates are correctly handled.

[4.2.6 - 2024-06-26]
- Updating `searchDiffAll`, when using general templates with different shape, creating a `dfCompl`.

[4.2.5 - 2024-06-25]
- Updating `searchDiffAll` to better use `pd.compare` when GENERIC_TEMPLATE is being used.
- Global Variables `PRE` and `POST`.
- `/environment no more` will not be parsed.

[4.2.4 - 2024-06-25]
- Updating `searchDiffAll` to better use `pd.compare`. 
- The function `searchDiffOnly()` is no longer available.

[4.2.3 - 2024-06-25]
- Updating `searchDiffAll` and `searchDiffOnly`: adjustments for comparision.
    - When the template is not general, uses `pd.merge` to compare the data from pre and post dataFrames.
    - If it's general template with the same length for pre and post dataFrames, uses `compare` from `pandas`.
    - When using general template and the dataFrames don't have the same size, the comparision should be done by specific template.
- New `parseStatus` for when its necessary to use specific template.

[4.2.2 - 2024-06-14]
- Updating `parseResults`, fix bug with multiple routers with `general.template`:
    - Add: `dNoMatchedLog`, to save information of no-matched commands in new dictionary, with the same structure of dLog.
    - Add: `noMatchedCmdAllRtr` - To save all no-matched commands, independently of router
    - Changed: `noMatchedCommand` to `noMatchedCmdPerRtr`
    - New for loop to interact with `dNoMatchedLog`, where the `general.template` is used.

[4.2.1 - 2024-06-12]
- Moving `general.template` inside setup.py, then it was necessary to update:
    - `readTemplate`: to read this template correclty;
    - `makeParsed`: importing `io` to use in a condition, for `results_template` to work with this general template;
- `writeDfTemp`: parameter optimization.

[4.2.0 - 2024-06-11]
- Updating of `parseResults`, changing the order of 'for's: for each command, all templates are tested in `match = prog.search(cmdsLogs)`. In this way, the existence of command log determines the presence of the data in the excel sheet. In previous versions we used the reverse order, so to have data in excel, it was necessary to have the specific template to parse.
- New: Generic template.
    - If a command/log don't match with any template available in the specified folder with templates, the parsing is done with `general.template`, available in src. Add structure in `readTemplate`, `parseResults`;
    - As many sheets as needed can be created by generic template;
- `parseResults` with new functions `detParseStatus` and `writeDfTemp`;
- `datosEquipo[tmpltName]['template']` in `datosEquipo[tmpltName]`, to better identification in cases with generic template, when this key is related to `dTmplt`. For example, in `searchDiffAll`, `searchDiffOnly`, `findMajor`;
- Index: for better identification, column `Command` added. 


[4.1.0 - 2024-04-10]

- New structure for `datosEquipo[tmpltName]`. Now with `datosEquipo[tmpltName]['parseStatus']` and `datosEquipo[tmpltName]['dfResultDatos']`. Created for better detection of the new statuses of parsing. They specify "no parsing" cases;
- Removed changes section and major error section in exported sheets, when these sections are empty;
- More constants indicated in the beginning of the code and add descriptions in some functions.

[4.0.1 - 2024-03-20]

- Update of libs:
    - textfsm==1.1.3
    - pandas>=1.5.2,<=2.0.3
    - XlsxWriter>=3.0.3,<=3.2.0
    - ttp>=0.9.0,<=0.9.5

[3.7.2 - 2023-07-04]

- Update of lib `textFSM` to 1.1.3.


[3.7.1 - 2023-01-10]

- New function `renderAtp(dictParam)`. This funcion, when invoked, will generate a Word docx document, with the information obtained from the `pre` and/or `post` folders.


[3.6.1 - 2023-01-10]

- New function `searchDiffOnly(datosEquipoPre, datosEquipoPost, dTmplt, routerId)`. This funcion, when invoked, will show only different fields when a comparison is made.

[3.5.10 - 2022-12-04]

- New function `fncRun(dictParam)`. `dictParam` is a dictionary containing all the configuration parameters.

[3.5.9 - 2022-11-28]
- Update of libraries
    - `textfsm==1.1.2`
    - `pandas==1.5.2`
    - `XlsxWriter==3.0.3`
    - `ttp==0.9.0`

[3.5.8 - 2022-11-09]
- The calling for function `main()` was commented out, so the program runs once when installed by `pip` and invoked from CLI.


[3.5.6 - 2022-11-09]
- Better control on the folders for templates.

[3.5.3 - 2022-11-09]
- Better control on the folders for templates.

[3.5.2 - 2022-11-08]
- The parameters `-tf` and `-tf-post` can be set independently. If none are set, templates are looked for under `Templates/`. If not, logChecker will pay attention to either or both `-tf` and/or `-tf-post`.

[3.5.1 - 2022-10-23]
- Reoder of files

[3.5.0 - 2022-10-23]
- First version on `PyPI`.
- Renamed to `logChecker`.


[3.4.0 - 2022-09-27]
- Control keywords for the templates to control the resulting columns in each report.
- CLI paramter to control wether we want to use the name of the router, its IP adress, or both.
- The variable `NAME` has bee removed from each and every template for the different Timos versions.

[3.2.3 - 2022-08-11]
- Tables for differences and/or errors, are now sorted by all the column names defined under the template. This makes it easier to do the visual comparison of data.

[3.2.2 - 2022-08-02]
- When the amount of templates for pre vs post comparison is different, an exception ocurred. Either control this by using a csv file or having the same amount of templates in each template folder.

[3.2.1 - 2022-08-01]
- Typo.

[3.2.0 - 2022-08-01]
- In the definition of the templates files, a new comment must be included `#majorDown:`. This comment should be followed by the keywords.
    - Example: `#majorDown: open,connect` will also count for major down on the analysis.
- The default folder for templates is `Templates/` under the option `-tf`
- New options for folders: `-tf-post`. Some times, a different folder is needed for comparison, for example, when there is a operating system change between tasks. With this option, a different set of templates can be used for the `post` folder.

[3.1.2 - 2022-07-24]
- In function `parseResults()`, better detection of `json` files.
    - When the name had a dot `.` in its name, parsing was not being performed. Is solved now.

[3.1.1 - 2022-07-04]
- Parameter `-json` with default = yes.
- Updates on when platform is windows (equal to win64 or win32), to handle with paths correctly:
    - In function `readLog()`: update of listContent.
    - In function `main()`: condition to replace `/` in templateFolder

[3.1.0 - 2022-07-03]

- The folder of the templates can now be specified by the parameter `--templateFolder`. The default is `TemplatesTextFSM/`.
- The file `--csvTemplate` is now optional. If omitted, then all the templates under the folder `--templateFolder` will be considered for parsing.
- Templates can be of type `textFSM` or `ttp`. To choose, use the parameter `-te/--templateEngine`.
    - Be sure to point to the correct folder of templates, when changing the engine.


[3.0.0 - 2022-07-01]

- ReWrite of functions `readTemplate()` , `readLog()` and `parseResults()`.

[2.0.0 - 2022-06-24]

- Starting major version `2.0.0`.
- ReWrite of function `constructExcel()`
    - If data is empty, because parsing detected nothing, tab color is now blue. This will help identify easily when parsing is not working.
    - Nex `index` tab implemented, with hyperlinks to all sheets.

[2022-05-06]

- Function `readLog()` modified.
    - New paramterer `jsonFormat` to distinguish the type of the logs.
    - If the host OS is not Windows or Linux, quits.

- Function `readLogJson()` removed.

- Function `readTemplate()` not returning variable `results_template` anymore.

- Function `parseResults()` modified.
    - changes inside the funcion
    - better handling of `json` files
    - input parameter `read_template` removed

- File `templateShow.csv` to match the contents of the `Template` folder.
