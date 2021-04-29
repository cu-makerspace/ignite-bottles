# Script to generate SVGs from names.lsv file and template.svg
import os
import zipfile


def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file),
                       os.path.relpath(os.path.join(root, file),
                                       os.path.join(path, '..')))

try:
    os.mkdir('./names')
except:
    pass

names = str(open("names.lsv", "r").read().replace("\r", "")).split("\n")
while("" in names):
    names.remove("")
print(names)

template_svg = open("template.svg", "r").read()

for name in names:
    first = name.split(" ")[0]
    last = " ".join(name.split(" ")[1:])
    output = template_svg.replace("$firstname", first).replace("$lastname", last)
    f = open(f'names/{name}.svg', "w")
    f.write(output)
    f.close()

zipf = zipfile.ZipFile('names.zip', 'w', zipfile.ZIP_DEFLATED)
zipdir('names/', zipf)
zipf.close()
