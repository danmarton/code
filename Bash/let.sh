#!/bin/bash

cnt=1
cnt=cnt+1
echo $cnt

cnt=1

let cnt=cnt+1

echo $cnt

let cnt+=1

echo $cnt

#cnt=cnt + 1 -> error
#let cnt = cnt + 1 -> error
#let cnt=cnt + 1 -> error