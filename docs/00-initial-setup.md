# Initial Setup

## Hardware

### Board

Raspberry Pi 4 Model B 2GB

### Peripherals

- **Display:** Waveshare 4.3" HDMI Capacitive Touchscreen
- **Audio:** USB audio dongle
- **Headset:** Generic 3.5mm headset
- **Power:** Canakit 3.5A USB-C supply with PiSwitch for Pi4

## Operating System Installation

https://archlinuxarm.org/platforms/armv8/broadcom/raspberry-pi-4

Note: Follow the steps for the AArch64 install

## Bootstrap

```bash
su -
# password: root
pacman-key --init
pacman-key --populate archlinuxarm
pacman -Syu
```

Create your user:

```bash
useradd -m -G wheel -s /bin/bash USERNAME
# Set your password
passwd USERNAME
# Enable wheel group sudo
sed -i 's/^# %wheel ALL=(ALL:ALL) ALL/%wheel ALL=(ALL:ALL) ALL/' /etc/sudoers
```

Remove alarm user:

```bash
userdel -r alarm
```

Hostname, timezone, locale:

```bash
hostnamectl set-hostname btwphone
# Change to your timezone - find with: timedatectl list-timezones
ln -sf /usr/share/zoneinfo/America/New_York /etc/localtime
hwclock --systohc
# Locale
echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen
locale-gen
echo "LANG=en_US.UTF-8" > /etc/locale.conf
```

```bash
# Exit root, log back in as your new user
exit
```

## Package Install

```bash
sudo pacman -S base-devel git python python-pip neovim sudo vim \
  tmux htop raspberrypi-utils

pip install setuptools pynvim --break-system-packages
```

## fstab + Swap config

```bash
# Edit fstab - add noatime,nodiratime,discard to the root entry
# This helps preserve SD Card life
# Verify your root device first
findmnt /
# Then add the netry using your SOURCE value from above
echo "/dev/mmcblk1p2 / ext4 defaults,noatime,nodiratime,discard 0 1" | sudo tee -a /etc/fstab
# Verify settings have applied
sudo mount -o remount /
findmnt /

# Create swapfile
sudo fallocate -l 2G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile
echo "/swapfile none swap defaults 0 0" | sudo tee -a /etc/fstab

# Lower swappiness
echo "vm.swappiness=1" | sudo tee /etc/sysctl.d/99-swappiness.conf
```

