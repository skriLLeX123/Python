#You are given an integer  followed by  email addresses. Your task is to print a list containing only valid email addresses in lexicographical order.
import re
def fun(s):
    f=s
    s=''.join(re.sub(" ","",s))
    list1=re.split('\@|\.',s)
    if len(list1)==3 and list1[0].replace("-","").replace("_","").isalnum() and list1[1].isalnum() and 0<len(list1[2])<=3:
        return True
    else:
        return False
    

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)

'''
Sample Input

3

lara@hackerrank.com
brian-23@hackerrank.com
britts_54@hackerrank.com

Sample Output

['brian-23@hackerrank.com', 'britts_54@hackerrank.com', 'lara@hackerrank.com']
'''
