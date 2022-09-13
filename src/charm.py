#!/usr/bin/env python3
import logging
import yaml

from ops.charm import CharmBase
from ops.main import main
from ops.model import ActiveStatus, MaintenanceStatus
from subprocess import check_call
from jinja2 import Environment, FileSystemLoader

log = logging.getLogger(__name__)


class BirdCharm(CharmBase):
    def __init__(self, *args):
        super().__init__(*args)
        self.environment = Environment(loader=FileSystemLoader("templates/"))
        self.framework.observe(self.on.install, self.install)
        self.framework.observe(self.on.config_changed, self.config_changed)

    def install(self, event):
        self.unit.status = MaintenanceStatus("Installing BIRD")
        check_call(["apt-get", "update"])
        check_call(["apt-get", "install", "-y", "bird"])

    def config_changed(self, event):
        self.unit.status = MaintenanceStatus("Configuring BIRD")

        bird_config = self.render_bird_conf()
        with open("/etc/bird/bird.conf", "w") as f:
            f.write(bird_config)
        check_call(["systemctl", "reload", "bird"])
        self.unit.status = ActiveStatus()

    def render_bird_conf(self):
        template = self.environment.get_template("bird.conf")
        config = {
            "as_number": self.config["as-number"],
            "peers": yaml.safe_load(self.config["bgp-peers"]),
        }
        return template.render(config)


if __name__ == "__main__":
    main(BirdCharm)
