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
make dep && make -j$(nproc)
```

The `-j$(nproc)` flag parallelizes the build across all 4 cores

## Install core libraries

```bash
sudo make install
sudo ldconfig
```

Build the python SWIG bindings:

```bash
cd pjsip-apps/src/swig/python
make
sudo make install
```

Other steps:

```bash
cp /home/saparj/pjproject/pjsip-apps/src/swig/python/build/lib.linux-aarch64-cpython-314/_pjsua2.cpython-314-aarch64-linux-gnu.so \
   /home/saparj/pjproject/pjsip-apps/src/swig/python/
echo "/usr/local/lib" | sudo tee /etc/ld.so.conf.d/pjsip.conf
sudo ldconfig
```

Validation:

```bash
python -c "import pjsua2; print('pjsua2 imported successfully')"
```

Install pjsip as a system package:

```bash
sudo chown -R saparj:saparj /home/saparj/pjproject/pjsip-apps/src/swig/python/pjsua2.egg-info
pip install . --break-system-packages
```

Test from home directory:

```bash
cd ~
python -c "import pjsua2; print('pjsua2 imported successfully')"
```

