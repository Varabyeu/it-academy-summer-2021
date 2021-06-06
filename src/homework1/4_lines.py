# indent your Python code to put into an email
import glob
# glob supports Unix style pathname extensions
from typing import Any, Union

python_files = glob.glob('*.py')
file_name: Union[Union[bytes, str], Any]
for file_name in sorted(python_files):
    print ('    ------' + file_name)

    with open(file_name) as f:
        for line in f:
            print ('    ' + line.rstrip())

    print()