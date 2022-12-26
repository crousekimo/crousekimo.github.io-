import base64
import zlib
import json

stubs = {
"esp8266": b"""
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\
""",
"esp32": b"""
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\
""",
"esp32s2": b"""
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\
""",
}

for key, stub in stubs.items():
    code = eval(zlib.decompress(base64.b64decode(stub)))
    print("Processing " + key)
    print("Text size:", str(len(code["text"])) + " bytes")
    print("Data size:", str(len(code["data"])) + " bytes")

    print(code["text"])
    print(base64.b64encode(code["text"]))
    code["text"] = base64.b64encode(code["text"]).decode("utf-8")
    code["data"] = base64.b64encode(code["data"]).decode("utf-8")

    jsondata = json.dumps(code, indent=2)

    f  = open(f"src/vendor/esptool/stubs/{key}.json", "w+")
    f.write(jsondata)
    f.close()
