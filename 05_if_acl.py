aclNum = int(input("What is the IPv4 ACL number? "))
if aclNum >= 1 and aclNum <= 99:
    print ("The is a standart IPv4 ACL.")
elif aclNum >= 100 and aclNum <= 199:
    print ("This is a extended IPv4 ACL.")
else:
    print ("This is not a standart or extended IPv4 ACL.")
