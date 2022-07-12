# Open source hehe
# Janggan lupa ngopi
from requests import get as _get_data_xenzi_
from requests import post as _post_data_xenzi_
from json import loads as _json_data_xenzi_
from os import system as _os_data_xenzi_
from time import sleep as _time_data_xenzi_

# url api Shortlink v1
url = "https://xenzi-ganz.herokuapp.com/api/shortlink_v1"
# download apikey nya dulu >_<
apikey = "Download apikey nya dulu >_< Trial"

def Shortlink_v1():
  _os_data_xenzi_('clear')
  print ("\r     [ Shortlink v1 ]")
  print ("\n  • Creator : Xenzi Gan'z \n")
  
  print ('  • masukan url yang Inggin di Shortlink')
  url_v1 = input('  • url :')
  if url_v1 in '':
    exit('  • Janggan kosong menu')
  else:
    api = _get_data_xenzi_(url,params={'apikey': apikey,'url':url_v1})
    api2 = _json_data_xenzi_(api.text)
    if api2['message'] in 'apikey invalid':
      print ('  • apikey eror')
    elif api2['status'] in 'false':
      print ('  • gagal shortlink v1')
    else:
      print (f'  • Berhasil Shortlink : {api2["shortlink"]}')
      
if __name__ == '__main__':
  Shortlink_v1()