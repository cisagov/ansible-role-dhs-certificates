# ansible-role-dhs-certificates #

[![GitHub Build Status](https://github.com/cisagov/ansible-role-dhs-certificates/workflows/build/badge.svg)](https://github.com/cisagov/ansible-role-dhs-certificates/actions)
[![Total alerts](https://img.shields.io/lgtm/alerts/g/cisagov/ansible-role-dhs-certificates.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/cisagov/ansible-role-dhs-certificates/alerts/)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/cisagov/ansible-role-dhs-certificates.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/cisagov/ansible-role-dhs-certificates/context:python)

This is an Ansible role for configuring trust of DHS CA certificates
at the OS level.

## Requirements ##

This role makes use of the [`community.general.json_query` Ansible
filter](https://docs.ansible.com/ansible/latest/user_guide/playbooks_filters.html#selecting-json-data-json-queries),
which requires that the [`jmespath` Python
package](https://pypi.org/project/jmespath/) be installed on the local
host.

## Role Variables ##

- `cert_url` - the URL where the DHS certificate p7b bundle can be
  downloaded.  Defaults to "https://pki.treas.gov/dhsca_fullpath.p7b".
- `single_cert_filename_prefix` - the prefix to use when creating the
  individual certificate files extracted from the DHS certificate p7b
  bundle.  If the prefix is "zz-" then individual certificate files
  will be named "zz-00", "zz-01", etc.  Defaults to "dhs-cert-".

## Dependencies ##

None.

## Example Playbook ##

Here's how to use it in a playbook:

```yaml
- hosts: all
  become: yes
  become_method: sudo
  roles:
    - dhs_certificates
```

## Contributing ##

We welcome contributions!  Please see [`CONTRIBUTING.md`](CONTRIBUTING.md) for
details.

## License ##

This project is in the worldwide [public domain](LICENSE).

This project is in the public domain within the United States, and
copyright and related rights in the work worldwide are waived through
the [CC0 1.0 Universal public domain
dedication](https://creativecommons.org/publicdomain/zero/1.0/).

All contributions to this project will be released under the CC0
dedication. By submitting a pull request, you are agreeing to comply
with this waiver of copyright interest.

## Author Information ##

Shane Frasier - <jeremy.frasier@trio.dhs.gov>
