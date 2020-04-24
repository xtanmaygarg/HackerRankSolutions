def mergeLists(head1, head2):
    Answer = SinglyLinkedList()

    while(head1 and head2):
        if head1.data < head2.data:
            Answer.insert_node(head1.data)
            head1 = head1.next
        else:
            Answer.insert_node(head2.data)
            head2 = head2.next
    
    while(head1):
        Answer.insert_node(head1.data)
        head1 = head1.next
    
    while(head2):
        Answer.insert_node(head2.data)
        head2 = head2.next
    
    return Answer.head
