
import re

variables = {}
functions = {}

def evaluate(expr):
    expr = expr.strip()
    for var in variables:
        expr = expr.replace(var, str(variables[var]))
    if expr.startswith('"') and expr.endswith('"'):
        return expr[1:-1]
    try:
        return eval(expr)
    except:
        return expr

def run_block(lines):
    for line in lines:
        run_line(line)

def run_line(line):
    line = line.strip()

    if line.startswith("say "):
        msg = line[4:].strip()
        print(evaluate(msg))

    elif line.startswith("set "):
        parts = line[4:].split("=", 1)
        var_name = parts[0].strip()
        var_value = evaluate(parts[1].strip())
        variables[var_name] = var_value

    elif line.startswith("if "):
        cond_match = re.match(r'if (.+?) \{', line)
        if cond_match:
            condition = cond_match.group(1)
            block_lines = get_block()
            if evaluate(condition):
                run_block(block_lines)

    elif line.startswith("repeat "):
        count_match = re.match(r'repeat (\d+) \{', line)
        if count_match:
            count = int(count_match.group(1))
            block_lines = get_block()
            for _ in range(count):
                run_block(block_lines)

    elif line.startswith("func "):
        func_match = re.match(r'func (\w+)\((.*?)\) \{', line)
        if func_match:
            name = func_match.group(1)
            args = [a.strip() for a in func_match.group(2).split(",") if a.strip()]
            block_lines = get_block()
            functions[name] = (args, block_lines)

    elif re.match(r'\w+\(.*\)', line):
        call_match = re.match(r'(\w+)\((.*?)\)', line)
        if call_match:
            name = call_match.group(1)
            args = [evaluate(a.strip()) for a in call_match.group(2).split(",")]
            if name in functions:
                arg_names, func_lines = functions[name]
                backup = dict(variables)
                for i in range(len(arg_names)):
                    variables[arg_names[i]] = args[i]
                run_block(func_lines)
                variables.clear()
                variables.update(backup)

    elif line == "" or line.startswith("//"):
        pass
    else:
        print(f"[RaptorScript Error] Unknown command: {line}")

def get_block():
    global code_lines
    block = []
    depth = 1
    while code_lines:
        line = code_lines.pop(0).strip()
        if "{" in line:
            depth += 1
        if "}" in line:
            depth -= 1
            if depth == 0:
                break
        block.append(line)
    return block

def run_raptorscript(filename):
    global code_lines
    with open(filename, "r") as f:
        code_lines = [line.strip() for line in f if line.strip()]
    while code_lines:
        run_line(code_lines.pop(0))

if __name__ == "__main__":
    run_raptorscript("example.rap")
