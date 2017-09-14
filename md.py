def h( i,string ):
	if (i < 1):
		i = 1
	if (i > 6):
		i = 6
	return '#'*i + " " + str(string)

def h1( string ):
	return h(1,string)

def h2( string ):
	return h(2,string)

def h3( string ):
	return h(3,string)

def h4( string ):
	return h(4,string)

def h5( string ):
	return h(5, string)

def h6( string):
	return h(6, string)

def i( string ):
	return "_" + str(string) + "_"

def b( string ):
	return "**" + str(string) + "**"

def s( string ):
	return "~~" + str(string) + "~~"

#github markdown
def table ( array ):
	table = []
	for i,row in enumerate(array):
		table.append('| ' + ' | '.join(row) + ' |')
		if (i == 0):
			table.append('| ' + ' | '.join(['----' for x in row]) + ' |')
	return "\n".join(table)

#github markdown
def string_to_table_array( string , row_delim = ",,", col_delim = ","):
	tables = string.strip().split(row_delim)
	for i,row in enumerate(tables):
		tables[i] = row.split(col_delim)
		tables[i] = [cell.strip() for cell in tables[i]]
	return tables

def ul( list ):
	return '\n'.join(["* " + str(elements) for elements in list])

def ol( list ):
	return '\n'.join([str(i+1) + ". " + str(elements) for i, elements in enumerate(list)])

def code( string ):
	return "`" * 3 + "\n" + string + "\n" + "`" * 3

#gitlab markdown
def code_with_highlighting( string , language = ""):
	return "`" * 3 + language + "\n" + string + "\n" + "`" * 3

def java( string ):
	return code_with_highlighting(string, "java")

def p ( string ):
	return " " * 4 + string;
