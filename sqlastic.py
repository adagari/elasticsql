#!/bin/python
import argparse,os,requests,json,readline

def main(host):
    query = set_query()
    data  = post_query(host,query)
    print_msg(host,data)

def set_query():
    user_input = input("sqlastic> ")
    if user_input == 'exit':
        print("Bye")
        exit()
    while not user_input.endswith(';'):
        user_input = user_input + ' ' + input("\t -> ")
    user_input = user_input.strip(';')
    if '"' in user_input:
        user_input = user_input.replace('"','\\"')
    query = '{"query":"' + user_input + '"}'
    return query

def post_query(host,query):
#    url = 'http://' + host + '_xpack/sql?format=txt'
    url = 'http://' + host + '/_sql?format=txt'
    headers = {'Content-Type':'application/json'}
    res = requests.post(url=url,data=query,headers=headers)
    if res.status_code == 200:
        data =  res.text
    else:
        data = json.loads(res.text)
        data = data["error"]["reason"] + "\n"
    return data

def print_msg(host,data):
    print("\n" + data)
    main(host)

def welcome_msg(host):
    os.system('clear')
    url = 'http://' + host
    res = requests.get(url)
    data = json.loads(res.text)
    print("-"*70)
    print("WELCOME TO SQLASTIC CLIENT")
    print("YOU ARE CONNECTED TO: " + data["name"])
    print("ELASTICSEARCH VERSION " + data["version"]["number"])
    print("-"*70 + "\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-i','--ip', action='store', dest='host',
                        default='127.0.0.1:9200',
                        help='Set the hostname as ip:port')
    host = parser.parse_args().host
    welcome_msg(host)
    main(host)
