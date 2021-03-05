"""Module containing the tests for the default scenario."""

# Standard Python Libraries
import os

# Third-Party Libraries
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


@pytest.mark.parametrize("pkg_name", ["ca-certificates", "openssl"])
def test_packages(host, pkg_name):
    """Verify that all expected packages were installed."""
    assert host.package(pkg_name).is_installed


@pytest.mark.parametrize(
    "file_name",
    [
        "dhs-cert-00",
        "dhs-cert-01",
        "dhs-cert-02",
        "dhs-cert-03",
        "dhs-cert-04",
    ],
)
def test_cert_files(host, file_name):
    """Verify that all expected certificate files were installed."""
    distribution = host.system_info.distribution
    if distribution in ["amzn", "fedora"]:
        path = "/etc/pki/ca-trust/source/anchors/"
    elif distribution in ["debian", "kali", "ubuntu"]:
        path = "/usr/local/share/ca-certificates/"
    f = host.file(path + file_name)
    assert f.exists
    assert f.is_file
    assert f.user == "root"
    assert f.group == "root"
    assert f.mode == 0o400
