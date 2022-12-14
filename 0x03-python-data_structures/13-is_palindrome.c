#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: address of a pointer to the singly linked list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *first = *head;

	int size = 0, i, j, mid;
	int data[2350];

	while (first)
	{
		data[size] = first->n;
		size++;
		first = first->next;
	}

	mid = size / 2;
	for (i = 0, j = size - 1; i < mid; i++, j--)
	{
		if (data[i] != data[j])
			return (0);
	}

	return (1);
}
