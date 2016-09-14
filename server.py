#!/usr/bin/python
#
# HTTP Chunked Encoding Example
# see RFC 2616, Section 3.6.1
# https://tools.ietf.org/html/rfc2616
#
import socket
import sys
import time
 
PORT = 8080
HOST = "localhost"
CHUNK_SIZE = 8
CRLF = "\r\n"
LAST_CHUNK = "0000" + CRLF
DATA_TO_SEND = "\nThe quick brown fox jumped over the lazy dog.\n\n"

def data_to_chunks(data, chunk_size):
    total_size = len(data)
    data_chunks = []
    for i in range(0, total_size):
        if (i%chunk_size) == 0:
            chunk = data[i:(i+chunk_size)]
            data_chunks.append(chunk)
    return data_chunks


def format_chunk(chunk):
    return ("%X" % len(chunk)) + CRLF + chunk + CRLF

def data_to_formatted_chunks(res, chunk_size):
    return map(format_chunk, data_to_chunks(res, chunk_size))

listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
# prevents address in use error
listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

try:
    listener.bind((HOST, PORT))
except socket.error as msg:
    print 'socket: error:' + str(msg[0]) + ' ' + msg[1]
    sys.exit()
     
listener.listen(10)
 
while 1:
    conn, addr = listener.accept()

    print("%s:%s" % (addr[0], str(addr[1])))
    print("Read: %s" % (conn.recv(1024)))

    STATUS_LINE = "HTTP/1.1 200 OK" 
    ENCODING = "Transfer-Encoding: chunked"

    conn.send(
        STATUS_LINE + CRLF
        # comment this out to disable client-side chunking (you will see dissasembled chunks in curl)
        + ENCODING + CRLF
        + CRLF
    )

    chunks = data_to_formatted_chunks(DATA_TO_SEND, CHUNK_SIZE)

    for chunk in chunks:
        conn.send(chunk)
        time.sleep(0.4)
    
    conn.send(LAST_CHUNK)
    conn.send(CRLF)

    conn.close()

listener.close()
