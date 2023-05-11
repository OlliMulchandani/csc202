#include <iostream>
#include <string>

struct Node {
    std::string data;
    Node* next;
};

class LinkedList {
public:
    LinkedList() : head(nullptr) {}

    // Function to add a node with data in alphabetical order
    void addNode(const std::string& data) {
        Node* newNode = new Node;
        newNode->data = data;
        newNode->next = nullptr;

        // If the list is empty or the new node comes before the head
        if (head == nullptr || newNode->data < head->data) {
            newNode->next = head;
            head = newNode;
        } else {
            Node* current = head;
            // Traverse the list to find the correct position for insertion
            while (current->next != nullptr && current->next->data < newNode->data) {
                current = current->next;
            }
            // Insert the new node in the appropriate position
            newNode->next = current->next;
            current->next = newNode;
        }
    }

    // Function to display the contents of the list
    void displayList() const {
        Node* current = head;
        while (current != nullptr) {
            std::cout << current->data << std::endl;
            current = current->next;
        }
    }

    // Destructor to deallocate memory for nodes
    ~LinkedList() {
        Node* current = head;
        while (current != nullptr) {
            Node* next = current->next;
            delete current;
            current = next;
        }
    }

private:
    Node* head;
};

int main() {
    LinkedList songList;

    // Get user input of songs
    std::string song;
    std::cout << "Enter songs (type 'exit' to finish):" << std::endl;
    while (true) {
        std::getline(std::cin, song);
        if (song == "exit") {
            break;
        }
        songList.addNode(song);
    }

    std::cout << "\nSong List:" << std::endl;
    songList.displayList();

    return 0;
}
