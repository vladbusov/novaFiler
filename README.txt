For activation name filer just put "enabled_filters = filterByName.FilterByName" text to the .conf file: /etc/nova/nova.conf.
#####################

_For example:_

[filter_scheduler]
track_instance_changes = False
enabled_filters = AvailabilityZoneFilter,ComputeFilter,ComputeCapabilitiesFilter,ImagePropertiesFilter,ServerGroupAntiAffinityFilter,ServerGroupAffinityFilter,SameHostFilter,DifferentHostFilter
enabled_filters = filterByName.FilterByName