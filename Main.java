class Node {
    int data;
    Node next;

    Node(int data) {
        this.data = data;
        this.next = null;
    }
}

class SinglyLinkedList {
    private Node head;
    private int count;

    // Constructor
    SinglyLinkedList() {
        head = null;
        count = 0;
    }

    // Insert at First
    public void insertFirst(int data) {
        Node newNode = new Node(data);
        newNode.next = head;
        head = newNode;
        count++;
    }

    // Insert at Last
    public void insertLast(int data) {
        Node newNode = new Node(data);

        if (head == null) {
            head = newNode;
        } else {
            Node temp = head;
            while (temp.next != null) {
                temp = temp.next;
            }
            temp.next = newNode;
        }
        count++;
    }

    // Delete First
    public void deleteFirst() {
        if (head == null) {
            System.out.println("List is Empty.");
            return;
        }

        head = head.next;
        count--;
    }

    // Delete Last
    public void deleteLast() {
        if (head == null) {
            System.out.println("List is Empty.");
            return;
        }

        if (head.next == null) {
            head = null;
            count--;
            return;
        }

        Node temp = head;
        while (temp.next.next != null) {
            temp = temp.next;
        }

        temp.next = null;
        count--;
    }

    // Print List
    public void printList() {
        if (head == null) {
            System.out.println("List is Empty.");
            return;
        }

        Node temp = head;
        while (temp != null) {
            System.out.print(temp.data + " -> ");
            temp = temp.next;
        }
        System.out.println("null");
    }

    // Check if List is Empty
    public boolean isEmpty() {
        return head == null;
    }

    // Return Size
    public int size() {
        return count;
    }

    // Find Node
    public Node findNode(int data) {
        Node temp = head;

        while (temp != null) {
            if (temp.data == data) {
                return temp;
            }
            temp = temp.next;
        }

        return null;
    }
}

public class Main {
    public static void main(String[] args) {

        SinglyLinkedList list = new SinglyLinkedList();

        // Insert Elements
        list.insertFirst(8);
        list.insertFirst(12);
        list.insertLast(15);
        list.insertLast(18);

        System.out.println("Linked List:");
        list.printList();

        // Delete First
        list.deleteFirst();
        System.out.println("\nAfter deleteFirst():");
        list.printList();

        // Delete Last
        list.deleteLast();
        System.out.println("\nAfter deleteLast():");
        list.printList();

        // isEmpty
        System.out.println("\nIs Empty? " + list.isEmpty());

        // Size
        System.out.println("Size: " + list.size());

        // Find Node
        Node found = list.findNode(30);

        if (found != null) {
            System.out.println("Node Found: " + found.data);
        } else {
            System.out.println("Node Not Found");
        }
    }
}