# HTTP chunked encoding server example.

Demonstrates [RFC 2616](https://tools.ietf.org/html/rfc2616) compliant Chunked Encoding.

# TODO: Explanation

# usage

`./server.py` to start the server

(in another terminal)

`./test.sh` to run the client (will output the result, 1 chunk at a time (cURL -N))

You can disabled chunked encoding by commenting out the `Transfer-Encoding: chunked` header. 

`+ ENCODING + CRLF`

The output from cURL will then be the raw HTTP compliant chunks, except they will be interpreted as plain text.

