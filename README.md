[//]: # (Image References)
[image_overview]: ./misc/weka_overview.png

# Weka document classification
![process overview][image_overview] 
Convert `.txt` files into weka accepted `.arff` files then classify the documents into four categories.

## Strategy
Project information as well as a guided walk through can be found in `./report.pdf`.

## Use
- The python conversion is hard coded to read specific files in `./input/`, convert them, then write the output to `./output/`.
- To use WEKA, please download weka from [here](http://www.cs.waikato.ac.nz/ml/weka/).  Then follow the highlighted instructions included in `./report.pdf`

## Note:
The conversion input expects a specified input.  This could be easily modified in `./convert_txt_to_arff_specific.py`.  Notes about this input format are included in the `report.pdf`