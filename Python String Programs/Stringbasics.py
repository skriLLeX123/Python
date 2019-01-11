#python strig startswith() method
a="www.google.com"
result=a.startswith("www.")
print(result)

#output
True

#-------------------------------------------------------#

#python strig endswith() method
a="www.google.com"
result=a.endswith("www.")
print(result)

#output
False

#-------------------------------------------------------#

#python string find() method

a="www.google.com"
result=a.find(".com")
print(result)

#output
10

#-------------------------------------------------------#


#python string rfind() method
a="www.google.com.com"
result=a.rfind(".com")
print(result)

#output
14


#-------------------------------------------------------#

#python string strip(), rstrip(), lstrip() method
a=" www.google.com.com "
a=a.strip()
print(a)
print(a.rstrip(".com"))
print(a.lstrip("www."))

#output
www.google.com.com
www.google
google.com.com


#-------------------------------------------------------#

#python string upper(), lower(), isupper(), islower() method

a="BHUSHAN Computer Science"
d="bhushan"
c="MAC"
print(a.lower())
print(a.upper())
print(a.islower())
print(a.isupper())
print(d.islower())
print(c.isupper())

#output
bhushan computer science
BHUSHAN COMPUTER SCIENCE
False
False
True
True

#-------------------------------------------------------#

#python string capitalize() method

a="computer science"
print(a.capitalize())

d=" computer science"
print(d.capitalize())

#output
Computer science
 computer science

#-------------------------------------------------------#

#python string split() method

a='computer science'
a=a.split()
print(a)
print('-'.join(a))

#output
['computer', 'science']
computer-science

#-------------------------------------------------------#

#python string replace() method

a='this is it this is it'
c=a.replace("it","real")
print(c)
d=a.replace("it","real",1)
print(d)

#output
this is real this is real
this is real this is it

#-------------------------------------------------------#

#python string swapcase() method

a="Computer science"
print(a.swapcase())

#output
cOMPUTER SCIENCE

#-------------------------------------------------------#

#python string title() method

a="computer science"
print(a.title())

#output
Computer Science

