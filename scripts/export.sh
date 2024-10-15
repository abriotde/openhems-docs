#!/bin/env bash

SCRIPT_PATH=`dirname $0`
DOC_FOLDER=$SCRIPT_PATH/../documents
cd $DOC_FOLDER
DOC_FOLDER=`pwd`

libreoffice --convert-to pdf *.fodp
libreoffice --convert-to pdf *.fodt
libreoffice --convert-to pdf *.fodg

