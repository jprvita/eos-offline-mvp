
import configparser
import sys
import os
import subprocess
import time
import shutil

# Perhaps OfflineMetrics would be a better name here, in-line with the other
# suggestions?
class EOSMetrics():
    def __init__(self):
        self.metrics_cache_dir = '/var/cache/metrics'
        self.tracking_id_path = '/etc/metrics/tracking-id'
        self.machine_id_path = '/etc/machine-id'
        self.systemd_service = 'eos-metrics-event-recorder.service'
        self.metrics_config_file = '/etc/metrics/eos-metrics-permissions.conf'
        self.eos_version = float(0) # JPRVITA: I recommend using string here instead
        self.config = configparser.ConfigParser()
        self.config.read(self.metrics_config_file)

    # JPRVITA: then this method would return a version string, like "3.8.6"
    def get_eos_version(self):
        f = open("/etc/os-release")
        for line in f.readlines():
            if line.startswith("VERSION="):
                fdot = line.find('=')
                ldot = line.rfind('.')
                major = line[fdot+2:ldot]
                self.eos_version = major
                return float(major)

    def get_upload_enable_config(self): # JPRVITA: unused method
        print(self.config.get("global", "uploading_enabled"))

    def get_environment_config(self): # JPRVITA: unused method
        print(self.config.get("global", "environment"))

    # JPRVITA: calling this method is_metrics_service_active() and making it
    # return a boolean will make the calling code easier to read
    def get_service_state(self):
        status = os.system('systemctl is-active --quiet ' + self.systemd_service)
        return (status)
