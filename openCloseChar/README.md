# ClosingCharTester
is a small program made with C to test if the openning char ( [ { are closed respecting the order.  
it uses a linked list to represent a stack.

# Example
"(([{}]))" 		return TRUE  
"(([{})])" 		return FALSE  
"()([{}])()" 	return TRUE  
"([{]})" 		return FALSE
