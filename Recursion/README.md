## Recursive Functions

What iterative solution can achieve, recursive funcs can too, but in a more elegant way!

## Idea

Kind of like the Induction in maths

1. Base case - the condition where the recursion should STOP.
2. Recursive case - the condition where we inspect the 'next case'. This should draw us closer to Base Case.

## Warnings

Stak.Over.Flow, of course!

1. Base case must be set - otherwise stack will overflow, which is like an infinite loop
2. Recursive case must bring us closer to the Base Case each step!

## Little more details

Every time the function is called again, it is pushed into the Call Stack.
Every time the function is resolved from the Call Stack, the returned value is added to the execution context, until all recursive functions are resolved.
