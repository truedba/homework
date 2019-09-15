"""ПОПРОБОВАТЬ СДЕЛАТЬ ЧЕРЕЗ JSON!!!"""

# setup file для установки

# Примитивные типы - int, float, complex, str, bool, None
# Словари - dict
# Коллекции - list, set, frozenset, tuple
#             (list)(int)1,(int)2,(int)3
import re


PRIMITIVE_TYPES = [
    int,
    float,
    complex,
    str,
    bool
]
CONTAINER_TYPES = [
    list,
    tuple,
    set,
    frozenset
]
PRIMITIVE_REGEX = re.compile(r"\{?\"([a-z\'\<\> ]+)\":\"(.+?)\"\}?$")
CONTAINER_REGEX = re.compile(r"(\"([a-z\'\<\> ]+)\":\"([^,]+))+")

output_list = []

def parse_type(str_type):
    if str_type == "<class 'str'>":
        return str
    elif str_type == "<class 'float'>":
        return float
    elif str_type == "<class 'int'>":
        return int
    elif str_type == "<class 'list'>":
        return list
    elif str_type == "<class 'set'>":
        return set
    elif str_type == "<class 'tuple'>":
        return tuple


def dump(obj, fp):
    if type(obj) in PRIMITIVE_TYPES:
        fp.write(f"{'{'}obj_type: {type(obj)}, obj_value:{obj}{'}'}")
    elif type(obj) in CONTAINER_TYPES:
        fp.write("{}\"object_type\":{}, \"object_values\":{}{}".format(
            "{",
            "\""+str(type(obj))+"\"",
            "{\""+"\",\"".join([f"{type(el)}\":\"{el}" for el in obj]),
            "\"}}"
        ))


def dump2(obj, fp, *args):

    if type(obj) in PRIMITIVE_TYPES:
        if len(args) > 0:
            fp.write(f"\"{type(obj)}\":\"{obj}\",")
        else:
            fp.write(f"{'{'}\"{type(obj)}\":\"{obj}\"{'}'}")
    elif type(obj) in CONTAINER_TYPES:
        if len(args) == 0:
            fp.write('{')
        fp.write(f"\"{type(obj)}\":{'{'}")
        additem = 1
        for el in obj:
            dump2(el, fp, additem)
        if len(args) > 0:
            fp.write('},')
        if len(args) == 0:
            fp.write('}}')

def load_json(fp):
    lines = fp.readlines()
    for line in lines:
        primitive_regex_result = PRIMITIVE_REGEX.match(line)
        if primitive_regex_result:
            print(primitive_regex_result.group(2))
            return parse_type(primitive_regex_result.group(1))(primitive_regex_result.group(2))
        else:
            open_bracket_pos, close_bracket_pos, nested_element_types = parse_brackets(line)
            result_container = parse_type(nested_element_types[0])()
            nested_element_types
            print(open_bracket_pos,' \n', close_bracket_pos)

            for i in range(0, len(open_bracket_pos) ):
                print(nested_element_types[i])
                container = parse_type(nested_element_types[i])()
               # print('line is ',line[open_bracket_pos[i]:close_bracket_pos[i]])
                for el in CONTAINER_REGEX.finditer(line[open_bracket_pos[i]:close_bracket_pos[i]]):
                    print(el.group())
                    primitive = PRIMITIVE_REGEX.match(el.group())
                    value = parse_type(
                        primitive.group(1)
                    )(primitive.group(2))
                    if type(container) == list:
                        container.append(value)
                    elif type(container) == tuple:
                        container = container + (value,)
                if type(result_container) == list:
                    result_container.append(container)
                elif type(result_container) == tuple:
                    result_container = result_container + (container,)
                print(result_container)


def load(fp):
    lines = fp.readlines()
    for line in lines:
        primitive_regex_result = PRIMITIVE_REGEX.match(line)
        container_regex_result = CONTAINER_REGEX.match(line)
        if primitive_regex_result:
            return parse_type(primitive_regex_result.group(1))(primitive_regex_result.group(2))
        elif container_regex_result:
            container = parse_type(container_regex_result.group(1))()
            for el in container_regex_result.finditer():
                primitive = PRIMITIVE_REGEX.match(el)
                value = parse_type(
                    primitive.group(1)
                )(primitive.group(2))
                container.append(value)


def parse_items(input_list):
    value_list_container = []
    print('line is ', input_list)
    for el in CONTAINER_REGEX.finditer(input_list):
        print(el.group())
        primitive = PRIMITIVE_REGEX.match(el.group())
        value = parse_type(
            primitive.group(1)
        )(primitive.group(2))
        value_list_container.append(value)
    return value_list_container


def parse_brackets(input_list):
    open_bracket_pos = []
    close_bracket_pos = []
    nested_element_types = []
    open_bracket_buff = []
    p = re.compile('[\{\}]')
    o = re.compile(r"\"([a-z\'\<\> ]+)\":\{")
    for v in o.finditer(input_list):
        nested_element_types.append(v.group(1))
    for m in p.finditer(input_list):
        if m.group() == '{':
            open_bracket_buff.append(m.end())
            if len(open_bracket_buff) > 1:
                container = parse_type(nested_element_types.pop())()
                value_list = parse_items(input_list[open_bracket_buff[-2]:open_bracket_buff[-1]])
                for value in value_list:
                    if type(container) == list:
                        container.append(value)
                    elif type(container) == tuple:
                        container = container + (value,)
                print(container)
        else:
            close_bracket_pos.append(m.start())
            open_bracket_buff.append(m.start())

    return open_bracket_pos, close_bracket_pos, nested_element_types




def test_load(fp):
    lines = fp.readlines()
    for line in lines:
        parse_brackets(line)


if __name__ == "__main__":
    a = 'Privet'
    b = [4.5, 'ssh', 'test', ('1oh', '2ah'), ('cat', 1), 'items', 123, [['bmw', 5], 'msq']]
    with open("tmp.txt", "w+") as f:
        dump2(b, f)

    with open("tmp.txt", "r+") as f:
        loaded_obj = load_json(f)
        print(type(loaded_obj), loaded_obj)


class MyObj(object):
    def __init__(self):
        self.name = 'Chuck Norris'
        self.phone = '+6661'


obj = MyObj()

print(obj.__dict__)

'''obj = MyObj()
for att in dir(obj):
    print(att, getattr(obj,att))
    
    
def dump(obj, fp):
    if type(obj) in PRIMITIVE_TYPES:
        fp.write(f"({type(obj)}){obj}")
    elif type(obj) in CONTAINER_TYPES:
        fp.write("({}){}".format(
            type(obj),
            ";".join([f"({type(el)}){el}" for el in obj])
        ))'''

'''   with open("tmp.txt", "r+") as f:
        loaded_obj = load(f)
        print(type(loaded_obj),loaded_obj)'''