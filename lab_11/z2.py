date = re.compile(r'[A-Z][a-z]{2}\s{1,2}\d{1,2}\s\d{2}:\d{2}:\d{2}')
dates = find_regex("auth.log",date)
dates= [datetime.strptime(x,'%b %d %H:%M:%S').replace(year=2023).strftime('%Y-%m-%d %H:%M:%S') for x in dates]                                                    #TODO
ip = re.compile(r'\d\sip-\d{1,3}-\d{1,3}-\d{1,3}-\d{1,3}')
ips = find_regex("auth.log",ip)
ips = [x[5:].replace("-",".") for x in ips]
user = re.compile(r'-\d{1,3}\s\w+-?\w+\[?\d*\]?:\s')
users = find_regex("auth.log",user)
users = [x[5:] for x in users]
pid = re.compile(r'\[\d+\]')
users = [x.split("[")[0].replace(":","") for x in users]
comm = re.compile(r'-\d{1,3}\s\w+-?\w+\[?\d*\]?:\s.+\n')
comms = find_regex("auth.log",comm)
comms = [x[x.find(": ")+2:] for x in comms]
comms = ["\""+x[:-1]+"\"" for x in comms]
with open('lab_11/zad2.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile,delimiter=";")
    for x in zip(dates, ips, users, comms):
        writer.writerow(x)