#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: pointer to head
 * @number: number to insert at node data
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *cur = *head;
	listint_t *prev = NULL;
	listint_t *node;

	node = malloc(sizeof(*node));
	if (!node)
		return (NULL);

	node->n = number;
	node->next = NULL;

	if (!(*head))
	{
		*head = node;
		return (node);
	}
	else if (cur->n >= number)
	{
		node->next = *head;
		*head = node;
		return (node);
	}
	else
	{
		while (cur)
		{
			if (cur->n >= number)
				break;
			prev = cur;
			cur = cur->next;
		}
	}

	node->next = prev->next;
	prev->next = node;
	return (node);
}
