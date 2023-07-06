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

None

### needrestart_dropin_config_options: (dict) 

None

## Example vars

```
needrestart_dropin_config_options:
  defno: 1
  restart: 'l'
```
