## WPK8S MicroK8S addons repository

A collection of repositories useful for small and medium MicroK8S clusters. It was started when MicroK8S announced support for community addons and the Storage addons did not fit any good High Availability and Horizontal Scalling scenario for Storage, and I, the author of [WordPress on MicroK8S](https://leanpub.com/wp-microk8s) book, did not agree with the implementation of the OpenEBS addons.

Probably some of this addons will make their way in the Canonical's community repo in time.

The current repository contains two addons:

  * openebs, Adds OpenEBS Localpath, Jiva and NFS storage support.


### How to use an addons repository

#### Adding repositories
3rd party addons repositories are supported on MicroK8s v1.24 and onwards. To add a repository on an already installed MicroK8s you have to use the `microk8s addons repo` command and provide a user friendly repo name, the path to the repository and optionally a branch within the repository. For example:
```
microk8s addons repo add wpk8s https://github.com/wpk8s/microk8s-addons-repo --reference main
```

As long as you have a local copy of a repository and that repository is also a git one in can also be added to a MicroK8s installation with:
```
microk8s.addons repo add wpk8s ./microk8s-addons-repo
```

#### Enabling/disabling addons

The addons of all repositories are shown in `microk8s status` along with the repo they came from. `microk8s enable` and `microk8s disable` are used to enable and disable the addons respectively. The repo name can be used to disambiguate between addons with the same name. For example:

```
microk8s enable wpk8s/openebs
```

#### Refreshing repositories

Adding a repository to MicroK8s (via `mcirok8s addons repo add`) creates a copy of the repository under `$SNAP_COMMON/addons` (typically under `/var/snap/microk8s/common/addons/`). Authorized users are able to edit the addons to match their need. In case the upstream repository changes and you need to pull in any updates with:
```
microk8s addons repo update wpk8s
```

#### Removing repositories

Removing repositories is done with:
```
microk8s addons repo remove wpk8s
```

### Future roadmap

* Support addons update process (currently they only enable/disable, and this is how MicroK8S works).
* Add Longhorn as alternative to OpenEBS
