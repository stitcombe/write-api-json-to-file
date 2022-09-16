import requests

BASEURL = 'https://www.breakingbadapi.com/api/'

def getRequest(APIURL):
  FULLURL = BASEURL + APIURL
  apiCall = requests.get(FULLURL)
  return apiCall

def main():
  a = getRequest('character/random')
  b = open("results.txt", "x")
  b.write(a.text)
  b.close()

if __name__ == "__main__":  
  main()