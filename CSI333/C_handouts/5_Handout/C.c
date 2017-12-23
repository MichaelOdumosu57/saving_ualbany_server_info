/*Handout 5.3
Program Example 9: The following C program creates a linked list. Each node of the list contains
an integer value and a pointer to the next node of the list.
The program reads positive integer values typed in by a user one at a time, and inserts a node
containing that value at the end of the linked list. When the user inputs zero or a negative value, the
program stops accepting input, prints the values in the linked list and terminates.*/



#include <stdio.h>
#include <stdlib.h>

struct node {
  int value;
  struct node *next;
};

int main(void) {
  
  void print_list(struct node*);
  void insert_node(struct node**, struct node**, int);


  struct node *head, *tail;
  int i; 
  head = tail = NULL; 

  do{

    printf("Next value = ");
    scanf("%d", &i);
      if (i <= 0) {  
          break;
      }
      insert_node(&head, &tail, i);
  } while (i > 0) ;

  print_list(head);
  print_list(head);  
  return 0;
} 
void insert_node (struct node **h, struct node **t, int v) {
  struct node *temp;
  if ((temp = (struct node *)malloc(sizeof(struct node))) == NULL) {
    printf("Node allocation failed. \n");
    exit(1); 
  }

  temp->value = v; temp->next = NULL;
  if (*h == NULL) {

    *h = *t = temp;
  }
  else { 

    (*t)->next = temp; *t = (*t)->next;
  }
} 
void print_list(struct node *h) {


  if (h == NULL) {
    printf("The list is empty.\n");
  }
  else {
    printf("Values in the list are:\n");
    while (h != NULL) {
      printf("%d\n", h->value);
      h = h->next;
    }
  }
} 
