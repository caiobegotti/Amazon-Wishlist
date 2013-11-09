#!/bin/bash
#
# tests all queries from sample applications, at once

bin/profile.py -i 13RB1XNS2VF62 -s jp
bin/profile.py -i 1LJ10M7BWAICD -s es
bin/profile.py -i 2POKVB3027QIK -s fr
bin/profile.py -i 2ZPN6SBGBP4X8 -s de
bin/profile.py -i 3BFG9M3CL83QR -s cn
bin/profile.py -i 3MCYFXCFDH4FA -s us
bin/profile.py -i 3W1RQNDJTCQC -s it
bin/profile.py -i MBI8TEEYJS10 -s uk
bin/profile.py -i PEK9J1M112UK -s ca
bin/profile.py -i ZVKVJQHOBAT2 -s in
# bin/profile.py -i -s mx
# bin/profile.py -i -s br

bin/search.py -q begotti -s jp
bin/search.py -q begotti -s es
bin/search.py -q begotti -s fr
bin/search.py -q begotti -s de
bin/search.py -q begotti -s cn
bin/search.py -q begotti -s us
bin/search.py -q begotti -s it
bin/search.py -q begotti -s uk
bin/search.py -q begotti -s ca
bin/search.py -q begotti -s in
# bin/search.py -q begotti -s mx
# bin/search.py -q begotti -s br
