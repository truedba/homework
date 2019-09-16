#!/usr/local/bin/python3


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
            if el == obj[-1]:
                fp.write('}')
            else:
                fp.write('},')
        if len(args) == 0:
            fp.write('}}')


def load_json(fp):
    lines = fp.readlines()
    result_container = []
    for line in lines:
        primitive_regex_result = PRIMITIVE_REGEX.match(line)
        if primitive_regex_result:
            result_container.append(primitive_regex_result.group(2))
            return parse_type(primitive_regex_result.group(1))(primitive_regex_result.group(2))
        else:
            result_container = parse_brackets(line)

    return result_container


def parse_items(input_list):
    value_list_container = []
    for el in CONTAINER_REGEX.finditer(input_list):
        primitive = PRIMITIVE_REGEX.match(el.group())
        value = parse_type(
            primitive.group(1)
        )(primitive.group(2))
        value_list_container.append(value)
    return value_list_container


def append_items(input_container,value_list):
    iterator = 0
    for value in value_list:
        if type(input_container) == list:
            input_container.append(value)
        elif type(input_container) == tuple:
            input_container = input_container + (value,)
    iterator += 1
    return input_container


def parse_brackets(input_list):
    nested_level = 0
    nested_level_indicator = 0
    container_list = []
    close_bracket_pos = []
    nested_element_types = []
    open_bracket_buff = []
    p = re.compile('[\{\}]')
    o = re.compile(r"\"([a-z\'\<\> ]+)\":\{")
    for v in o.finditer(input_list):
        nested_element_types.append(v.group(1))
    for m in p.finditer(input_list[1:-1]):
        if m.group() == '{':
            open_bracket_buff.append(m.end())
            if len(open_bracket_buff) > 1:
                if nested_level_indicator == 0:
                    prev_cont_type = nested_element_types.pop(0)
                    container = parse_type(prev_cont_type)()
                    container_list.append(container)
                value_list = parse_items(input_list[open_bracket_buff[-2]:open_bracket_buff[-1]])
                for value in value_list:
                    container_list[nested_level].append(value)
                nested_level += 1
                nested_level_indicator = 0
        else:

            close_bracket_pos.append(m.start())
            if nested_level_indicator == 0:
                nested_level -= 1
                container = parse_type(nested_element_types.pop(0))()
                value_list = parse_items(input_list[open_bracket_buff[-1]:close_bracket_pos[-1]])
                open_bracket_buff.append(m.start())
                container_list[nested_level].append(append_items(container, value_list))
            else:
                value_list = parse_items(input_list[open_bracket_buff[-1]:close_bracket_pos[-1]])
                open_bracket_buff.append(m.start())
                for value in value_list:
                    container_list[nested_level].append(value)
                if nested_level > 0:
                    container_list[nested_level-1].append(container_list[nested_level])
                    container_list.pop(nested_level)
                    nested_level -= 1
            nested_level_indicator =1

    return container_list


def test_load(fp):
    lines = fp.readlines()
    for line in lines:
        parse_brackets(line)


if __name__ == "__main__":
    a = 'Privet'
    b = [4.5, 'ssh', 'test', ('1oh', '2ah'), ('cat', 1), 'items', 123, [('bmw',5), ['msq', ['this',('is','super nested')]]], 'the end']
    with open("tmp.txt", "w+") as f:
        dump2(b, f)

    with open("tmp.txt", "r+") as f:
        loaded_obj = load_json(f)
        print(type(loaded_obj), loaded_obj)
