# Validate PyPi names

Super simple CLI to quickly validate your PyPi package names. Available here: https://pypi.org/project/validate-pypi-name/

## usage
Assume you want to check if the package "package_name" is available.
```
pip3 install validate-pypi-name
valid -n package_name
```

That's about it.

## Future work
The really interesting aspect of this is managing the peripheral cases of invalid package name- where PyPi tells you "This package name is too similar to an existing package." This package doesn't handle that case, but I plan on implementing that functionality in the future
