def read_line (n, file):
    if type(n)== int:
        try:
            open_file = open (file, 'r')
            file = open_file.read()
            lines = file.split('\n')
            if n > len(lines) or n < 1:
                return ('line ' + str(n) + ' doesn\'t exist')
            else:
                return (lines[n-1])
        except:
            return ('file not found')
    else:
        return ('invalid input detected')
print (read_line(4, 'ex3_text.txt'))
print (read_line(9, 'ex3_text.txt')) 
print (read_line(29, 'ex3_text.txt'))
print (read_line('c', 'ex3_text.txt'))
print (read_line(9, 'ex4_text.txt')) 

    
def longest_words (file):
    words = []
    try:
        open_file2 = open (file, 'r')
        file2 = open_file2.read()
        for char in file2:  
            if char.isalpha() == False:
                file2 = file2.replace(char,' ') 
        words = file2.split()
        words.sort(key = len, reverse = True)
        return words[0:5]
    except:
        return ('file not found', words)

print (longest_words('ex3_text.txt'))
print (longest_words('ex4_text.txt'))