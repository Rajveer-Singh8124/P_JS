# PJS 

PJS is a utility class for writing and reading JSON data in Python.

## Example Usage

```python
import json
import gzip
from pjs import PJS

data = {"key": "value"}

# Write compressed data
PJS.write_compressed_data(data, "output")

# Read compressed data
read_data = PJS.read_compressed_data("output")
print(read_data)





