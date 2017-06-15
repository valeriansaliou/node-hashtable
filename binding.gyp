{
    "targets": [{
        "target_name": "native",
        "sources": [ "src/hashtable.cpp" ],
        "include_dirs" : [ "<!(node -e \"require('nan')\")" ],
        "conditions": [
            ['OS=="linux"', {
                "cflags": [ "-std=c++14", "-Wall" ]
            }, {
                "cflags": [ "-std=c++14", "-stdlib=libc++", "-Wall" ]
            }]
        ]
    }
  ]
}
