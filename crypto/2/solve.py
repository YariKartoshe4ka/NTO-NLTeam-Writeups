import requests

def binasc(data):
    binary_int = int(data, 2);
    byte_number = binary_int.bit_length() + 7 // 8
    binary_array = binary_int.to_bytes(byte_number, "big")
 
    # Converting the array into ASCII text
    ascii_text = binary_array.decode()
 
    # Getting the ASCII value
    print(ascii_text)

# URL, на который собираетесь отправлять запрос
url = 'http://10.10.24.10:1177/guess_bit'

n= 87282560815220843038250014810039477684684070283769203406585435850371115053570026597118498765163762164403692160395958477910825986946012162688343826181673963273157790228932614367441290233841031776814108741444267327057272508606770654217633425737988863059905188830300473802664754489103853373670969508924457898743
params = {
    'bit': '0',
}
data = []
bins = []
for i in range(134):
    r = requests.get(url=url, params={'bit': f'{i}'}) 
    num = r.json()['guess']   
    data.append(num)
    bins.append("1" if num < n//2 else "0")
print(*bins)

for i in range(len(bins)):
    status_num = []
    for j in range(20):
        r = requests.get(url=url, params={'bit': f'{i}'}) 
        num = r.json()['guess']
        status_num.append(num < n//2)
    if any(status_num):
        bins[i] = "1"
    elif set(status_num) == {False}:
        bins[i] = "0"
    else:
        print("error")
print("".join(bins[::-1]))
binasc("".join(bins[::-1]))
