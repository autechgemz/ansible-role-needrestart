# ansible-role-needrestart

## Description

needrestart checks which daemons need to be restarted after library upgrades.

## Requirements

None

## Dependencies

None

## OS Platforms

- Ubuntu-22,04 or higher

## Example Playbook

```
- hosts: all
  roles:
    - needrestart
```

## Role Variables

### needrestart_package_ensure: (string) 

```
needrestart_package_ensure: present
```

### needrestart_config_options: (dict) 

```
  blacklist:
    - 'qr(^/usr/bin/sudo(\.dpkg-new)?$)'
    - 'qr(^/sbin/(dhclient|dhcpcd5|pump|udhcpc)(\.dpkg-new)?$)'
    - 'qr(^/usr/bin/apt-get(\.dpkg-new)?$)'
  override_rc:
    'qr(^dbus)': 0
    'qr(^gdm)': 0
    'qr(^kdm)': 0
    'qr(^nodm)': 0
    'qr(^sddm)': 0
    'qr(^wdm)': 0
    'qr(^xdm)': 0
    'qr(^lightdm)': 0
    'qr(^slim)': 0
    'qr(^lxdm)': 0
    'qr(^bird)': 0
    'qr(^network)': 0
    'qr(^NetworkManager)': 0
    'qr(^ModemManager)': 0
    'qr(^wpa_supplicant)': 0
    'qr(^openvpn)': 0
    'qr(^quagga)': 0
    'qr(^frr)': 0
    'qr(^tinc)': 0
    'qr(^(open|free|libre|strong)swan)': 0
    'qr(^bluetooth)': 0
    'qr(^getty@.+\.service)': 0
    'qr(^user@\d+\.service)': 0
    'qr(^zfs-fuse)': 0
    'qr(^mythtv-backend)': 0
    'qr(^xendomains)': 0
    'qr(^lxcfs)': 0
    'qr(^libvirt)': 0
    'qr(^virtlogd)': 0
    'qr(^virtlockd)': 0
    'qr(^docker)': 0
    'qr(^emergency\.service$)': 0
    'qr(^rescue\.service$)': 0
    'qr(^elogind)': 0
    'qr(^apt-daily\.service$)': 0
    'qr(^apt-daily-upgrade\.service$)': 0
    'qr(^unattended-upgrades\.service$)': 0
    'qr(^cron-.*\.service$)': 0
    'qr(^rc-local\.service$)': 0
    'qr(^systemd-logind)': 0
  override_cont: {}
  blacklist_interp:
    - 'qr(^/tmp/)'
    - 'qr(^/var/)'
    - 'qr(^/run/)'
  blacklist_mappings:
    - 'qr(^/(SYSV00000000( \(deleted\))?|drm(\s|$)|dev/))'
    - 'qr(^/memfd:)'
    - 'qr(^/\[aio\])'
    - 'qr#/orcexec\.[\w\d]+( \(deleted\))?$#'
    - 'qr(/#\d+( \(deleted\))?$)'
    - 'qr#/jna\d+\.tmp( \(deleted\))?$#'
    - 'qr#^(/var)?/tmp/#'
    - 'qr#^(/var)?/run/#'
  skip_mapfiles: -1
```

### needrestart_dropin_config_options: (dict) 

None

## Example vars

```
needrestart_dropin_config_options:
  defno: 1
  restart: 'l'
```
