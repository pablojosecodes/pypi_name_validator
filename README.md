# Validate PyPi names

Super simple CLI to quickly validate your PyPi package names. Available here: https://pypi.org/project/validate-pypi-name/

## Usage
Assume you want to check if the package "package_name" is available.
```
pip3 install validate-pypi-name
valid -n package_name
```
If you want to run the "intensive workload" version, where we iterate through all possible collisions, use the -i tag
```
pip3 install validate-pypi-name
valid -n package_name -i
```


That's about it.
