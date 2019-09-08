import re

PRIMITIVE_TYPES = [
    int,
    float,
    str,...
]

PRIMITIVE_REGEX = re.compile(r"(^\((.+?)\))(.+?)$")
CONTAINER_REGEX = re.compile(r"(^\((.+?)\))(^\((.+?)\))(^\((.+?)\))+$")

def dump(obj,fp):
    if type(obj) in PRIMITIVE_TYPES:
        fp.write(f"(type(obj)}){obj}")
    elif type(obj) in CONTAINER_TYPES:
        fp.write("({},{}){}".format(
            type(obj),
            ":".join([f"({type(el)}){el}" for el in obj])
        )


def pase_type(str_type):
    if str_type == "<class 'str'>":
        return str
    elif str_type == "<class 'list'>":
        return list
    elif str_type == "<class 'set'>":
        return set

def load(fp):
    line = fp.readlines()
    for line in lines:
        regex_result = PRIMITIVE_REGEX.match(line)
            if regex_result:
                return parse_type(regex_result.group(1))(regex_result.group(1)))


            примитивы,словари,коллекции + setup_file