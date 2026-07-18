---
title: "[Solution] Python Astropy Astronomy Error — How to Fix"
description: "Fix Python Astropy astronomy errors. Resolve coordinate transformation failures, FITS reading issues, and unit conversion problems."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
comments: true
weight: 5
---

# Python Astropy Astronomy Error

An `astropy.units.UnitsError` or `astropy.coordinates.errors` occurs when Astropy fails to convert units, perform coordinate transformations, or read FITS files due to missing headers or incompatible data formats.

## Why It Happens

Astropy provides astronomy data structures. Errors arise when unit conversions are dimensionally incompatible, when coordinate frames are not defined, when FITS files have malformed headers, or when time scales are mismatched.

## Common Error Messages

- `UnitsError: Can only convert between systems with compatible dimensions`
- `ValueError: Time scale gps not supported`
- `OSError: File does not appear to be a FITS file`
- `ValueError: Latitude angle must be within -90 to 90 degrees`

## How to Fix It

### Fix 1: Fix unit conversions

```python
from astropy import units as u

# Wrong — incompatible unit conversion
# length = 10 * u.meter
# time = length.to(u.second)  # UnitsError

# Correct — convert compatible units
length = 10 * u.meter
km = length.to(u.km)
print(f"{length} = {km}")

# Chain conversions
speed = 300000 * u.km / u.s
light_speed = speed.to(u.m / u.s)
print(f"Speed of light: {light_speed}")
```

### Fix 2: Handle coordinate transformations

```python
from astropy.coordinates import SkyCoord
import astropy.units as u

# Wrong — undefined coordinate frame
# coord = SkyCoord(ra=180, dec=45, unit="deg")

# Correct — specify frame explicitly
coord = SkyCoord(ra=180, dec=45, unit=(u.deg, u.deg), frame="icrs")
print(f"ICRS: {coord}")

# Transform to galactic
galactic = coord.galactic
print(f"Galactic: {galactic.l}, {galactic.b}")

# Convert to altaz with observer location
from astropy.coordinates import EarthLocation, AltAz
from astropy.time import Time

location = EarthLocation(lat=40 * u.deg, lon=-74 * u.deg, height=0 * u.m)
time = Time("2024-01-01T12:00:00", scale="utc")
altaz = coord.transform_to(AltAz(obstime=time, location=location))
print(f"Altitude: {altaz.alt}, Azimuth: {altaz.az}")
```

### Fix 3: Read FITS files correctly

```python
from astropy.io import fits

# Wrong — assuming FITS format
# data = fits.open("data.csv")

# Correct — open and validate FITS
with fits.open("data.fits") as hdul:
    print(f"HDU count: {len(hdul)}")
    print(f"Header: {hdul[0].header}")
    data = hdul[0].data
    print(f"Data shape: {data.shape}")

# Write FITS file
from astropy.io import fits
import numpy as np

data = np.random.rand(100, 100)
hdu = fits.PrimaryHDU(data)
hdu.header["OBJECT"] = "Test Star"
hdu.header["EXPTIME"] = 300
hdu.writeto("output.fits", overwrite=True)
```

### Fix 4: Handle time scales

```python
from astropy.time import Time
import astropy.units as u

# Wrong — mixing time scales
# t1 = Time("2024-01-01", scale="utc")
# t2 = Time("2024-01-01", scale="tai")
# diff = t1 - t2  # may give unexpected results

# Correct — convert to same time scale
t1 = Time("2024-01-01T00:00:00", scale="utc")
t2 = t1.tai  # convert to TAI
diff = t1 - t2
print(f"UTC-TAI difference: {diff}")

# Use format conversion
t = Time("2024-01-01T12:00:00", scale="utc")
print(f"JD: {t.jd}")
print(f"MJD: {t.mjd}")
```

## Common Scenarios

- **Unit mismatch** — Converting between dimensionally incompatible units (e.g., meters to seconds).
- **Frame not specified** — Creating coordinates without specifying the reference frame defaults to ICRS.
- **Time scale confusion** — UTC and TAI differ by leap seconds, causing unexpected time differences.

## Prevent It

- Always specify coordinate frames explicitly using `frame="icrs"` or `frame="galactic"`.
- Check FITS headers with `hdul[0].header` before accessing data arrays.
- Use `Time.scale` to verify the time scale before performing time arithmetic.

## Related Errors

- [UnitsError](/languages/python/units-error/) — incompatible unit conversion
- [ValueError](/languages/python/valueerror/) — invalid coordinate values
- [OSError](/languages/python/oserror/) — FITS file cannot be opened
