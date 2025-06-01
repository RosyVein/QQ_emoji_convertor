# QQ emoji convertor
Convert local emoji files into usable files for QQ on macOS.

Tested on QQ9 v.6.9.67-33259 App Store version. The way QQ store emoji files may change, please be cautious.



## Features

Convert emoji files downloaded by QQ into normal pictures files.

You can find emoji files in path:

`/Users/<user>/Library/Containers/com.tencent.qq/Data/Library/Application Support/QQ/nt_qq_<QQ_path_hash>/nt_data/Emoji/marketface`



The script will convert all emoji files within the folder and add a proper extension to the name.

*⚠️ This script may corrupt files, please backup first or use copies to run the script.*



## Todo

- Get the info about emoji from ~~market page~~ local JSON files local in `marketface/json`
  - Rename the folder to proper name
  - Rename each files to proper name
  - Auto-detect the file in diffrent way when files locate differently 
  
- Cleanup thumbnail files (Optional)
- Create new files rather than replace (Optional)
- If input folder is `marketface` itself, batch all folders under it
