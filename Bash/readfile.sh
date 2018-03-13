#!/bin/bash

function f1
{
	num=1
	while read line
	do
		echo line$num: $line
		let num++
	done < $1
}

function f2
{
	num=1
	for i in `cat $1`
	do
		echo line$num: $i
		let num++
	done
}
