#!/bin/bash
if [[ $PYPI_TOKEN ]]; then
  use $PYPI_TOKEN
fi
printf "[global]\n" > /etc/pip.conf
printf "extra-index-url =\n" >> /etc/pip.conf
printf "\thttps://$PYPI_TOKEN@<YOUR INDEX URL>\n" >> /etc/pip.conf