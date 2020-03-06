#!/bin/python
import argparse,os,requests

def main():
    args  = set_args()
    host  = set_host(args)
    query = set_query()
#    post_query(query)

def set_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i','--ip', action='store', dest='host',
                        default='127.0.0.1:9200',
                        help='Set the hostname as ip:port')
    args = parser.parse_args()
    return args

def set_host(args):
    os.system('clear')
    print(args.host)

def set_query():
    user_input = input("elasticsql> ")
    while not user_input.endswith(";"):
        user_input = user_input + " " + input("\t -> ")
    user_input = user_input.strip(";")
    if '"' in user_input:
        user_input = user_input.replace('"','\\"')
    print(user_input)
    return user_input

#def post_query(query):

if __name__ == "__main__":
    main()
