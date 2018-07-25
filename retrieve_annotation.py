import sys
from Bio import Entrez

# *Always* tell NCBI who you are
Entrez.email = "pombrolm@oregonstate.edu"

#if len(sys.argv) != 1:
#    print("Usage: python retrieve_annotation.py <list of IDs>")
#    quit()

#id_list = sys.argv[0]

import io

fhandle = io.open("/nfs1/MICRO/Halsey_Lab/lightlim_tp/DB/DEG_names.txt", "rU")
names_list=[]
degs=[]

for line in fhandle:
    names_list.append(line.strip())

for item in names_list:
    degs.append(item.encode("utf-8"))

list=["7443890"]

def retrieve_annotation(id_list):

    """Annotates Entrez Gene IDs using Bio.Entrez, in particular epost (to
    submit the data to NCBI) and esummary to retrieve the information.
    Returns a list of dictionaries with the annotations."""

    request = Entrez.epost("gene",id=",".join(id_list))
    try:
        result = Entrez.read(request)
    except RuntimeError as e:
        #FIXME: How generate NAs instead of causing an error with invalid IDs?
        print "An error occurred while retrieving the annotations."
        print "The error returned was %s" % e
        sys.exit(-1)

    webEnv = result["WebEnv"]
    queryKey = result["QueryKey"]
    data = Entrez.esearch(db="gene",term=id_list, webenv=webEnv, query_key =
            queryKey)
    annotations = Entrez.read(data)

    print "Retrieved %d annotations for %d genes" % (len(annotations),
            len(id_list))

    return annotations

print(list)
print(retrieve_annotation(list))
