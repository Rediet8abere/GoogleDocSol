"""Find the middle item in a singly linked list or two middle items
    if it contains an even number of nodes.

    input: linkedlist
    output: the data(datas) in middle

    len of linkedlist, find mid , mid+1
    loop and keep track of count. if count is equal to mid and return data,
    if it’s mid-1, return data, mid, return data

    Node cls = data,  next
    linkedlist cls = head, tail
"""



def middleitem(ll):
	length_ll = ll.length
	mid = 0
if length_ll %2 == 0:
	mid = length_ll/2+1
else:
	mid = (length_ll/2)
	count = 0
	cur_node = ll.head
	middle_items = []
while count <= mid:
	cur_node = cor_node.next
	count += 1
	if length_ll  %2 ==0 and  count == mid-1:
		middle_items.append(cur_node.data)
middle_items.append(cur_node.data)
