import subprocess
import pickle
import json
import os

'''
from logging import loggingSetting

logger = loggingSetting("meta")
'''

def pushaction(contract, action, data, f):
    cmd = [
        "cleos",
        "-u",
        "http://api.eosbeijing.one",
        "push",
        "action",
        contract,
        action,
        json.dumps(data),
        "-p",
        f,
    ]
    return runcleos(cmd)

def runcleos(cmd):
    a = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    return a.stdout

def getMeta():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    accountFile = os.path.join(current_dir, "meta.json")
    with open(accountFile) as f:
        row = json.loads(f.read())
        return row

def newportal(from_, id, parent_id, creator_fee, ref_fee, k, price, st):
    return pushaction("cryptomeetup", "newportal", [from_, id, parent_id, creator_fee, ref_fee, k, price, st], "cryptomeetup")

if __name__ == "__main__":
    raw = getMeta()
    s = json.dumps(raw)
    creator = json.loads(s)["creator"]
    id = json.loads(s)["id"]
    parent = json.loads(s)["parent"]
    creator_fee = json.loads(s)["creator_fee"]
    ref_fee = json.loads(s)["ref_fee"]
    k = json.loads(s)["k"]
    price = json.loads(s)["price"]
    st = json.loads(s)["st"]
    '''
    print("creator", creator, "id", id, "parent", parent, "creator_fee", creator_fee, "ref_fee", ref_fee, "k", k, "price", price, "st", st)
    '''
    newportal(creator, id, parent, creator_fee, ref_fee, k, price, st)
    
