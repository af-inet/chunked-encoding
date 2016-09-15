# HTTP chunked encoding server example.

Demonstrates [RFC 2616](https://tools.ietf.org/html/rfc2616) compliant Chunked Encoding.

# TODO: Explanation

# usage

`./server.py` to start the server

(in another terminal)

`./test.sh` to run the client (will output the result, showing chunks as they're received `curl -N`)

You can disabled chunked encoding by commenting out the `Transfer-Encoding: chunked` header. 

`+ ENCODING + CRLF`

The output from `test.sh` will then be the raw chunks, interpreted as plain text.

