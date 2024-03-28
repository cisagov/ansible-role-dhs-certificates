# ansible-role-dhs-certificates #

[![GitHub Build Status](https://github.com/cisagov/ansible-role-dhs-certificates/workflows/build/badge.svg)](https://github.com/cisagov/ansible-role-dhs-certificates/actions)
[![CodeQL](https://github.com/cisagov/ansible-role-dhs-certificates/workflows/CodeQL/badge.svg)](https://github.com/cisagov/ansible-role-dhs-certificates/actions/workflows/codeql-analysis.yml)

This is an Ansible role for configuring trust of DHS CA certificates
at the OS level.

## Requirements ##

This role makes use of the [`community.general.json_query` Ansible
filter](https://docs.ansible.com/ansible/latest/user_guide/playbooks_filters.html#selecting-json-data-json-queries),
which requires that the [`jmespath` Python
package](https://pypi.org/project/jmespath/) be installed on the local
host.

## Role Variables ##

| Variable | Description | Default | Required |
|----------|-------------|---------|----------|
| cer\_filename | The filename to use for the DHS certificate cer bundle (translated from the p7b bundle). | `dhsca.cer` | No |
| cert\_url | The URL where the DHS certificate p7b bundle can be downloaded. | `https://pki.treas.gov/dhsca_fullpath.p7b` | No |
| p7b\_filename | The filename to use for the DHS certificate p7b bundle after it is downloaded from `cert\_url`. | `dhsca.p7b` | No |
| single\_cert\_filename\_prefix | The prefix to use when creating the individual certificate files extracted from the DHS certificate p7b bundle.  If the prefix is "zz-" then individual certificate files will be named "zz-00", "zz-01", etc. | `dhs-cert-` | No |

## Dependencies ##

None.

## Installation ##

This role can be installed via the command:

```console
ansible-galaxy install --role-file path/to/requirements.yml
```

where `requirements.yml` looks like:

```yaml
---
- name: skeleton
  src: https://github.com/cisagov/skeleton-ansible-role
```

and may contain other roles as well.

For more information about installing Ansible roles via a YAML file,
please see [the `ansible-galaxy`
documentation](https://docs.ansible.com/ansible/latest/galaxy/user_guide.html#installing-multiple-roles-from-a-file).

## Example Playbook ##

Here's how to use it in a playbook:

```yaml
- hosts: all
  become: true
  become_method: sudo
  tasks:
    - name: Install and trust DHS certificates
      ansible.builtin.include_role:
        name: dhs_certificates
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

Shane Frasier - <jeremy.frasier@gwe.cisa.dhs.gov>
