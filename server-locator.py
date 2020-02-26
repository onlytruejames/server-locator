import geocoder as g
import socket as s
x=1
def run(str):
    while x==1:
        hostname=input("Input a domain to find its location and ip address \n")
        ip=s.gethostbyname(hostname)
        print("Location:\n",g.ip(ip)) #gets location
        gg=g.ip(ip)
        ggg=gg.latlng
        print("Coordinates:\n",ggg)   #gets coordinates
        print("IP address:\n",ip)     #gets ip address
run(str)
