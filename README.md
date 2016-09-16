# HTTP chunked encoding server example.

Demonstrates [RFC 2616](https://tools.ietf.org/html/rfc2616) compliant Chunked Encoding.

## usage

`./server.py` to start the server

(in another terminal)

`./test.sh` to run the client (will output the result, showing chunks as they're received `curl -N`)

You can disabled chunked encoding by commenting out the `Transfer-Encoding: chunked` header. 

`+ ENCODING + CRLF`

The output from `test.sh` will then be the raw chunks, interpreted as plain text.


## explanation

Chunked Transfer Encoding is a feature of HTTP/1.1 which allows a payload to be delivered in many individual chunks.

An advantage of chunking is that you do not need to specify a `Content-Length` header, since each chunk contains it's own length.

This also means you can transfer a payload without knowing it's size ahead of time.

## formal definition ([Augmented Backus–Naur Form](https://en.wikipedia.org/wiki/Augmented_Backus–Naur_Form))

```
 Chunked-Body   = *chunk
                  last-chunk
                  trailer
                  CRLF

 chunk          = chunk-size [ chunk-extension ] CRLF
                chunk-data CRLF
 chunk-size     = 1*HEX
 last-chunk     = 1*("0") [ chunk-extension ] CRLF

 chunk-extension= *( ";" chunk-ext-name [ "=" chunk-ext-val ] )
 chunk-ext-name = token
 chunk-ext-val  = token | quoted-string
 chunk-data     = chunk-size(OCTET)
 trailer        = *(entity-header CRLF)
```

