# Building pjsip on Arch Linux ARM

Tested on Raspberry Pi 4 Model B running Arch Linux ARM - March 2026

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
echo 'export CXXFLAGS += -fPIC' >> user.mak
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
# Copy the compiled extension to where the wrapper can find it
find ~/pjproject/pjsip-apps/src/swig/python/build -name "_pjsua2*.so" \
  -exec cp {} ~/pjproject/pjsip-apps/src/swig/python/ \;

# Register pjsip shared libraries with the dynamic linker
echo "/usr/local/lib" | sudo tee /etc/ld.so.conf.d/pjsip.conf
sudo ldconfig
```

Validation:

```bash
python -c "import pjsua2; print('pjsua2 imported successfully')"
```

Install pjsip as a system package:

```bash
# If make install ran as root, fix permissions before pip install
sudo chown -R $USER:$USER ~/pjproject/pjsip-apps/src/swig/python/pjsua2.egg-info
pip install . --break-system-packages
```

Test from home directory:

```bash
cd ~
python -c "import pjsua2; print('pjsua2 imported successfully')"
```

