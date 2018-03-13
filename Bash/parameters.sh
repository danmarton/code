#!/bin/bash

function f1 { echo $1; } #This is a local $1

function f2 { echo $1; } #This is another local $1

f1 asd
f2 sdf

echo $1 #This is the global $1
