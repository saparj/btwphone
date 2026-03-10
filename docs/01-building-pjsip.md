# Building pjsip on Arch Linux ARM

Tested on Raspberry Pi 3 Model B+ running Arch Linux ARM - March 2026

## Install build dependencies

```bash
sudo pacman -S alsa-lib alsa-utils openssl swig
```

- `alsa-lib` - Audio library pjsip links against for sound device access
- `openssl` - Needed for TLS and SRTP
- `swig` - Generates Python bindings from the C++ API

## Clone the pjsip source

```bash
cd ~
git clone https://github.com/pjsip/pjproject.git
cd pjproject
```

## Create build config

```bash
echo 'export CFLAGS += -fPIC' > user.mak
echo 'export LDFLAGS += -fPIC' >> user.mak
```

## Configure

```bash
./configure --enable-shared
```

Watch to make sure it detects ALSA and OpenSSL.

## Build

```bash
make dep
make
```

## Install core libraries

```bash
sudo make install
sudo ldconfig
```

Build the python SWIG bindings:

```
Note: The SWIG binding compilation (`pjsua2_wrap.cpp`) is a single-file compile that peaked at ~1148 MB RAM+swap on a 1 GB Pi 3B+. A swapfile is essential on boards with less than 2 GB RAM.
```

```bash
cd pjsip-apps/src/swig/python
# Setuptools is a workaround - Python 3.12+ removed distutils and 3.14 doesn't ship setuptools, so this step is needed on newer Python versions
pip install setuptools --break-system-packages
make
```

If you're on a shared environment please be nice and use .venv instead of breaking system packages.

```bash
sudo make install
```

The moment of truth:

```bash
python -c "import pjsua2; print('pjsua2 imported successfully')"
```

