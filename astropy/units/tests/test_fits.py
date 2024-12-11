# Licensed under a 3-clause BSD style license - see LICENSE.rst
"""
Test FITS compatibility for `astropy.units`.
"""

import pytest
from astropy.units import Unit, dex

def test_fits_format_dex():
    """
    Test if `dex` units are correctly formatted in FITS standard.
    """
    unit = dex(Unit("solMass"))
    formatted = unit.to_string(format="fits")
    assert formatted == "log(solMass)", f"Expected 'log(solMass)', got '{formatted}'"

def test_fits_parse_log_unit():
    """
    Test if `log(solMass)` is correctly parsed as a FITS unit.
    """
    unit = Unit("log(solMass)", format="fits")
    assert unit.to_string() == "dex(solMass)", f"Expected 'dex(solMass)', got '{unit.to_string()}'"

def test_fits_invalid_log_unit():
    """
    Test for invalid FITS units that do not conform to standards.
    """
    with pytest.raises(ValueError, match="did not parse as fits unit"):
        Unit("log(unknownUnit)", format="fits")

def test_fits_custom_unit_error_message():
    """
    Ensure the error message suggests custom unit definitions for unrecognized units.
    """
    with pytest.raises(ValueError) as excinfo:
        Unit("log(nonStandardUnit)", format="fits")
    assert "define it with 'u.def_unit'" in str(excinfo.value)



