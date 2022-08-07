#!/usr/bin/env python3

import json
import os
import sys
import traceback

FUNCTION_PATH = '../backend/function'
TARGETS = [
    'addTasks',
    'deleteTasks',
    'tasks'
]

def get_targets_file_path():
    path_list = []
    for target in TARGETS:
        path = FUNCTION_PATH + '/' + target + '/' + target + '-cloudformation-template.json'
        if os.path.exists(path):
            path_list.append(path)
        else:
            raise FileNotFoundError
    return path_list

def update_iam(path):
    try:
        f = open(path, 'r+')
        template = json.load(f)
        additional = {
            "Effect": "Allow",
            "Action": "ec2:*",
            "Resource": "*"
        }
        template['Resources']['lambdaexecutionpolicy']['Properties']['PolicyDocument']['Statement'].append(additional)
        f.seek(0)
        f.write(json.dumps(template, indent=2))
        f.truncate()
    except Exception as e:
        raise e

def update_vpc(path):
    try:
        f = open(path, 'r+')
        template = json.load(f)
        additional = {
            "Effect": "Allow",
            "Action": "ec2:*",
            "Resource": "*"
        }
        template['Resources']['lambdaexecutionpolicy']['Properties']['PolicyDocument']['Statement'].append(additional)
        f.seek(0)
        f.write(json.dumps(template, indent=2))
        f.truncate()
    except Exception as e:
        raise e

if __name__ == '__main__':
    try:
        for path in get_targets_file_path():
            #update_iam(path)
            update_vpc(path)
    except:
        traceback.print_exc()
