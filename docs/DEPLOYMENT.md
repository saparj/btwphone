# It's 01:00 on a worknight, I'll make this pretty later

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

Note to self here: created a 1024Mb swapfile, watch htop during `make` and see if it actually uses it.
RPi3 has 1024Mb of physical ram while RPi4 has 2048 so this shouldn't be an issue but still worth noting.
Yes - uses around 1148Mb of RAM+Swapfile

## Install core libraries

```bash
sudo make install
sudo ldconfig
```

Build the python SWIG bindings:

```bash
cd pjsip-apps/src/swig/python
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

