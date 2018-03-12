def toJadenCase(string):
    return ' '.join([ i.capitalize() for i in string.split() ])
print toJadenCase("what the heck is dis shiet")