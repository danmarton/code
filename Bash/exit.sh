#!/bin/bash

function quit 
{
	 exit   #This terminates the whole script, not just the function.
}

echo foo
quit
echo bar   #This statement is skipped.