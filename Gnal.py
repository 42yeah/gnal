import sys
import time 
var = {}
var['n'] = '\n'
var['r'] = '\r'
destination = 1
width = 0
if len(sys.argv) == 1:
    line = raw_input()
else:
    try:
        line = open(sys.argv[1], 'r').read()
        if '\n' in line:
            width = len(line.split('\n')[0]) + 1 
    except:
        print('Unable to load gnal script. ')
        quit()
destination = 1
each = -1

def next():
    global destination, each
    if destination == 1: each += 1
    if destination == 2: each -= 1
    if destination == 3: each += width
    if destination == 4: each -= width
    try:
        return line[each]
    except:
        panic(10)
def prev():
    global destination, each
    if destination == 1: each -= 1
    if destination == 2: each += 1
    if destination == 3: each -= width
    if destination == 4: each += width
    try:
        return line[each]
    except:
        print each
        panic(10)
         
def period(end, *conf):
    ign = 0
    if end == '"': start = '"'
    if end == ')': start = '('
    if end == ']': start = '['
    if end == '}': start = '{'
    if end == '(': start = ')'
    if end == '\'': start = '\''
    if end == '!': start = '!'
    global destination, each
    st = ''
    passive = True
    if len(conf) == 0:
        passive = False
    else:
        eac = each
    while 1:
        if passive is False:
            g = next()
        else:
            g = prev()
        if g == end and ign == 0:
            break
        elif g == start:
            ign += 1
            st = st + g
        elif g == end and ign > 0:
            ign -= 1
            st = st + g
        else:
            st = st + g
    if passive is True:
        each = eac + 1
    return st
           
def panic(what):
    global each
    print('Process panic with the code ' + str(what))
    print('In block number ' + str(each + 1))
    print('I mean, the "' + line[each] + '" block. ')
    print('========================================')
    for a in range(0, len(line)):
        if a != each:
            sys.stdout.write(line[a])
        else:
            sys.stdout.write('\033[91m*\033[0m')
    print
    print('========================================')
    quit()
    
    
