from Bio import Entrez

Entrez.email="pombrolm@oregonstate.edu"

import io

#Uses the text file containing the names ("THAPS...") of DE genes on every new line
fhandle = io.open("/nfs1/MICRO/Halsey_Lab/lightlim_tp/DB/DEG_names.txt", "rU")
names_list=[]
degs=[]

records_list={}

for line in fhandle:
    names_list.append(line.strip())

for item in names_list:
    degs.append(item.encode("utf-8"))

#Maps names to Entrez IDs using the organism taxon identifier for T. pseudonana CCMP 1335
for item in degs:
    handle=Entrez.esearch(db="gene", term="txid296543[orgn]" + " " + item)
    record=Entrez.read(handle)
    records_list[item]=record['IdList']

print(records_list)

test=[]

"""Annotates Entrez Gene IDs using Bio.Entrez, in particular epost (to
submit the data to NCBI) and esummary to retrieve the information.
Returns a list of dictionaries with the annotations."""

for value in records_list.values():
    request = Entrez.epost("gene",id=value)
    try:
        result = Entrez.read(request)
    except RuntimeError as e:
        #FIXME: How generate NAs instead of causing an error with invalid IDs?
        print "An error occurred while retrieving the annotations."
        print "The error returned was %s" % e
        sys.exit(-1)

    webEnv = result["WebEnv"]
    queryKey = result["QueryKey"]
    data = Entrez.esummary(db="gene",term=value, webenv=webEnv, query_key =
            queryKey)
    annotations = Entrez.read(data)

    list=(annotations['DocumentSummarySet'].values())
    for dictionary in list:
        print(dictionary[1])
    #list=list[0]
    #test=test.append(list['Description'])
    #print(test)
    #records_list[value]=[records_list[value], list['Description']]
    

print("end")
