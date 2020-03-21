from oslo_log import log as logging
import re

from nova.scheduler import filters

LOG = logging.getLogger(__name__)


class FilterByName(filters.BaseHostFilter):
    run_filter_once_per_request = True
    RUN_ON_REBUILD = False

    def _containNameTest(self, name):
        result = re.findall(r'test', name.lower())
        if len(result) > 0:
            return True
        return False

    def host_passes(self, host_state, spec_obj):
        image_name = spec_obj.image.get("name") if spec_obj.image else ""
        if not self._containNameTest(image_name):
            LOG.debug("%(host_state)s does not support requested "
                      "instance_properties", {'host_state': host_state})
            return False
        return True