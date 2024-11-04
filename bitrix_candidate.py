#!/usr/bin/env python
# -*- coding: utf-8 -*-

from BX24 import Bitrix24
from openpyxl import Workbook

BITRIX_WEBHOOK_URL = 'https://b24-f4kgfp.bitrix24.ru/rest/1/8ee1njm7naiu47s7/'

def parse_webhook(webhook):
    domain = BITRIX_WEBHOOK_URL.partition("https://")[2].partition('.')[0]
    webhook_key = BITRIX_WEBHOOK_URL.partition("rest/")[2].partition('/')[2]
    return domain, webhook_key

candidate_id=1
    
def get_candidate_data(candidate_id):
    domain, webhook_key = parse_webhook(BITRIX_WEBHOOK_URL)
    bx24 = Bitrix24(domain, webhook_key, candidate_id)
    return bx24.call('user.get')['result'][0]


def create_excel_file(data, filename):
    wb = Workbook()
    ws = wb.active
    keys = list(map(lambda key: key if isinstance(key, int) else (key if isinstance(key, str) else 'val'),
                    data.keys()))
    values = list(map(lambda val: val if isinstance(val, int) else (val if isinstance(val, str) else f'{val}'),
                      data.values()))
    for key, val in zip(keys, values):
        ws.append([key, val])
    wb.save(f'{filename}.xlsx')

create_excel_file(get_candidate_data(1), 'canidate_table')