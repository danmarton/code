#!/bin/bash

if [ "`cd $1 2>&1`" == "" ]
then
	echo "This directory exists."
else
	echo "This directory does not exist."
fi