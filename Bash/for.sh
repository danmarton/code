#!/bin/bash

for i in $(ls)
do
	echo item: $i
done

for i in $(seq 0 9)
do
	echo item $i
done