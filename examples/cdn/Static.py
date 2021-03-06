#!/usr/bin/python
# coding=utf-8


import os
import sys
import time
from openstack import connection

os.environ.setdefault('OS_CDN_ENDPOINT_OVERRIDE', 'https://cdn.myhwclouds.com/v1.0')

username = "xxxxxxxxxxx"
password = "xxxxxxxxxxx"
projectId = "xxxxxxxxxxx"
userDomainId = "xxxxxxxxxxx"
auth_url = "https://iam.cn-north-1.myhuaweicloud.com/v3"

conn = connection.Connection(
    auth_url=auth_url,
    user_domain_id=userDomainId,
    project_id=projectId,
    username=username,
    password=password
)


def query_total_flux(domain_name, start_time, end_time):
    print('Query the total network traffic: ')
    total_traffic = conn.cdn.query_network_traffic(domain_name=domain_name, start_time=start_time, end_time=end_time)
    print(total_traffic)

def query_detail_flux(domain_name, start_time, end_time):
    print('Query the network traffic detail: ')
    traffic_detail = conn.cdn.query_network_traffic_detail(domain_name=domain_name, start_time=start_time, end_time=end_time, interval=300)
    print(traffic_detail)

def query_bandwidth_peak(domain_name, start_time, end_time):
    print('Query bandwidth peak: ')
    bandwidth_peak = conn.cdn.query_bandwidth_peak(domain_name=domain_name, start_time=start_time, end_time=end_time)
    print(bandwidth_peak)

def query_detail_bandwidth(domain_name, start_time, end_time):
    print('Query bandwidth peak detail: ')
    bandwidth = conn.cdn.query_bandwidth(domain_name=domain_name, start_time=start_time, end_time=end_time, interval=300)
    print(bandwidth)

def query_summary_by_type(domain_name, start_time, end_time, query_type):
    print('Query static summary by type - ' + query_type + ': ')
    summary = conn.cdn.query_summary(domain_name=domain_name, start_time=start_time, end_time=end_time, stat_type=query_type, service_area='mainland_china')
    print(summary)

def query_summary_detail_by_type(domain_name, start_time, end_time, query_type):
    print('Query static summary detail by type - ' + query_type + ': ')
    summary = conn.cdn.query_summary_detail(domain_name=domain_name, start_time=start_time, end_time=end_time, stat_type=query_type, service_area='mainland_china')
    print(summary)

def query_domains_summary_detail_by_type(domain_name, start_time, end_time, query_type):
    print('Query static domains summary detail by type - ' + query_type + ': ')
    summaries = conn.cdn.summaries(domain_name=domain_name, start_time=start_time, end_time=end_time, stat_type=query_type, service_area='mainland_china')
    for summary in summaries:
        print(summary)


if __name__ == "__main__":
    end_time = int(time.time() * 1000)
    start_time = end_time - 3600000
    domain_name = "ALL"
    
    query_total_flux(domain_name, start_time, end_time)
    
    query_detail_flux(domain_name, start_time, end_time)
    
    query_bandwidth_peak(domain_name, start_time, end_time)
    
    query_detail_bandwidth(domain_name, start_time, end_time)
    
    for query_type in ['bw', 'flux', 'bs_bw', 'bs_flux', 'req_num', 'req_hit_rate', 'flux_hit_rate', 'bs_fail_rate', 'qps', 'http_code_2xx', 'http_code_3xx', 'http_code_4xx', 'http_code_5xx']:
        query_summary_by_type(domain_name, start_time, end_time, query_type)
    
    for query_type in ['bw', 'flux', 'bs_bw', 'bs_flux', 'req_num', 'req_hit_rate', 'flux_hit_rate', 'bs_fail_rate', 'qps', 'http_code_2xx', 'http_code_3xx', 'http_code_4xx', 'http_code_5xx']:
        query_summary_detail_by_type(domain_name, start_time, end_time, query_type)
    
    domain_name = "cdn-python-sdk-a.example.com,cdn-python-sdk.example.com.com"
    start_time = end_time - 23 * 3600 * 1000
    for query_type in ['bw', 'flux', 'bs_bw', 'bs_flux', 'req_num', 'req_hit_rate', 'flux_hit_rate', 'bs_fail_rate', 'qps', 'http_code_2xx', 'http_code_3xx', 'http_code_4xx', 'http_code_5xx']:
        query_domains_summary_detail_by_type(domain_name, start_time, end_time, query_type)
    
