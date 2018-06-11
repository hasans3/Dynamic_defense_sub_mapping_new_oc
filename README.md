# Dynamic_defense_sub_mapping_new_oc

## How to run the main method `static_defense_substations_v1_test.py`?
  
To run the defense method, the following steps are needed:
1. `Install the OpenDSS` from  [Download Link](https://sourceforge.net/projects/electricdss/#Link) on the Windows machine as OpenDSS is not mac compatible.
2. `Download and save` the system models from the "System Models" folder to the local drive. 
3. `Install` Spyder, PyCharm or any other Python IDE.
4. `Install` all the necessary inbuilt python packages using `pip install package name`. Example `pip install numpy`.
5. `Open` the `static_defense_substations_v1_test.py` method and set the paths for the `filepath, comp_filename, load_file_name` as per the 
directory where the downloaded files are stored from the "System Models" folder. 

`filepath` is the path where `.dss` file is stored on the local drive.

`comp_filename` is the local drive path where `component_data_subs.txt` file is stored.

`load_file_name` is the path for the `load_data.txt` file stored on the local drive. For certain models the file name can be `load_data1.txt` or `load_data_testing1.txt`, etc.

6. Run `static_defense_substations_v1_test.py`.
