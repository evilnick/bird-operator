# BIRD Operator Charm

The [BIRD][] project aims to develop a dynamic IP routing daemon with full support
of all modern routing protocols, easy to use configuration interface and
powerful route filtering language, primarily targeted on (but not limited to)
Linux and other UNIX-like systems and distributed under the GNU General
Public License.

Currently, this charm is intended to validate BGP functionalities in different 
charms of Charmed Kubernetes such as Calico or Kube-OVN.

[BIRD]: https://bird.network.cz/

# Developers

## Building

To build the BIRD Operator charm use the following command:

```bash
charmcraft pack
```

## Deploying

After building the BIRD charm, you can deploy it by running the following command:
```bash
juju deploy ./bird_ubuntu-20.04-amd64-arm64_ubuntu-22.04-amd64-arm64.charm
```
