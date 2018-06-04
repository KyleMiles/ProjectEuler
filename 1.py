#!/usr/bin/env python3

print(sum( [i for i in range(1, 1000) if (not i % 5 or not i % 3) ] ))
