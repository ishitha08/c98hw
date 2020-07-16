inp = open('input.txt','r')
out = open('output.txt', 'w')
prev = inp.readline()
for line in inp:
    if line.endswith('move to first perimeter point'):
        prev = line
        if line.endswith('restore layer Z'):
            out.write(line)
            out.write(prev)
    else:
        out.write(prev)
    prev = line
out.write(prev)
out.close()
inp.close

with open('input.txt', 'r') as f:
    s = f.readlines()
def = swap_lines_in_text(s, 
                        first_line_text = 'move to first perimeter point', 
                        second_line_text = 'restore layer Z')
print('\n'.join(df.Text.tolist()))
with open('output.txt', 'w') as f:
    f.writelines(df.Text.tolist())