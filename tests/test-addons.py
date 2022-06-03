import sh
import yaml

from utils import microk8s_enable, wait_for_pod_state, microk8s_disable


class TestAddons(object):
    def test_openebs(self):
        microk8s_enable("openebs")
        wait_for_pod_state("", "default", "running", label="app=openebs-nfs-provisioner")
        status = yaml.safe_load(sh.microk8s.status(format="yaml").stdout)
        expected = {"openebs": "enabled"}
        microk8s_disable("openebs")