def exe(line):
    global destination, each, var, width 
    each = -1
    start = False
    while 1:
        import os
        #os.system('clear')
        #for a in range(0, len(line)):
        #    if a != each:
        #        sys.stdout.write(line[a])
        #    else:
        #        sys.stdout.write('\033[91m*\033[0m')
        #time.sleep(1)
        if destination == 1: each += 1
        if destination == 2: each -= 1
        if destination == 3: each += width
        if destination == 4: each -= width
    
        if each < 0: panic(2)
        try:
            proceed = line[each]
        except Exception, e:
            panic(1)
        
        if proceed == '@' and start is False:
            start = True
        
        if start is True:
            if proceed == '>': destination = 1
            if proceed == '<': destination = 2
            if proceed == 'v': destination = 3
            if proceed == '^': destination = 4
            if proceed == '$': 
                name = next()
                if name == '(':
                    name = period(')')
                v = next()
                if v == '"':
                    v = period('"')
                var[name] = v
            if proceed == '#':
                break
            if proceed == 't':
                print(var)
            if proceed == ':':
                try:
                    g = next()
                    if g == '(':
                        varname = period(')')
                        print(var[varname])
                    elif g != '"':
                        print(var[g])
                    else:
                        st = ''
                        while 1:
                            n = next()
                            if n != '"':
                                st = st + n
                            else:
                                break
                        print(st)
                except Exception, e:
                    panic(55)
            if proceed == 'i':
                try:
                    name = next()
                    if name == '(':
                        name = period(')')
                    var[name] = int(var[name])
                except Exception, e:
                    panic(58)
            if proceed == 's':
                name = next()
                if name == '(':
                    name = period(')')
                try:
                    var[name] = str(var[name])
                except: panic(233)
            if proceed == '_':
                name = next()
                if name == '(':
                    name = period(')')
                try:
                    var[name] = raw_input()
                except:
                    panic(12)
            if proceed == '%':
                g = next()
                try:
                    if g == '"':
                        g = period('"')
                    elif g == '(':
                        g = var[period(')')]
                    else:
                        g = var[g]
                except:
                    panic(502)
                try:
                    mode = next()
                    if mode != 'r' and mode != 'w':
                        panic(503)
                    f = open(g, mode)
                    while 1:
                        cmd = next()
                        if cmd == 'r':
                            g = next()
                            if g == '(':
                                g = period(')')
                                var[g] = f.read()
                        if cmd == 'w':
                            g = next()
                            if g == '"':
                                g = period('"')
                                f.write(g)
                            elif g == '(':
                                g = var[period(')')]
                                f.write(g)
                            else:
                                g = var[g]
                                f.write(g)
                        if cmd == 'c':
                            break
                    f.close()
                except:
                    panic(504)
            if proceed == '=':
                try:
                    name = next()
                    if name == '(':
                        name = period(')')
                    value = next()
                    if value != '"':
                        value = next()
                        var[name] = value
                    else:
                        value = ''
                        while 1:
                            g = next()
                            if g == '"':
                                var[name] = value
                                break
                            else:
                                value = value + g
                except:
                    panic(90)
            if proceed == '?':
                try:
                    name1 = next()
                    if name1 == '(':
                        name1 = period(')')
                    name2 = next()
                    if name2 == '(':
                        name2 = period(')')
                    var[name1]
                    var[name2]
                except:
                    panic(103)
                if var[name1] == var[name2]:
                    g = next()
                    if g == '^':
                        destination = 4
                    elif g == 'v':
                        destination = 3
                    elif g == '<':
                        destination = 2
                    elif g == '>':
                        destination = 1
                    else:
                        panic(291)
                else:
                    next()
                    g = next()
                    if g == '^':
                        destination = 4
                    elif g == 'v':
                        destination = 3
                    elif g == '<':
                        destination = 2
                    elif g == '>':
                        destination = 1
                    else:
                        panic(291)
            if proceed == '"':
                c = next()
                if c == '(':
                    period(')')
            if proceed == '*':
                operator = prev()
                next()
                g = next()
                if g == '(':
                    g = period(')')
                h = next()
                if h == '(':
                    h = period(')')
                try:
                    num1 = var[g]
                    num2 = var[h]
                except:
                    panic(395)
                try:
                    num1 + 1
                    num2 / 5
                except:
                    panic(396)
                if operator == '+':
                    var[g] = var[g] + var[h]
                elif operator == '-':
                    var[g] = var[g] - var[h]
                elif operator == '*':
                    var[g] = var[g] * var[h]
                elif operator == '/':
                    try:
                        var[g] = float(var[g]) / var[h]
                    except: panic(397)
                    # Divide by zero
                else:
                    panic(398)
            elif proceed == '+':
                try:
                    name = next()
                    if name == '(':
                        name = period(')')
                    value = next()
                    if value == '(':
                        value = period(')')
                    var[name] = var[name] + var[value]
                except:
                    panic(90)
            if proceed == '&':
                None
            if proceed == '\'':
                stack = period('\'')
                sed = destination
                see = each
                exe(stack)
                destination = sed
                each = see
            if proceed == 'p':
                order = prev()
                next()
                if order != '.':
                    try:
                        name = next()
                        if name == '(':
                            name = var[period(')')]
                        elif name == '"':
                            name = period('"')
                        else:
                            None
                    except: panic(485)
                    try:
                        exec('import ' + name)
                    except:
                        panic(486)
                else:
                    try:
                        name = next()
                        if name == '(':
                            name = var[period(')')]
                        elif name == '"':
                            name = period('"')
                        elif name == '$':
                            name = 'var["'
                            g = next()
                            if g == '(':
                                g = period(')')
                            name = name + g + '"]'
                        else:
                            None
                        order = next()
                        if order == '(':
                            order = var[period(')')]
                        elif order == '"':
                            order = period('"')
                    except: panic(969)
                    argv = period('!')
                    try:
                        exec('ret = ' + name + '.' + order + '(' + argv + ')') in globals(), locals()
                        give = next()
                        if give == '(':
                            give = period(')')
                        var[give] = ret
                    except Exception, e:
                        print(e)
                        panic(970)
                                
    print('Proceed finished without errors. ')
    
exe(line)
