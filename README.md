# ICS_FileFilterer
This script allows to filter events of multiple `.ics` files and create a new file with all the filtered events of the 
input files.

## Run instructions
All the settings are editable in the `settings.json` file:
* `calendar_files`: here you can put the path of every 
single file.
* `conditions`: here you can set custom conditions for each different parameter of an `ics` event. Each property has
`in` and `not_in` lists because there you can add your custom condition and it will be used based on `in` or `not_in`.
These are the properties:
    * `location`
    * `summaries`
    * `descriptions`
    * `dtstarts`
    * `dtends`
    * `exdates`
* `verbose`: this one is for debugging purpose: if is setted to true, when you run the script you will be notified of the
various operations that have been done.
* `cursor`: here you can customize the cursor of the log that will be printed if `verbose` is true.
* `output_file`: here you can insert the path for the output file. If the output file already exists it will be 
overwritten.
