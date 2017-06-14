# -*- coding: utf-8 -*-
#
# Copyright 2017 HuaWei Tld
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from openstack.load_balancer import load_balancer_service as lb_service
from openstack import resource2 as resource


class LoadBalancer(resource.Resource):
    resource_key = 'loadbalancer'
    resources_key = 'loadbalancers'
    base_path = '/elbaas/loadbalancers'
    service = lb_service.LoadBalancerService()

    # capabilities
    allow_create = True
    allow_list = True
    allow_get = True
    allow_delete = True

    _query_mapping = resource.QueryParameters(
        'id', 'name', 'status', 'type', 'bandwidth', 'admin_state_up',
        'vpc_id', 'vip_subnet_id', 'vip_address', 'security_group_id',
        'description',
        is_admin_state_up='admin_state_up',
    )

    #: Properties
    #: The load balancer name
    name = resource.Body('name')
    #: The load balancer status
    status = resource.Body('status')
    #: The load balancer type.
    #: Valid values include ``Internal``, ``External``
    type = resource.Body('type')
    #: The availability zone.
    availability_zone = resource.Body("az")
    #: The load balancer charge mode.
    #: Valid values include ``bandwidth``, ``traffic``, bandwidth by default
    charge_mode = resource.Body("charge_mode")
    #: The load balancer eip type
    #: Valid values include ``5_telcom``, ``5_union``, ``5_bgp``.
    bandwidth = resource.Body('eip_type')
    #: The load balancer bandwidth
    bandwidth = resource.Body('bandwidth')
    #: The administrative state of the load balancer
    admin_state_up = resource.Body('admin_state_up')
    #: VPC of load balancer
    vpc_id = resource.Body('vpc_id')
    #: VIP subnet of load balancer
    vip_subnet_id = resource.Body('vip_subnet_id')
    #: VIP address of load balancer
    vip_address = resource.Body('vip_address')
    #: Security Group of load balancer
    security_group_id = resource.Body('security_group_id')
    #: The load balancer description
    description = resource.Body('description')
    #: Timestamp when the load balancer was created
    created_at = resource.Body('created_at')
    #: Timestamp when the load balancer was last updated
    updated_at = resource.Body('updated_at')


class LoadBalancerJob(LoadBalancer):
    #: Job Id of load balancer asynchronous job
    job_id = resource.Body('job_id')
    #: Job uri
    uri = resource.Body('uri')
