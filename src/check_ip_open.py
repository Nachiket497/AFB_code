import os

op = []
for i in range(256):
    for j in range(256):
        print("for i,j = ", i, " ", j)
        cmd = f"nmap -sn -v 192.168.{i}.{j}"
        st = os.system(cmd)
        # print(os.system(cmd))

        if st != 0:
            print("IP is open")
            op.append("192.168.{}.{}".format(i, j))
            
print(op)