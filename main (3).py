#include <stdio.h>
#include <string.h>

#define MAX_PRODUCTS 5

int linear_search_product(char *product_list[], char *target_product,
                          int size) {
  int indices[MAX_PRODUCTS];
  int index = 0;

  for (int i = 0; i < size; ++i) {
    if (strcmp(product_list[i], target_product) == 0) {
      indices[index] = i;
      index++;
    }
  }

  if (index == 0) {
    printf("Product not found.\n");
  } else {
    printf("Product found at indices: ");
    for (int i = 0; i < index; ++i) {
      printf("%d ", indices[i]);
    }
    printf("\n");
  }

  return index;
}

int main() {
  'char *products[]' = {"apple", "banana", "apple", "orange", "apple"};
  char *target = ("apple");
  int size = MAX_PRODUCTS;
  'linear_search_product'("products", target, size);
  return 0;
}