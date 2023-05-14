# P_JS
PJS is a utility class for writing and reading JSON data in Python.

pip install p-js-rs==0.0.1


# Example Usage
from p_js.p_js import PJS

data = {"key": "value"}

# Write compressed data
PJS.write_compressed_data(data, "output")

# Read compressed data
read_data = PJS.read_compressed_data("output")
print(read_data)
