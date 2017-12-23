#include <stdio.h>
#include <stdlib.h>
#include <string.h>


struct node {
  int value;
  struct node *next;
}test;

void print_list(struct node *);
struct node *search_list(struct node *,int);
void add_node(struct node *,int);

int main (void){

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

  void *search_list(struct node *h, int x) {
    
    while (h != NULL) {
      if (h->value == x)
	return h;
      h = h->next;
    }
    
    return NULL;
  } 

  void add_node(struct node h,int x) {
    struct node *j;
    if( h.next == NULL) {
	j->value = x;
	h.next = j;
	struct node *k;
	*k = h;
	//print_list(k);
    }
    else {
      j = h.next;
      add_node(*j,x);
    }
  }
   
  test.value =7;
  add_node(test,5);
  add_node(test,3);
  return 0;
}

