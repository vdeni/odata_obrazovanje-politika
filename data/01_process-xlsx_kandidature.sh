#!/bin/bash
set -eu -o pipefail

# convert to semicolon delimited csv
libreoffice --convert-to csv:"Text - txt - csv (StarCalc)":59,34,33,1,1\
    --outdir $1 ${1}/${2%.csv}.xlsx

rm ${1}/${2%.csv}.xlsx

# convert to utf-8 encoding from WIN-1250
enconv -L hr -x utf-8 ${1}/${2}

# squash repeating whitespace, strip whitespace from ends
sed -E -i -e 's/\s{2,}/ /g' ${1}/${2}
sed -E -i -e 's/\s;|;\s/;/g' ${1}/${2}
