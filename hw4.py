def rep_char(c,n):
    print(c * n)

def draw_line_string(name):
    msg1 = "Hello "+ name +","
    msg2 = "Welcome to Seoul."
    nstr = len(msg1) if (len(msg1) > len(msg2)) else len(msg2)

    rep_char("_",nstr)
    print(f' \n{msg1}\n{msg2}')
    rep_char('_',nstr)




name = input("Input his/her name:")
draw_line_string(name)
