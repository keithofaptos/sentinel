# coding=utf-8
from urlparse import urljoin

from .node import node
from ..config import MASTER_NODE_URL
from ..config import VERSION
from ..utils import fetch


def list_node():
    body = {
        'hash': node.config['register']['hash']
    }
    url = urljoin(MASTER_NODE_URL, 'node')
    try:
        response = fetch().post(url, json=body)
        if response and response.status_code == 200:
            data = response.json()
            if data['success']:
                return None, data
            return {
                       'code': 2,
                       'message': 'Response data success is False.'
                   }, None
        return {
                   'code': 2,
                   'message': 'Response status code is not 200.'
               }, None
    except Exception as error:
        return str(error), None


def update_node(update_type):
    body = {
        'accountAddress': node.config['account']['address'],
        'token': node.config['register']['token'],
        'type': update_type
    }
    if update_type == 'details':
        body['details'] = {
            'IP': node.ip,
            'pricePerGB': node.config['price_per_gb'],
            'encMethod': node.config['enc_method'],
            'location': node.location,
            'netSpeed': node.net_speed,
            'version': VERSION
        }

    url = urljoin(MASTER_NODE_URL, 'node')
    try:
        response = fetch().put(url, json=body)
        if response and response.status_code == 200:
            data = response.json()
            if data['success']:
                return None, data
            return {
                       'code': 2,
                       'message': 'Response data success is False.'
                   }, None
        return {
                   'code': 2,
                   'message': 'Response status code is not 200.'
               }, None
    except Exception as error:
        return str(error), None
