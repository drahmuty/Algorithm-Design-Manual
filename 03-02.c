#include <stdio.h>

typedef struct Node {
    char *value;
    struct Node *next;
} Node;

void reverse(Node **head) 
{
    Node *prev, *curr, *next;
    prev = NULL;
    curr = *head;
    next = NULL;
    
    while (curr) {
        next = curr->next;
        curr->next = prev;
        prev = curr;
        curr = next;
    }
    *head = prev;
    return;
}
