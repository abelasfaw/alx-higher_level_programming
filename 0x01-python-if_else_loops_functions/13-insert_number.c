#include "lists.h"
#include <stdlib.h>
#include <stdio.h>
/**
 * get_nodeint_at_index- returns nth node of a listint_t type list
 * @head: pointer to first node of list
 * @index: index of node to return
 * Return: nth node of list if node exists, else return 0
 */
listint_t *get_nodeint_at_index(listint_t *head, unsigned int index)
{
	unsigned int counter;
	listint_t *node;

	if (head == NULL)
	{
		return (NULL);
	}
	if (index == 0)
	{
		return (head);
	}
	counter = 0;
	node = head;
	while (counter < index)
	{
		if (node->next == NULL)
		{
			return (NULL);
		}
		node = node->next;
		counter += 1;
	}
	return (node);
}
/**
 * insert_node- inserts a number into a sorted linked list
 * @head: pointer to first node of list
 * @number: value of node to insert
 * Return: null if it fails,else return new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *current, *prev_node;
	unsigned int index = 0;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
	{
		return (NULL);
	}
	new_node->n = number;
	if ((*head) == NULL)
	{
		new_node->next = NULL;
		(*head) = new_node;
		return (new_node);
	}
	current = (*head);
	while (current != NULL)
	{
		if (current->n >= number)
		{
			new_node->next = current;
			prev_node = get_nodeint_at_index((*head), (index - 1));
			if (prev_node != NULL)
			{
				prev_node->next = new_node;
			}
			if (index == 0)
			{
				(*head) = new_node;
			}
			return (new_node);
		}
		index += 1;
		current = current->next;
	}
	prev_node = get_nodeint_at_index((*head), (index - 1));
	prev_node->next = new_node;
	new_node->next = NULL;
	return (new_node);
}
