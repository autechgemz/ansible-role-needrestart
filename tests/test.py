
def test_architecture(host):
    assert host.system_info.arch == 'x86_64'

def test_system_type(host):
    assert host.system_info.type == "linux"

def test_linux_dist(host):
    assert host.system_info.distribution in ["ubuntu"]

def test_packages(host):
    for name, version in {
        ("needrestart", ""),
        }:
        package = host.package(name)
        assert package.is_installed

def test_configrations(host):
    for name in (
        "/etc/needrestart/needrestart.conf",
        ):
      config = host.file(name)
      assert config.exists
      assert config.user == 'root'
      assert config.group == 'root'
      assert config.mode == 0o644
